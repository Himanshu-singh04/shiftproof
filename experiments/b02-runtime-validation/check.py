"""Portable identity controls: synthetic metadata and mocked dispatch, never load packages."""

import argparse
import copy
import json
from pathlib import Path
import shutil
import tempfile
from unittest.mock import Mock

import validate as v


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scratch', required=True, type=Path)
    args = parser.parse_args()
    # On the assigned Mac, portable checks obey the same mount/storage boundary.
    if v.platform.system() == 'Darwin':
        v.mount_check()
        v.require(args.scratch.resolve().is_relative_to(v.CACHE), 'scratch outside B02 cache')
    v.require(args.scratch.is_dir(), 'scratch must already exist')
    pins = v.load(v.HERE / 'pins.json')
    v.inputs_check(v.HERE, pins['inputs']['b02'])
    v.inputs_check(v.B01, pins['inputs']['b01'])
    print('PASS: committed B01/B02 inputs and lock identities')
    # Disposable copies of real manifests/locks, synthetic installed package metadata.
    with tempfile.TemporaryDirectory(prefix='identity-controls-', dir=args.scratch) as directory:
        root = Path(directory)
        experiment = v.Experiment(root)
        experiment.npm = root / 'mock-npm'
        experiment.npm.mkdir()
        experiment.command = Mock(return_value=None)
        experiment.runtime = lambda: v.runtime_check(v.RUNTIME.copy())
        for label, source in [('b01', v.B01), ('b02', v.HERE)]:
            dest = root / label
            dest.mkdir()
            for name in pins['inputs'][label]:
                shutil.copyfile(source / name, dest / name)
        experiment.inventories = {}
        for label in ('b01', 'b02'):
            for name, entry in v.load(root / label / 'package-lock.json')['packages'].items():
                if not name or not v.applicable(entry):
                    continue
                path = root / label / name / 'package.json'
                path.parent.mkdir(parents=True)
                path.write_text(json.dumps({'name': entry.get('name', name.removeprefix('node_modules/')),
                                            'version': entry['version']}))
                archive = entry['resolved'].rsplit('/', 1)[-1]
                experiment.inventories[archive] = [{'path': 'package/package.json', 'kind': 'manifest',
                                                    'sha256': v.digest(path.read_bytes())}]
        npm_manifest = experiment.npm / 'package.json'
        npm_manifest.write_text('{"name":"npm","version":"12.2.3"}')
        experiment.inventories['npm-12.2.3.tgz'] = [{'path': 'package/package.json', 'kind': 'manifest',
                                                   'sha256': v.digest(npm_manifest.read_bytes())}]
        npm = lambda: experiment.npm_command(['--version'])
        compiler = lambda: experiment.package_command('b02', ['MOCK-COMPILER-SENTINEL'])
        sdk = lambda: experiment.package_command('b01', ['MOCK-SDK-SENTINEL'])
        for label, call in [('npm', npm), ('compiler', compiler), ('SDK', sdk)]:
            experiment.command.reset_mock()
            call()
            v.require(experiment.command.call_count == 1, 'positive dispatch missing')
            print(f'PASS: mock {label} positive dispatch')

        def rejected(label, call, message):
            experiment.command.reset_mock()
            try:
                call()
            except ValueError as error:
                v.require(message in str(error), f'wrong rejection: {error}')
            else:
                raise ValueError(f'accepted negative: {label}')
            v.require(experiment.command.call_count == 0, f'tooling loaded after {label}')
            print(f'PASS: {label}; rejected before mocked tooling/SDK dispatch')

        for field, wrong in [('version', 'v24.22.3'), ('platform', 'linux'), ('arch', 'x64')]:
            observed = {**v.RUNTIME, field: wrong}
            experiment.runtime = lambda: v.runtime_check(observed)
            rejected(f'mock wrong runtime {field}', compiler, 'unsupported runtime')
        experiment.runtime = lambda: v.runtime_check(v.RUNTIME.copy())
        paths = [
            ('wrong npm version', npm_manifest, npm),
            ('wrong compiler version', root / 'b02/node_modules/typescript/package.json', compiler),
            ('wrong native compiler version', root / 'b02/node_modules/@typescript/typescript-darwin-arm64/package.json', compiler),
            ('modified SDK identity', root / 'b01/node_modules/stripe-target/package.json', sdk),
            ('modified transitive identity', root / 'b01/node_modules/qs/package.json', sdk),
            ('modified lock', root / 'b02/package-lock.json', compiler),
            ('modified manifest', root / 'b02/package.json', compiler),
        ]
        for label, path, call in paths:
            original = path.read_bytes()
            data = json.loads(original)
            data['version'] = '0.0.1-MOCK'
            path.write_text(json.dumps(data))
            rejected(label, call, 'modified identity')
            path.unlink()
            rejected('missing ' + label, call, 'missing/linked identity')
            path.write_bytes(original)
        # Even if a new manifest hash is mistakenly accepted, lock consistency rejects it.
        path = root / 'b02/package.json'
        original = path.read_bytes()
        data = json.loads(original)
        data['dependencies']['typescript'] = '0.0.1-MOCK'
        path.write_text(json.dumps(data))
        experiment.pins = copy.deepcopy(pins)
        experiment.pins['inputs']['b02']['package.json'] = v.digest(path.read_bytes())
        rejected('manifest/lock disagreement with refreshed manifest hash', compiler, 'manifest/lock mismatch')
        path.write_bytes(original)
        # Explicit trust-boundary control: implementation-only tampering is NOT authenticated.
        (root / 'b01/node_modules/stripe-target/unverified-code.js').write_text('throw new Error("MOCK");')
        experiment.command.reset_mock()
        sdk()
        v.require(experiment.command.call_count == 1, 'metadata-only trust boundary changed')
        print('PASS: documented boundary — arbitrary implementation edit not detected, code never executed')
    print('PASS: portable controls complete; disposable mock directory removed')


if __name__ == '__main__':
    main()
