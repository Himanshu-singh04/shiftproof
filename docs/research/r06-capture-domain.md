# R06: capture hash-domain decision packet

Status: **recommend original-domain/refusal wording; adoption prerequisites unresolved**,
for [issue #27](https://github.com/Himanshu-singh04/shiftproof/issues/27).
Documentation only; proposed wording below is not an adopted contract or schema.

## Authority and bound

Existing founder mandate authorizes ongoing research; this task dispatches the distinct
rawHash/redactedArtifact decision to the same persistent GPT-6 Astra / OpenCode worker.
No subagents, portfolio investigation or model/provider/permission changes.
Successful start **2026-11-20 07:08:41 UTC**; deadline **09:08:41 UTC**, earlier if enough.
One 180–250-line note; at most three external primary documents and eight paper cases.
Approved main: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.

Preserve founder-unapproved predecessor branches/checkouts/live PR heads:
- B03a #16: `644be51bbbac996f7fc9023530516bf37a409190`; full source/acceptance audit pending.
- R01 #18: `0de10807e8a02c918e19f6ee6c0f7a0320158d39`.
- R02 #20: `6dd79d5b9714eddfcfc3985aa50518055fecb8e5`.
- R03 #22: `8ac7ae8f2007d729d60aac443a2b9df6e6acf204`.
- R04 #24: `4a2c280d3848aa5389ffb452f13fb8ea6000f485`.
- R05 #26: `955ffe9e08ae0172aba2f61e6c5bc7050b0a1bee`; independent A1–A6 audit passed.

## A1: authority and distinct domains

All line references are at approved main: [EC](../evidence-contract.md),
[OP](../operations.md), [testing](../testing.md) and [SDD](../specs/001-mvp/solution-design.md).
The field names specify intended behavior, not an implemented schema. R05's
[exact reviewed note](https://github.com/Himanshu-singh04/shiftproof/blob/955ffe9e08ae0172aba2f61e6c5bc7050b0a1bee/docs/research/r05-redaction-identity.md)
is provisional context; none of its recommendations is imported as current authority.

| Exact clauses | Requirement / unanswered question |
| --- | --- |
| EC L36–51 | Required fields/lists, unknown null plus gap, closed revision, SHA-256 digest with byte size; hashes are not authentication. Generic null language does not decide capture-field nullability or which bytes are hashed. |
| EC L139–153 | Observation includes rawHash/redactedArtifact/normalizedHash, execution and gaps; typed distinctions retained, no silent stringification; redact before persistence, required dimension lost => unknown, no secret hashes. Redaction/encoding order and each hash's domain remain unspecified. |
| EC L164–180 | Ordered, reviewed normalization; default none; no broad deletion of material differences; retain redacted raw and normalized views. Redaction is not automatically a normalization rule; no explicit Observation path to the normalized view is listed. |
| EC L184–208, L228–288 | Keep every attempt, unknown selected-observation IDs are null, exact gap reason codes; validate identity/capture/isolation before comparison. Missing capture cannot become an empty successful observation. Unknown is not a malformed-record exemption. |
| EC L306–338 | Findings contain exact observation/outcome/obligation/citation/gap closure; Comparison assigns status, Report never invents missing fields. Redaction cannot remove an attempt from closure to obtain a favorable result. |
| EC L340–367 | Validated inert rendering, verified artifact bytes, safe marker publication, whole-record semantic projection. Only listed operational exclusions; raw capture hashes remain semantic. A manifest hash alone is not an unspecified substitute for an Observation identity. |
| OP L63–65, L77–92, L100–114; T03–T05/T07–T11 | Complete statuses use exits 0/1/2; invalid/failed/incomplete uses 3. Safe redacted diagnosis/retention, no status repair or automatic resume; secrets absent from reports/logs/hashes. Publication and replay enforcement remain separate gates. |

Distinct domains, named only for this discussion, not new schema fields:
- **Captured value:** runtime event/value before any byte encoding; not itself a file.
- **Typed encoding:** preserves absent/present, null/undefined, numbers, binary, event
  order, arrays and structured exceptions. EC requires these distinctions, not a codec.
- **Pre-redaction bytes:** that encoding applied to the selected original capture.
  This is a conceptual domain; secret-bearing bytes need not be serialized or hashed.
- **Retained bytes:** encoding of the safely redacted typed capture, before comparison
  normalization. Removing a value changes this domain even if its position is masked.
- **Normalized view:** retained typed capture after declared ordered normalization,
  encoded under the same fixed format; normalization is not allowed to restore secrets.
- **Semantic projection:** EC L350–367's whole RunRecord, not either artifact byte stream.

No external sources fetched (**0 of 3**); repository clauses suffice. The typed byte
grammar, redaction classifier and safe omission representation remain prerequisites,
not ordinary JSON serialization or a secret scanner. No hashes/examples are computed.

## A2: three alternatives and exact proposed wording

**Current wording being clarified:** EC L141 lists “rawHash, redactedArtifact,
normalizedHash”; L152–153 says “Raw artifacts are redacted before persistence. If
redaction removes a required comparison dimension, report unknown; hashes of secrets
must not be published.” L179 says “Retain redacted raw and normalized views so reviewers
can inspect every change.” These sentences do not identify matching artifact/hash pairs.
All quoted replacement/addition text below is **proposed**, including stricter refusal.

### Common proposed addition, conditional on choosing one alternative

> Every retained capture view uses the schema revision's fixed typed encoding. Hash
> size counts the exact encoded artifact bytes, not decoded characters, original-value
> length or a different file. Hash references retain EC's SHA-256 representation.
> redactedArtifact is a required, non-null contained bundle-relative path. Add required,
> non-null normalizedArtifact to Observation, identifying a separate normalized view;
> normalizedHash is required and non-null and binds precisely that view's bytes.
> Both referenced files must exist and pass size/hash/type validation before display.
> The typed redaction policy is fixed by the recorded tool/adapter build; it is not an
> undeclared per-run setting. Policy/build or normalization changes require a new run.
> No pre-redaction secret bytes or hashes enter files, scratch, caches, logs or records.
> Observation events/assertionResults must agree with the safe retained view; removed
> assertion evidence becomes a gap, never a fabricated successful assertion.

`normalizedArtifact` is **new proposed wording**, not already in EC: it makes SDD L222's
separate-view reference explicit. Every alternative requires a new schema revision and
unknown-revision rejection; no number is assigned. Build identity does not prove correct
redaction. Configurable redaction needs a separate policy-identity decision, not an
undisclosed reuse of normalizationPolicy or operationalMetadata.

### A — original-domain only, refusal when that domain cannot be retained safely

**Proposed addition to EC L139–153 / replacement of the ambiguous rawHash meaning:**
> rawHash is required and non-null. It identifies the exact typed pre-redaction capture
> bytes. A collected Observation may be published only if privacy validation establishes
> that redaction is byte-preserving and the same safe bytes exist at redactedArtifact.
> If redaction changes the capture or its original domain cannot be safely established,
> refuse completion of the evidence bundle; do not omit the collected Observation,
> substitute a derivative hash, or make rawHash null. Preserve only safe diagnostic/
> attempt evidence; return failed/incomplete execution with exit 3 and no final marker.

Reader can recompute rawHash from identical retained bytes: relative byte integrity,
not proof that no producer altered them or that the SDK emitted them. Irrelevant and
material removal are both refused, a coverage cost **not currently adopted**. No
original-domain exception based on entropy, local-only storage or operator confidence.

### B — retained-domain identity with an explicitly changed meaning

**Alternative proposed wording for EC L139–153 and L363:**
> rawHash is required and non-null and means the exact bytes at redactedArtifact after
> typed redaction and before normalization. It does not identify pre-redaction bytes;
> readers must label it retained-capture identity and must not claim original equality.
> No original capture digest is persisted. rawHash, normalizedHash and both view paths
> remain in the semantic projection. Redaction loss is recorded in existing gaps;
> removing any required comparison evidence makes affected outcomes unknown. Removing
> an irrelevant value does not alone settle an outcome: all EC prerequisites still apply.
> A loss gap is nonblocking only if no frozen prerequisite/dimension was lost; uncertainty
> about that determination is blocking, not evidence of irrelevance.

This preserves derivative artifacts but changes an existing field's semantics. No silent
reinterpretation of old records/readers, even for no-op redaction. Irrelevance needs
frozen comparison dimensions and policy evidence, never matching hashes alone. Original
capture identity is intentionally not represented; provenance remains limited.

### C — narrowly represented unknown original, with separate retained identity

**Alternative proposed additions/replacements for EC L36–47, L139–153, L253–258, L363:**
> rawHash retains A's original-domain meaning. Permit null only for a collected capture
> whose original cannot be safely identified and verified from retained bytes after
> redaction. Its safe derivative must exist. Null requires blocking REDACTION_LOSS and forces
> outcomes unknown, even when the removed value is described as irrelevant.
> Add required non-null retainedHash, binding exactly redactedArtifact's encoded bytes
> and size. When original and retained bytes are safely identical, rawHash is non-null
> and equals retainedHash; otherwise this alternative stores no original digest.
> retainedHash, rawHash including null, both view paths and normalizedHash are semantic.
> Missing artifacts or no capture do not qualify for this null exception. Required
> fields may never be omitted; unknown does not excuse a wrong-domain hash.

C needs **retainedHash plus normalizedArtifact**, explicit nullable rawHash validation
and an original-identity prerequisite for comparison, all proposed versioned changes.
Manifest-only derivative hashing leaves raw Observation byte identity outside its semantic
projection when rawHash is null. C permits diagnosis but yields unknown more often than B;
the extra field supplies neither authenticity nor original reconstruction.

## A3: shared paper lifecycle and failure dispositions

1. A future enforced capture yields a bounded typed value plus side/attempt identity.
   No execution happens here. Unsafe acquisition or missing isolation blocks upstream;
   identity policy cannot enable replay. Preserve safe attempt facts, never secret logs.
2. Apply a reviewed, fixed typed redaction policy before persistence. Treat original
   byte encoding as conceptual until its safety is established; do not hash a secret to
   decide whether it is safe. No temporary originals, upload or operator-source deletion.
3. Apply A's byte-preserving acceptance/refusal, B's retained-only identity, or C's
   explicit original-unknown rule. Exactly one versioned policy applies to the record;
   no per-observation switching of meanings, opportunistic retries or favorable omissions.
4. Check typed completeness and required comparison dimensions. Redaction must not turn
   absence into null, remove event ordering or counterfeit a captured value. A partial
   capture uses truthful completeness/execution gaps; unsupported encoding refuses a
   complete record rather than serializing a misleading empty payload.
5. Comparison normalizes the retained typed view under frozen rules and emits the
   separate normalized view. Losing a required dimension remains REDACTION_LOSS/unknown;
   normalization cannot erase that gap. Safe unchanged captures still need every EC
   identity, assertion, mapping, citation, isolation and execution prerequisite.
6. Validate fields, both view references, safe bytes, hash domains/sizes and full closure.
   Keep every collected attempt in observationIds and matching findings. If a collected
   observation cannot be represented, refuse the completed bundle, not just that row.
7. A reader checks actual retained bytes and renders persisted outcomes without deriving
   a new status from digest equality. Wrong/missing artifacts => rejected completed display.
   Even known-valid data cannot be published while the publisher gate remains unresolved.

**Valid identity** is separate from **semantic completeness**: B can bind safe retained
bytes while a lost dimension makes the comparison unknown. C additionally makes missing
original identity blocking. A refuses when redaction changes bytes rather than inventing
a nullable field. A redaction gap never licenses a secret digest or a fabricated artifact.
Complete valid unknown could use exit 2 only after independent safe publication; invalid
identity/record, incomplete execution or refusal uses exit 3/no successful completion.
Failed/cancelled runs may retain validated incompatibility per EC, not become complete.
An earlier completed report is not edited to repair status; new evidence requires a new run.

## A4: eight paper oracles, no fixtures or values

Notation below is prose only: **present** means a required non-null field, **null** is
C's proposed explicit exception, **refuse** means no completed bundle/exit 3. All
alternatives need both required artifact paths and normalizedHash when an Observation is
retained. C additionally requires retainedHash. None is a measured or adopted result.
Each negative uses C1's safe, stable control for the relevant transition. No completed
publication or compatible result is authorized while replay/publication remain blocked.

| Case / control and change | Proposed field/domain and permissible reader claim | Outcome / remaining uncertainty |
| --- | --- | --- |
| C1 Safe unchanged typed capture, no normalization change | A rawHash present = original/retained bytes; B present = retained only; C rawHash and retainedHash present = identical safe bytes. normalizedHash binds its separate view; reader verifies bytes, never authenticated origin. | No missing evidence invented; future equivalent/different requires all EC prerequisites, not matching hashes. Actual round has no capture; replay remains unknown. Fixed encoding/policy still undecided. |
| C2 Remove an irrelevant value, unlike C1's no-op redaction | A refuses; B rawHash present binds derivative; C rawHash null, retainedHash present, blocking REDACTION_LOSS. Both views remain required for B/C; no original equality claim. | B may preserve usable comparison evidence only if irrelevance and all prerequisites are established; C outcome unknown/selected IDs null; A no completed record. Unproven irrelevance blocks comparison, never a favorable default. |
| C3 Remove a required comparison value from C1 | A refuses; B derivative rawHash present; C rawHash null and retainedHash present. Safe retained/normalized bytes verify only what remains. | B/C unknown with REDACTION_LOSS; no asserted material changedPaths. Required identity/closure must still validate or refuse. A cannot downgrade to C without a new adopted version. |
| C4 Two distinct originals collapse to identical retained bytes, versus identical unchanged control | A refuses changed captures; B equal retained hashes attest derivative equality only; C null originals plus separately present retained hashes do not identify the originals. | Never deduplicate attempts or infer original/semantic equality. Required-value loss => unknown; any claim of irrelevance needs evidence independent of the sanitized match. This is redaction information loss, not a demonstrated hash collision. |
| C5 Substitute null, omit a field or supply an original/normalized hash in the retained-domain position | A/B reject null rawHash; C accepts it only with its narrow gap/artifact rules. All reject omitted required fields, wrong size/domain or missing normalizedArtifact/normalizedHash; C also rejects absent retainedHash. | Invalid record/refuse, not complete unknown. If differing domains happen to yield identical bytes, digest checks alone cannot expose mislabelling; schema/version and production-policy evidence remain necessary. |
| C6 Remove/change either retained view after review, unlike C1's intact views | Both paths required in all alternatives; raw/retained and normalized domains verified separately against actual bytes. A stored matching string is insufficient; C null original does not waive derivative verification. | Missing/mismatched view => reader rejection/failed validation exit 3. Rewriting both bytes and reference values cannot prove prior review or origin; any new evidence needs a new record/review. |
| C7 Change normalization order or redaction policy with C1 bytes held stable where possible | Ordered normalization IDs and fixed tool/adapter policy build identity change the semantic record even if artifact bytes happen to match; all required view/hash fields remain present except C's qualified null. | New run/digest/review required; never reinterpret old observations. If redaction policy can change without recorded build identity, the proposed package is unsupported until an explicit policy-identity decision, not an operationalMetadata note. |
| C8 Never-started capture versus an attempted/collected-but-redacted capture | Never-started scenario may have no Observation and empty observationIds with NOT_RUN/ISOLATION_UNAVAILABLE; no synthetic empty artifact/hash. Collected capture must stay represented: A refuses changed bytes, B retained fields, C qualified null plus retained fields. | B/C retain all attempts and applicable loss gaps. An attempted run with no safe representable capture is incomplete/refused, not relabelled never-started; generic null does not decide its artifact rules. Missing evidence cannot pass. |

Exact reasonCodes remain the distinct referenced Gap codes; unknown selected observation
IDs remain null, observationIds retain attempts, and finding closure follows EC L318–330.
No case changes aggregate fail precedence, makes Report recompute outcomes or allows a
normalized digest to stand in for a raw/retained artifact. No entropy-based exception.

## A5–A6: recommendation, reconciliation and next question

Recommend **A plus the common explicit normalized-view reference clauses** as the
smallest coherent policy package among these choices: keep original meaning, verify
it from the same safe retained bytes, and refuse when redaction changes them. It adds
one explicit artifact path but no second raw identity or nullable-hash branch. This is
stricter coverage than current unresolved wording, so research acceptance cannot adopt it.
It deliberately forgoes B's useful derivative comparisons and C's redacted diagnostics
as completed records; safe incomplete attempt diagnostics remain required.

Adoption is still **blocked** on a fixed typed serialization, demonstrated privacy/
byte-preserving acceptance rule, and agreement to the proposed field/version changes.
If these cannot be specified, the result remains refusal, not a claim of safe intake.
If product needs require publishing changed captures, return to B/C for explicit policy
choice rather than silently weakening A. No implementation or qualification authorized.

| Reconciliation surface, only after explicit policy adoption | Required change / compatibility boundary |
| --- | --- |
| EC L20–28, L36–51, L139–153, L164–180 | Add normalizedArtifact path/required-field rules, selected raw/normalized byte domains and refusal condition; settle typed encoding. C would also add retainedHash/null exception; B would explicitly change rawHash meaning. |
| EC L184–208, L241–288, L306–367 | Preserve attempts/closure; selected alternative's prerequisite/gap behavior and all new evidence fields stay semantic. Unknown revisions rejected; no operationalMetadata escape or silent migration of old digests. |
| OP L63–65, L87–114; T03–T05/T07/T08/T10/T11 | Document refusal versus complete unknown without changing exits; retain safe diagnostics, no secret originals. Later approved checks must distinguish the eight paper cases and encoding/policy drift; none added or run now. |
| SDD L134–135, L189–190, L222–254, L340–348, ADR-04 | Reconcile Replay.run Observation output, Comparison.evaluate inputs/results and Report.write validation; new versioned public evidence contract/reader behavior. No SDD heading or interface is changed by this note. |

No implemented product records justify reinterpreting revision 0.1 or research captures.
Use a separately adopted revision; no number/converter is selected. Research review/merge
accepts this recommendation record only; founder policy adoption, normative reconciliation
and later implementation/qualification are separate authorizations.

One distinct later question: **can a fixed typed capture encoding represent incomplete
and unsupported values truthfully without manufacturing an empty successful capture?**
Prerequisites: selected domain policy, EC L148–151 distinctions, bounded representable
types and explicit partial-attempt semantics. Stop if it needs secret persistence,
silent stringification, deleted attempts or unapproved fields; return a decision gap.
This is a later specification question, not permission to build a codec or corpus now.

Operators bear refusal handling and review of safe diagnostics; maintainers must pin
encoding/policy to build identity, review omission/materiality behavior and maintain
versioned readers and two retained views. A sacrifices coverage; B adds derivative-claim
discipline; C adds identity/null branches. Costs, performance and customer value are
unmeasured. Source/lock/citation domains remain unsolved; no static-only scope adopted.
Publication stays blocked; replay **disabled / unknown / ISOLATION_UNAVAILABLE**.
ReleaseLens scope/sequence applies there only; PR #19 awaits independent review, not
approval/merge. No founder decision/approval request active and no cross-project import.
Existing repository checks only; no code/schema/fixtures/hashes/runtime/native/corpus
tests, installs, customer operations or spend. Checks, failures, exact head/base/CI and
literal Sourcery are in the PR handoff. Synthetic text is not assent; provider/quota
error stops without retry/bypass. Stop for coordinator review.
