"""Bounded synthetic B03 measurements; no SDK or customer-code execution."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import plistlib
import selectors
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
import uuid


HERE = Path(__file__).resolve().parent
CACHE = Path('/Volumes/AIWorkspace/caches/shiftproof/b03')
NODE = Path('/opt/homebrew/Cellar/node/26.13.0_2/bin/node')
SANDBOX = Path('/usr/bin/sandbox-exec')
CAP = 8192
ACTIONS = ('startup', 'inside-read', 'inside-write', 'outside-read', 'outside-write',
           'outside-list', 'parent-traversal', 'symlink-read', 'symlink-write',
           'async-read', 'spawn', 'exec', 'tcp', 'http', 'udp', 'environment')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mount_check():
    require(platform.system() == 'Darwin' and platform.machine() == 'arm64', 'unsupported host')
    require(Path('/Volumes/AIWorkspace').is_mount(), 'missing mount; no fallback')
    info = plistlib.loads(subprocess.check_output(['/usr/sbin/diskutil', 'info', '-plist', '/Volumes/AIWorkspace']))
    require(info['VolumeUUID'] == 'EAD8504C-B540-47B5-95EA-FBA54591ACAC', 'wrong volume')
    require(CACHE.resolve() == CACHE, 'redirected cache')


def filtered(source, inside):
    return {'HOME': str(inside), 'TMPDIR': str(inside),
            **{key: source[key] for key in ('B03_KEEP',) if key in source}}


def measure(argv, cwd, env, wall=2.0):
    """Byte/wall caps on this pipe and process group, NOT a general descendant sandbox."""
    start = time.monotonic()
    process = subprocess.Popen(list(map(str, argv)), cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               start_new_session=True, close_fds=True)
    selector = selectors.DefaultSelector()
    for name, stream in [('stdout', process.stdout), ('stderr', process.stderr)]:
        os.set_blocking(stream.fileno(), False)
        selector.register(stream, selectors.EVENT_READ, name)
    output = {'stdout': bytearray(), 'stderr': bytearray()}
    reason = 'exit'
    group_cleanup = 'sent'
    try:
        while selector.get_map():
            if time.monotonic() - start >= wall:
                reason = 'wall-limit'
                break
            for key, _ in selector.select(0.02):
                chunk = os.read(key.fileobj.fileno(), min(4096, CAP + 1 - sum(map(len, output.values()))))
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                output[key.data].extend(chunk)
                if sum(map(len, output.values())) > CAP:
                    reason = 'output-limit'
                    break
            if reason != 'exit':
                break
        # Observe leader exit without reaping it; retain PID ownership until group cleanup.
        while reason == 'exit' and os.waitid(os.P_PID, process.pid, os.WEXITED | os.WNOHANG | os.WNOWAIT) is None:
            if time.monotonic() - start >= wall:
                reason = 'wall-limit'
                break
            time.sleep(0.01)
    finally:
        # Do not reap the leader before signaling: its PID cannot be reused meanwhile.
        # This group belongs to this Popen; no host-wide process enumeration/signals.
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            group_cleanup = 'absent'
        except PermissionError:
            # macOS can reject signaling an already-exited group. Retain this as evidence,
            # never equate the attempted group signal with descendant cleanup.
            group_cleanup = 'EPERM'
            if os.waitid(os.P_PID, process.pid, os.WEXITED | os.WNOHANG | os.WNOWAIT) is None:
                process.kill()
        process.wait(timeout=2)
        selector.close()
        process.stdout.close()
        process.stderr.close()
    # Keep at most CAP bytes total; record truncation rather than interpreting it as an SDK error.
    raw_count = sum(map(len, output.values()))
    stdout = bytes(output['stdout'][:CAP])
    stderr = bytes(output['stderr'][:CAP - len(stdout)])
    return {'argv': list(map(str, argv)), 'cwd': str(cwd), 'pid': process.pid,
            'exit': process.returncode, 'termination': reason, 'groupCleanup': group_cleanup, 'observedBytes': raw_count,
            'retainedBytes': len(stdout) + len(stderr), 'elapsedMs': round((time.monotonic() - start) * 1000, 2),
            'stdout': stdout.decode(errors='replace'), 'stderr': stderr.decode(errors='replace')}


class Listeners:
    """Only ephemeral IPv4 loopback endpoints, exact synthetic request tokens."""
    def __init__(self, token):
        self.token = token.encode()
        self.stop = threading.Event()
        self.counts = {'tcp': 0, 'udp': 0}
        self.tcp = socket.socket()
        self.tcp.bind(('127.0.0.1', 0))
        self.tcp.listen(4)
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.bind(('127.0.0.1', 0))
        for sock in (self.tcp, self.udp):
            sock.settimeout(0.1)
        self.threads = [threading.Thread(target=self.serve, args=(kind,), daemon=True) for kind in ('tcp', 'udp')]
        for thread in self.threads:
            thread.start()

    def serve(self, kind):
        while not self.stop.is_set():
            try:
                if kind == 'tcp':
                    connection, _ = self.tcp.accept()
                    with connection:
                        connection.settimeout(0.3)
                        request = connection.recv(4096)
                        if b'GET /' + self.token + b' HTTP/' in request:
                            self.counts[kind] += 1
                            connection.sendall(b'HTTP/1.0 200 OK\r\nContent-Length: ' +
                                               str(len(self.token)).encode() + b'\r\n\r\n' + self.token)
                else:
                    request, address = self.udp.recvfrom(4096)
                    if request == self.token:
                        self.counts[kind] += 1
                        self.udp.sendto(self.token, address)
            except (TimeoutError, OSError):
                continue

    def close(self):
        self.stop.set()
        self.tcp.close()
        self.udp.close()
        for thread in self.threads:
            thread.join(timeout=1)
            require(not thread.is_alive(), 'listener cleanup failure')


def profile(inside, outside):
    # Diagnostic only: deny owned outside sentinels. Other host paths/services remain allowed.
    # This is deliberately NOT promoted to a production filesystem allowlist.
    quote = lambda value: json.dumps(str(value))
    return ('(version 1)\n(allow default)\n(deny network*)\n'
            f'(deny file-read* file-write* (subpath {quote(outside)}))\n'
            '(deny process-fork)\n(deny process-exec)\n'
            f'(allow process-exec (literal {quote(NODE)}))\n')


def parse_probe(record, action):
    if record['termination'] != 'exit':
        return {'outcome': 'harness-limit', 'reason': record['termination']}
    if action == 'exec' and record['exit'] == 0 and record['stdout'] == 'B03_EXEC':
        return {'outcome': 'allowed', 'value': True}
    try:
        result = json.loads(record['stdout'])
        require(result['action'] == action and result['outcome'] in ('allowed', 'denied', 'error'), 'invalid probe')
        require(record['exit'] == 0, 'probe process failure')
        return result
    except (ValueError, KeyError):
        return {'outcome': 'harness-failure', 'reason': 'no-valid-completed-probe'}


def decision():
    # Reviewed support constraints cannot be overridden by passing synthetic probes.
    manual = Path('/usr/share/man/man1/sandbox-exec.1')
    facts = {'sandboxExecPresent': SANDBOX.is_file(), 'observedNodePathPresent': NODE.is_file(),
             'sandboxExecDeprecated': 'DEPRECATED' in manual.read_text() if manual.is_file() else None,
             'approvedCompleteBoundaryImplemented': False}
    return {'replay': 'disabled', 'status': 'unknown', 'reason': 'ISOLATION_UNAVAILABLE',
            'capabilities': facts,
            'blockers': ['sandbox-exec deprecated; diagnostic policy is not a complete boundary',
                         'Node permission model excludes malicious-code protection',
                         'whole-tree resource containment and detached-child cleanup not established']}


def launch_replay(launch):
    result = decision()
    if result['replay'] != 'disabled':
        launch()
    return result


def owned_state(pid, token):
    query = subprocess.run(['/bin/ps', '-ww', '-p', str(pid), '-o', 'stat=', '-o', 'command='],
                           capture_output=True, text=True, timeout=2, env={})
    if not query.stdout.strip():
        return 'gone'
    if query.stdout.lstrip().startswith('Z'):
        return 'zombie'
    require('owned-child' in query.stdout and token in query.stdout and 'probe.cjs' in query.stdout,
            'child PID identity changed; refuse signal')
    return 'alive'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--decision', action='store_true', help='read-only no-go detection; never launch replay')
    if parser.parse_args().decision:
        print(json.dumps(decision()))
        return
    mount_check()
    require(NODE.is_file() and SANDBOX.is_file(), 'required observed mechanism absent; replay disabled')
    CACHE.mkdir(exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix='run-', dir=CACHE))
    print(f'Raw observations: {work}', flush=True)
    raw = work / 'observations.ndjson'
    def emit(row):
        with raw.open('a') as output:
            output.write(json.dumps(row) + '\n')
    observed = subprocess.check_output([NODE, '-p',
        'JSON.stringify({version:process.version,platform:process.platform,arch:process.arch})'], env={}, text=True)
    require(json.loads(observed) == {'version': 'v26.13.0', 'platform': 'darwin', 'arch': 'arm64'}, 'observed runtime drift')
    emit({'kind': 'inventory', 'runtime': json.loads(observed), 'os': platform.mac_ver()[0],
          'python': sys.version, 'node': str(NODE), 'nodeSha256': sha(NODE),
          'sandboxSha256': sha(SANDBOX), 'sourceHashes': {name: sha(HERE / name) for name in ('probe.cjs', 'run.py')}})
    token = 'b03-' + uuid.uuid4().hex
    listeners = Listeners(token)
    source_env = {'B03_SYNTHETIC_SECRET': 'B03_SYNTHETIC_ONLY', 'B03_KEEP': 'B03_PUBLIC'}
    try:
        for mechanism in ('baseline', 'sandbox-exec', 'node-permission'):
            base = work / mechanism
            inside, outside = base / 'inside', base / 'outside'
            inside.mkdir(parents=True)
            outside.mkdir()
            for directory in (inside, outside):
                (directory / 'sentinel').write_text('B03_SENTINEL')
            (inside / 'escape').symlink_to('../outside', target_is_directory=True)
            shutil.copyfile(HERE / 'probe.cjs', inside / 'probe.cjs')
            env = filtered(source_env, inside)
            prefix = [NODE]
            if mechanism == 'sandbox-exec':
                policy = base / 'diagnostic.sb'
                policy.write_text(profile(inside, outside))
                prefix = [SANDBOX, '-f', policy, NODE]
            elif mechanism == 'node-permission':
                prefix += ['--permission', f'--allow-fs-read={inside}', f'--allow-fs-write={inside}']
            def argv(action):
                return [*prefix, inside / 'probe.cjs', action, inside, outside,
                        str(listeners.tcp.getsockname()[1]), str(listeners.udp.getsockname()[1]), token]
            for action in ACTIONS:
                before = listeners.counts.copy()
                record = measure(argv(action), inside, env)
                result = parse_probe(record, action)
                emit({'kind': 'probe', 'mechanism': mechanism, 'action': action,
                      'result': result, 'listenerBefore': before, 'listenerAfter': listeners.counts.copy(), **record})
            # Environment positive control sends only our synthetic canary, never host environment.
            if mechanism == 'baseline':
                record = measure(argv('environment'), inside, {**env, **source_env})
                emit({'kind': 'environment-positive', 'result': parse_probe(record, 'environment'), **record})
            for action in ('output', 'wait'):
                record = measure(argv(action), inside, env, wall=0.4 if action == 'wait' else 2)
                emit({'kind': 'limit', 'mechanism': mechanism, 'action': action, **record})
            for action in ('parent-failure', 'detach-failure', 'detach-wait'):
                record = measure(argv(action), inside, env, wall=0.5)
                row = {'kind': 'tree', 'mechanism': mechanism, 'action': action, **record}
                messages = [json.loads(line) for line in record['stdout'].splitlines() if line.startswith('{')]
                children = [message for message in messages if 'pid' in message]
                require(len(children) <= 1, 'unexpected child count')
                for child in children:
                    require(child['token'] == token and type(child['pid']) is int, 'child identity mismatch')
                    pid = child['pid']
                    state = owned_state(pid, token)
                    row['afterGroupCleanup'] = state
                    if state == 'alive':
                        # Safe cleanup of this exact reported, token-checked synthetic child only.
                        os.kill(pid, signal.SIGKILL)
                    deadline = time.monotonic() + 1
                    while owned_state(pid, token) == 'alive' and time.monotonic() < deadline:
                        time.sleep(0.02)
                    row['afterOwnedCleanup'] = owned_state(pid, token)
                    require(row['afterOwnedCleanup'] != 'alive', 'owned child cleanup failed')
                row['messages'] = messages
                emit(row)
            emit({'kind': 'filesystem-state', 'mechanism': mechanism,
                  'insideWritten': (inside / 'written').read_text() == 'B03_WRITE',
                  'outsideWritten': (outside / 'written').exists(),
                  'symlinkWritten': (outside / 'link-written').exists(),
                  'sentinelUnchanged': (outside / 'sentinel').read_text() == 'B03_SENTINEL'})
        # Positive executable sentinel, then actual blocked dispatch to the same command.
        marker = work / 'launch-marker'
        sentinel = [NODE, '-e', 'require("node:fs").writeFileSync(process.argv[1],"B03_LAUNCHED")', marker]
        record = measure(sentinel, work, filtered(source_env, work))
        require(marker.read_text() == 'B03_LAUNCHED', 'launch sentinel positive failed')
        marker.unlink()
        called = []
        def launch():
            called.append(True)
            return measure(sentinel, work, filtered(source_env, work))
        result = launch_replay(launch)
        require(not marker.exists() and not called, 'no-go allowed launch')
        emit({'kind': 'denied-launch', 'positive': record, 'result': result,
              'dispatchCount': len(called), 'markerExists': marker.exists()})
    finally:
        listeners.close()
    emit({'kind': 'decision', **decision(), 'listenerTotals': listeners.counts,
          'sdkExecuted': False, 'externalNetworkOrDnsProbed': False})
    print(json.dumps(decision()))
    print('Measurements retained; run check.py against this file for explicit oracles.')


if __name__ == '__main__':
    main()
