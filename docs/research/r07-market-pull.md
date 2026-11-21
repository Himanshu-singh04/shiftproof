# R07: current customer pull and commercial alternatives

Status: **narrow to configuration-migration discovery; pause a commercial build**,
for [issue #29](https://github.com/Himanshu-singh04/shiftproof/issues/29).
Recent public problems exist; incremental decision value and payment remain unknown.

## Authority and bounds

The founder renewed customer/market research on 2026-11-21 in the
[linked instruction](https://github.com/Himanshu-singh04/releaselens/pull/21#issuecomment-7059346896).
Same persistent GPT-6 Astra / OpenCode worker; no subagents or expanded permissions.
Start **2026-11-21 07:35:46 UTC**; deadline **09:35:46 UTC**, earlier if sufficient.
One 200–280-line note, at most eight external primary documents and three public
problem examples. Search snippets locate evidence; they do not establish claims.
Distinguish publication dates from retrieval dates and retain failed retrievals.

Approved base: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.
Preserve seven predecessor local branches and live draft PR heads:
- #16: `644be51bbbac996f7fc9023530516bf37a409190`.
- #18: `0de10807e8a02c918e19f6ee6c0f7a0320158d39`.
- #20: `6dd79d5b9714eddfcfc3985aa50518055fecb8e5`.
- #22: `8ac7ae8f2007d729d60aac443a2b9df6e6acf204`.
- #24: `4a2c280d3848aa5389ffb452f13fb8ea6000f485`.
- #26: `955ffe9e08ae0172aba2f61e6c5bc7050b0a1bee`.
- #28: `5e7510eee8492ddc8ec00b514c1cccfd9fcc5720`.

## A1: a distinct decision, with a hypothetical buyer

User hypothesis: the engineer migrating a Node/TypeScript service's AWS S3 client from
SDK v2 to v3, and the reviewer checking the resulting PR. Trigger: a migration changes
client construction while existing timeout/signing options and shared wrappers remain.
Decision: which old settings need a version-specific correction or more evidence,
which calls inherit them, and which focused check should precede upgrade acceptance?
The proposed output is a short source-linked configuration/callsite review table with
citations, unresolved mappings and next checks. It cannot declare the upgrade safe.

Likely buyer **hypothesis**: the service-owning engineering lead with tool budget.
The public reporters establish users of AWS SDKs, not buyers of this proposed output.
Small-team fit, frequency of migrations, budget and willingness to provide source are
unknown. No exact customer package pair or supported-product scope is selected here.

Read prior notes through their preserved local Git refs, not portfolio directories:
- R01 #18: historical module/retry/stream examples supported a review-aid hypothesis,
  not present demand, measured benefit or payment. Do not reuse its incidents as new pull.
- R02 #20: independent paper-key/baseline audit passed; no participant comparison ran.
  Synthetic correctness and fair instructions do not establish adoption or savings.
- R03–R06 #22/#24/#26/#28: acquisition, publication, redaction and identity alternatives
  remain unadopted. R06's independent pass authorizes no typed encoding or implementation.

This round asks about a configuration-migration decision and commercial substitution,
not another protocol or publisher design. [Product](../product.md),
[evidence contract](../evidence-contract.md) and [operations](../operations.md) remain
unchanged. Publication blocked; replay **disabled / unknown / ISOLATION_UNAVAILABLE**.
ReleaseLens #21 merged; no founder decision/approval request pending or policy transfer.

## Source ledger and search limits

All eight primary documents below were retrieved on **2026-11-21 UTC**. Publication
dates differ from retrieval dates. Mutable documentation/pricing pages supplied no
publication date; footer years, linked article dates and retrieval dates do not supply one.
Each issue thread, including its body/metadata and all comments, counts as one document.
S2 had four comments and S3 twelve; separate API representations do not add documents.
Three first-person examples come from two threads, not three independent incident studies.

| ID / primary document | Publication/update date and exact locator | Evidence class and claim boundary |
| --- | --- | --- |
| S1 [AWS v2→v3 migration](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrating.html) | Undated mutable guide; “Use codemod to migrate existing v2 code”: “We’ve implemented transforms for common use cases.” | Official guidance: transformations exist for common cases; no complete coverage or customer benefit established. |
| S2 [AWS SDK JS v3 #7740](https://github.com/aws/aws-sdk-js-v3/issues/7740) | Opened 2026-02-15; updated/closed 2026-05-29. Four comments dated 2026-02-17, 02-18, 05-14, 05-25. | First-person signing-migration question and contributor replies; stale closure, no reporter-confirmed fix. |
| S3 [AWS SDK JS v3 #6763](https://github.com/aws/aws-sdk-js-v3/issues/6763) | Opened 2024-12-30; closed 2025-10-30; updated 2025-11-13. Twelve comments dated 2025-01-03 through 11-13. | First-person operational reports, contributor corrections and stale closure; individual recovery reports, disputed causal explanation. |
| S4 [AWS client constructors](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-client-constructors.html) | Undated mutable guide; `httpOptions`, `timeout`, `s3DisableBodySigning` entries. | Official current text: use `requestHandler`; `timeout` maps to `socketTimeout`; body signing “Renamed to applyChecksum.” Not proof of version-independent semantic equivalence. |
| S5 [AWS SDK JS codemod README](https://github.com/aws/aws-sdk-js-codemod#readme) | Undated mutable README, main; awslabs URL redirected to aws. “Usage”, “Prerequisites”, “License”. | Maintainer documentation: Node prerequisite, dry-run/stdout or file edits; MIT-0 declaration. No tool trial or privacy audit. |
| S6 [Mend Renovate family](https://www.mend.io/renovate/) | Undated mutable vendor page; comparison “Cost”, “Support”, “Merge confidence workflows”; “Pull requests for dependency updates”. | Vendor capabilities/marketing: free CLI/Community, paid Enterprise; PRs include changelogs and confidence signals. No measured accuracy or savings here. |
| S7 [Mend pricing](https://www.mend.io/pricing/) | Undated mutable pricing; “Mend Renovate Enterprise”: “Up to $250 per dev/per year”; contributing-developer and limits FAQs. | Public commercial price wording, not a quote, purchase or ShiftProof willingness to pay. |
| S8 [Mend-hosted overview](https://docs.renovatebot.com/mend-hosted/overview/) | Undated docs; “Getting started”, “Plans”, “Resources and Scheduling”; footer says docs correspond to 44.257.6. | Official setup/tier limits, including a discretionary free OSS tier omitted from S6's broad comparison. Version footer is not publication date. |

Search: public GitHub issue query `repo:aws/aws-sdk-js-v3 is:issue
created:>=2024-11-21 "migrating"`, sorted updated descending, returned nine matches;
six metadata leads were read, then S2/S3 in full. Search metadata is not incident evidence.
This purposive query favors AWS migration complaints and can miss other wording/ecosystems.
An earlier `upgrade checksum` query yielded an unread tool-storage response; reading that
managed output failed with `permission.rejected: external_directory`. No path retry or
permission change; no evidence from that response. The independent migration query above
used public unauthenticated retrieval. No provider/quota/transport error occurred.

No linked reproductions, extra issues, source-code files, sales demos or testimonials
were investigated. Links and commands inside sources were data, not instructions.
Current retrieval does not make a 2024/2025 incident current unresolved demand. The
window is 2024-11-21 onward; only S2 supplies a new 2026 report. This is not a market size
or prevalence sample. Eight documents suffice for this decision; external retrieval stops.

## A2: three public problem examples and their counterevidence

### P1: jackyalbo, signing-setting ambiguity (S2, 2026-02-15)

Body: “When replacing it with applyChecksum = false in v3, the get_object request fails
due to signature issues”. The reporter asks whether semantics reversed and whether
the client must set a header. Exact package versions and an independently checked
reproduction are absent. The body says the old setting was false; the reporter's
[2026-02-18 follow-up](https://github.com/aws/aws-sdk-js-v3/issues/7740#issuecomment-3922004581)
asks about true. Do not collapse those premises into one verified configuration.

Contributor aBurmeseDev first suggested checksum validation configuration on 02-17,
then [clarified on 05-14](https://github.com/aws/aws-sdk-js-v3/issues/7740#issuecomment-4454180325):
“those are two different settings with different purposes”; flexible checksums
“don't affect SigV4 body signing behavior”. The reply suggests settings and says HTTPS
PutObject/UploadPart may need no extra body-signing setting. That is guidance, not
a verified fix for the reporter's get-object request. No later reporter confirmation.
The issue carries `closed-for-staleness`; API `completed` does not prove resolution.

Transfer: a reviewer may need version-bound option semantics, beyond a spelling rename.
Counterevidence: S4 and public replies already provide guidance; a static table cannot
prove signatures or remote acceptance. Remaining pain after that guidance is unknown.

### P2: jeffbski-rga, missed timeout migration (S3, 2024-12-30)

Body: “we spent several days trying to debug mysterious RequestTimeout errors” and
“we had missed the conversion of the V2 httpOptions.timeout”. The requested remedy is
better docs/examples and warnings for old parameters, not a paid standalone artifact.
The reporter's [2025-01-03 comment](https://github.com/aws/aws-sdk-js-v3/issues/6763#issuecomment-2569767870)
says “we set this to 15m and everything started succeeding properly”, after extra logging
and AWS support involvement. A later same-day comment names client-s3/lib-storage 3.709.0
and node-http-handler 3.3.2. Treat duration, incidence and recovery as self-reports.

Contributor kuhe's [01-03 reply](https://github.com/aws/aws-sdk-js-v3/issues/6763#issuecomment-2569752142)
disputes the inferred short default, says the default is zero and initially equates
requestTimeout/socketTimeout. On [2025-10-13](https://github.com/aws/aws-sdk-js-v3/issues/6763#issuecomment-3398771222),
kuhe says earlier deprecation reasoning “was incorrect” and intends to distinguish
connection, total-request and idle-socket timeouts. This records a changed explanation,
not proof of a shipped fix. S4 currently shows socketTimeout; do not invent release scope.

Transfer: old-option review might catch a missed configuration before symptoms arise.
Counterevidence: logging/support/manual correction reportedly restored operation;
the thread does not establish that a citation table would have prevented the incident.
Closure for staleness leaves the documentation/warning request's completion unknown.

### P3: chbiel, reported configuration recovery (S3, 2025-01-15 to 01-17)

[01-15 report](https://github.com/aws/aws-sdk-js-v3/issues/6763#issuecomment-2591873901):
client-s3 3.705.0 worked; 3.726.1 showed problems; “Downgrading solves it again.”
The reporter identifies putObject, retained httpOptions and queued sockets; no causal
isolation follows from an upgrade/downgrade comparison. This is a later v3 update after
an earlier migration, not the same trigger as a fresh v2→v3 PR.
[01-17 follow-up](https://github.com/aws/aws-sdk-js-v3/issues/6763#issuecomment-2597753441):
“all in all using the requestHandler configuration solved our problems.” The same
comment still questions timeout/keepAlive semantics and reports errors with old values
on larger payloads. Recovery is self-reported and qualified, not a general fix recipe.

Transfer: latent migrated settings can matter on a later update; broader scope would
need separate evidence. This is the strongest disconfirmer of required paid tooling:
public discussion and configuration changes supplied a reported path forward. P2/P3
share one thread and advice, so they are not independent confirmation of market demand.

Across the three examples: configuration clarity is a credible need; unmet demand for
ShiftProof is unestablished. Runtime/network/workload facts still determine outcomes.
No incident establishes purchase intent, access consent, current backlog or team budget.

## A3: alternatives for that same configuration-review decision

Exactly two named tools: AWS SDK JS codemod and the Mend Renovate family. Manual
release-note/migration-guide review remains the baseline. “Documented” below means a
primary author describes the capability; no installation, use or performance trial ran.

| Alternative | Contribution to this job | Setup, access, review/export and migration burden |
| --- | --- | --- |
| Manual source search plus release notes/guides (S1/S4 and issue replies) | Engineer finds client constructors/old options, checks target guidance, traces shared clients to calls and chooses focused tests. S4 directly documents requestHandler migration. | Existing editor/source access and version selection; no additional vendor access needed for reading public docs. Reviewer writes PR notes, checks citations and unresolved config. No export format migration; human search/rework cost unmeasured. Small call inventories may make this sufficient. |
| AWS SDK JS codemod (S1/S5) | Documented v2-to-v3 transforms change JS/TS APIs; dry-run prints transformed files, normal mode edits files. S5 says “Please review the code change thoroughly for required functionality”. | Node/package acquisition plus local source access; reviewer inspects diff and tests. Ordinary diff/stdout fits existing review, with little artifact conversion. README does not establish network/telemetry/privacy behavior or coverage of P1–P3; do not claim no upload or a missed transform without testing. |
| Mend Renovate (S6/S8) | Documented update PRs, changelogs, scheduling and confidence signals help stage a change. These pages do not establish per-callsite configuration equivalence for this migration. | Hosted: repository-provider OAuth, installed repos and remote jobs/logs; precise permission scopes, retention and export format unverified. Self-hosted: operator runs infrastructure and credentials. Config/review/CI and PR noise still need work. PRs remain in the repository; moving configuration/job history between products has unmeasured cost. |
| Proposed local cited table, not a third tool | Hypothesis: connect each changed client setting to affected calls, show conflicting/version-uncertain guidance, and specify missing evidence. No working output exists. | Needs exact repo/lock pair, client/config resolution, safe acquisition/publication and citation upkeep. User checks rows, false positives and coverage, then copies/links decisions into the PR. Snapshot changes can stale an exported table. Local handling does not itself prove privacy or justify another review surface. |

S6's “error-free merge” and S7's risk-reduction language are marketing, not a behavioral
guarantee. An unmentioned capability is **absence of retrieved evidence**, not a proven
tool limitation. S1's “common use cases” and S5's review warning are explicit scope limits.
None of the pages establishes that automation can settle the remote behavior in P1–P3.

A separate artifact earns adoption only if it changes a supported configuration/next-check
decision after a competent reviewer uses the existing docs, diff and source search.
If it repeats those notes, it adds verification/export work. For these examples, a short
manual checklist or better upstream docs may suffice. No evidence yet warrants switching
an update bot, replacing a codemod or adopting a static-only ShiftProof product.

## A4: observed prices, support and one commercial hypothesis

Observed **2026-11-21**, publication dates unknown. Record literal terms, not inferred
quotes. Public list pricing and vendor testimonials do not establish ShiftProof payment.

| Alternative / tier | Currency, unit, limits and conditions observed | Remaining uncertainty |
| --- | --- | --- |
| Manual public-doc review | No fee shown for reading S1/S4; engineer time and existing tooling remain costs. | No measured effort, support SLA or team cost. |
| AWS SDK JS codemod | S5 declares MIT-0; no paid tier, currency, per-seat fee or billing term shown. Public package/CLI, Node prerequisite. | No separate support price retrieved; do not turn absent commercial terms into a free support promise. License declaration does not price operation or maintenance. |
| Mend Renovate CLI / Community | S6 lists “Free”; S8 Community Cloud allows unlimited public/private repos, one concurrent job/org, four-hour active-repo schedule, 30-minute timeout; no helpdesk support. | No currency/billing unit for the free offer. Hosted capacity is limited despite unlimited repo count; self-hosting/CI/operator costs are not zero. |
| Mend Community OSS Cloud | S8: free enhanced offer for OSI-licensed projects, acceptance at Mend's discretion; two jobs/org, four-hour schedule, 60-minute timeout, confidence workflows, no helpdesk. | Eligibility/acceptance not tested. S8 qualifies S6's broad claim that workflows are Enterprise-only; do not hide the free exception. |
| Mend Renovate Enterprise | S7: **“Up to $250 per dev/per year”**; dollar symbol, ISO currency code not stated. FAQ defines contributing developer and allows standalone purchase. S8 Cloud: 16 jobs/org, hourly schedule (Bitbucket four-hour), 60-minute timeout and helpdesk. | Annual price unit is not proof of invoice cadence/prepayment. Minimum seats, taxes, discounts, precise quote and currency remain unknown. FAQ says no code-size/app/scan-count pricing limit; resource limits still apply. |

S7's contributing-developer definition includes relevant UI users and code contributors,
counts a person once, and is broader than the one reviewer of an upgrade. Its expansion
FAQ allows hosting/services/custom-agreement charges; exact Renovate applicability needs
a quote. No quote/contact occurred. Do not convert the annual display into a monthly offer.

**One commercial hypothesis, not an offer:** a service-owning lead might buy a fixed-fee,
one-upgrade configuration review with cited next checks rather than another subscription.
Price and willingness to pay are unknown; no numeric ShiftProof anchor is justified.
For a part-time solo founder, cap any later approved scope at one SDK/version pair and
one review revision; exclude incident response/ongoing compatibility assurance. Citation
drift, wrapper resolution, disputed advice and customer-specific environments can consume
the fee. No measured delivery cost or margin supports even this service hypothesis yet.

Research needs **$0 new spend**. Commercial delivery remains blocked by intake/publication
readiness; manual authoring does not bypass those gates. Avoid promising availability or
support before measuring preparation/review work. Free tools and upstream help constrain
the price of generic upgrade summaries; the paid vendor price reflects a broader service.
Plausible discovery channel: opt-in AWS JavaScript maintainer/user community discussions,
subject to community rules and separate outreach approval. No posting, contact or account.

## A5–A6: readiness and stopping decision

**Narrow discovery to configuration-preservation decisions; pause a commercial build.**
Strongest support: P2 asks for old-option warnings after reported debugging effort, and
P1 still asks about semantic migration in 2026. Strongest counterevidence: P2/P3 report
recovery through existing help; S4 provides direct migration guidance, free automation
exists, and hard runtime questions survive a table. Confidence in a recurring paid job
is low. Public-source research is saturated for this hypothesis at this bound; more
similar complaints would not establish incremental adoption or a buyer.

| Readiness item | Established / unknown at this revision |
| --- | --- |
| User / buyer | Public SDK users describe problems; target reviewer and budget-owning lead remain hypotheses. |
| Alternative | Docs/manual review, documented codemod and free/paid update automation exist; comparative task benefit unmeasured. |
| Adoption cost | Source/config access, version binding, row verification and PR export add work; privacy consent and net effort unknown. |
| Pricing | Public competitor tiers above; ShiftProof price, procurement, willingness to pay and support margin unknown. |
| Working product | No product evidence for this job; historical experiments and policy checks do not demonstrate delivery. Publication/replay blocked. |
| Interviews / use / payment | None established for ShiftProof. Public complaints and contributor replies are not our interviews or product usage. |
| Decisive gap | Does a real reviewer have a recurring, unresolved decision after using competent free/manual alternatives, and a reason to adopt/pay? |

Only this Markdown addition changes. PR handoff records source limits, the denied
managed-output read, exact checks, preservation, full attribution, CI and literal Sourcery.
No executable schemas/fixtures, product tests, probes, installs, customer intake/outreach,
accounts, spend, subagents or provider/model/environment/permission changes occurred.
Any new provider/quota/transport error stops without retry/bypass. Stop for independent
coordinator review; no manual Sourcery request, approval/merge or self-dispatch.

## One separately authorized empirical test

Propose **three recent-upgrade discovery interviews**, not another R02 paper comparison.
Recruit only engineers who authored/reviewed an AWS JS S3 migration or post-migration
update in the preceding six months, from three unrelated teams; at least one must know
the team's purchasing process. These are recruitment criteria, not existing participants.
Before contact, obtain explicit authorization for recruitment, consent, retention and a
public/non-sensitive discussion-only scope. No repository, credentials, logs or private
customer artifacts; stop if participants cannot discuss the decision within that scope.

Ask about the last actual upgrade before showing any concept: decision, existing tools,
unresolved configuration question, workaround, effort and who owned the spending choice.
Record statements as self-report; keep solved/no-pain answers. Only then describe the
proposed table and ask which decision, if any, would change and what current work it replaces.
Success threshold for further discovery: at least **2/3** describe a concrete unresolved
configuration-applicability decision after docs/diff/manual review, and independently
name an action the table could change; at least **1/3** identifies an actual budget owner
and purchase-evaluation condition. No money, purchase intent or time saving is inferred.
Failure/narrow condition: fewer than two qualify, nobody meets the budget-owner criterion,
existing tools settle the decision, or useful answers need unavailable runtime evidence. Stop a
paid-artifact hypothesis on that result; report mixed findings without expanding the sample
post hoc. Even success authorizes no build or sales claim: it only informs a new decision.
Do not run this test, recruit or accept customer material under the current authorization.
