# Proposed roadmap and bounded backlog

Status: planning only. Task IDs below are local backlog identifiers, not claims
that GitHub issues or implementations exist. All architecture ADRs require review.
Dependencies form release gates; a failed gate stops downstream implementation.
See [product](product.md), [design](specs/001-mvp/solution-design.md),
[testing](testing.md), and [operations](operations.md).

## Milestones

| Milestone | Depends on | Observable exit | Verification |
| --- | --- | --- | --- |
| M0: scope and selection | Planning review | One justified pair selected or documented no-go; runtime/isolation options measured enough to decide | B01–B03 records reviewed |
| M1: evidence and discovery | M0, ADR confirmation | Exact identity and bounded discovery produce validated unknown reports | B04–B05 contract/negative tests |
| M2: offline differential | M1, isolation gate | Same fixtures expose a known difference and a known equal case with honest gaps | B06–B08 golden/e2e tests |
| M3: local MVP | M2 | Installable local artifact, JSON/Markdown parity, reproducibility and recovery demonstrated | B09–B10 release rehearsal |
| M4: limited pilot | M3, consent | At most three upgrade reviews with documented usability outcomes | B11 task observations, no invented validation |
| M5: optional explanations | M3 and separate approval | Local/customer-owned model passes bounded evidence eval or remains disabled | B12 offline eval |
| Later: harness/proposals | Separate scope approval | Explicit trust contract and inert proposals reviewed | B13 design/tests before implementation |

## Initial bounded task: B01 SDK/version selection spike

Budget: at most two working days and three candidate packages; no implementation
commitment or customer credentials. The first package/source/target pair remains
**UNSELECTED** until the coordinator and owner review the evidence.

Entry: approved problem boundary and fixture licensing policy. Investigate:

1. Exact package identity, source and target versions, resolution paths and artifact availability.
2. At least one documented, reproducible semantic change observable offline;
   compilation-only or undocumented speculative changes do not qualify.
3. At least one unchanged control and one failure/unsupported scenario.
4. Maintained primary docs/release notes with version applicability and capturable citations.
5. A narrow transport/capture seam permitting synthetic fixtures without running customer code.
6. Deterministic clocks/state, install-script constraints, fixture licensing and practical isolation.

Deliver a candidate matrix, source URLs/excerpts, exact reproduction inputs,
observed outcomes, limitations and a recommendation or no-go. Clearly separate
observed results from planned experiments. Do not publish proprietary fixtures.
Acceptance: a reviewer can reproduce the semantic difference and equal control
from the written procedure without a paid service. If none qualify, stop and
propose a narrower scope; do not silently select the easiest unvalidated package.
Verification: independent rerun and citation/version review. PRD: SP-01, SP-03–SP-07.
Pair-specific schema/adapter hardening cannot start before this task passes.

## Issue-sized implementation candidates

Each row becomes a separately scoped issue after approval; split any task exceeding
two focused working days. Tests here are future acceptance expectations.

| ID | Task / dependencies | Acceptance criteria | Tests / requirements |
| --- | --- | --- | --- |
| B02 | Runtime/package manager pin / B01 | Choose exact supported Node/TypeScript versions and one lockfile format; document clean install, script policy and pinned transitive tree | Clean offline-after-provisioning install; mismatched identity rejection / SP-01, SP-09 |
| B03 | Replay isolation feasibility / B01 | Demonstrate enforceable network/filesystem/process limits for reviewed SDK harness; record unsupported platforms; choose mechanism or disable replay | Denied egress/write/child-process probes, timeout/cleanup / SP-09, SP-11 |
| B04 | Schema revision and aggregator / B01, B02 | Harden pair-specific fields from spike; validate references; implement exact unknown/different precedence | T01, T03, T05–T07 property and table cases / SP-01, SP-03, SP-05–SP-07 |
| B05 | Read-only discovery / B04 | Supported imports/aliases mapped; computed calls, escapes, parse failures and exclusions visible; no module execution | T02 fixtures including malicious top-level code / SP-02, SP-09 |
| B06 | Selected adapter / B03, B04 | Declare capability support, source expectations, transport seam and identical scenario mapping | T03, T04 known change/equal/error cases / SP-03, SP-04 |
| B07 | Controlled replay / B06 | Pin both environments, enforce limits, capture tagged outputs, preserve attempts, classify nondeterminism | T04, T09, T11 isolation and interrupted-run cases / SP-04, SP-09, SP-11 |
| B08 | Normalization and coverage / B05, B07 | Rules preserve material differences; every call has obligations/gaps; zero calls is unknown | T05–T07 counterexamples and report corpus / SP-05–SP-07 |
| B09 | Local reports / B08 | JSON/Markdown parity, escaped citations, atomic completion manifest, redaction loss shown | T08, T10 malformed references, secret sentinel, disk failure / SP-08, SP-10 |
| B10 | Packaging and operator rehearsal / B09 | Pinned local artifact installs on declared platform; recovery and rollback documented; benchmark recorded | Clean-machine rehearsal, three-run digest, measured target table / SP-01, SP-08, SP-11 |
| B11 | Consent-based pilot / B10 | At most three maintainers review one upgrade each; record actionable/not actionable findings and missing coverage | Scripted tasks, traceability inspection, qualitative feedback / SP-02, SP-05, SP-06 |
| B12 | Optional local explanations / B10, ADR-05 | Model/license/resource fit chosen through eval; bounded retrieval, citations and abstention; no paid fallback | T12 injection, unsupported claims, offline/model-unavailable cases / SP-12 |
| B13 | Trusted harness and proposal design / B10, separate approval | Define explicit execution trust and inert patch contract; no implicit execution or auto application | T09, T13 authorization boundary and file-hash mismatch design tests / SP-09, SP-13 |

## Decision checkpoints and release discipline

- M0 confirms ADR-01 runtime and ADR-02 pair; B03 gates ADR-03 isolation.
- M1 confirms ADR-04 evidence contract with observed adapter limitations.
- M3 requires all product tests relevant to supported scope plus existing foundation
  checks. A green foundation check is not a product release gate by itself.
- M4 cannot broaden coverage claims beyond tested corpus or pilot scenarios.
- M5 is independent of MVP success; inability to run a suitable local model must
  leave deterministic reports usable. Retrieval indexes/models are not provisioned.
- B13 does not authorize automated code transformations or remote-service replay.
- Record reviewed SHA, evidence, limitations and explicit owner decision through
  [development](development.md); task completion does not self-authorize merge.

## Stop conditions

Stop a run or milestone when identity cannot be established, required evidence
cannot be retained, offline isolation is unavailable, or known unknown cases
are classified compatible. Record an actionable gap/no-go rather than making
claims narrower only after seeing failed outcomes. Re-scope through review.
