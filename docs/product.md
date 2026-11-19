# Product requirements: first SDK upgrade

Status: planning approved and merged in [PR #5](https://github.com/Himanshu-singh04/shiftproof/pull/5).
No product implementation, approved version pair, customer validation, or pilot results exist.
The [B01 recommendation](b01-sdk-selection.md) has synthetic research evidence only.
Architecture choices in the [solution design](specs/001-mvp/solution-design.md) require confirmation.

## Problem and narrow customer hypothesis

A maintainer of a small TypeScript service must decide whether one SDK upgrade
changes behavior at the SDK calls their service uses. Compilation and release
notes help, but neither demonstrates equivalent request construction, returned
values, or error handling for the service's scenarios.

Hypothesis: maintainers with an imminent upgrade, a committed lockfile, and
reviewable synthetic fixtures will value a local report that connects source
locations to reproducible differences. Initial users are the engineer preparing
the upgrade and the reviewer deciding what additional evidence is necessary.
This is a discovery hypothesis, not an established market or willingness to pay.

Recruit at most three consenting design partners after the synthetic demo gate.
Ask for one upgrade task, redacted source patterns, and acceptance scenarios;
do not require production credentials or customer traffic. Proposed pilot success:
two participants can identify a concrete next action from the report and trace
it to evidence without the author explaining it. Record disagreements and time
spent; do not turn this small sample into a general accuracy claim.

## Product boundary

- One TypeScript SDK package and one exact source/target version pair per run.
- First package, source version, target version, and lockfile format: **UNSELECTED**.
- Offline analysis and reviewed synthetic/mocked API fixtures come first.
- Results concern SDK behavior under those fixtures, not actual remote-service compatibility.
- Static discovery does not execute the repository or its configuration modules.
- Only a reviewed, product-owned adapter and pinned SDK packages may execute in replay.
- An explicit trusted local customer test harness is a later opt-in feature.
- Local JSON and Markdown are the initial deliverables; no hosted dashboard is required.
- Patch proposals may later be attached for human review; never automatically apply or merge them.
- Code transformations, universal migrations, multi-SDK upgrades, production replay,
  live-service certification, hosted multi-tenancy, and autonomous PRs are outside MVP.

## User workflow

1. Select the supported pair and supply source snapshot, source/target lockfile
   snapshots, scope exclusions, reviewed fixture bundle, and output directory.
2. Inspect preflight: exact resolved package identities, adapter support,
   missing documentation evidence, unsupported syntax, and execution boundaries.
3. Discover statically resolvable SDK calls and unresolved SDK-related candidates.
4. Review mappings from call sites to required capability scenarios.
5. Replay identical scenario inputs against isolated source and target SDK environments.
6. Read report status, scope, coverage gaps, differences, and evidence citations.
7. Decide whether to change application code, add scenarios, or defer the upgrade.
   A later patch proposal is an input to that decision, never its authorization.

## Requirements

IDs are stable; changing scope requires a documented revision, not silent renumbering.
Every requirement is proposed and has planned verification in [testing](testing.md).

| ID | Requirement and observable acceptance | Design owner / test |
| --- | --- | --- |
| SP-01 | Bind each run to exact source/target resolved package versions, lockfile hashes, repository snapshot, runtime, adapter and fixture versions. Ambiguous resolution is unknown, never inferred from a version range. | Inventory / T01 |
| SP-02 | Discover supported static SDK calls with file/range/symbol evidence; inventory parse failures, exclusions, unresolved imports, computed calls and alias escapes. Never describe discovered calls as all runtime calls. | Discovery / T02 |
| SP-03 | Declare a pair-specific capability matrix with supported, partial and unsupported capabilities and reasons. Map each discovered call to required scenarios or explicit gaps. | Adapter / T03 |
| SP-04 | Run the same immutable scenario against each version, record observations and provenance, and distinguish equivalent behavior, material difference and missing evidence. | Replay / T04 |
| SP-05 | Emit exactly compatible-within-tested-scope, incompatible or unknown under deterministic aggregation; only a validated fail mapping obligation establishes scoped incompatibility. Show positive evidence and gaps; compilation cannot supply behavioral success. | Comparison / T05 |
| SP-06 | Link findings to a consistent closure of source locations, scenario records, exact versions and versioned citations; reject cross-case attribution and unsafe link targets. Missing citations remain visible and block dependent claims. | Evidence / T06 |
| SP-07 | Preserve raw observations alongside versioned normalization rules; never normalize away meaningful ordering, omitted fields, errors or retry behavior without an explicit scope decision. | Comparison / T07 |
| SP-08 | Produce local traceable JSON and Markdown with identical statuses, coverage and evidence IDs; publish through verified directory/mount handles, suppress completion on identity loss and keep partial runs visibly incomplete. | Report / T08 |
| SP-09 | Keep customer files read-only; do not import arbitrary customer modules, run package scripts or transmit data. Enforce replay limits and report enforcement gaps. | CLI, Replay / T09 |
| SP-10 | Keep output local, redact sensitive values using a declared policy, and record redaction-related evidence loss. Do not claim hashes establish authenticity. | Evidence, Report / T10 |
| SP-11 | Reproduce semantic results from pinned inputs; isolate clocks, state and randomness or mark affected scenarios unknown. Report operational failures distinctly from incompatibility. | Replay / T11 |
| SP-12 | Later explanations must cite evidence, abstain on gaps and preserve deterministic results; bounded local/customer-owned inference has no paid fallback. MVP requires no model. | Deferred explanation boundary / T12 |
| SP-13 | Later optional patch proposals include rationale, assumptions and verification needs; user review is mandatory and no write/apply/merge action is provided. Transformations are deferred. | Report extension / T13 |

## Acceptance journeys

- Known equal fixture: supported call, complete identity/citation/mapping evidence,
  source and target observations, no gaps; report compatible-within-tested-scope.
- Known changed fixture: comparable observations differ on a declared material
  dimension and a supported, representative call mapping validates as fail; report
  incompatible and identify that call, scenario and observation paths. Different
  fixtures with only unknown mappings remain supplemental and yield unknown.
- Incomplete fixture: target timeout, unsupported dynamic call, missing required
  citation, or a missing observation; report unknown unless another validated fail
  mapping establishes incompatibility. List the missing evidence even then.
- Compilation succeeds but replay is absent: unknown, with compile evidence
  separately labeled as static evidence.
- Offline fixture passes: explicitly state synthetic/mocked scope and that actual
  remote-service behavior was not tested. Never report simply “safe to upgrade.”
- No SDK calls found: unknown; show scanned paths and discovery limitations instead
  of vacuous compatibility.

## Proposed measures and release gates

All targets below are unmeasured. These are gates for a bounded benchmark corpus,
not promised performance or population accuracy.

- Zero false compatible outcomes in the reviewed unknown/incompatible regression corpus.
- Every result references resolvable evidence IDs; every gap has a reason code.
- Three repeated offline runs produce identical semantic digests under pinned inputs.
- Proposed local baseline: 1,000 TypeScript files / 50,000 lines / 20 scenarios,
  at most 60 seconds elapsed and 2 GiB peak process-tree memory, concurrency one.
- Revisit the baseline after measuring the selected adapter on the actual Mac;
  observed 16 GiB RAM and eight logical CPUs are inventory, not a benchmark.
- Pilot usability target: evidence for a selected finding reachable within two
  report links; record completion time rather than inventing a productivity gain.

## Decisions and sequencing

The [roadmap](roadmap.md) starts with a two-working-day, at-most-three-candidate
selection spike. It must find reproducible semantic differences, offline fixtures,
maintained primary docs and a narrow adapter boundary. A negative result is useful:
record why no pair qualifies and stop pair-specific implementation.
Pair-specific schema and adapter hardening follow selection, not the reverse.
Exact runtime, package manager, network isolation mechanism and future model are
unresolved gates in the SDD. Reviewable planning is not architecture approval.

See [evidence contract](evidence-contract.md) for statuses and provenance,
[operations](operations.md) for storage and execution, and
[development](development.md) for the coordinator/owner delivery process.
