# B01: SDK/version selection evidence

Status: **`stripe` 12.18.0 → 13.0.0 selected for research**, accepted in
[PR #10](https://github.com/Himanshu-singh04/shiftproof/pull/10), merged as
`6efbbd35398dd08a9232bd24cffda0d84fdb474b` after coordinator verification and founder
approval. No shipped SDK compatibility is claimed. This is research for
[issue #9](https://github.com/Himanshu-singh04/shiftproof/issues/9), not a migration
recommendation for a real application or approval of runtime/isolation ADRs.

## Original request and bounded scope

Original founder instruction: “ok proceed”, responding to assigning the first
bounded decision tasks, including SDK-version selection for ShiftProof.

Compare at most three packages within two working days. Recommend one exact pair
only after actual pinned artifacts reproduce a documented semantic difference,
an unchanged control and a failure/unsupported scenario without service access.
Preserve synthetic inputs, raw observations, lockfile and exact rerun commands.
No product adapter, CLI, analyzer or report implementation is authorized.

Acceptance follows issue #9 A1–A6: candidate identity/licensing/citations;
actual offline differential evidence; reproducible provisioning and provenance;
narrow capture seam with honest isolation gaps; recommendation with remaining
gates and current provisioning status; issue-linked, attributed and verified PR.

## Candidate matrix (two packages)

Public metadata and official documentation were retrieved on 2026-11-19. These
are historical pairs chosen for a documented, reproducible change, not suggested
current production dependencies. No customer demand or market validation was measured.

| SDK / exact pair | Product fit, artifacts and license | Evidence and disposition |
| --- | --- | --- |
| `stripe` **12.18.0 → 13.0.0** | Stripe's service SDK for payments/billing/customer APIs, with bundled TypeScript declarations; not a generic HTTP utility. Official npm [source metadata](https://registry.npmjs.org/stripe/12.18.0) and [target metadata](https://registry.npmjs.org/stripe/13.0.0) advertise MIT tarballs; both were actually installed. Registry gitHeads: `ca229a6e9eda6f2da2b041dc36e6035f14f578f6` and `3799c9a611b1f5c7d7718157f20d4046a91a811e`. | **Propose**: C1–C5 below document retry/return/error semantics and the HTTP injection seam. Three repeated runs on each actual artifact reproduce the difference and controls. Two direct dependency declarations (`qs`, `@types/node`), 23 installed packages including the two aliases. Trade-offs: old pair; a private diagnostic shim; broader v13 API changes are excluded. |
| `@aws-sdk/client-s3` **3.726.1 → 3.729.0** | AWS's S3 service SDK, with bundled TypeScript declarations and service commands. Official npm [source metadata](https://registry.npmjs.org/@aws-sdk/client-s3/3.726.1) and [target metadata](https://registry.npmjs.org/@aws-sdk/client-s3/3.729.0) advertise Apache-2.0 tarballs. Availability here is registry metadata only; neither artifact was installed or executed. | **Reject for this first spike**, not intrinsically unsuitable: C6 documents default integrity protections, but the target is explicitly deprecated for GetObject checksum validation problems (C7). Its many AWS/Smithy middleware, signing and credential-provider dependencies widen the review/clock/state surface. A later candidate could use a corrected target; this bounded task does not silently substitute one. |

Artifact URLs for Stripe are `https://registry.npmjs.org/stripe/-/stripe-12.18.0.tgz`
and `https://registry.npmjs.org/stripe/-/stripe-13.0.0.tgz`. The lockfile records both
SHA-512 integrity values and all transitives. S3 metadata advertises
`https://registry.npmjs.org/@aws-sdk/client-s3/-/client-s3-3.726.1.tgz` and
`https://registry.npmjs.org/@aws-sdk/client-s3/-/client-s3-3.729.0.tgz`.
No S3 behavior is represented as observed.

## Version-scoped citations and expectations

Short excerpts are retained here, with publisher attribution and exact locators.
Stripe's installed MIT documentation/source was inspected before execution;
its notice is retained in [UPSTREAM-NOTICE.txt](../experiments/b01-sdk-selection/UPSTREAM-NOTICE.txt).
SDK source is provisioned from npm, not vendored into Git. AWS's release-note
fragment is attributed to the AWS SDK for JavaScript team ([Apache-2.0 license](https://github.com/aws/aws-sdk-js-v3/blob/v3.729.0/LICENSE)).

- **C1 — Stripe v13 release**: [immutable CHANGELOG, 13.0.0 section, line 7](https://github.com/stripe/stripe-node/blob/3799c9a611b1f5c7d7718157f20d4046a91a811e/CHANGELOG.md#L7):
  “Change the default behavior to perform 1 reattempt on retryable request failures
  (previously the default was 0).” The same section states the default API version
  becomes `2023-08-16`; our explicit `2022-11-15` configuration holds that separate
  change constant. Full retrieved changelog SHA-256:
  `251adac2d85f29a6dfc82f0fb395e5aa45df90a6a082a526b48cb0471fd90644`.
- **C2 — Stripe source-side docs**: [12.18.0 README, Network retries](https://github.com/stripe/stripe-node/blob/ca229a6e9eda6f2da2b041dc36e6035f14f578f6/README.md#network-retries):
  “Automatic network retries can be enabled with the `maxNetworkRetries` config option.”
  Installed README lines 254–258 and source `cjs/stripe.core.js:74` (default `0`)
  establish the baseline; this is not inferred merely from a major version number.
- **C3 — Stripe target-side docs**: [13.0.0 README, Network retries](https://github.com/stripe/stripe-node/blob/3799c9a611b1f5c7d7718157f20d4046a91a811e/README.md#network-retries):
  “stripe-node will automatically do one reattempt for failed requests that are safe
  to retry.” Installed README line 256 and `cjs/stripe.core.js:74` (default `1`).
  Both READMEs' “Examining Responses” describe `lastResponse.requestId/statusCode`.
- **C4 — Retry and response/error oracle**: Stripe's versioned
  [source RequestSender](https://github.com/stripe/stripe-node/blob/ca229a6e9eda6f2da2b041dc36e6035f14f578f6/src/RequestSender.ts)
  and [target RequestSender](https://github.com/stripe/stripe-node/blob/3799c9a611b1f5c7d7718157f20d4046a91a811e/src/RequestSender.ts).
  Inspected shipped `cjs/RequestSender.js:135–169` on both sides: exhausted retry
  budgets stop; absent retry directives, status >=500 retries and 400 does not.
  Lines 171–187 compute the first 500-ms delay. Lines 72–129 return JSON or construct
  errors; `cjs/Error.js:5–23` maps `api_error` to `StripeAPIError` and
  `invalid_request_error` to `StripeInvalidRequestError`. Thus C4 supports both
  the 200 control and 400 failure, not a claim that a real server returns our fixture.
- **C5 — Injection seam**: Stripe's [13.0.0 HttpClient source](https://github.com/stripe/stripe-node/blob/3799c9a611b1f5c7d7718157f20d4046a91a811e/src/net/HttpClient.ts)
  (identical shipped `cjs/net/HttpClient.js` in 12.18.0). Lines 7–11 document a
  custom client extending `HttpClient` and response extending `HttpClientResponse`.
  Inspected constructor accepts `httpClient` on both sides. Customers' shipped
  `cjs/resources/Customers.js:9` declares GET `/v1/customers/{customer}`.
- **C6 — AWS 3.729.0 release**: [versioned client-s3 CHANGELOG](https://github.com/aws/aws-sdk-js-v3/blob/v3.729.0/clients/client-s3/CHANGELOG.md),
  3.729.0 / Features, describes “new default integrity protections for S3 requests.”
  Applicable to the target, not proof of an observed change against 3.726.1.
  Full retrieved file SHA-256:
  `6d9a76eb71649dba009792154325695ffdf44398faa63f7b3f790ffec9e35f3e`.
- **C7 — AWS registry deprecation**: target metadata linked above says
  “Please upgrade to >=3.735.0, which contains fixes for checksum validation in S3
  getObject calls” and links [upstream issue #6827](https://github.com/aws/aws-sdk-js-v3/issues/6827).
  This is exact-version metadata observed on the retrieval date, not a live-service test.

Hashes of the installed Stripe documentation and behavior-bearing files (SHA-256):

| File | 12.18.0 | 13.0.0 |
| --- | --- | --- |
| `README.md` | `c16573a28fc04513db812f2336bdb23527a6d9bb5526205d13163995cd2e9152` | `7df3f8a99774079635135bcf2b2fb09426c9e07420938576b51d5ac91f54a636` |
| `cjs/stripe.core.js` | `ab5b59fa0d75c2c0ce2b53d2088e320bece20752e9e53e868a3b902954cc6877` | `5535c1726f3f8b3e43403ecf187b7a67654ea914ca6e58a2645fad4e99d0dd5d` |
| `cjs/RequestSender.js` | `4e26afd029a043660fc1a954cc5b85c1fc3e0032b7dc7da9b786e4453da94cdd` | `3e6e337426f6fba964e3e24402737f7df3136c6cbcb88699642293a9ffb6610e` |
| `cjs/net/HttpClient.js` | `562c6baa3f5d4bd8c301b9988482c4ac4170f198d08e59ce50bdad26d33481a5` | same |
| `cjs/Error.js` | `3d7cdd0001780a7ae37db5df38678958785413eabd89f34476a07c919e4333fa` | same |

## Reproduction and provenance

Research files live in [experiments/b01-sdk-selection](../experiments/b01-sdk-selection).
Observed execution environment: **Node v26.13.0, npm 11.20.0, darwin arm64**.
These are observations, not B02's supported-runtime or TypeScript choices.
The harness is plain CommonJS JavaScript exercising the SDK's shipped Node entrypoint;
no transpilation, customer imports or new framework is involved.

From the repository root on the coordinator/worker host, provision public packages
(network allowed only here). The exact observed command is retained:

```sh
npm ci --prefix experiments/b01-sdk-selection --ignore-scripts --no-audit --no-fund --cache /Volumes/AIWorkspace/caches/shiftproof/npm
```

On this host, the authorized pendrive checkout/cache remain mandatory. Verify the
AIWorkspace mount using the provisioning procedure before execution; if it is
missing or unwritable, stop. Do not recreate its mount path or fall back to Mac
storage. The command above is not itself a mount-identity enforcement mechanism.

**External reviewers on a different host** may explicitly choose a writable cache
outside their checkout, without requiring the AIWorkspace mount. For example, from
their repository root in a POSIX shell:

```sh
REVIEW_CACHE="$HOME/.cache/shiftproof-b01/npm"
npm ci --prefix experiments/b01-sdk-selection --ignore-scripts --no-audit --no-fund --cache "$REVIEW_CACHE"
```

Replace that assignment with an appropriate writable absolute path on the reviewer's
host. This is a separate external-reviewer example, not an automatic fallback for
the coordinator/worker host. It has not been executed on another host. The check
below resolves research files relative to its checkout; captured runtime/platform
metadata can differ from the retained darwin arm64 observation.

Then the **one-command offline spike check** is:

```sh
node experiments/b01-sdk-selection/check.cjs
```

It prints raw NDJSON to stdout and a PASS summary to stderr; assertion failure,
unexpected SDK diagnostics, child timeout or differing repeat observations exits
nonzero. It never provisions packages. Save stdout outside Git for independent
comparison; do not overwrite the reviewed [observations.ndjson](../experiments/b01-sdk-selection/observations.ndjson).

Initial provisioning ran `npm install --ignore-scripts --no-audit --no-fund --cache
/Volumes/AIWorkspace/caches/shiftproof/npm` in the experiment directory: 23 packages.
A clean `npm ci --offline --ignore-scripts --no-audit --no-fund --cache
/Volumes/AIWorkspace/caches/shiftproof/npm` in that directory also installed 23
packages successfully from the provisioned cache. The spike passed after this reinstall.
Offline installation requires a populated cache; missing artifacts must fail, not
silently fetch. Do not run `npm update` to reproduce this decision.

The committed npm lockfile v3 pins both aliases at logical paths
`node_modules/stripe-source` and `node_modules/stripe-target` and all transitives
(including shared `qs` 6.17.1 and `@types/node` 26.6.6). It records current resolution
of upstream ranges, not the dependency tree used by Stripe in 2023. `npm ci` checks
tarball integrity; the spike checks installed names/versions before importing.
Hashes bind content, not publisher authenticity or a tamper-proof installation.
Fresh side processes avoid sharing module state even though transitive files are shared.

All 23 installed manifests were inspected for lifecycle hooks. No preinstall,
install or postinstall hooks were present; upstream prepack/build scripts exist
but were not run. Every install disables scripts/audit/funding; no global tools
or configuration changed. No dependency or cache content is committed.

[fixtures.json](../experiments/b01-sdk-selection/fixtures.json) and the harness are
original product-owned synthetic work for this issue, not copied customer or SDK
test fixtures. The repository has no root LICENSE; the private experiment is
`UNLICENSED` and grants no new license to repository-owned material. Stripe is MIT;
installed transitives are MIT except `qs` (BSD-3-Clause), as recorded in the lock.
The synthetic customer, request IDs, error messages and null/empty fields were
reviewed before retention. No API key is supplied, no Authorization header is
permitted, and no credentials or customer evidence appear in the captures.

### Historical dependency maintenance

The scoped npm entry in [.github/dependabot.yml](../.github/dependabot.yml) follows
the existing Monday/weekly schedule, three-open-version-PR limit and `chore(deps)`
prefix. Stripe 12.18.0 and 13.0.0 are fixed experimental inputs. Ignore rules name
both manifest aliases (`stripe-source`, `stripe-target`) and their real package
name (`stripe`); `versioning-strategy: lockfile-only` additionally forbids updates
requiring manifest changes. These exclusions apply to security updates too: an
advisory affecting a historical Stripe artifact needs explicit triage and a bounded
decision to retain, retire or replace the experiment, not an automatic pair upgrade.

Coverage is deliberately limited: unignored vulnerable transitives in the lockfile
remain eligible for Dependabot security-update PRs where remediation is possible
within the fixed pair. This is not a promise to routinely refresh every non-vulnerable
npm transitive. GitHub's [official options reference](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)
(consulted 2026-11-19, `allow`, `ignore`, `versioning-strategy`, and
`open-pull-requests-limit`) distinguishes default direct version updates from
lockfile security updates; it does not list npm as supporting `dependency-type: indirect`
under `allow`. Its `lockfile-only` definition says to ignore versions requiring manifest
changes. Security updates have a separate limit; the three-PR cap is for version PRs.

The [upstream npm parser](https://github.com/dependabot/dependabot-core/blob/main/npm_and_yarn/lib/dependabot/npm_and_yarn/file_parser.rb)
was inspected on the same date: `dealias_package` can map an npm alias to its real
name, while `ignore_requirement?` skips alias requirements when de-aliasing is off.
The three explicit ignores cover the alias and normalized names; they do not rely
on aliases remaining unsupported. No hosted Dependabot update run was performed in
this correction; actual proposal behavior must be inspected when the configuration
reaches the default branch.

Any proposed transitive change, including a security fix, changes the experiment's
identity. Before merging, verify both exact Stripe aliases and their lock entries,
inspect the dependency diff, perform script-disabled provisioning, capture a new
three-repeat spike result, compare it to the prior evidence, and obtain coordinator
review and founder approval. Preserve the old revision/captures for comparison;
never reuse old observations as proof for a changed lockfile. Non-security transitive
refreshes require a bounded maintenance issue and the same evidence. If a fix cannot
preserve the pair, record the limitation and escalate instead of silently changing it.

## Observed results

Same `customers.retrieve('cus_shiftproof_synthetic')` call and immutable fixture
sequence on each side. No `maxNetworkRetries` override is supplied. API version is
explicitly `2022-11-15`, host `offline.invalid`, telemetry disabled. Each scenario
gets a new client/response sequence; each side/attempt gets a fresh process with
empty environment. Input and lockfile SHA-256 values are in the provenance row.

| Scenario / oracle | Source 12.18.0 | Target 13.0.0 |
| --- | --- | --- |
| `retry-500-then-200` / C1–C4 | One request; consumes 500 only; throws `StripeAPIError`, status 500, message `Synthetic temporary failure`; no sleep | Two requests; consumes 500 then 200; requests one 500-ms sleep; returns the synthetic customer |
| `equal-200` / C2–C4 | One request; returns fixture JSON with `description: null`, empty metadata and `lastResponse.statusCode: 200` | Same complete captured return, including non-enumerable `lastResponse` |
| `failure-400` / C4 | One request; throws `StripeInvalidRequestError`, status 400, code `resource_missing`, param `id`; no retry | Same complete captured error; no retry |

Three repetitions per version (six fresh processes, 18 scenario executions) were
identical within each side across the entire captured value/event sequence. There
was no observed nondeterminism. This is not a benchmark or a whole-SDK evaluation.
The extra attempt and throw-to-return change are semantic observations, not compile
failures or version-string comparisons. The 400 case is an expected SDK failure,
not a harness crash or a declaration that the upgraded SDK is defective.

Raw captures retain ordered request/response and SDK events, all request arguments,
response status/headers/JSON text, requested sleep durations, returned own fields
and structured errors. `undefined` is tagged `{"$undefined":true}`; omitted keys
remain omitted and null remains null. Error stacks (host/source locations) are
outside the declared capture surface; unsupported object types fail the capture.
No output normalization is applied. Version-bearing User-Agent headers differ and
remain visible: the equal control asserts returned-data/error semantics and count,
not complete wire equality. Raw request headers are not discarded to manufacture equality.

## Capture seam, controls and unsupported capabilities

| Boundary | Measured or controlled | Explicit limit |
| --- | --- | --- |
| `HttpClient.makeRequest` / `HttpClientResponse` | Actual SDK constructs requests and decides retries; injected transport records arguments and returns JSON fixtures | No sockets, TLS, actual service behavior or native transport timeout semantics tested |
| Clock and randomness | `Date.now()` starts at `1700000000000`; `Math.random()` returns `0.25`; timer shim records the SDK-requested delay and advances virtual time before callback | Scheduled delay is observed, not elapsed wall time; no general fake-clock framework or backoff-range validation |
| Diagnostic platform input | One private shim, `_platformFunctions.getUname`, returns `shiftproof-synthetic-platform`; inspected Node implementation otherwise executes `uname -a` | Diagnostic path not exercised; shim stability is a future adapter review obligation |
| Authentication/state | Null key, no auth header; GET avoids POST UUID/idempotency generation; telemetry off; fresh clients/processes; child env `{}` | No auth, POST idempotency, connection resets, telemetry, pagination, streams, webhooks or arbitrary argument coverage |
| Failure signals | 400/500 structured errors, unexpected request rejection, identity checks, repeat comparison; parent 10-second timeout and 1-MiB output cap | Not descendant/resource sandboxing; no adversarial process/filesystem/network-denial probes |

This trusted spike was explicitly authorized before B03. It does **not** enforce
egress denial, filesystem confinement or process isolation. Injected transport and
an invalid hostname are not a security boundary. B03 must test OS-level enforcement
and cleanup or disable product replay; future product evidence stays unknown if
isolation is unavailable. These research observations are not a valid product
RunRecord or a callsite-scoped `incompatible` result under the evidence contract.

The seam is practical for a narrow future adapter: only one service call and a
small transport interface need instrumentation, without customer code. The private
diagnostic shim and loaded Node modules remain review obligations. Shared dependency
resolution, runtime pinning, clocks, redaction and unsupported values must be made
explicit in B02/B03/B04/B06 rather than inheriting this trusted harness as production code.

## Recommendation and remaining gates

Stripe 12.18.0 → 13.0.0 is accepted for reproducible retry/error/return research. Its
benefit is a directly documented semantic change with a small offline seam. Its
cost is deliberately narrow and historical coverage; fixing API version excludes
the concurrent remote API-version change, not evidence of compatibility with it.
No package publication, pilot, paid service, product inference or production feature
was undertaken. No third candidate is needed to justify this bounded recommendation.

- Coordinator independent A1–A6 verification and founder approval completed in
  PR #10. The pair is selected for research; shipped SDK support remains unimplemented.
- B02/ADR-01: select supported Node/TypeScript/package manager and lockfile policy;
  measure clean installation and identity rejection rather than adopting this machine's runtime.
- B03/ADR-03: enforce egress/filesystem/process limits, filtered environment,
  descendant cleanup and unsupported-platform behavior before product replay.
- B04/ADR-04: pair-specific schema/citation/mapping/capture validation; no callsite
  mapping or aggregate compatibility claim exists here.
- B06 and later: review actual adapter coverage, default API-version differences,
  failure/unknown handling and fixture representativeness before implementation.

Planning PR #5 and App-rename PR #7 are merged, and
[provisioning #8](https://github.com/Himanshu-singh04/shiftproof/issues/8#issuecomment-6999733805)
is complete. The handoff main SHA was `24c8760cbb0d1c0ddc55f7858525484e569afa49`;
branch creation followed fetch and a successful fast-forward-only synchronization.
Worker history/OAuth is on pendrive; coordinator history and the App key remain
on Mac. Worker inference uses the existing subscription; product inference is
unprovisioned, optional and unnecessary for this experiment. Planning/provisioning
completion does not resolve any technical gate above.

## Verification record

The PR timeline records exact pushed SHAs, foundation checks and CI links. The
spike command above passed initially and after clean offline reinstall, including
strict repeat equality and all three independent scenario oracles.

Local foundation results: `python3 scripts/check_repository.py` passed;
`python3 -m unittest discover -s scripts -p 'test_*.py'` passed all **25 tests**;
`/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=`
passed (exit 0); `git diff --check` and `git diff --cached --check` passed.
Retained capture input hashes and synthetic request/response boundary checks passed.
The reviewed raw capture SHA-256 is
`dcbb84d75584697828fc5fe9c753a17823b67088fadc9d10e13dd254f49dd3a1`.

Research/tooling failures retained: reading root `LICENSE` returned file-not-found
(hence no repository license assumed); the first issue-8 lookup combined incompatible
`--comments`/`--json` flags and exited 1, then succeeded with JSON alone. A Python
`urllib` citation fetch failed local issuer certificate verification; normal verified
`curl` retrieval succeeded without disabling TLS verification or changing configuration.
`git diff --no-index` of the two SDK cores exited 1 as expected because it found the
version and default-retry changes; this was not a failed check.

Initial remote `pr-record` failed: `research:` is not an accepted PR-title prefix,
and an automated summary appended after the co-author trailer invalidated its
final-block placement. The delivery uses `chore:` and restores the trailer after
the summary; the PR timeline records revalidation and current CI at the pushed revision.

Not run: product suites (none exist), TypeScript compilation, live SDK services,
S3 replay, adversarial B03 isolation, additional platforms/runtimes, full security
audit, benchmarks or pilot validation. npm audit was deliberately disabled during
provisioning. The coordinator independently verified the original research head
`488314fd97260f2a46366b3cee1bf3301b809893`, including byte-identical captures and all
ten documented SDK file hashes. Subsequent corrections and founder approval are
complete; [final coordinator verification](https://github.com/Himanshu-singh04/shiftproof/pull/10#issuecomment-7000545190)
records the accepted research result. These are historical B01 outcomes; the separate
[B02 record](b02-runtime-validation.md) investigates the runtime without replacing
this experiment's original source, fixtures, lock or observations.
