"""Trusted B02 experiment, not a customer-code sandbox. Python 3.11+ with tar data filter."""

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import platform
import plistlib
import shutil
import subprocess
import tarfile
import tempfile


HERE = Path(__file__).resolve().parent
B01 = HERE.parent / 'b01-sdk-selection'
CACHE = Path('/Volumes/AIWorkspace/caches/shiftproof/b02')
NODE_DIR = 'node-v26.13.1-darwin-arm64'
RUNTIME = {'version': 'v26.13.1', 'platform': 'darwin', 'arch': 'arm64'}
HOOKS = ('preinstall', 'install', 'postinstall', 'prepare', 'prepublish',
         'prepublishOnly', 'prepack', 'postpack')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text())


def check_hash(path, expected):
    require(path.is_file() and not path.is_symlink(), f'missing/linked identity: {path}')
    require(digest(path.read_bytes()) == expected, f'modified identity: {path}')


def inventory(path):
    """Read bytes, never import package code. Include nested/bundled manifests."""
    records = []
    with tarfile.open(path) as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            name = Path(member.name).name
            if name == 'package.json':
                data = archive.extractfile(member).read()
                manifest = json.loads(data)
                records.append({'path': member.name, 'kind': 'manifest',
                                'sha256': digest(data), 'name': manifest.get('name'),
                                'version': manifest.get('version'),
                                'license': manifest.get('license'),
                                'engines': manifest.get('engines'),
                                'hooks': {k: v for k, v in manifest.get('scripts', {}).items()
                                          if k in HOOKS}})
            elif name.upper().startswith(('LICENSE', 'LICENCE', 'COPYING', 'NOTICE')):
                records.append({'path': member.name, 'kind': 'license',
                                'sha256': digest(archive.extractfile(member).read())})
    return sorted(records, key=lambda row: row['path'])


def archive_check(path, entry):
    check_hash(path, entry['sha256'])
    if entry.get('integrity'):
        actual = 'sha512-' + base64.b64encode(hashlib.sha512(path.read_bytes()).digest()).decode()
        require(actual == entry['integrity'], f'tarball integrity: {path}')
    if entry.get('shasum'):
        require(hashlib.sha1(path.read_bytes()).hexdigest() == entry['shasum'],
                f'registry SHA-1: {path}')


def runtime_check(observed):
    require(observed == RUNTIME, f'unsupported runtime: {observed}')


def inputs_check(root, expected):
    for name, sha in expected.items():
        check_hash(root / name, sha)
    manifest, lock = load(root / 'package.json'), load(root / 'package-lock.json')
    require(lock['lockfileVersion'] == 3, 'lock format must be 3')
    for field in ('name', 'version', 'dependencies', 'engines'):
        require(manifest.get(field) == lock['packages'][''].get(field),
                f'manifest/lock mismatch: {field}')
    for name, entry in lock['packages'].items():
        if name:
            require(entry['resolved'].startswith('https://registry.npmjs.org/'), 'artifact origin')
            require(entry['integrity'].startswith('sha512-'), 'missing lock integrity')


def installed_check(root, records):
    # Metadata detects identity drift, not arbitrary modifications to implementation files.
    for row in records:
        if row['kind'] == 'manifest':
            relative = Path(row['path']).parts[1:]
            check_hash(root.joinpath(*relative), row['sha256'])


def applicable(entry):
    return ('os' not in entry or 'darwin' in entry['os']) and (
        'cpu' not in entry or 'arm64' in entry['cpu'])


def packages_check(root, artifacts, inventories):
    for name, entry in load(root / 'package-lock.json')['packages'].items():
        if not name or not applicable(entry):
            continue
        filename = entry['resolved'].rsplit('/', 1)[-1]
        require(entry['integrity'] == artifacts[filename]['integrity'], 'lock/archive mismatch')
        installed_check(root / name, inventories[filename])


