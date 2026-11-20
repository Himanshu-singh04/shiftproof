# R03: source acquisition and report publication readiness

Status: **narrow to boundary specification; customer-source publication not ready**,
for [issue #21](https://github.com/Himanshu-singh04/shiftproof/issues/21).
No producer interface, runtime, scope, schema field or product guarantee adopted.

## Authority and bound

Founder asked non-build sessions to keep researching business/development plans while
ReleaseLens has priority, rotating afterward, and said **“resume everything”**.
Coordinator dispatched this documentation-only lifecycle/readiness round. Same persistent
GPT-6 Astra / OpenCode worker; no subagents or permission/model/provider changes.
Start **2026-11-20 05:59:17 UTC**; deadline **07:59:17 UTC**, earlier if sufficient.
At most six external primary documents and one 200–260-line Markdown record.

Approved base: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.
[R02 exact revision](https://github.com/Himanshu-singh04/shiftproof/blob/6dd79d5b9714eddfcfc3985aa50518055fecb8e5/docs/research/r02-paper-comparison.md)
already passed independent key/source/baseline audit; no participant experiment occurred.
[R01 exact revision](https://github.com/Himanshu-singh04/shiftproof/blob/0de10807e8a02c918e19f6ee6c0f7a0320158d39/docs/research/r01-customer-value.md)
also passed coordinator review; both remain founder-unapproved/unmerged.
[B03a exact revision](https://github.com/Himanshu-singh04/shiftproof/blob/644be51bbbac996f7fc9023530516bf37a409190/docs/b03a-path-decision.md)
still awaits full source audit. Preserve these branches/PRs without adopting proposals.
Replay remains **disabled / unknown / ISOLATION_UNAVAILABLE**.

## A1: current obligations and evidence boundary

References below use line numbers at the approved base above: [product](../product.md)
(SP), [evidence contract](../evidence-contract.md) (EC), [operations](../operations.md)
(OP), [testing](../testing.md) (T) and [SDD](../specs/001-mvp/solution-design.md).
These are approved planning obligations with unimplemented guarantees; accepting a
research result did not implement them or approve the SDD's pending architecture.

| Boundary | Exact current obligation | Readiness distinction |
| --- | --- | --- |
| Select inputs | SP-01/09, workflow 1; EC L20–34, L55–76; OP L41–62: explicit source/lock snapshots, workspace/resolution, frozen scope, separate bases | Immutable source generation and concurrent-read policy unqualified. Commit SHA alone omits dirty inputs. |
| Read/interpret | SP-02/09; EC L104–115, L155–160; SDD L409–413; T02/T09: read-only bounded files, no customer config/module import, unsupported syntax/config stays a gap | B02's compiler experiment does not qualify a product parser or config loader. No parser/budget mechanism selected here. |
| Source/citation identity | SP-01/06; EC L47–49, L80–100, L104–109: file hash/range, exact versions, retained excerpt/snapshot and locator, retention restrictions, closed link policy | Hashes identify bytes relative to a reference; they neither authenticate the publisher nor prove those bytes were acquired safely. |
| Redact | SP-10; EC L109, L152–153; OP L87–92; T10: minimal excerpts, redaction before persistence, no secret hashes, evidence loss stays unknown | Redaction policy and sensitive-source identity handling need specification; no sanitization success measured. |
| Evaluate | SP-03/05/06; EC L124–128, L228–246, L271–288, L306–341: representative mappings, Comparison-owned status, exact finding closure | No replay means unknown, not a pass. A free-form cited question table is not automatically a valid Finding; scope-gap findings have no citation IDs. |
| Publish/read | SP-08; EC L340–348, L365–367; OP L77–85; SDD ADR-04/B09; T08: verified directory/mount binding for every write/rename/marker, marker last, reader verifies artifacts | No publication mechanism selected or qualified. Path polling followed by ordinary writes is explicitly insufficient. |
| Fail/recover | OP L63–65, L98–114: exit 2 only for complete unknown; exit 3 for invalid/failed/incomplete, no marker on identity loss, no fallback/recreation, retained partials | An unsafe output location forbids even a completed unknown report. Stderr is the redacted diagnostic channel. |

[B02](../b02-runtime-validation.md), “Identity gate and limits” and “Reproduction and
storage”: verified Node 26.13.1/tool pins and scoped offline research, but metadata
checks do not detect arbitrary implementation changes, redirection or concurrent mutation.
Its volume UUID preflight is explicitly not a mount-removal race defense.
[B03](../b03-isolation-feasibility.md), “Actual attack matrix” and “Accepted-main
integration”: historical Node 26.13.0 permission-model symlink escapes, targeted
sandbox denials and cleanup gaps support NO-GO, not Node 26.13.1 confinement.
Accepted B03 research on main leaves publication and source acquisition unqualified.
None of those probes is rerun here; no complete product RunRecord exists from them.

## Primary API evidence: six documents, read 2026-11-20

P1 scopes a runtime API survey to B02's research pin; it does not select a product
runtime. P2/P4 specify POSIX.1-2024, not measured Darwin conformance. P3/P5/P6 are
Apple archives, not current-host qualification. No API/sample code was executed.

| ID / exact source | Locator, supported statement and limit |
| --- | --- |
| P1 [Node v26.13.1 fs](https://raw.githubusercontent.com/nodejs/node/v26.13.1/doc/api/fs.md) | `FileHandle` wraps a numeric descriptor; `read`, `stat`, `write`, `sync` act on it. `fsPromises.open/mkdir/rename/statfs` take paths; no `openat`/`renameat` API appears in this document. `access` warns of check/use races; `copyFile` follows symlinks and gives no atomicity guarantee. These documented calls do not establish the required whole lifecycle. |
| P2 [POSIX open/openat](https://pubs.opengroup.org/onlinepubs/9799919799/functions/open.html) | DESCRIPTION: relative `openat` paths resolve from the supplied directory descriptor; `O_CREAT` + `O_EXCL` atomically checks/creates the named entry; `O_NOFOLLOW` rejects a named symlink. RATIONALE discusses directory-relative race avoidance. No whole-path containment, immutable byte snapshot or mount-generation guarantee follows from these alone. |
| P3 [Apple: Race Conditions and Secure File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html) | Updated 2016-09-13. “Avoiding Race Conditions”: contents can change after open. “Working ... Using POSIX Calls”: descriptor-based checks for normal file/type/ownership/links; pass the open descriptor. “Other Tips”: a local pathname can name remote storage. Archived mitigation guidance is not an enforcement proof. |
| P4 [POSIX rename/renameat](https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html) | DESCRIPTION/RATIONALE: rename has atomic directory-entry replacement semantics; `renameat` uses old/new directory descriptors for relative paths. Existing destinations may be removed/replaced; EXDEV/EIO remain possible. Atomic rename is neither no-overwrite publication nor power-loss durability nor whole-run atomicity. |
| P5 [Apple archived fsync(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fsync.2.html) | DESCRIPTION: drive buffering/reordering can leave partial/no data after power loss; refers to `F_FULLFSYNC` for tighter guarantees. P1 also says `sync` is OS/device-specific. This is a durability caveat, not authority to add a new durability promise or assume APFS/device behavior. |
| P6 [Apple archived fstatfs(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fstatfs.2.html) | DESCRIPTION: filesystem statistics including `f_fsid`; `fstatfs` obtains information via an open descriptor. No stable mount-generation token or atomic “identity still valid + publish” guarantee is stated. Current SDK availability and unplug/remount behavior remain unknown. |

Response SHA-256 values (P1 raw Markdown; P2–P6 HTML, not rendered text):

```text
P1 12c847ec2eb748eb25c2b24da5ac4cd58915483367907c329b2b0907d79658f1
P2 57b770918aa3e0c25186972675df8c96da119cf4b973335ed4487405e260dc3a
P3 f4ea2984e67b3e9910dbf5d137f8fe8753a0569d8cb1017428c6aea224d3ef27
P4 06671610134b0a52cdf4dcdaf382f72fef85ef51088b8a52b8679c7f03829318
P5 6f2812ad0289bff54203ea3912be236d48f3aaf87db41bb3afe5af85aa7fd1f7
P6 ffe51557570a9e125cac72401fa37592607d856739817dcf654fcf7baf77897a
```

## A2: one candidate paper lifecycle

Candidate only: the existing TypeScript/Node local-CLI direction, one run at a time
on the B02 darwin-arm64/local-APFS research target, with an **unselected, separately
reviewed native boundary if needed** for missing handle-relative operations. This is
one proposed path, not a replacement platform, new runtime decision or bridge design.
No `/dev/fd` pathname trick, shell utility or current-directory switching substitutes
for the missing primitive evidence. If ordinary Node cannot meet a boundary, stop.

Actors: operator selects owned roots/scope; trusted CLI coordinates; untrusted source,
config and documentation supply bytes only; trusted parser/Comparison/renderer interpret
those bytes; publisher alone holds output authority. Host OS/tool integrity and the
existing trusted-operator boundary remain assumptions, not new guarantees against a
compromised same-user host process. Accidental concurrent edits, hostile input links,
parser failure and mount loss still require explicit handling; trust is not an excuse
to remove the specified checks. No customer module receives a handle or executes.

| Stage | Needed authority / identities / limits | Failure disposition and missing evidence |
| --- | --- | --- |
| 1. Select | Read operator JSON as data; bind manifest-directory-relative inputs and invocation-relative output once to explicit bases; choose exact pair/workspace and pre-run exclusions | Reject unknown fields/unsafe roots/ambiguous resolution; exit 3 diagnostic. No default cwd resolution or automatic latest/download. Root selection API and immutable-generation evidence unqualified. |
| 2. Acquire | Read-only source/lock/doc authority; retained verified base/child handles, regular-file type and object identity, allowed mount, component traversal under the designated base; per-file and total byte/count/depth bounds | External symlink, ancestor substitution, special file, alias collision or changed generation stops acquisition with an identity/IO diagnostic. `realpath` then `readFile` is not proof. No source write or execution. |
| 3. Freeze | Bind exactly consumed bytes to a sorted source manifest, dirty flag/optional SHA, lock/resolution and scope identities; keep a run-owned immutable byte set for interpretation | Reading through an fd freezes neither content nor a multi-file generation. Require a demonstrated immutable input generation; detectable change => IO_FAILURE/exit 3, no mixed-snapshot completed record. Copying/hashing alone cannot supply this guarantee. |
| 4. Interpret | Bounded parser consumes only frozen bytes; config/include/import resolution uses the same contained read service, no plugin/module/hooks or compiler subprocess; approved syntax subset only | Missing dynamic config, lost wrappers/aliases or unsupported syntax remain PARSE_FAILED/DYNAMIC_CALL/MAPPING_INCOMPLETE as applicable. Counts retain failed/unresolved inputs. Resource failure is not a clean empty scan. |
| 5. Bind evidence | Doc bytes already deliberately provisioned offline under a separate base; exact applicability, publisher/URL/date/locator, permitted excerpt and content identity; no fetch during validation/viewing | Missing/uncertain versions create citation gaps. Validate closed HTTPS/run-relative link policy; unsafe target => CITATION_UNSAFE, never repair it. Documentation instructions remain data. |
| 6. Reduce/render | Redact before persistence, then validate EC identities/references/closure; Comparison alone assigns outcomes/status; renderer projects validated JSON to Markdown with escaped text | No observations => unknown obligations, no fabricated pass/fail. Malformed closure => diagnostic, not renderer-invented fields. If redaction loses evidence, retain REDACTION_LOSS; unsafe provenance cannot be silently rehashed as original. |
| 7. Publish | Independently qualified output directory/mount binding, exclusive new run, bounded redacted artifacts, sequential checked writes and handle-bound renames, final completion manifest only after validation | Unavailable binding, existing target, disk-full, cancellation, identity loss or write/rename error => exit 3, suppress completion; retain owned partials where safe. No reopen/recreate/pathname fallback. Primitive composition remains blocker. |
| 8. Consume/recover | Reader binds explicit snapshot/bundle bases, requires valid completion manifest, checks each referenced file/hash and inert rendering; operator reviews owned partials for cleanup | Missing/corrupt files or identity mismatch => reject completed display. No status repair, partial merge/resume or automatic deletion. New run needs fresh verified handles. |

This candidate proposes rejecting **all** symlink components and unqualified cross-mount
reads to avoid claiming an untested internal-symlink resolver. That is a conservative
scope-policy proposal, not an adopted change. Hard-link aliases and case/Unicode name
collisions also need an explicit regular-file policy; lexical prefixes do not prove
containment. Verify type before consuming bytes; opening a device/FIFO can itself block
or have effects, so a post-open `stat` alone does not establish safe acquisition (P2/P3).

The immutable-generation prerequisite is unresolved: pre/post size/mtime/inode checks
can catch some changes, but a same-inode rewrite or change-and-restore can evade them.
Holding handles does not prove cross-file consistency. An operator saying “read-only”
or a read-only open flag does not prevent other writers. No snapshot/copy utility is
selected; inability to freeze the selected generation blocks customer-source use.

Bounds must cover enumeration, open handles, file/total bytes, config include depth,
syntax nodes, URL decoding, output bytes and parser elapsed/memory use. Numeric parser/
file ceilings remain to be specified and measured. SP's 1,000 files/50,000 lines and
60-second/2-GiB proposals are not enforced parser limits; B03's capture/time observations
do not provide whole-process parser containment. Reject budget excess explicitly.

Source identity and privacy need a precise policy: EC requires source hashes/ranges
but forbids publishing hashes of secrets. Never replace an original file hash with a
redacted-file hash while keeping its original identity label. If safe original identity
cannot be represented, use only contract-valid unknown/gap handling or suppress the
artifact; no new “redacted source” field/mode is introduced here. Unredacted scratch,
logs, error excerpts and temp files are persistence too, not a redaction bypass.

P2/P4 describe useful directory-relative operations, but an open directory is not a
complete proof of still-valid root/mount identity across detach, replacement or parent
movement. P6 metadata inspection is not an atomic guard. P4 rename can overwrite, so
exclusive initial creation alone does not prove no-clobber final publication. The
exact non-replacing marker commit and failure boundary require platform evidence.
Readers must reject partial/corrupt markers; marker presence alone cannot attest the
artifacts. P5 also prevents treating atomic visibility as a tested unplug/power-loss
recovery guarantee. Existing no-fallback/no-marker-on-loss requirements remain intact.

## A3: eight distinguishing paper schedules, none executed

P = portable pure-data specification; N = native/filesystem/runtime qualification.
An N schedule requires an owned disposable environment and separate authorization;
mock success cannot qualify a host primitive. Every negative needs a working positive
under the same policy. Expected evidence below is a future oracle, not a result.

| ID / kind | Schedule and positive control | Required evidence / disposition |
| --- | --- | --- |
| O1 P + N boundary | Fixed reviewed synthetic byte set, exact identities and a well-formed unknown record; then alter one referenced byte without changing its declared hash | P: deterministic validation/JSON–Markdown parity with unknown status; altered bytes rejected, never authenticated by hash. N: only separately qualified acquisition/publication may yield a completed bundle/exit 2. Paper inputs alone prove no filesystem safety. |
| O2 N | Normal contained regular file reads; then replace a selected leaf or ancestor with an outside symlink between selection and open; separately present a FIFO/device or colliding alias | Evidence of actual read authority and zero outside content consumption/source writes; bounded refusal rather than hang, exit 3. A denied error without a working regular-file read is insufficient. Type/traversal primitives remain unqualified. |
| O3 N | Immutable generation A is read consistently; then edit/replace one source or lockfile during acquisition, including same-inode rewrite/change-and-restore | Either mechanism demonstrably prevents mutation of selected generation or rejects it without a completed hybrid. Record safe identities/IO diagnostic, no secret bytes. Passing pre/post metadata comparisons alone is not the oracle. |
| O4 P + N | Plain supported config resolves from frozen bytes; then config requests an executable module/plugin, recursive/out-of-root include or exceeds declared parser budget | P: unsupported config/parse gaps and failed counts, no silent exclusion. N: zero module/script dispatch or external reads, bounded parser termination/resource evidence. A child process/time limit alone is not containment proof. |
| O5 P | Resolved call with declared required scenario has exact mapping evidence; replace argument/config evidence with unresolved runtime input, with replay absent in both | Required mapping/callsite-gap obligations stay unknown, include MAPPING_INCOMPLETE and relevant NOT_RUN/ISOLATION_UNAVAILABLE gaps; no compatible result or invented citation closure. Preserve counts and next evidence action. |
| O6 P | Valid exact-version HTTPS/local citation and harmless text; substitute nested-encoded traversal/unsafe scheme, raw HTML/Markdown/autolink, wrong-version text or a secret in required evidence | Unsafe links inert with CITATION_UNSAFE; wrong version blocks dependent claim; zero auto-load instructions, secrets or secret hashes in published payloads/logs. REDACTION_LOSS remains unknown. Safe text/link positive must still render; actual viewer no-fetch behavior needs later renderer qualification. |
| O7 N | Stable owned output root publishes once; then swap a parent/output directory or remove/replace the mount after preflight, during file write, rename and immediately before marker commit; preexist a target entry | No underlying-host/new-root writes or overwrite, no directory recreation/path reopen, no completion marker on identity loss; exit 3 and redacted stderr. Independent side-effect observations at each cut point, not polling-only logs. Missing primitive => blocked, not pass. |
| O8 P + N | Reader accepts intact final bundle; interrupt before marker, force a write/rename failure or disk-full, then remove/modify one artifact in a formerly complete bundle | N: partial retained without successful completion; errors checked, owned recovery only. P: reader rejects absent/malformed marker, missing/hash-mismatched references and invalid closure. Exit 3 on failed publication; no merge of partial attempts or manual status repair. |

O1/O5's complete-unknown examples presume schema-valid identity and independent safe
publication; otherwise exit 3. Oracles do not reclassify infrastructure failure as SDK
incompatibility. Source-byte hashes never override failed containment/immutability.

## A4: smallest blockers and burden

| Blocker | Missing evidence / cost category |
| --- | --- |
| B1 acquisition generation | Component-safe reads, special-file/open behavior and a coherent immutable generation on the target; operator snapshot preparation and alias/exclusion review; capture/parser resource qualification |
| B2 publication transaction | Current Darwin API availability, directory creation/open/rename/no-replace marker composition and mount-loss behavior; possible native bridge review, packaging, build/ABI upkeep and recovery evidence |
| B3 evidence/presentation | Safe identity-versus-redaction policy, parser/config subset, EC closure/link validator and renderer behavior; versioned citation upkeep, edge-case corpus and support for disputed findings |

Bundled reviewed synthetic **in-memory/paper** data can remove customer snapshot and
privacy variability from a later pure-data specification exercise. It still cannot
prove N schedules or make an unqualified disk publisher safe. It is not a new evidence
mode or producer interface, and no executable fixture is created by this note.
Customer-source use adds dirty/mutable workspaces, config resolution, aliases, secrets,
licensing/retention, source access and operator interpretation of unknowns. A local
report avoids a hosted service, not these acquisition/publication obligations.
New paid spend this round: $0. Engineering hours, performance, support demand and
operating cost are unmeasured; no delivery-time quote or new paid dependency proposed.
Qualify every supported runtime/OS/filesystem revision and maintain failure/recovery
evidence; B02 pins alone do not cover that maintenance. Secure publication is necessary
for a report, but does not establish incremental upgrade-review decisions or demand.

## A5–A6: recommendation and next bounded work

**Narrow to one publication-transaction specification; pause customer-source artifact
delivery.** Confidence high that current evidence leaves B1/B2 open; confidence in a
particular native solution remains low. Six documents support useful primitives and
failure modes, not an enforcement result. No code, platform or requirement adoption.

Smallest proposed later task: specify only the **new-run/commit-marker transaction**
for the existing darwin-arm64/local-APFS direction. Prerequisites: exact current OS/API
documentation, agreed identity-loss predicate, safe ownership/cleanup model, no-overwrite
semantics and unchanged OP/EC clauses. Deliver one operation/capability table and O7/O8
cut-point plan; show how each step stays handle-bound or return a precise unsupported
primitive. Review any native mechanism before separately authorizing code/qualification.
Do not test live mount removal, install tools or create a bridge under this proposal.

Disconfirmers: a documented API composition plus independent target qualification could
remove B2; a proven immutable acquisition generation could remove B1. If those need
unapproved privileges, new runtime scope or costs, retain the blocker. If reviewers
cannot use the resulting evidence to improve a decision beyond manual review, a secure
report still does not justify product adoption. Pure-data tests cannot remove N gates.

1. **Can the marker transaction meet OP L77–85 without pathname fallback?** Deliver
   the single-task capability/cut-point specification above, or a missing-primitive
   blocker. No broad platform/VM survey or premature native implementation.
2. **What source identity can remain truthful after required redaction?** Deliver a
   clause-level handling table for original source/lock/doc hashes, retained excerpts
   and evidence loss; distinguish contract-valid unknowns from cases that must refuse
   publication. Any needed schema/scope revision returns for a separate decision.

Coordinator dispatch only. R02 independent audit is already complete, not repeated or
relabelled as an experiment. All existing bytes/55 headings and pending branches stay
unchanged. Required repository/policy/actionlint/diff/preservation, exact head/base,
attribution/CI and automatic Sourcery status are in the PR handoff. All six sources
were accessible with TLS verification. No research execution, fixtures, VM survey,
installs/probes/customer input/outreach/accounts/environment changes or spend occurred.
