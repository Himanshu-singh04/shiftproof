# R01: customer value of cited upgrade triage

Status: **narrow the hypothesis; continue investigation only**, for
[issue #17](https://github.com/Himanshu-singh04/shiftproof/issues/17).
Incremental decision value and willingness to pay remain unestablished.
Coordinator review pending; no scope or product claim adopted.

## Authorization, question and bounds

Founder instructed the non-build sessions to “keep on researching and improving the
plan from business and development perspective in all aspects”, with roles rotating
after the current ReleaseLens build priority. Founder explicitly said **“resume
everything”** on 2026-11-20 after quota interruptions. Same persistent GPT-6 Astra /
OpenCode worker; no subagents, provider change or expanded permissions.

Question: does callsite-linked, cited upgrade triage add a useful decision beyond
release notes, existing tools and manual review when replay is unavailable?
Successful start: **2026-11-20 05:29:52 UTC**; stop by **07:29:52 UTC**, earlier if
supported. At most eight primary documents, three incidents and two tools; snippets
may locate sources but cannot establish claims. No execution, installations, probes,
customer input, accounts, outreach, marketing or paid spend.

Approved base: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.
[Pending B03a record at its exact revision](https://github.com/Himanshu-singh04/shiftproof/blob/644be51bbbac996f7fc9023530516bf37a409190/docs/b03a-path-decision.md)
is provisional only; its branch and draft PR #16 remain unchanged. No predecessor
proposal is merged or adopted. Replay stays disabled / unknown / ISOLATION_UNAVAILABLE.
The historical Stripe pair is research, not shipped or current-market support.

## Recommendation and confidence

Investigate one small benefit: help an upgrade author and reviewer locate relevant
release changes and agree on the next evidence to collect. A callsite/citation map
could reduce repeated searching, but this round did not observe that saving or a
decision improved over competent manual review. Do not fund a static-only product
or change the compatibility promise on this evidence. Replay remains unavailable.

Confidence: **moderate** that this is a coherent review aid; **low** that it changes
decisions enough to justify another tool; **unknown** commercial demand. Two public
reporters describe failures. Neither asks for this report, supplies a buying signal
or establishes incident frequency. A release announcement supplies the third case,
not a third customer incident. Historical examples cannot establish present demand.

## A1: one workflow, user and hypothetical buyer

Target hypothesis: the engineer maintaining one small TypeScript/Node service has
an SDK-update PR, an exact lockfile pair and several SDK callsites. Before review,
the engineer asks which release changes apply, which configuration needs inspection
and which scenarios need tests. A second engineer reviews that evidence and chooses
to proceed with existing checks, request focused checks or defer the upgrade.
This is the workflow in [product planning](../product.md), not an observed customer.

User: upgrade author and reviewer. Hypothetical buyer: the service-owning engineering
lead who controls developer-tool spending; in a small team these may be one person.
No source identifies an actual buyer, procurement process or budget. The decision
here concerns review effort and missing evidence, not certification of compatibility.
The two reports below establish specific failures only. Small-team fit, repeated
review burden, willingness to provide source and ability to pay remain hypotheses.

## Source ledger: eight primary documents

Read on **2026-11-20**. Source dates below describe the evidence, not this research.
HTML and API representations of the same issue/release count as one document.
No issue comments, linked reproduction repositories, linked migration guides or
secondary sources were read. Search results only located the node-fetch report.
The ledger includes the two less-informative GitHub pages; neither disappears from
the budget because it failed to establish the hoped-for pricing detail.

| ID / exact source | Date, locator and brief evidence | Claim boundary |
| --- | --- | --- | --- |
| S1 [node-fetch #1226](https://github.com/node-fetch/node-fetch/issues/1226) | Opened 2021-07-28; updated 2021-08-31. Body: “When upgrading ... to `v3.0.0-beta.10`” with TypeScript CommonJS output, `ERR_REQUIRE_ESM`. | Firsthand reported failure; body/metadata only. Closed state does not establish a successful workaround. |
| S2 [node-fetch v3.0.0 upgrade guide](https://raw.githubusercontent.com/node-fetch/node-fetch/v3.0.0/docs/v3-UPGRADE-GUIDE.md) | Version-tagged historical guide, publication date not supplied. “Converted to ES Module”: ESM-only since `3.0.0-beta.10`; “stay on v2” for CommonJS or async `import()`. | Official migration guidance, not proof the reporter applied it or present-day support advice. Guide says it is not exhaustive. |
| S3 [AWS SDK JS v3 #6827](https://github.com/aws/aws-sdk-js-v3/issues/6827) | Opened 2025-01-18; updated 2025-02-09. Title/body: stream promise “never settle from 3.729.0”; body also says “stream pipe crashes”. | Firsthand report with symptom ambiguity; author's causal attribution, no independently verified root cause or resolution. |
| S4 [Stripe node v13.0.0 release](https://github.com/stripe/stripe-node/releases/tag/v13.0.0) | Published 2023-08-16T20:23:24Z; updated 2025-06-21. “1 reattempt ... (previously ... 0)”; pinned API `2023-08-16`; deprecated `del` removal. | Maintainer release claims; no customer complaint. Tag targets `3799c9a611b1f5c7d7718157f20d4046a91a811e`. Linked API changelog/migration guide not read. |
| S5 [GitHub: Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates) | Mutable docs, read date above. “Updates for packages”: manifest PRs; “review the changelog and release notes included in the pull request summary”. | Official capability claim; operator still checks tests/reviews/merges. No independent tool trial or exact version-update price here. |
| S6 [Mend Renovate family comparison](https://www.mend.io/renovate/) | Mutable vendor page, read date above. Comparison “Cost”: CLI Free, Community Free, Enterprise Paid. Benefits: PRs include “age, adoption, passing rates, and complete change logs”. | Vendor claims and listed tiers, not validated savings or behavior at a particular callsite. Numeric Enterprise price absent. |
| S7 [GitHub: Dependabot quickstart](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide) | Mutable docs, read date above. “About Dependabot” separates alerts/security/version updates; setup uses repo settings and `dependabot.yml`. | Onboarding evidence; no price established. Tutorial instructions were read as data, not executed; no fork/account/setup performed. |
| S8 [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans) | Mutable docs, read date above. “GitHub Free for personal accounts” includes Dependabot **alerts**; organization Free adds to personal Free. | Does not explicitly price version updates. Do not substitute alerts availability for verified version-update pricing. |

Limitations: eight purposively chosen documents, two reported incidents and one
release-only example; no representative sample, incidence rate or market sizing.
S1 predates stable v3 and S3 concerns specific Node/SDK combinations. Selection favors
visible public failures. Neither closed issue's comments were examined, so this
record cannot claim a confirmed fix, measured downtime or failed manual-review time.
All documents were accessible. One Python HTTPS reread failed certificate-chain
validation; `/usr/bin/curl` retrieved the same sources with TLS verification enabled.
No trust settings changed. Price uncertainty reflects source coverage, not a quote.

## A2: incident and release evidence matrix

“Could” below marks a worker hypothesis. No application source was analyzed and no
reported reproduction was run. Exact affected callsites in real services are unknown.

| Case / applicability | Reported pain and existing response | Cited static triage could answer | Execution/remote evidence still needed; missing facts |
| --- | --- | --- | --- |
| C1: node-fetch `3.0.0-beta.10`; TS `4.3.5`, Node `14.15.3`, npm `7.19.1`, WSL2 (S1, 2021-07-28) | Reporter compiles CommonJS then gets `ERR_REQUIRE_ESM`; asks for dual packaging. S2 explains the restriction and recommends v2 or async import. This is a docs-answerable migration choice. | Link an import and declared module configuration to the exact guide; ask whether to retain the historical CJS-compatible major or migrate module loading. This is often project-level, so per-callsite detail may add little. | Actual loader/build-chain behavior and success of migration need execution. Compile settings may differ by build target. No confirmed resolution or time saved; do not recommend old v2 as a current security/support choice. |
| C2: `@aws-sdk/client-s3` `3.729.0` and `3.731.1` vs reported-working `3.726.1`; Node `22.13.0`/`23.6.0` (S3, 2025-01-18) | Reporter says `Body.transformToWebStream().pipeTo(Writable.toWeb(destinationStream))` never settles and also describes a crash. Says prior docs/forum search found no solution. Suggests avoiding streaming at memory cost. | Locate that chain or unresolved wrapper and link the version-specific report; ask whether a representative stream-completion check is missing. Cannot infer the same defect from matching names alone. | Completion/crash, backpressure, memory and runtime interaction need representative execution; actual S3 request/response behavior may need service evidence. No reproduction, workaround validation, fixed version or causal attribution verified. |
| C3: Stripe `12.18.0` → `13.0.0` as the repository's historical pair; release S4 (2023-08-16) | Maintainer documents default retry 0→1, request-level retry disabling, API-version change and `del`→`cancel`. No user failure or workaround outcome in this source. | Connect known calls/config to retry/API-version review questions; locate direct deprecated method references. Explicit overrides could narrow a question if data flow is resolved, otherwise mark uncertainty. | Retry attempts/error timing require scenarios; remote API semantics require further evidence. Removed methods can already surface in type checking/manual search. S4 alone is incomplete migration coverage; historical B01 results do not prove customer value. |

**Existing-solution counterexample:** S2 supplies a documented answer to C1's module
loading choice. The additional benefit would be locating/applying that answer, not
discovering a new solution. No verified “reporter solved it” case was established
within this source set; closed status cannot substitute for that evidence. C3's
explicit rename is another change a reviewer can find without a new analyzer.

**Behavior-only counterexample:** C2 asks whether a stream completes under a particular
SDK/runtime combination. A citation or type-correct callsite cannot answer it. Even
offline replay would need representative stream behavior and would not establish
live-service compatibility. Report the next check and retain unknown behavior.

No case demonstrates a maintainer making a better decision with callsite-linked triage
than with the documented baseline. C2 does show a reported gap after manual searching,
but it points toward missing runtime evidence, not demand for static output.

## A3: alternatives at the task level and economics

Only two tools: Dependabot and Renovate, plus manual review. Claims describe official
documentation as of 2026-11-20; no installation or comparative product test occurred.
Absence of a capability in these pages is not proof the tool lacks it elsewhere.

| Task / alternative | Documented contribution | Limit for this hypothesis | Price and operating burden |
| --- | --- | --- | --- |
| Open/update a dependency PR: Dependabot (S5/S7/S8) | Reads configured manifests; creates update PRs with release notes/changelog; user reviews/tests. S5 describes a default three-day version-update cooldown, excluding security updates. | The pages do not establish a versioned behavioral explanation at each application callsite. Existing bundled notes weaken a generic summarizer's value. | Alerts appear in GitHub Free (S8); exact version-update price/conditions remain **unknown in this bounded set**. Repo configuration/access and test maintenance still cost effort; no inference that all CI usage is free. |
| Automate/prioritize update PRs: Renovate (S6) | Vendor lists update PRs, changelogs and merge-confidence ratings; configuration supports scheduling/grouping and CI integration. | Age/adoption/passing-rate signals do not prove this service's semantics. No callsite-proof capability established by this page. Vendor's “error-free merge” wording is not a guarantee this research adopts. | CLI self-hosted Free; Community cloud/self-hosted Free; Enterprise cloud/self-hosted Paid, numeric amount unknown. Comparison lists support only for Enterprise. CLI lacks listed automatic job scheduling; merge-confidence workflows appear only in Enterprise. Hosting, credentials, configuration and maintenance remain user work. |
| Decide applicability: manual release-note/guide review and source search (S2/S4/S5) | Human reads exact changes, searches imports/options and selects tests; C1 has direct guidance and C3 an explicit rename. | Human may miss wrappers or relevant defaults; frequency and cost of misses unmeasured. Manual review remains a strong baseline for a small call inventory. | No listed license charge for reading these public pages; engineer time, test upkeep and source handling are real costs with no measured amount here. |

S6's free offerings create price pressure for basic update automation. Its paid tier
does not show that a buyer would pay for ShiftProof or for callsite mapping. No vendor
ROI, customer count or marketing testimonial becomes demand evidence in this record.
Founder infrastructure spend for this round: **$0 new paid services**. Ongoing work
would include citation/version maintenance, analyzer precision, packaging, safe input/
output handling and support for disputed findings. No engineering cost, margin or
subscription price has been measured; $0 hosting does not mean $0 delivery cost.

## A4: possible benefit, smallest output and development burden

Potential benefit: a reviewer gets a short list of **source-linked questions and next
checks for one exact upgrade**, rather than searching the whole change history again.
Counterevidence: small codebases may need only source search; bots already supply
notes; obvious renames need little explanation; hard runtime cases remain unknown.
This benefit must beat those baselines after setup and false-positive review time.

Smallest useful output hypothesis: one local review table with exact source/target
versions, source file/range and import identity, cited change/excerpt/version scope,
applicability reason, unresolved configuration/wrappers and one suggested next check.
Include scanned/excluded/failed counts and a prominent behavioral-unknown limitation.
Do not turn missing calls or successful compilation into “safe to upgrade”. This is
a proposed research artifact, not a new schema/status, UI feature or accepted release.

Inputs/onboarding: selected repo snapshot, lockfile pair, approved source roots and
versioned documentation; user supplies the intended build target and reviews coverage
gaps. Dynamic imports, aliases, generated code, wrappers and external configuration
raise mapping cost. No credentials, production payloads or customer module execution
are necessary for the hypothesized table. Actual willingness to provide those inputs
is unknown; local handling may help privacy but does not remove parser/output risks.

Development implications: preserve read-only bounded acquisition, parse configuration
as data, constrain resource use and mark unsupported resolution. Treat citations and
source as untrusted; redact before persistence, render inert output and use the safe
publication boundary in [operations](../operations.md). Missing safe boundaries block
completion. The [evidence contract](../evidence-contract.md) still governs claims;
a static-only mode would need separate approval. No contract/status or roadmap gate
changes here. Choose a current SDK pair only through a separately approved decision.
The historical Stripe experiment proves neither present relevance nor willingness to
pay, and accepted B02 darwin tooling supplies no Linux/isolation validation.

## A5: unperformed future validation and stopping criteria

The following is a draft for a later authorized interview/pilot, **not outreach or
permission to collect customer input**. No participant, interview or pilot exists.

- Ask an upgrade author: “For your last SDK update, which decision took the most work?
  Show the notes/tests you used; what remained unresolved?” Avoid suggesting a need.
- Ask the reviewer: “Which calls/configuration changed your review decision? Could
  your existing bot plus source search locate them? What did that process cost?”
- Show a bounded mock report only after recording the baseline: “What would you do
  differently? Which row is redundant, wrong or requires runtime evidence?”
- Ask the potential buyer: “Who owns this work and tool budget? What would you replace,
  what input can you share, and what evidence would justify purchasing?” A favorable
  answer is stated interest, not payment or validated willingness to pay.

Proposed later pilot: compare the same exact upgrade under existing bot/docs/manual
review and a callsite-linked table; counterbalance order to limit learning effects.
Record setup, total review time, correct applicable changes, missed material changes,
false positives and the concrete decision/next-check difference. Reviewer adjudication
must use source/version evidence; unresolved runtime outcomes stay unknown.

Provisional success bar: in at least two of three independently reviewed upgrade
tasks, yield a correct actionable next-check/applicability decision the baseline missed
or reduce total review effort including setup by at least 20%, without a material miss
or a false compatibility assurance. These thresholds are proposed, not statistically
validated results. Separate authorization must define safe participants and artifacts.
Stop or narrow further if competent baseline review matches the result at lower cost,
most useful answers require runtime evidence, source/config burden dominates savings,
or reviewers mistake unknown for permission to merge. A commercial decision also
needs buyer evidence; even a successful usability comparison would not prove payment.

## Ranked next questions and handoff

1. **Does the proposed output beat manual review on a bounded task?** Deliver a
   pre-specified comparison protocol and three paper-only, source-cited task/answer
   packets, including a docs-solved and behavior-only control. Use reviewed synthetic
   examples; distinguish author-constructed expectations from observed customer value.
   Coordinator should authorize any new source budget or later independent evaluation.
2. **Can a local review table be acquired and published safely at acceptable effort?**
   Deliver an interface/unknowns note for source snapshots, citation identity, parsing
   limits, redaction and verified-handle publication, with concrete acceptance oracles
   and a feasibility blocker if needed. Documentation alone cannot close runtime gates.

Worker stops after this round; coordinator chooses and dispatches further work.
Issue #17 A1–A6 stay fixed. This record supplies the hypothesis, evidence/counterevidence,
bounded alternatives, recommendation and future questions; A2's confirmed successful
incident resolution remains **not established**, as allowed when evidence is absent.
All requirements, experiments, fixtures, captures, locks, workflows and 55 SDD headings
remain unchanged. PR records exact preservation/check/attribution/CI results, failures
and automatic Sourcery output. No research/customer execution, installation, probe,
interview, outreach, account creation or paid service occurred.