def mount_check():
    require(platform.system() == 'Darwin' and platform.machine() == 'arm64',
            'manual run supports darwin-arm64 only')
    require(Path('/Volumes/AIWorkspace').is_mount(), 'AIWorkspace mount missing; no fallback')
    info = plistlib.loads(subprocess.check_output(['/usr/sbin/diskutil', 'info', '-plist',
                                                '/Volumes/AIWorkspace']))
    require(info['VolumeUUID'] == 'EAD8504C-B540-47B5-95EA-FBA54591ACAC', 'wrong volume')
    require(CACHE.resolve() == CACHE, 'cache path must not redirect through symlinks')


def environment(work):
    for name in ('home', 'tmp', 'config'):
        (work / name).mkdir(exist_ok=True)
    for name in ('user.npmrc', 'global.npmrc'):
        (work / 'config' / name).write_text('')
    # Deliberately no inherited credentials, NODE_OPTIONS, NODE_PATH or user npm config.
    return {'HOME': str(work / 'home'), 'TMPDIR': str(work / 'tmp'),
            'NPM_CONFIG_USERCONFIG': str(work / 'config/user.npmrc'),
            'NPM_CONFIG_GLOBALCONFIG': str(work / 'config/global.npmrc'),
            'NPM_CONFIG_CACHE': str(CACHE / 'npm-cache'),
            'NPM_CONFIG_IGNORE_SCRIPTS': 'true', 'NPM_CONFIG_AUDIT': 'false',
            'NPM_CONFIG_FUND': 'false', 'NPM_CONFIG_UPDATE_NOTIFIER': 'false',
            'NPM_CONFIG_ENGINE_STRICT': 'true'}


class Experiment:
    def __init__(self, work):
        self.work = work
        self.env = environment(work)
        self.pins = load(HERE / 'pins.json')
        self.artifacts = self.pins['artifacts']
        self.inventories = {}
        for row in (HERE / 'inventory.ndjson').read_text().splitlines():
            record = json.loads(row)
            self.inventories[record['archive']] = record['records']
        self.node = CACHE / 'tools' / NODE_DIR / 'bin/node'
        self.npm = CACHE / 'npm-12.2.3/package'

    def command(self, args, cwd=None, status=0):
        args = list(map(str, args))
        result = subprocess.run(args, cwd=cwd or self.work, env=self.env,
                                text=True, capture_output=True, timeout=120)
        # Preserve failures before asserting; never replace earlier runs.
        with (self.work / 'commands.ndjson').open('a') as output:
            output.write(json.dumps({'argv': args, 'cwd': str(cwd or self.work),
                                     'status': result.returncode, 'stdout': result.stdout,
                                     'stderr': result.stderr}) + '\n')
        require(result.returncode == status,
                f'command exit {result.returncode}, expected {status}: {args}\n{result.stderr}')
        return result

    def runtime(self):
        check_hash(self.node, self.pins['nodeBinarySha256'])
        observed = json.loads(self.command([self.node, '-p',
            'JSON.stringify({version:process.version,platform:process.platform,arch:process.arch})']).stdout)
        runtime_check(observed)

    def npm_command(self, args, cwd=None):
        self.runtime()
        installed_check(self.npm, self.inventories['npm-12.2.3.tgz'])
        return self.command([self.node, self.npm / 'bin/npm-cli.js', *args,
                             '--ignore-scripts', '--no-audit', '--no-fund'], cwd)

    def package_command(self, label, args, status=0):
        self.runtime()
        root = self.work / label
        inputs_check(root, self.pins['inputs'][label])
        packages_check(root, self.artifacts, self.inventories)
        return self.command([self.node, *args], root, status)

    def provision(self):
        for name, entry in self.artifacts.items():
            path = CACHE / 'downloads' / name
            if not path.exists():
                self.command(['/usr/bin/curl', '--fail', '--silent', '--show-error', '--location',
                              '--proto', '=https', '--proto-redir', '=https',
                              '--output', path, entry['url']])
            archive_check(path, entry)
            require(inventory(path) == self.inventories[name], f'unreviewed inventory: {name}')
        for name, destination in [(NODE_DIR + '.tar.gz', CACHE / 'tools'),
                                  ('npm-12.2.3.tgz', CACHE / 'npm-12.2.3')]:
            if not destination.exists():
                destination.mkdir()
                with tarfile.open(CACHE / 'downloads' / name) as archive:
                    archive.extractall(destination, filter='data')
        for name in self.artifacts:
            if name.endswith('.tgz') and name != 'npm-12.2.3.tgz':
                self.npm_command(['cache', 'add', CACHE / 'downloads' / name, '--offline'])

    def run(self):
        self.runtime()
        inputs_check(HERE, self.pins['inputs']['b02'])
        inputs_check(B01, self.pins['inputs']['b01'])
        require(self.npm_command(['--version']).stdout.strip() == '12.2.3', 'npm version')
        for label, source in [('b01', B01), ('b02', HERE)]:
            destination = self.work / label
            destination.mkdir()
            for name in self.pins['inputs'][label]:
                shutil.copyfile(source / name, destination / name)
            inputs_check(destination, self.pins['inputs'][label])
            self.npm_command(['ci', '--offline'], destination)
            inputs_check(destination, self.pins['inputs'][label])
            packages_check(destination, self.artifacts, self.inventories)
        compiler = self.work / 'b02/node_modules/typescript/bin/tsc'
        def compile_(args, status=0):
            return self.package_command('b02', [compiler, *args], status)
        require(compile_(['--version']).stdout.strip() == 'Version 7.0.2', 'compiler version')
        compile_(['good.ts', '--strict', '--target', 'ES2022', '--module', 'commonjs',
                  '--outDir', 'out', '--noEmitOnError'])
        self.command([self.node, self.work / 'b02/out/good.js'])
        bad = compile_(['bad.ts', '--strict', '--noEmit', '--pretty', 'false'], status=1)
        require('error TS2322' in bad.stdout and "not assignable to type 'string'" in bad.stdout,
                'type-error control did not diagnose assignment')
        capture = self.package_command('b01', [self.work / 'b01/check.cjs'])
        (self.work / 'observations.ndjson').write_text(capture.stdout)
        compare(B01 / 'observations.ndjson', self.work / 'observations.ndjson')
        print(f'PASS: fresh offline installs, compile/type-error, 18 B01 scenarios; {self.work}')


