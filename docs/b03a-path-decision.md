# B03a: replay-or-static path decision, round one

Status: **Frontier-ready — recommend pause on product-path adoption**, for
[issue #15](https://github.com/Himanshu-singh04/shiftproof/issues/15).
This documentation-only recommendation awaits coordinator/founder review. Neither
path is adopted; only coordinator-dispatched research continues during ReleaseLens build priority.

## Authorization and bound

Founder asked “whats next, whats the plan, how much is all the three projects completed”.
After the coordinator proposed ReleaseLens-first implementation and bounded decisions
for the other products, founder replied **“ok proceed”** on 2026-11-20.
Subsequent instructions keep the two non-build sessions researching business and
development plans, with roles rotating later. This is only the first bounded round.
Same persistent GPT-6 Astra / OpenCode worker; no subagents.

Base: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`; B03 PR #14 is accepted research.
Replay remains **disabled / unknown / ISOLATION_UNAVAILABLE**. B02 darwin-arm64
tooling does not validate a Linux guest. B01's Stripe 12.18.0 → 13.0.0 is historical
research, not current-market or shipped SDK support.

Compare exactly one candidate: an offline Linux guest on Apple
Virtualization.framework, guest-owned ephemeral storage, no host shares or network
device during replay, reviewed harness only, bounded outputs and supervised lifecycle.
Alternative: explicitly proposed non-executing discovery and cited upgrade review,
with unknown behavioral results. Static input acquisition and report publication
remain security boundaries, not consequences of disabling replay.

Deadline: **2026-11-20 07:15 UTC**, earlier completion preferred; at most eight new
primary-source documents. No installations, probes, guest/native work, mounts,
permissions, storage configuration changes, customer code or paid spend.
Issue #15 A1–A6 are fixed: actors/attack surface; source-backed feasibility/cost;
honest static alternative; exact proposed requirement deltas; one recommendation
and one drafted next issue; preserved artifacts and attributed verified delivery.

## Decision and the missing facts that change it

| Path | Useful result if later validated | Cost / disqualifying unknown now | Round-one verdict |
| --- | --- | --- | --- |
| One offline Linux guest on Virtualization.framework | Preserves the intended differential-fixture evidence, with a guest/host boundary instead of a host process group | New native runner, entitled build, reviewed boot/root artifacts and Linux toolchain; no measured termination/host-resource or publication guarantee | Plausible configuration; **not ready to authorize provisioning or replay** |
| Explicit static-only first release | Call inventory, cited review questions and actionable evidence gaps without SDK execution | Still needs bounded parsing/acquisition, new evidence mode/claim representation, safe publication and proof of incremental utility | Less execution machinery, but **not a demonstrated safe/useful replacement** |
| Pause adoption; continue bounded planning | Avoids committing scarce build time to an unvalidated product promise | Delays a usable ShiftProof MVP; research cannot itself close empirical gates | **Recommend now**, with the concrete reopening conditions below |

Missing fact 1: can a specific $0 entitled runner plus reviewed arm64 guest artifacts
boot offline and reclaim the entire guest on deadline/runner failure within a declared
host budget? P1–P5 do not establish this. If no, VM validation must remain NO-GO;
if yes after separate authorization/measurement, retain behavioral scope rather than
silently relaxing SP-09/SP-11. Missing fact 2: does callsite-linked cited triage add a
decision a maintainer cannot get from existing release notes/tooling without replay?
No demand evidence exists here. If supported, static re-scope merits a separate
contract decision; if not, removing replay also removes the unvalidated differentiator.
Both paths additionally require ADR-04/B09 publication feasibility, not just a parser.

## Primary evidence ledger — eight documents, read 2026-11-20

P1–P5 use Apple's exact DocC JSON representations; locators below name their sections
or properties. These are documentation observations, **zero new enforcement measurements**.
Short excerpts/claim locators and response SHA-256 values are retained here; full
upstream documents/artifacts are not vendored. Mutable docs must be rechecked before
implementation; hashes identify retrieved bytes, not authenticity or API guarantees.

| ID / primary source | Exact support and limit |
| --- | --- |
| P1 [Apple: Running Linux in a Virtual Machine](https://developer.apple.com/tutorials/data/documentation/virtualization/running-linux-in-a-virtual-machine.json) | “Configure the Sample Code Project”: kernel and initial RAM disk must match the Mac CPU architecture. Boot sample uses `VZLinuxBootLoader`, two CPUs, 2 GiB and a serial console. It stops in initramfs; it is not a provisioned Node appliance. Its terminal-attached bidirectional console is unsuitable unchanged. |
| P2 [Apple: VZVirtualMachineConfiguration](https://developer.apple.com/tutorials/data/documentation/virtualization/vzvirtualmachineconfiguration.json) | Overview: specifies devices exposed to the guest; `validate()` checks configuration, including entitlement. Properties list network, directory-sharing, socket, serial, storage and USB devices. `memorySize` is memory the **guest** recognizes; `cpuCount` is guest CPUs. Neither says host aggregate RSS/CPU-time cap. |
| P3 [Apple: stop(completionHandler:)](https://developer.apple.com/tutorials/data/documentation/virtualization/vzvirtualmachine/stop(completionhandler:).json) | Destructive stop gives guest no clean shutdown chance; callback occurs after stop or error. No maximum latency, host-process-death cleanup or hard deadline is specified. Metadata: macOS 12+. Guest shutdown request is not forced-stop evidence. |
| P4 [Apple: VZDiskImageStorageDeviceAttachment](https://developer.apple.com/tutorials/data/documentation/virtualization/vzdiskimagestoragedeviceattachment.json) | Overview: guest sees a disk, writes land in the supplied image; RAW maps offsets 1:1. Attachment has read-only configuration. Host backing storage is still host authority/capacity, not a shared host directory or proven disk quota. No image-creation command was run. |
| P5 [Apple: virtualization entitlement](https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.virtualization.json) | Boolean entitlement permits framework use; `validate()` checks entitlement availability. No existing qualifying runner/signature/account is established by reading this page. |
| P6 [Apple: Developer account overview](https://developer.apple.com/help/account/basics/about-your-developer-account) | “You don’t need an account” for most documentation; advanced capabilities/distribution require program membership. Requested `/support/compare-memberships/` redirected here. No price or guarantee of a free signing route for this runner was established; no account created. |
| P7 [Linux kernel licensing rules](https://docs.kernel.org/process/license-rules.html) | Opening: kernel is GPL-2.0-only with syscall exception; UAPI boundary does not extend kernel GPL requirements merely through syscalls. This does not license an entire guest image, userspace, firmware or its redistribution. Page identifies 7.4.0-rc3 docs, **not a selected kernel**. |
| P8 [Node v26.13.1 BUILDING.md](https://raw.githubusercontent.com/nodejs/node/v26.13.1/BUILDING.md) | “Platform list”/“Official binary platforms”: GNU/Linux arm64 Tier 1, kernel >=4.18, glibc >=2.28; binaries need libstdc++ >=6.0.25 and, from Node 25, libatomic. EOL distributions unsupported. Supports a prerequisite checklist, not a tested guest or reuse of darwin binaries. |

Response digests (SHA-256; P6 is final redirected HTML, P7 HTML, P8 raw Markdown):

```text
P1 7a13088059648fa4cab6d456d8fe11a7b1f185855ddd69822681cc09a972267d
P2 d40959840b5ef503c7e37df0c68c83e6c7cce5bc9fdff28ed8687ff7e3cc4069
P3 38d6f295b687a45aa9b1ece5696cdb6ee2734d0fa7e84c0c7c079de87cba0121
P4 20672557a3efe05e0957ed3d675b01398a1463fdbc97aa346ffcab9c4efa1ce3
P5 b143d72ca5d6d5cae4398156a09dba3f54d3560447c47130dbbef0ddb8c6bae9
P6 6713c50f154fa961a36d54cdfcf1632970a5d0eef905894e38f58fada82cf97e
P7 8a8e8272ac57dbf1c2028fc6b744504de8a16a4bbb9415ced3033e553d9fad7e
P8 715e9a278d6bbcfcf5372fc329b46eee5276f8c661bf09e4c2aebf96e23b6896
```

## Candidate actor model and interfaces — proposal, not deployment

One native arm64 Linux guest at a time; each source/target side starts from fresh
reviewed guest state, sequentially. No Rosetta, second hypervisor or platform survey.

| Actor / seam | Proposed authority | Attack surface and required evidence |
| --- | --- | --- |
| Guest SDK/reviewed harness | Execute only pinned reviewed artifacts, synthetic fixtures and guest scratch; no customer module | Treat guest output as untrusted. Guest child/exec operations are not automatically denied by a VM: separate guest user/filesystem/process restrictions and bounded-child tests remain required. |
| Guest kernel/init/supervisor | Own guest memory, processes and virtual disks; initialize filtered synthetic environment | Kernel is trusted for in-guest restrictions, not host credentials. Kernel compromise is a VM-escape/device-parser risk, not proof of confinement. No guest root authority becomes host admin authority. |
| Host native runner → VM | Configure only boot loader, bounded block images and one pipe-backed serial result channel | Empty network/directory-sharing/socket/USB and other unneeded device lists; reject extra devices. No host home, checkout, caches, credentials or raw host disk attached. Config validation is not enforcement testing. |
| Host operator/admin → runner | Supply approved artifacts and owned output location; existing user authority only | Trusted host OS/hypervisor, runner and checkout; malicious same-UID host modification/admin/kernel compromise remain excluded exactly as in B03. No new account, privilege or entitlement is granted by this record. |
| Output reader ← report | Read validated redacted JSON/Markdown and explicit limitations | No guest-controlled host filename, shell command, HTML, URL auto-load or deserialization hook. Forged completion, ANSI/terminal escapes, oversize/deep JSON and secret output must fail closed. |

Guest-owned means exclusive guest filesystem contents backed by task-owned bounded
host files, **never host-directory passthrough**. Propose immutable read-only input/root
images and a fresh fixed-capacity writable scratch image per side; host never mounts
a guest-mutated filesystem to extract results. Image provisioning/identity-safe opening
and cleanup are unimplemented. No restored running snapshot carries prior SDK state.
Input is a frozen reviewed scenario descriptor plus pinned artifacts, not source trees.
Deliver inputs before replay through reviewed images; no network-enabled setup state
may be resumed into a replay run. Missing packages stop, never trigger downloads.

The serial channel is deliberate guest-to-host egress despite absence of a NIC.
Use capped framing and bounded parser buffers, no terminal attachment or proxy/RPC
commands, no vsock/helper that can open host paths or forward sockets. Host validates
IDs, side/scenario bindings and sizes, then redacts **before** persistent raw evidence,
hash publication or logs. Redaction loss stays unknown. Synthetic-only inputs reduce
exposure but do not make arbitrary output safe. No host environment/credentials are
inherited by guest; environment initialization must also omit provisioning secrets.

Host artifact provisioning is a distinct, separately authorized network phase with
exact URLs, authenticated-origin/integrity evidence, license inventory and no arbitrary
package hooks. Linux kernel/initramfs/rootfs/libc, Node and native TypeScript packages
need their own pins and checks; B02's macOS observations cannot supply them. A custom
native VM runner, guest init/harness supervisor, image builder, protocol validator and
failure-recovery path are missing components, not provided by framework availability.

## Feasibility, limits and costs

| Prerequisite | Source verdict | Current readiness / consequence |
| --- | --- | --- |
| Boot/configuration and device omission | **Met as documented capability** (P1/P2) | Unverified on assigned host; omit all host shares/NICs, audit alternate channels. No claim a qualifying VM exists. |
| Exact offline artifact supply and Linux runtime | **Unmet** for this candidate (P1/P8 prerequisites only) | No chosen distro/image/kernel hashes, libc closure, guest compiler or offline provisioning recipe; stop before building/downloading. |
| Entitled native runner at $0 | **Unverified** (P2/P5/P6) | Installed SDK/build/signing route and applicable distribution rights uninspected. If new paid membership, account or privilege is necessary, return for a decision, not a fallback. |
| Guest memory/CPU/storage configuration | **Met as configuration**, enforcement unverified (P2/P4) | Guest vCPU count is not CPU-time quota; guest RAM excludes host runner/framework overhead. Fixed disk capacity does not bound host logs, copies or swap. |
| Hard stop / descendant reclamation | **Unverified** (P3) | No bounded completion guarantee; guest shutdown cooperation insufficient. Runner death, stuck callback and residual host VM resources require independent evidence. |
| Safe output/acquisition and repeatability | **Unmet** as implementation | ADR-04/B09 remains separate; no new observation, guest workload or performance target measured. |

Current spend **$0**; no new hosting/inference/service charge authorized. Future local
validation has a $0 acquisition ceiling, not a claim every distribution/signing route
is free. P6 did not establish a numeric membership fee, so it is **unknown**, not $0.
Kernel notices/source obligations and each userspace/firmware/package license need
artifact-specific review before redistribution (P7); Apple SDK/sample terms also
remain to be checked before code reuse. B01/B02 license inventories cover their
historical bytes only; no license for a new combined appliance is inferred.

Planning estimates, not measured quotes: VM readiness/provenance 1–2 focused days,
minimal runner/provisioning/protocol work 3–5, boundary/recovery verification 2–4;
**6–11 engineer-days before adapter/product work**, split into <=2-day issues.
Static contract/discovery 2–4 days plus acquisition/publication/recovery 2–4:
**4–8 days before a release rehearsal**, with native publication feasibility capable
of blocking either estimate. No dates/throughput promised. VM host disk capacity
must cover base + fresh side disk + provisioning cache + evidence; exact GiB unknown
until artifacts chosen. Maintain guest/kernel/runtime security updates, licenses,
offline rebuilds and regression evidence on every pin/host OS change; no free upkeep.

Conditional later VM validation: reviewed synthetic positives must boot, exchange one
framed result, access allowed guest scratch and repeat from fresh state. Negatives
must reject wrong hashes/extra devices, deny owned outside-guest and restricted guest
paths, retain environment canary removal, bound finite output/waits/owned descendants,
and establish termination/reclamation after guest and runner failure. No exhaustion,
external target or SDK execution is implied. Whole-host limits must count VM services,
runner and buffers, not just guest allocation. Missing stop/resource proof => NO-GO;
no reinterpretation of asynchronous `stop` as a hard 5-second host deadline.

## Static-only alternative and proposal-only deltas

Observable proposed outputs: exact pair/lock/source identity (or gaps), file/range/
import-symbol call inventory, scanned/excluded/failed counts, versioned cited review
notes, unresolved obligations and concrete next evidence actions in local JSON/Markdown.
Support only tested direct imports/aliases; computed calls, runtime imports, escaped
objects, unresolved wrappers/config and parse failures stay explicit unknown candidates.
No SDK import, customer config/plugin execution, compiler subprocess or package install.
No calls found is unknown; compile success and documentation alone never create pass,
fail, equivalent/different or compatibility. Utility is a **hypothesis**, with loss of
retry/error/serialization observations and no answer to actual behavioral equivalence.

Read-only acquisition still needs explicit source/lock/doc bases, verified handles,
regular-file/size/depth limits, no symlink/special-file/out-of-root resolution or
network module resolution. Parse source/config as data; no unreviewed helper silently
imports configuration. Parser bugs/resource exhaustion remain a host attack surface;
no mechanism is selected to contain them. Publication still requires verified
directory/mount handles, no pathname fallback, redaction, inert links/text and final
manifest only after validation. If either boundary is unavailable, stop/exit 3;
do not promise even a completed unknown report merely because replay is disabled.

The **recommended pause changes no requirement**. The following exact replacement/
addition text is only for a later independently approved alternative, not adopted here.

| Old requirement / location | Proposed text if that path is chosen | Trade-off / new acceptance oracle |
| --- | --- | --- |
| VM: SP-01; contract Identity; SDD ADR-01/03 | “A VM run binds host OS/runner build and device configuration, guest kernel/root/input-image hashes, guest OS/libc/runtime and all artifact identities separately. darwin research pins do not validate Linux.” | Larger provenance closure; changed/missing identity blocks launch before guest execution. |
| VM: SP-09/11; contract Scenarios; operations Execution controls; SDD Replay.run | “Replay uses one offline guest per fresh side, no NIC/share/socket forwarding, reviewed artifacts only, restricted guest scratch/process authority and capped inert result channel. Failed host/guest boundary verification blocks replay.” | Native runner replaces simple process IPC; positive/negative guest and host-channel controls required, with no expansion to customer execution. |
| VM: product release baseline; testing Resource limits; SDD QR-3 | “The proposed 60-second, 2-GiB workload budget includes host runner, VM services, guest allocation and capture buffers; record boot cost separately and within total elapsed time. Retain 5-second scenario and 16-MiB capture proposals; missing whole-boundary enforcement blocks release, and revisions require approval.” | No covert replacement of host budget by guest RAM; measure full accounting/stop latency before acceptance, not assumed feasible. |
| Static: product Boundary/workflow steps 4–6 and SP-03/04 | “Initial static release inventories supported calls and cited review questions only. Replay and scenario execution are unavailable; unsupported capabilities and absent mappings remain gaps. Behavioral journeys are deferred, not passed.” | Loses behavioral demo; customer-execution sentinel never fires, all absent-replay cases unknown. |
| Static: contract Scope evidenceMode; Identity required fields; SP-01 | “Add static-review in a separately versioned schema. Keep all identity fields; unavailable artifact/adapter/fixture identities are null with blocking gaps, never invented values. Runtime identifies the analyzer, not an executed SDK.” | New mode/readers, old revision rejects it; round-trip null-plus-gap cases without fabricated hashes or fixtures. |
| Static: contract outcomes/obligations/status; SP-05/07/11; T03–T05/T07/T11 | “Static-review creates no pass/fail mapping or equivalent/different outcome. Declared scenarios get unknown outcomes and NOT_RUN gaps; otherwise retain empty scenario collections and explicit coverage gaps. Comparison alone assigns unknown, including zero calls. Repeatability concerns static evidence only.” | No compilation or docs-only incompatibility; reject imported replay outcomes/forged passes; deterministic unknown corpus and no fake observations. |
| Static: contract Citation/Finding closure; SP-06; T06 | “Add a separate reviewNotes collection: id, callsiteIds, citationIds, gapIds, question and nextAction; references must validate and notes assert no behavioral status. Include notes in the semantic digest; existing Finding closure remains unchanged.” | Existing scope-gap Finding cannot carry arbitrary cited notes; new schema/renderer tests reject cross-call/wrong-version/unsafe citations and status-bearing notes. |
| Static: roadmap M0/M1/M3/B09/B10; SDD ADR-04 | “M0 may close with accepted replay NO-GO. After explicit static-scope/schema approval, M1 may produce a static unknown slice; a static report/release track depends on B04/B05 plus independent acquisition/publication validation, redaction, packaging and recovery, not M2. M2 behavioral and original M3 gates remain unmet.” | M1 already permits in-memory unknown records; shipping reports earlier needs a dependency change. T01–T03, unknown T05, T06/T08–T10 and static determinism/recovery must pass; M2 tests cannot be relabeled complete. |
| Either: SP-08/09/10; operations Publication; ADR-04/B09 | “No relaxation: source remains read-only; absent safe acquisition/publication suppresses completion. Persist redacted evidence and inert links only.” | Retains a blocking development cost; mount/directory replacement, secret, malicious-link and parser-input tests must fail closed. |

SP-02 discovery gaps remain required; SP-12/13 explanations/patches remain deferred.
No new SDK versions are chosen. Any market-facing pair needs fresh selection evidence
and a separate support declaration; neither option converts the historical Stripe
pair, existing synthetic captures or green compilation into current-market support.

## Exactly one drafted next issue — not created or authorized

**Title:** “Research: test the incremental value of callsite-linked upgrade review”.
Purpose: resolve missing fact 2 before spending on either implementation path.
Inputs: public first-party maintainer issue/release discussions and official competing
tool documentation; no private repositories, outreach, accounts or personal-data harvest.
Bound: one coordinator-assigned research round, <=2 hours and <=8 primary documents,
at most three documented upgrade incidents and two existing tools; $0, no code execution.
Output: one evidence matrix separating stated pain, current workaround, what static
triage can answer, what requires replay, tool claims, missing evidence and confidence.
Positive evidence: a directly sourced concrete upgrade decision needing the proposed
callsite/citation linkage, with an explicit limitation of the documented workaround.
Negative controls: an incident solved by existing docs/tooling and a behavior-only
question that static output cannot answer; retain counterevidence, not just matches.
Acceptance: every claim has exact URL/date/excerpt/applicability; distinguish vendor
claims from observed user reports and both from willingness to pay. Zero qualifying
incidents or inaccessible evidence is a valid “not established”, not invented demand.
Stop at time/source bound or access/account request. Recommend continue/pause with
specific missing facts; do not select a new pair, adopt scope or authorize interviews.
Any later VM/runtime provisioning or normative contract adoption needs separate
explicit authorization after coordinator review; this draft grants neither.

## Ranked next research questions and handoff

1. **Customer/demand/competition:** does static cited triage add an actionable decision
   beyond existing workflows? Evidence/deliverable: the drafted issue's public matrix,
   including counterexamples; no fabricated interviews, adoption or revenue claims.
2. **Development readiness:** can the proposed host tool safely acquire snapshots and
   publish through verified handles? Evidence: exact runtime/platform APIs and failure
   semantics; deliver one acquisition/publication interface and adversarial test plan,
   with a native-helper decision or blocker. Documentation alone cannot close B09.
3. **Guest validation readiness:** which exact boot/root/tool artifacts, licensing and
   $0 signing route fit this one candidate, and how will whole-VM reclamation be proved?
   Evidence: publisher manifests/licenses/support and lifecycle API guarantees; deliver
   a frozen prerequisite bill of materials and bounded validation authorization packet,
   marking every measurement still needed. No alternate platform survey.

Coordinator chooses the next useful round after verification; worker stops here.
A1 met as proposed actor/interface inventory; A2 met as documented/unmet/unverified
assessment with current NO-GO; A3/A4 met as explicit alternative and non-adopted deltas;
A5 met via pause, concrete missing facts and one draft; A6 worker checks recorded in PR.
No enforcement, Linux support, demand, publication safety or product acceptance claimed.
Eight-source bound reached; no ninth document or alternate candidate pursued.
P6 redirect did not answer pricing/signing feasibility: preserved as unknown rather
than guessing a fee or expanding research. All source retrievals succeeded with TLS
verification. No native/research probe reruns, installations, storage/privilege changes,
customer execution, SDK/Node commands, benchmarks or outreach performed. Existing
repository/policy/actionlint/diff/preservation checks and exact CI/head are in the PR
handoff; CI's unchanged portable research checks are not fresh host measurements.
