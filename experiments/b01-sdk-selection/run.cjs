'use strict';

// Trusted B01 spike only: injected transport and clock are not a sandbox.
const assert = require('node:assert/strict');
const fixtures = require('./fixtures.json');
const side = process.argv[2];
assert.ok(['source', 'target'].includes(side));
const Stripe = require(`stripe-${side}`);
const realSetTimeout = global.setTimeout;

// Preserve undefined, null, own non-enumerable fields and array order.
// Error stacks are operational locations, outside this spike's capture dimensions.
function capture(value) {
  if (value === undefined) return { $undefined: true };
  if (value === null || ['string', 'boolean'].includes(typeof value)) return value;
  if (typeof value === 'number' && Number.isFinite(value)) return value;
  if (Array.isArray(value)) return value.map(capture);
  assert.ok(value instanceof Error || Object.getPrototypeOf(value) === Object.prototype,
    'unsupported captured value');
  return Object.fromEntries(Object.getOwnPropertyNames(value)
    .filter((key) => !(value instanceof Error && key === 'stack'))
    .map((key) => [key, capture(value[key])]));
}

async function run(scenario) {
  let clock = fixtures.clockStartMs;
  let consumed = 0;
  let transportFailure;
  const events = [];
  Date.now = () => clock;
  Math.random = () => fixtures.randomValue;
  global.setTimeout = (callback, delay, ...args) => {
    events.push({ kind: 'sleep', requestedMs: delay });
    return realSetTimeout(() => {
      clock += delay;
      callback(...args);
    }, 0);
  };

  class OfflineResponse extends Stripe.HttpClientResponse {
    constructor(response) {
      super(response.status, structuredClone(response.headers));
      this.body = JSON.stringify(response.body);
      this.raw = { statusCode: response.status, headers: this._headers, body: this.body };
    }
    getRawResponse() { return this.raw; }
    async toJSON() { return JSON.parse(this.body); }
  }
  class OfflineClient extends Stripe.HttpClient {
    getClientName() { return 'shiftproof-offline-fixture'; }
    async makeRequest(host, port, path, method, headers, body, protocol, timeout) {
      try {
        assert.equal(host, 'offline.invalid');
        assert.equal(path, `/v1/customers/${fixtures.customerId}`);
        assert.equal(method, 'GET');
        assert.ok(!Object.keys(headers).some((key) => key.toLowerCase() === 'authorization'));
        assert.ok(consumed < scenario.responses.length, 'unexpected extra request');
        events.push({ kind: 'transport-request', request: capture({
          host, port, path, method, headers, body, protocol, timeout,
        }) });
        const response = new OfflineResponse(scenario.responses[consumed++]);
        events.push({ kind: 'transport-response', response: capture(response.raw) });
        return response;
      } catch (error) {
        transportFailure = error;
        throw error;
      }
    }
  }

  const client = new Stripe(null, {
    host: 'offline.invalid', apiVersion: fixtures.apiVersion,
    telemetry: false, httpClient: new OfflineClient(),
  });
  // Node's SDK otherwise shells out to uname -a. Replace only this diagnostic
  // input with synthetic text; leave request/retry/error implementation intact.
  client._platformFunctions.getUname = async () => 'shiftproof-synthetic-platform';
  client.on('request', (value) => events.push({ kind: 'sdk-request', value: capture(value) }));
  client.on('response', (value) => events.push({ kind: 'sdk-response', value: capture(value) }));
  let outcome;
  try {
    outcome = { kind: 'return', value: capture(await client.customers.retrieve(fixtures.customerId)) };
  } catch (error) {
    if (!(error instanceof Stripe.errors.StripeError)) throw error;
    outcome = { kind: 'throw', class: error.constructor.name, value: capture(error) };
  }
  if (transportFailure) throw transportFailure;
  return { scenario: scenario.id, consumed, events, outcome };
}

(async () => {
  const observations = [];
  for (const scenario of fixtures.scenarios) observations.push(await run(scenario));
  process.stdout.write(JSON.stringify({ side, version: Stripe.PACKAGE_VERSION, observations }) + '\n');
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
