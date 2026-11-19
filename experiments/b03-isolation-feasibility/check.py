"""Portable evidence/oracle checks. Does not execute any sandbox, Node or SDK."""

import argparse
import copy
import json
from pathlib import Path

from run import ACTIONS, CAP, HERE, decision, launch_replay, parse_probe, require, sha


def check(rows):
    by_kind = {}
    for row in rows:
        by_kind.setdefault(row['kind'], []).append(row)
    require(len(by_kind.get('inventory', [])) == 1, 'missing inventory')
    require(by_kind['inventory'][0]['runtime'] == {
        'version': 'v26.13.0', 'platform': 'darwin', 'arch': 'arm64'}, 'runtime drift')
    require(by_kind['inventory'][0]['sourceHashes'] == {
        name: sha(HERE / name) for name in ('probe.cjs', 'run.py')}, 'probe/supervisor source changed; new measurements required')
    probes = {(r['mechanism'], r['action']): r for r in by_kind.get('probe', [])}
    mechanisms = ('baseline', 'sandbox-exec', 'node-permission')
    require(len(probes) == len(by_kind.get('probe', [])) == 3 * len(ACTIONS), 'missing/duplicate probes')
    for mechanism in mechanisms:
        for action in ACTIONS:
            row = probes[(mechanism, action)]
            result = parse_probe(row, action)
            require(result == row['result'], 'derived result differs from raw stdout/exit')
            expected = 'denied'
            if mechanism == 'baseline' or action in ('startup', 'inside-read', 'inside-write', 'environment'):
                expected = 'allowed'
            if mechanism == 'node-permission' and action in ('symlink-read', 'symlink-write'):
                expected = 'allowed'  # A measured escape, NOT an acceptable isolation outcome.
            require(result['outcome'] == expected, f'{mechanism}/{action}: changed observation; review raw evidence')
            if expected == 'allowed':
                value = 'ready' if action == 'startup' else {'removed': True, 'kept': True} if action == 'environment' else True
                require(result['value'] == value, f'{mechanism}/{action}: positive did not work')
            else:
                require(result['code'] == ('EPERM' if mechanism == 'sandbox-exec' else 'ERR_ACCESS_DENIED'),
                        'unexpected denial class')
            if action in ('tcp', 'http', 'udp'):
                protocol = 'udp' if action == 'udp' else 'tcp'
                delta = row['listenerAfter'][protocol] - row['listenerBefore'][protocol]
                require(delta == (1 if mechanism == 'baseline' else 0), 'listener delivery disagreement')
    environments = by_kind.get('environment-positive', [])
    require(len(environments) == 1 and environments[0]['result']['value'] == {'removed': False, 'kept': True},
            'environment canary positive missing')
    limits = {(r['mechanism'], r['action']): r for r in by_kind.get('limit', [])}
    require(len(limits) == len(by_kind.get('limit', [])) == 6, 'missing/duplicate limit controls')
    for mechanism in mechanisms:
        for action in ('output', 'wait'):
            row = limits[(mechanism, action)]
            require(row['termination'] == ('output-limit' if action == 'output' else 'wall-limit'), 'wrong cap oracle')
            require(row['exit'] == -9 and row['retainedBytes'] <= CAP, 'cap or termination failed')
            require(row['groupCleanup'] == 'sent', 'live group signal failed')
            require(row['elapsedMs'] < 2500, 'bounded wait exceeded independent expiry')
    trees = {(r['mechanism'], r['action']): r for r in by_kind.get('tree', [])}
    require(len(trees) == len(by_kind.get('tree', [])) == 9, 'missing/duplicate tree controls')
    for mechanism in mechanisms:
        for action in ('parent-failure', 'detach-failure', 'detach-wait'):
            row = trees[(mechanism, action)]
            require(len(row['messages']) == 1, 'tree probe did not complete its handshake')
            if mechanism == 'baseline':
                require(row['messages'][0]['outcome'] == 'allowed', 'child positive failed')
                require(row['exit'] == (-9 if action == 'detach-wait' else 23), 'parent failure oracle')
                require(row['afterGroupCleanup'] in (('gone', 'zombie') if action == 'parent-failure' else ('alive',)),
                        'group cleanup behavior changed; investigate')
                require(row['afterOwnedCleanup'] in ('gone', 'zombie'), 'owned child still executing')
            else:
                require(row['messages'][0]['outcome'] == 'denied' and row['exit'] == 0, 'child denial failed')
                require('afterGroupCleanup' not in row, 'denied child incorrectly treated as created')
    states = {r['mechanism']: r for r in by_kind.get('filesystem-state', [])}
    require(len(states) == len(by_kind.get('filesystem-state', [])) == 3, 'missing filesystem confirmation')
    for mechanism in mechanisms:
        row = states[mechanism]
        require(row['insideWritten'] and row['sentinelUnchanged'], 'owned file control failed')
        require(row['outsideWritten'] == (mechanism == 'baseline'), 'outside write side effect mismatch')
        require(row['symlinkWritten'] == (mechanism != 'sandbox-exec'), 'symlink write side effect mismatch')
    launches = by_kind.get('denied-launch', [])
    require(len(launches) == 1 and launches[0]['positive']['exit'] == 0, 'launch positive missing')
    require(launches[0]['dispatchCount'] == 0 and not launches[0]['markerExists'], 'no-go launched executable')
    decisions = by_kind.get('decision', [])
    require(len(decisions) == 1, 'missing final decision')
    for result in (decisions[0], launches[0]['result'], decision()):
        require(result['replay'] == 'disabled' and result['status'] == 'unknown'
                and result['reason'] == 'ISOLATION_UNAVAILABLE', 'unsupported replay must stay unknown')
    require(decisions[0]['sdkExecuted'] is False and decisions[0]['externalNetworkOrDnsProbed'] is False,
            'scope expanded')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('observations', nargs='?', type=Path,
                        default=Path(__file__).parent / 'evidence/observations.ndjson')
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.observations.read_text().splitlines()]
    check(rows)
    calls = []
    require(launch_replay(lambda: calls.append(True))['status'] == 'unknown' and not calls, 'denied dispatch failed')
    # Counterexamples must not turn incomplete evidence or harness crashes into denials.
    for mutation in ('missing', 'crash', 'false-compatible'):
        changed = copy.deepcopy(rows)
        if mutation == 'missing':
            changed = [r for r in changed if not (r['kind'] == 'probe' and r['action'] == 'tcp')]
        elif mutation == 'crash':
            next(r for r in changed if r['kind'] == 'probe' and r['action'] == 'outside-read')['exit'] = -6
        else:
            next(r for r in changed if r['kind'] == 'decision')['status'] = 'compatible-within-tested-scope'
        try:
            check(changed)
        except ValueError:
            print(f'PASS: rejects {mutation} evidence')
        else:
            raise ValueError(f'accepted {mutation} evidence')
    print('PASS: 48 operation probes, 6 cap controls, 9 tree controls, environment/filesystem/denied-launch controls')
    print('NO-GO: replay disabled / unknown; no SDK executed, no external network/DNS probed')


if __name__ == '__main__':
    main()
