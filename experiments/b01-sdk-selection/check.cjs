'use strict';

const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { spawnSync } = require('node:child_process');
const root = __dirname;
const read = (path) => readFileSync(join(root, path));
const json = (path) => JSON.parse(read(path));
const hash = (path) => createHash('sha256').update(read(path)).digest('hex');
const lock = json('package-lock.json');
const fixtures = json('fixtures.json');

// Check the installed identities before importing SDK code in child processes.
for (const [path, entry] of Object.entries(lock.packages)) {
  if (!path) continue;
  const installed = json(`${path}/package.json`);
  assert.equal(installed.version, entry.version, path);
  assert.equal(installed.name, entry.name || path.slice('node_modules/'.length), path);
  assert.ok(entry.integrity.startsWith('sha512-'), path);
  for (const hook of ['preinstall', 'install', 'postinstall']) {
    assert.ok(!installed.scripts?.[hook], `${path}: unexpected install hook; review first`);
  }
}
const inputs = Object.fromEntries(['fixtures.json', 'run.cjs', 'check.cjs', 'package.json', 'package-lock.json']
  .map((path) => [path, hash(path)]));
console.log(JSON.stringify({ kind: 'provenance', node: process.version,
  platform: process.platform, arch: process.arch, inputs,
  packages: ['source', 'target'].map((side) => ({ side, ...lock.packages[`node_modules/stripe-${side}`] })) }));

const baseline = {};
for (let attempt = 1; attempt <= 3; attempt++) {
  for (const [side, version] of [['source', '12.18.0'], ['target', '13.0.0']]) {
    const child = spawnSync(process.execPath, [join(root, 'run.cjs'), side], {
      cwd: root, env: {}, encoding: 'utf8', timeout: 10000, maxBuffer: 1024 * 1024,
    });
    assert.ifError(child.error);
    assert.equal(child.status, 0, child.stderr);
    assert.equal(child.stderr, '', 'unexpected SDK diagnostics');
    const result = JSON.parse(child.stdout);
    // Emit raw capture before assertions, so failed attempts remain inspectable.
    console.log(JSON.stringify({ attempt, ...result }));
    assert.equal(result.version, version);
    const [changed, equal, failure] = result.observations;
    assert.deepEqual(result.observations.map((x) => x.scenario),
      ['retry-500-then-200', 'equal-200', 'failure-400']);
    assert.equal(changed.consumed, side === 'source' ? 1 : 2);
    assert.equal(changed.outcome.kind, side === 'source' ? 'throw' : 'return');
    if (side === 'source') {
      assert.equal(changed.outcome.class, 'StripeAPIError');
      assert.equal(changed.outcome.value.statusCode, 500);
    } else {
      assert.deepEqual(changed.outcome, equal.outcome);
    }
    assert.deepEqual(changed.events.filter((x) => x.kind === 'sleep'),
      side === 'source' ? [] : [{ kind: 'sleep', requestedMs: 500 }]);
    assert.equal(equal.consumed, 1);
    assert.equal(equal.outcome.kind, 'return');
    assert.equal(equal.outcome.value.id, 'cus_shiftproof_synthetic');
    assert.equal(equal.outcome.value.description, null);
    assert.equal(equal.outcome.value.lastResponse.statusCode, 200);
    const { lastResponse, ...customer } = equal.outcome.value;
    assert.deepEqual(customer, fixtures.scenarios[1].responses[0].body);
    assert.equal(lastResponse.body, JSON.stringify(customer));
    assert.equal(failure.consumed, 1);
    assert.equal(failure.outcome.kind, 'throw');
    assert.equal(failure.outcome.class, 'StripeInvalidRequestError');
    assert.equal(failure.outcome.value.statusCode, 400);
    assert.equal(failure.outcome.value.code, 'resource_missing');
    assert.equal(failure.outcome.value.param, 'id');
    for (const observation of [equal, failure]) {
      assert.deepEqual(observation.events.filter((x) => x.kind === 'sleep'), []);
    }
    if (attempt === 1) baseline[side] = result;
    else assert.deepEqual(result, baseline[side], 'nondeterminism blocks recommendation');
  }
}
// Equal means returned data and error behavior, not identical version-bearing UAs.
for (const index of [1, 2]) {
  assert.deepEqual(baseline.source.observations[index].outcome,
    baseline.target.observations[index].outcome);
}
console.error('PASS: 3 fresh-process repetitions per version; changed retry, equal return, equal 400 error.');