def compare(old_path, new_path):
    old = [json.loads(x) for x in old_path.read_text().splitlines()]
    new = [json.loads(x) for x in new_path.read_text().splitlines()]
    require(len(old) == len(new) == 7, 'capture count')
    require(old[0]['node'] == 'v26.13.0' and new[0]['node'] == 'v26.13.1', 'capture runtime')
    # Preserve raw evidence. Normalize only the two explicitly version-bearing fields.
    new[0]['node'] = old[0]['node']
    for row in new[1:]:
        for observation in row['observations']:
            for event in observation['events']:
                if event['kind'] == 'transport-request':
                    headers = event['request']['headers']
                    ua = json.loads(headers['X-Stripe-Client-User-Agent'])
                    require(ua['lang_version'] == 'v26.13.1', 'unexpected SDK runtime UA')
                    ua['lang_version'] = 'v26.13.0'
                    headers['X-Stripe-Client-User-Agent'] = json.dumps(ua, separators=(',', ':'))
    require(old == new, 'B01 semantic/provenance difference outside explicit runtime fields')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('provision', 'run'))
    args = parser.parse_args()
    mount_check()
    CACHE.mkdir(exist_ok=True)
    (CACHE / 'downloads').mkdir(exist_ok=True)
    (CACHE / 'npm-cache').mkdir(exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix=args.mode + '-', dir=CACHE))
    print(f'Raw logs: {work}', flush=True)
    experiment = Experiment(work)
    if args.mode == 'provision':
        experiment.provision()
    else:
        experiment.run()


if __name__ == '__main__':
    main()
