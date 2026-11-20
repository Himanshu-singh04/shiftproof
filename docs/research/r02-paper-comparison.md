# R02: paper comparison of upgrade-review decisions

Status: **draft protocol complete; narrow investigation to independent paper audit**,
for [issue #19](https://github.com/Himanshu-singh04/shiftproof/issues/19).
No evaluation results, participants, product or scope adoption. Coordinator review pending.

## Authority and bounds

Founder instructed non-build workers to “keep on researching and improving the plan
from business and development perspective in all aspects” and said **“resume everything”**
on 2026-11-20. Coordinator dispatched this bounded round under that continuing mandate.
Same persistent GPT-6 Astra / OpenCode worker; no subagents or permission/model changes.
Start: **2026-11-20 05:45:10 UTC**; deadline **07:45:10 UTC**, finish earlier if complete.
At most six external primary documents, including reused sources; exactly three inert
synthetic task/answer packets in one roughly 250–320-line Markdown protocol.

Approved base: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.
[R01 at its preserved revision](https://github.com/Himanshu-singh04/shiftproof/blob/0de10807e8a02c918e19f6ee6c0f7a0320158d39/docs/research/r01-customer-value.md)
passed coordinator verification, but remains founder-unapproved and unmerged.
[B03a at its preserved revision](https://github.com/Himanshu-singh04/shiftproof/blob/644be51bbbac996f7fc9023530516bf37a409190/docs/b03a-path-decision.md)
still awaits full source audit. Both are provisional; neither proposal is adopted here.
Replay stays **disabled / unknown / ISOLATION_UNAVAILABLE**. Historical packages below
are paper research examples, not supported SDK pairs or present-day recommendations.

## A1: frozen comparison design, revision 0.1

Decision: for the named change and shown callsites, identify what needs action, what
does not apply and what stays unresolved; choose the next evidence before considering
an upgrade. This is not a whole-upgrade merge decision or a compatibility verdict.
Population for any later authorized exercise: engineers able to read Node/TypeScript
and SDK documentation. No recruitment, participant count or evaluation is authorized.

**Manual arm M:** exact participant sheets P1–P3, shared D1–D3 excerpts below and access
to the full frozen documents. Allow text search, editor navigation, notes and a manually
created table. Give explicit relevant section names and exact version scope; do not
hand M a document dump while giving T curated facts. No installation, execution or
AI assistance in either arm. M may use normal reasoning about the supplied premises.
**Table arm T:** all M material plus the corresponding T1–T3 table supplements below.
The intervention is curated mapping/organization and derived questions, not extra facts.
T must check citations and may reject rows. Tables are author-created mock artifacts,
not analyzer output; their quality does not establish automated mapping feasibility.

Before any later session, an independent facilitator freezes this document's Git SHA,
source digests and distribution manifest. Make a participant copy containing only
the instructions, D excerpts/access and P sheets; add T supplements only for T.
Withhold author keys, scoring expectations and business recommendation from both arms.
This repository file is **not** a blinded participant handout: it contains all answers.
Prior key access contaminates either arm; prior table access contaminates M. Exclude
such sessions from the primary comparison but retain their history. The author is not
an independent participant.

Assign each reviewer to one arm only, within prior Node/Stripe-familiarity strata;
use a recorded random assignment before exposure. Balance all six P1/P2/P3 orders
within each arm if numbers permit. No same-person crossover on these tasks. P2/P3
share Stripe concepts, so report order and prior familiarity with each result; small
or unbalanced groups support descriptions only. Separate participants cannot share
answers. These are future design choices, not a claim that allocation/blinding occurred.

Use identical source access, editor help and clarification script. Restrict web access
to frozen documents in both arms so later revisions/new evidence cannot favor one.
Clarification script: “Use only written premises; missing facts stay unknown.” Offer
navigation help only, log requests, and do not add hints or unrecorded source facts.
Full copies must match the digests below; if unavailable or changed, pause, preserve
the attempt and review a new protocol revision before resuming. Do not grade missing
source access as reviewer failure. Preserve alternative supported reasoning in disputes.
An independent assessor should score anonymized answers with arm labels removed where
possible; wording may reveal T exposure, so do not claim guaranteed assessor blinding.
The same agent wrote tasks, tables and keys: selection and answer-author bias remain.

## Shared evidence: three primary documents, read 2026-11-20

These are all external primary documents consulted this round, including reused ones.
Linked changelogs, issues and service docs were not fetched; unknowns remain unknown.
Sources are upstream-authored documentation, not observed behavior of these snippets.

| ID / exact source | Locators and verbatim excerpts supplied to both arms |
| --- | --- |
| D1 [node-fetch v3.0.0 upgrade guide](https://raw.githubusercontent.com/node-fetch/node-fetch/v3.0.0/docs/v3-UPGRADE-GUIDE.md) | **D1a**, “Converted to ES Module”: “This module was converted to be a ESM only package in version `3.0.0-beta.10`.” “`node-fetch` is an ESM-only module - you are not able to import it with `require`.” **D1b**, same section: “We recommend you stay on v2 which is built with CommonJS unless you use ESM yourself.” “Alternatively, you can use the async `import()` function from CommonJS to load `node-fetch` asynchronously”. |
| D2 [Stripe v13.0.0 release](https://github.com/stripe/stripe-node/releases/tag/v13.0.0) | Published 2023-08-16; read via release API. **D2a**, #1803 bullet: “Change the default behavior to perform 1 reattempt on retryable request failures (previously the default was 0).” **D2b**, #1808: “Allow request-level options to disable retries.” **D2c**, first bullet: “This release changes the pinned API version to `2023-08-16`.” |
| D3 [Stripe v13.0.0 README](https://raw.githubusercontent.com/stripe/stripe-node/v13.0.0/README.md) | **D3a**, Configuration note: “Both `maxNetworkRetries` and `timeout` can be overridden on a per-request basis.” **D3b**, Network retries: “stripe-node will automatically do one reattempt for failed requests that are safe to retry.” “Automatic network retries can be disabled by setting the `maxNetworkRetries` config option to `0`.” **D3c**, same section: “You can also set a higher number to reattempt multiple times, with exponential backoff.” “Idempotency keys are added where appropriate to prevent duplication.” |

D1/D3 publication dates are not supplied; tags scope their historical content. D2 is
mutable (API updated_at 2025-06-21); source digests below bind the read, not authenticity.
D3's per-request example sets `maxNetworkRetries: 2` in the second argument to
`customers.create`. That example and D3a supply the option position in P2/P3.
No current support/security recommendation follows from these historical docs.

```text
SHA-256; D1/D3 raw HTTP payload bytes, D2 API JSON body string encoded UTF-8
D1 beb08cbbb9de21b26da05e8adc60f2eb79df5ba923c82d3c3161a45de449872a
D2 4a46cf98626d1caa2d76c8b436ddc91033d858553398807cc7b3844ea5f73b30
D3 7df3f8a99774079635135bcf2b2fb09426c9e07420938576b51d5ac91f54a636
```

## Participant instructions and exactly three task sheets

All snippets are **inert synthetic text**, not programs to run. Line IDs are part of
the paper, not source syntax. Names, paths and configuration are fictional; there are
no credentials, customer inputs or network targets. Assume only explicit premises.
For each packet return: decision on the named change; one classification per named
callsite (`applies`, `does-not-apply`, `unresolved`); citation + premise; unresolved
behavior; and a specific next check with its needed evidence. State scope explicitly.
Classification concerns the named change, not the safety of the entire application.

### P1: docs-solved module-loading control

Scope: node-fetch `2.6.1` → `3.0.0`; hypothetical Node `14.15.3`, TypeScript `4.3.5`.
Premise P1-S: both arms receive the following authored source/config/emitted text;
no compilation occurred. The emitted file below is the deployment entry, no bundler,
loader override or transformation intervenes. No assertion of a successful v2 run.

```text
P1-L1  tsconfig fragment: { "compilerOptions": { "module": "commonjs" } }
P1-L2  src/load.ts: import fetch from "node-fetch";
P1-L3  src/load.ts: export const load = (url) => fetch(url);
P1-L4  dist/load.js: const fetchModule = require("node-fetch");
```

Named change: v3 ESM-only loading. Question: can the unchanged P1-L4 loading strategy
be retained according to D1, and what is the smallest review decision now? Cite D1's
choices without treating its historical v2 advice as current support guidance.
State what remains unproven after any chosen source/configuration change.

### P2: request-option applicability question

Scope: Stripe `12.18.0` → `13.0.0`; synthetic TS service on Node `18.17.1`.
Premise P2-S: shown client has no global retry override or later mutation. Each named
call below uses that same client. `runtimeOptions` is an external config value whose
contents are absent; it may include a retry override. No trace or build result exists.
`PLACEHOLDER` denotes an unspecified credential, not a usable secret.

```text
P2-L1  client = new Stripe(PLACEHOLDER);
P2-L2  A: client.customers.create({ description: "paper A" });
P2-L3  B: client.customers.create({ description: "paper B" }, { maxNetworkRetries: 0 });
P2-L4  C: client.customers.create({ description: "paper C" }, runtimeOptions);
```

Named change: the SDK default retry count rising from zero to one (D2a). For A/B/C,
classify whether that changed default determines the target's configured retry policy.
Give the documented target setting where knowable and one targeted review action.
Do not equate a configured retry count with observed attempts or overall compatibility.
Assess target applicability, not undocumented old-version handling of request options.

### P3: behavior-only control

Scope: Stripe `12.18.0` → `13.0.0`; separate synthetic TS service, Node `18.17.1`.
Premise P3-S: no wrapper, global override or mutation; the change under review affects
the SDK's retry policy. Scenario prompt: a connection drops after the server **may**
have accepted a create. No error classification, request/response trace, elapsed-time
measurement, idempotency evidence or server-side result is supplied for either version.

```text
P3-L1  client = new Stripe(PLACEHOLDER);
P3-L2  client.customers.create({ description: "paper retry scenario" });
P3-L3  requested acceptance claim: "one remote creation, completion under 100 ms"
```

Question: does D2/D3 plus P3-L1/L2 establish P3-L3 or even an observed second attempt?
Explain the documented conditional policy, distinguish local attempts from remote
effects, and name the next evidence needed. Decide whether the named acceptance claim
is established, disproved or unknown. Do not invent a failure trace or timing value.

## Table-arm supplements only: T1–T3

Facilitator supplies only the matching table to T; M sees neither tables nor keys.
These rows are proposed assistance, open to challenge. They assert no runtime result.
Each source, premise and limitation also appears in M's materials above.

| T1 location | Cited mapping | Suggested next check |
| --- | --- | --- |
| P1-L2/L4 | D1a applies to the specified emitted `require`; TypeScript import spelling does not change supplied emitted text. | Review a D1b loading strategy, then obtain build/loader evidence for the chosen target. |

| T2 location | Cited mapping | Suggested next check |
| --- | --- | --- |
| A / P2-L2 | D2a + D3b: absent an override, target default is one conditional reattempt. | Decide whether inherited retry policy fits this call's requirements; request a scoped failure test if needed. |
| B / P2-L3 | D2b + D3a/b: request-level zero disables target retries; changed default does not determine this call's setting. | Verify this explicit option remains the intended configuration; do not raise a default-increase finding solely from package version. |
| C / P2-L4 | D3a + P2-S: configuration missing; target policy unresolved. | Obtain resolved request options before classifying default applicability. |

| T3 location | Cited mapping | Suggested next check |
| --- | --- | --- |
| P3-L2/L3 | D2a + D3b/c define a conditional retry policy; no trace establishes actual attempts, time or remote creations. | Specify retryability/attempt/timing evidence and remote outcome evidence; retain unknown acceptance. |

## Author keys: adjudicator only, not participant instructions

These are source-based expectations written by the task author, **not observations**.
Independent reviewers can dispute every row by citing the premise or official text.
Accept equivalent supported reasoning and scoped alternatives; do not grade phrasing.
Freeze disputed-row handling before evaluation: mark unscorable, retain both readings,
exclude that row from the denominator in both arms and report the exclusion. If a core
decision row is disputed, pause that packet; resolve/version it before new sessions.

### K1: expected statements and counterexamples

| ID | Supported expected statement | Dependency / reasoning | Material wrong answer |
| --- | --- | --- | --- |
| K1.1 | The ESM-only change applies to P1-L4; unchanged `require` conflicts with documented loading support. | D1a + P1-S/L4. This is a documented mismatch, not an observed exception. | “Source uses import, so unchanged emitted code is supported.” |
| K1.2 | Request a loading/build strategy decision; D1b offers async import or ESM, and historical retention of v2. | D1b + P1-L1/L4; author inference that changing the shown loading strategy needs review. Any supported option suffices; no forced migration choice. | “v2 is currently supported/secure” based only on the old guide, or “change one spelling and all behavior is compatible.” |
| K1.3 | Changed loader/build behavior and service behavior remain unverified; next obtain emitted-output/loader evidence for the selected strategy. | P1-S contains no build/run; D1a/b describe loading, not whole-service outcomes. | “Safe to upgrade after this edit” or an invented successful run. |

Negative control rationale: a competent reviewer can answer directly from D1; a table
may add no decision and may take longer to inspect. Matching M and T is valid evidence.

### K2: expected statements and counterexamples

| ID | Supported expected statement | Dependency / reasoning | Material wrong answer |
| --- | --- | --- | --- |
| K2.1 | A: applies; documented target default permits one reattempt on eligible failures; source default was zero. | D2a + D3b + P2-S/L1/L2. “Permits” describes policy; no observed attempt count. | Miss the default change, or promise exactly two attempts on every request. |
| K2.2 | B: does-not-apply to the default increase; explicit target request setting is zero. | D2b + D3a/b + P2-L3; per-request option overrides the default. No claim about old request-option implementation. | Flag B as inheriting one retry solely because the SDK changed; this is a material false positive. |
| K2.3 | C: unresolved; fetch the effective options/configuration before classifying. | D3a + P2-S/L4; absent data cannot prove either an override or default inheritance. | Assign zero/one from an imagined config or silently omit C as unaffected. |
| K2.4 | Review A's desired policy, distinguish B's explicit setting and resolve C; runtime outcomes and other upgrade changes remain open. | K2.1–3 + D2c (separate API-version change); source-based next-action inference only. No business requirement establishes which policy is preferable. | “All calls safe because overrides exist” or blanket testing instructions without resolving C. |

### K3: expected statements and counterexamples

| ID | Supported expected statement | Dependency / reasoning | Material wrong answer |
| --- | --- | --- | --- |
| K3.1 | Default change applies to the shown unoverridden call; one retry is conditional on a safe-to-retry failure. | D2a + D3b + P3-S/L1/L2. Missing failure classification prevents applying that condition to a trace. | Treat every connection drop as proven retryable, or miss the changed default entirely. |
| K3.2 | P3-L3 is unknown, not established or disproved. Actual second attempt, elapsed time and number of remote creations are unknown. | P3-S supplies none of those observations; D3b/c states policy/backoff, not a 100-ms bound. | “One retry means exactly two attempts”, “under 100 ms”, or “the upgrade caused duplicate creation.” |
| K3.3 | Request a scoped trace with failure/retryability, attempts and timing, plus evidence binding request identity to remote effects. | D3b/c + P3-S; author inference about evidence needed to assess P3-L3. Offline evidence alone cannot establish actual remote effects. | Treat “Idempotency keys are added where appropriate” (D3c) as observed exactly-once behavior or unconditional “safe to upgrade”. |

No table can supply the missing runtime/remote observations. “Unknown” alone is not a
complete answer: reviewer must name the conditional policy and missing evidence.

## A4: prespecified scoring and future effort procedure

Score each K row 0 = absent/unsupported/contradicted, 1 = correct conclusion with missing
source/premise or incomplete requested action, 2 = correct scoped answer with source,
premise and requested action/limitation. Record the exact answer span and justification.
Maximums P1=6, P2=8, P3=6; report packet scores separately, not just a pooled advantage.
If a non-core row is excluded, subtract two from both arms' available maximum.
Packet correctness requires all its rows at 2 and zero material false assurance.
These scores are a proposed rubric, not measurements or validated psychometrics.

Coverage denominator: named mappings P1-L4, P2 A/B/C, P3-L2 (five total); count correct
classification **and rationale** per mapping. Report expected applies (three), does-not-
apply (one), unresolved (one) separately; do not reward flagging everything. K2.3's
unresolved mapping counts as covered only when its missing configuration is identified.
Material miss: a wrong/omitted named mapping or required K-row decision/evidence gap.
False positive: asserting an unsupported definite impact, especially B inheriting the
default increase. False assurance: any unsupported runtime fact or whole-upgrade safety
claim, including the examples in keys. Count flags separately; one answer can have both
a miss and a false positive. Any false assurance blocks a positive task verdict.

Actionable difference: compare distinct supported `location + decision + next evidence`
triples from M and T; count new correct triples, not extra words or repeated citations.
Report per-packet frequencies by arm and individual scores/times with their ranges;
avoid pairing unrelated people or pooling one arm's union against one person's answer.
Keep negative and redundant differences. A table cannot claim benefit for adding a
check the baseline already chose; correct “do not act on default increase at B” counts.
Have a second independent assessor resolve disagreements before revealing arm labels
where feasible; no author self-score can supply independent evidence of an advantage.

Future human effort log, never filled with agent time: record shared setup/source-access
time, arm-specific table orientation/verification time and each packet's reading,
searching, note/answer and rework time. Include interruptions separately and disclose
incomplete tasks as censored, not fast completions. Same provisional cap: 10-minute
setup + 20 minutes per packet in both arms; no timing has been run or calibrated.
Retain capped attempts; revise an infeasible cap prospectively, not after viewing winners.
Report per-person total setup + all task time and correctness alongside per-task time.
Record table-authoring/source-curation/maintenance effort separately as provider cost;
free pre-authored tables cannot establish a favorable production cost or onboarding ROI.

Do not adopt R01's 20%/two-of-three suggestion as a statistical threshold. These three
purpose-built tasks cannot estimate population effects, significance, demand or payment.
For this round, the gate is independent agreement that the keys and equal-evidence
design are defensible. A later authorized feasibility exercise could justify further
research if T adds a correct action or reduces measured total effort with no material
miss/false assurance; report mixed results and require replication before value claims.
Pause/revise on unequal access, key leakage, unresolved key disputes or false assurance.
Narrow/pause the value hypothesis if competent M matches T at equal/lower effort, or
useful decisions remain dependent on evidence T cannot supply. No results exist here.

## A5–A6: decision, next questions and delivery boundary

**Narrow investigation to independent paper audit before implementation.** The design
can expose a bad mapping or unsupported assurance, but author-crafted tasks favor what
the author knows. P1 may be solved faster without T; P2 is also answerable from the
same short docs; P3 cannot be closed by a table. Successful paper correctness would
not establish incremental human or commercial value, automated accuracy or readiness.

Minimum future artifact proposal: facilitator-separated, frozen evidence/sheet/key
copies and a blank observation form. Any later implementation needs a separate decision;
no analyzer is needed to audit this protocol. Onboarding would require exact versions,
source ranges and resolved config, plus citation review and unsupported-mapping handling.
Customer access/consent and source handling remain unvalidated; no outreach authorized.

1. **Are keys and baseline fair under independent challenge?** Deliver a row-by-row
   source/premise audit, disputed-key log and corrected frozen facilitator packet if
   needed. Do not report that audit as a participant experiment or demand signal.
2. **Can acquisition/publication support this artifact safely?** Deliver a bounded
   interface/feasibility note for snapshot identity, parser/config limits, citations,
   redaction and verified-handle output, with acceptance oracles or an explicit blocker.

Coordinator chooses the next round. No automatic dispatch, product scope/contract or
status-field changes. Existing requirements, research artifacts and 55 SDD headings
remain byte-identical. No executable fixture, SDK/analyzer/customer run, benchmark,
installation, probe, account, environment change or spend occurred. PR records exact
checks, preservation, failed attempts, live attribution/CI and literal Sourcery state.
