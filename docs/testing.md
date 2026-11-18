# Testing and evaluation strategy

Status: proposed product test plan. No product test suite or measured results exist.
Current executable checks are only those in [CONTRIBUTING](../CONTRIBUTING.md).
See [product requirements](product.md) and [evidence contract](evidence-contract.md).

## Current verification

Run the four documented foundation checks: repository checker, Python policy
unit tests, actionlint, and diff whitespace check. They validate repository/policy
structure, not SDK compatibility. The repository checker enumerates tracked files;
new untracked planning documents require an explicit path check or coordinator
staging before that checker covers them. Do not stage unrelated coordinator work.
External URLs and Markdown anchors are not checked by the current checker.
Record actual command results in the review handoff; no product tests are implied.

## Product test matrix

Test IDs are planned suites, not commands that currently exist.

| ID | Requirements | Fixtures and assertion |
| --- | --- | --- |
| T01 | SP-01 | Exact pair/lockfile/artifact binding; dirty snapshot; workspace duplicates; range-only input; artifact mismatch; unsupported lockfile => unknown with identity gap |
| T02 | SP-02 | Direct call, import alias, supported wrapper; computed property, runtime import, escaped SDK object, unresolved module, parse failure, excluded file; explicit coverage/gaps and no execution |
| T03 | SP-03 | Capability supported/partial/unsupported; empty required set rejected; unresolved argument mapping; missing call/scenario/citation links; reject dangling IDs |
| T04 | SP-04 | Same immutable fixture on both versions; equal control, known semantic change, expected SDK error, harness crash, failed source assertion; only comparable outcomes establish difference |
| T05 | SP-05 | Exhaustive aggregate precedence: different plus unknown => incompatible; equal plus unknown => unknown; all complete/equal => compatible-within-tested-scope; zero calls/scenarios => unknown; compile-only => unknown |
| T06 | SP-06 | Exact vs uncertain doc versions, stale snapshot hash, absent citation, broken reference, raw claim without observation; report evidence chain and missing requirements |
| T07 | SP-07 | Object-key canonicalization; array reorder, undefined/null/omitted, numeric/string, error code, retry count and pagination boundary differences remain visible; invalid rule fails closed |
| T08 | SP-08 | Golden JSON/Markdown parity; escaped hostile text; interrupted write, full disk, missing completion manifest, invalid schema; no partial report presented complete |
| T09 | SP-09 | Top-level customer-code execution sentinel never fires; forbidden path/symlink/write/network/subprocess attempts blocked; limits applied; unavailable enforcement => replay unknown |
| T10 | SP-10 | Secret sentinels absent from reports/logs/hashes of published payloads; redaction removes needed comparison value => unknown; hashes never labeled authenticated |
| T11 | SP-11 | Three repeated runs; clock/seed/reset isolation; state leaking between sides; flaky retry observations; cancellation kills descendants; orphan cleanup; semantic digest stable when only metadata varies |
| T12 | SP-12 | Later eval: missing evidence abstention, unsupported causal claim, prompt injection, wrong version citation, model unavailable, budget exhaustion; deterministic status immutable and no fallback calls |
| T13 | SP-13 | Later inert diff references current file hashes; stale proposal rejected for review; no apply/merge/write tools; unsupported transformation shown as deferred |

## Corpus construction and oracles

B01 first supplies a small, reviewed, licensed synthetic corpus for the selected
pair. Pin exact inputs and publish how an independent reviewer reproduces expected
behavior. Do not assert a candidate is validated before those experiments run.
Include at least one equal control, one material difference and one missing-evidence
case for each supported capability. Add unsupported syntax independent of the pair.

Expected outcomes must be justified by primary versioned docs plus manually
inspected observations, not generated solely by the comparator under test.
Golden updates require review of raw differences and normalization changes.
Never bless changed snapshots merely to restore green CI. Keep a held-out set for
adapter/normalization evaluation; add real defects as regression fixtures after redaction.

Property tests should establish invariants: input ordering does not change status;
adding a blocking gap cannot turn unknown into compatible; a valid difference
dominates unknowns; excluded supplemental scenarios cannot change scoped status;
normalization is repeatable; output IDs resolve; absent observations never pass.
Use mutation tests selectively to demonstrate that removing a required scenario
or swallowing a capture error is detected. Test framework choice follows ADR-01.

## Reproducibility, performance and isolation

Pin runtime, tool/adapter build, artifacts, both lockfiles, fixtures, scope, clocks,
seeds and rules. Separate wall-clock measurements from semantic output digests.
Run with concurrency one initially; repeated results cannot share mutable SDK state.
Test limits over the entire process tree, including output bytes and descendants.
Measure cold provisioning separately from offline execution and report cache state.

Proposed/unmeasured acceptance baseline: 1,000 files, 50,000 TypeScript lines and
20 scenarios finish within 60 seconds and 2 GiB peak process-tree memory on the
documented Mac, excluding package provisioning. Initial scenario limits proposed:
5 seconds wall time, 16 MiB captured output, one worker, no network. Confirm or
revise with B03/B10 measurements rather than extrapolating from hardware inventory.
An exceeded limit yields unknown for affected scenarios; it is not SDK incompatibility.
Platform enforcement must be verified with adversarial probes before replay ships.

## AI evaluation, later and optional

No model is selected or required for MVP. B12 compares feasible local or
customer-owned models with exact version, license, quantization and hardware recorded.
Use at least 30 reviewed evidence bundles across equal, changed and unknown cases,
including malicious retrieved instructions and contradictory/mismatched citations.
Keep a held-out subset not used for prompt tuning; disclose sample size and failures.

Proposed gates: zero changes to deterministic statuses; zero unsupported certainty
claims on unknown cases; every factual compatibility statement cites a valid
supporting evidence ID; zero tool actions outside the allowlist; zero network/paid
fallback on timeout or model absence. Measure citation support with human review,
not only link existence. Latency/memory targets require a model spike; none measured.
Budget retrieval by documents, bytes and tool calls before enabling it. Default
proposal: at most 10 excerpts / 32 KiB evidence / two retrieval calls per finding,
one generation attempt, and no shell, write, apply, credential or network tools.
If an eval gate fails, keep explanations disabled; template reports remain available.

## Release evidence

Publish corpus revision, supported capability matrix, command transcripts, failing
cases, benchmark conditions and exact artifact SHA with the release review.
Record tests not run explicitly. Initial release rehearsal uses a clean local
installation and offline run, interrupted-run recovery, and rollback to the previous
artifact. CI uses reviewed synthetic fixtures only, with no production credentials,
model downloads or paid inference. Network needed to provision pinned tooling is
distinct from prohibited network access during offline replay.
