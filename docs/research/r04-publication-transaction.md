# R04: new-run and completion-marker transaction

Status: **blocked composition; no qualified publisher**, for
[issue #23](https://github.com/Himanshu-singh04/shiftproof/issues/23).
No publisher, native bridge, runtime, storage choice or requirement adopted.

## Authority and preserved baseline

Founder requested ongoing business/development research while ReleaseLens is prioritized,
followed by rotation, and said **“resume everything”**. Coordinator dispatched this
documentation-only transaction round to the same GPT-6 Astra / OpenCode worker.
No subagents or model/permission/provider changes. Successful start **2026-11-20
06:14:59 UTC**; deadline **08:14:59 UTC**, stopping earlier when evidence is sufficient.
One 180–250-line note; at most six primary documents and eight paper cut points.
Approved base: `04c25991698612b9aabe8e2d1bfaee58bf9fb7a8`.

Preserved founder-unapproved research, usable only provisionally at these revisions:
- [B03a #16](https://github.com/Himanshu-singh04/shiftproof/pull/16), `644be51bbbac996f7fc9023530516bf37a409190`; full source audit pending.
- [R01 #18](https://github.com/Himanshu-singh04/shiftproof/pull/18), `0de10807e8a02c918e19f6ee6c0f7a0320158d39`.
- [R02 #20](https://github.com/Himanshu-singh04/shiftproof/pull/20), `6dd79d5b9714eddfcfc3985aa50518055fecb8e5`; independent key/baseline audit complete.
- [R03 #22](https://github.com/Himanshu-singh04/shiftproof/pull/22), `8ac7ae8f2007d729d60aac443a2b9df6e6acf204`; independent A1–A6/source/check audit passed.

## A1: exact promises, different properties

Line references are at approved main: [operations](../operations.md) (OP),
[evidence contract](../evidence-contract.md) (EC), [SDD](../specs/001-mvp/solution-design.md)
and [testing](../testing.md) (T). These are intended behavior, not shipped guarantees.

| Property | Exact obligation / decision boundary |
| --- | --- |
| New run / no overwrite | EC L342: “Write artifacts into a new run directory”; OP L52–62 selects a new output directory and explicit bases; SDD L116 says “no overwrite/path fallback”. Existing run, artifact and marker entries must not be replaced. Exclusive creation is not immutable ownership of the entry afterward. |
| Marker / visibility | EC L342–348: “publish a completion manifest last”; a directory without it is partial, readers verify references/hashes. SDD ADR-04 proposes atomic completion. Single-entry visibility does not make all artifact writes atomic or make marker presence sufficient for acceptance. |
| Root / mount binding | OP L41–45 binds all creation/writes/renames/publication to verified directory/mount identities, including removal/replacement; EC L344–346 matches. Object identity, namespace attachment and mount-instance continuity are distinct; exact loss predicate is not defined. |
| Loss / exit | OP L77–85: “If identity is lost or binding cannot be guaranteed, stop publication with exit 3, retain no completion marker”; no recreation, reopening substitute pathname or underlying-directory fallback. T L97–100 includes removal/replacement immediately before marker. Polling is explicitly insufficient. |
| Cancellation / recovery | SDD L340–348: IO/cancellation leaves partial artifacts, exit 3 and incomplete-run labeling; OP L101–112 retains partials, new verified handles for a new run, no automatic resume/deletion. A commit/cancel ordering point and uncertain-result recovery are not specified. |
| Reader / status | EC L20–34, L340–348, L365–367: explicit source/bundle bases, contained references, validated JSON/inert Markdown and verified artifact bytes. OP L63–65: exits 0/1/2 only for complete compatible/incompatible/unknown; failed/incomplete is 3. No new status or exit code proposed. |
| Durability | OP/EC do not specify an acknowledged power-loss-durable commit or a device flush protocol. Suppression on identity loss remains required; no durability assumption may weaken it. A lost/corrupt post-crash bundle must fail reader validation, not be repaired into compatibility. |

Candidate predicate **for decision, not adoption**: retain the selected root object,
run object and mount instance; the root stays under its verified selected base and the
run stays its owned child; the original mount remains attached at the approved binding
through the commit instant. An observed loss latches failure even after restoration.
Unknown continuity is not success. This makes parent movement/root replacement before
commit failure candidates even if an fd still accesses the original object. Whether
all such movement counts as loss is a requirement clarification, not settled by R04.
Post-completion relocation is separately allowed by EC L365–367 with explicit bases;
the candidate does not retroactively invalidate a previously completed portable bundle.

## Source boundary: five API documents plus revision metadata

Six primary records total, accessed 2026-11-20; no linked manual or implementation
file was followed. P1 returned `xnu-12377.1.9`, commit
`f6217f891ac0bb64f3d375211650a4c1ff8ca1ea`, dated 2025-10-16. P2–P6 are pinned
public Apple XNU manual sources at that revision, not a current installed SDK audit.
[B02](../b02-runtime-validation.md) L39–40 records macOS 27.2.1 (26B131), arm64,
external APFS. These sources do **not** establish correspondence to that build or its
APFS implementation. Current-target applicability remains **unknown**; stop that
inference here. No local SDK/OS/filesystem inspection or capability test was performed.

| ID / primary source | Locator and bounded support |
| --- | --- |
| P1 [Apple XNU revision metadata](https://api.github.com/repos/apple-oss-distributions/xnu/commits/main) | `sha`, commit subject and committer date identify the returned public revision. The URL is mutable; pinned P2–P6 and the response digest below identify this reading. No assertion that this is the kernel shipped on the target. |
| P2 [open(2)](https://raw.githubusercontent.com/apple-oss-distributions/xnu/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/bsd/man/man2/open.2) | DESCRIPTION: relative `openat` uses a directory fd; `O_DIRECTORY`, `O_CREAT` + `O_EXCL`, `O_NOFOLLOW_ANY`, `O_RESOLVE_BENEATH` have documented conditions. `O_UNIQUE` checks hard-link uniqueness at open. These are not continuing exclusion or mount-attachment guards; flag availability on the recorded target is unknown. HISTORY dates `openat` to OS X 10.10, not every flag. |
| P3 [mkdir(2)](https://raw.githubusercontent.com/apple-oss-distributions/xnu/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/bsd/man/man2/mkdir.2) | DESCRIPTION/ERRORS: `mkdirat` creates relative to a directory fd; existing name yields EEXIST, errors include ENOSPC/EIO; mode is restricted by umask. RETURN VALUES returns 0/-1, not the created directory's fd. No atomic create-and-return-handle or parent-mutation exclusion is documented. |
| P4 [rename(2)](https://raw.githubusercontent.com/apple-oss-distributions/xnu/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/bsd/man/man2/rename.2) | DESCRIPTION: `renameatx_np` supplies source/destination directory fds and flags; `RENAME_EXCL` rejects an existing destination on supporting filesystems. `RENAME_NOFOLLOW_ANY`/`RENAME_RESOLVE_BENEATH` constrain resolution, not external mount continuity. Ordinary rename removes an existing destination. ERRORS includes ENOTSUP/EXDEV/EIO; listed errors say neither argument file is affected. |
| P5 [statfs(2)](https://raw.githubusercontent.com/apple-oss-distributions/xnu/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/bsd/man/man2/statfs.2) | DESCRIPTION: `fstatfs` returns filesystem information through an open fd, including `f_fsid`, names and flags. No non-reusable mount-generation token, continuous-attachment guarantee or conditional-rename transaction is specified. Metadata equality is not a commit guard. |
| P6 [fsync(2)](https://raw.githubusercontent.com/apple-oss-distributions/xnu/f6217f891ac0bb64f3d375211650a4c1ff8ca1ea/bsd/man/man2/fsync.2) | DESCRIPTION: host-to-drive flush can leave some/no data after power loss and reordered persistence; references `F_FULLFSYNC` for tighter guarantees. ERRORS includes EIO/EINTR and unsupported file types. Directory/device behavior and crash-consistent multi-file ordering are not established here. |

P4's statement that an instance of the new name survives a crash must not be promoted
to persistence of every byte/reference in a newly published bundle; P6 expressly limits
that inference. P4's filesystem-capability reference was not followed and capability
availability was not tested. Unsupported flags must stop, never fall back to rename.
P2's path-resolution flags do not justify extra privileges or a selected native bridge.
[R03's exact note](https://github.com/Himanshu-singh04/shiftproof/blob/8ac7ae8f2007d729d60aac443a2b9df6e6acf204/docs/research/r03-io-readiness.md)
records Node FileHandle operations and the path-API gap; reused provisionally only,
not current native-API or complete-transaction qualification.

SHA-256 of full retrieved response bytes (P1 JSON; P2–P6 raw manual source):

```text
P1 d91e35278ca8d094dd5ed1fc3b2461791e61393a76f8f338f24db182a48fb1ed
P2 42211a5d4312c4db41854b8e07cfe0e7bba3309331dae8d65e793b063f2c48ee
P3 50bea0084b9907889a280c46c5c88b3b87fac7120c0a60c9383b3b42e552a94e
P4 896c6a278dcfd14601147661cf2a4588d85b271ec8798bbec7913c1d17967033
P5 0a31bf1b96a9bce33535b69c79bd3847d9c61e1e49d54ec89bb838fe1fb98ed7
P6 2399c28e11ea3a1e71b85d0002ac96b540372d405926657a101025f70ae10006
```

## A2: one operation/capability chain, conditional throughout

Existing local TypeScript/Node direction; one publisher, one new run, on the recorded
darwin-arm64/APFS research target only. Native names below identify required capabilities,
not a bridge design or callable Node interface. Source acquisition/redaction and a
schema-valid complete unknown RunRecord are prerequisites, not solved again here.
Use single-component generated names beneath held directories; no absolute/`..`/cwd
fallback. All stages require bounded names, file counts, byte totals and checked IO;
numeric ceilings and a demonstrably exclusive ownership boundary remain unspecified.
Trusted OS/runtime and prevalidated input remain assumptions. They do not eliminate
accidental competing writers or mount changes; no new hostile-kernel threat model is
introduced, and same-user trust does not prove the required transaction properties.

| Step / held authority | Candidate primitive and preconditions | Atomic support / error and uncertainty |
| --- | --- | --- |
| 1. Bind selected root | Operator-selected explicit base; directory search/create authority; P2 `openat` directory/no-follow/beneath conditions plus object checks and P5 filesystem metadata | Resolution constraints documented, initial trusted base acquisition and mount-instance identity not established. Absolute paths/AT_FDCWD are not substitutes. Any unsafe/unknown binding: refuse creation, exit 3. |
| 2. Create exclusive run | Held verified root; one absent child name; P3 `mkdirat`, bounded restrictive mode, parent mutation excluded by a proven mechanism | EEXIST prevents reuse; 0 returns no fd. Separate P2 directory open can target a substituted child. Without exclusion or an atomic returned identity, creation-to-handle binding is blocked. Do not delete an entry merely because its name matches. |
| 3. Create/write artifacts | Held run and newly opened file fds; P2 relative `O_CREAT` + `O_EXCL`; provisional R03 FileHandle `write`, exact prevalidated/redacted bytes and publisher-only mutation authority | Exclusive name acquisition is documented; native-fd/runtime handoff, short-write accounting and safe close/error handling still need evidence. No truncate/overwrite existing file. Incomplete/zero progress, quota/disk-full, cancellation or uncertain write => no marker, retained owned partial, exit 3. |
| 4. Validate complete artifact set | Held owned artifact handles; expected sizes/hashes, closed references and inert JSON/Markdown; bound validation to the same bytes readers will consume | EC validation is deterministic specification support, not an OS primitive. Hash equality does not exclude later mutation/substitution. No artifact-byte mutator may remain during commit; inability to establish that authority blocks publication. |
| 5. Prepare manifest privately | Same run directory, exclusive temporary marker file; full validated manifest bytes, bounded write/validation; P2 creation; P6 flush only under a separately specified policy | Temporary entry is not a completion marker. Direct exclusive creation of the final marker followed by writes exposes incomplete content. Precommit write/flush/close error => no final marker, exit 3. No new durable-acknowledgement promise inferred. |
| 6. Commit marker | Held run directory for both names, fully prepared marker entry, absent final name, P4 `renameatx_np` with `RENAME_EXCL` on a supporting filesystem; cancellation and identity predicate need a commit ordering point | Non-replacing directory-relative rename is supported at source-spec level only. It names the source entry, not its open file fd; concurrent source substitution remains possible. No documented atomic external identity guard. Unsupported/error => stop; unobserved result => indeterminate, not automatic retry. |
| 7. Acknowledge / retain | Known successful commit and required IO outcomes; no new writes to published content; OP complete status/exits | For this replay-disabled case, known valid completion would be unknown/exit 2. Error after an effective commit or lost acknowledgement can leave a marker with exit 3/no observed exit; rollback is not assumed safe or possible. This unresolved outcome is a gate, not an authorized exception. |
| 8. Reader acceptance / recovery | Read-only explicit source/bundle bases; bind marker and referenced files; validate actual bytes/size/hash, schema/closure and inert presentation before display | No marker, malformed marker or damaged/missing reference => reject completed display. Render checked bytes, not a reopened pathname. Reader can validate content but cannot reconstruct writer cancellation or lost mount-continuity history from hashes. Recovery requires separately verified ownership and fresh handles. |

No step inherits “qualified” from a prior one. A future native wrapper would need
independent review of every error/ownership transition, runtime binding and target API.
There is no such wrapper, local SDK proof, schema implementation or publisher here.

## A3: precise race and failure frontier

**Object binding is narrower than selected-location validity.** Relative operations
refer to a held directory rather than resolving the operator's original pathname on
every call. This can avoid redirection into a replacement root or underlying directory.
It does not establish that the old root still has the selected parent, that its mount
has stayed attached, or that content cannot change. A moved live directory may still
be usable through its fd; a successful call alone does not prove the proposed predicate.
P2's note about event-only fds and unmount is not proof that other fds prevent every
detach, replacement, physical removal or IO failure. Actual outcomes remain unknown.

**Two distinct namespace races remain.** P3 creation then P2 open has no returned
created-object identity to compare atomically. Later, P4 source-name lookup can select
a replacement temporary marker even while the original file fd is held. Restrictive
permissions reduce access; one CLI worker does not exclude another process with the
same effective authority. A random name, advisory convention or trusted-user assertion
does not prove either boundary. Concurrent creators must get non-overwriting failure;
concurrent mutators require a demonstrated exclusion boundary or publication stays blocked.

**Missing predicate-and-commit composition.** Even matching object/fsid/path samples
immediately before rename leave an interval for movement or detach; change-and-restore
can hide intervening loss. P4's documented operation has no argument requiring that a
verified external mount instance remained attached since binding. A before/after P5
check or notification does not atomically guard commit. Postcommit detection cannot
erase a marker already observed, and removing it may itself be unsafe after identity
loss. This is a specific missing proof, not proof that every possible OS mechanism is
impossible. No additional platform survey or weaker “same fd therefore safe” claim follows.

**Acknowledgement is separate from visibility.** P4 documents no mutation for its
listed errors; R04 does not claim EIO necessarily means a partially effective rename.
Instead, rename may succeed and a later close/flush/reporting operation fail, or the
process may stop before recording the result. A marker may then exist despite writer
uncertainty. Blind retry, deletion or a new run at the same name cannot establish the
first outcome; EEXIST is not success attribution. Retain uncertainty and redacted stderr
if alive, exit 3 for failed/incomplete execution; a killed process supplies no CLI exit.

**Cancellation needs a decision boundary.** Before commit, cancellation must suppress
the marker and yield partial/exit 3. During the commit/result interval, a “cancelled”
acknowledgement cannot promise rollback. Treating cancellation after linearization as
too late, or allowing a valid committed bundle after a failed acknowledgement, needs
explicit reconciliation with SDD IO/cancellation wording and OP loss suppression.
These are proposed semantic questions, not permission to change exits or publish now.
Content validation alone cannot tell a later reader whether the strict loss rule was
violated; no new receipt/status/manifest field is silently introduced to hide this gap.

## A4: eight paper cut points, no fixtures or execution

D = deterministic state-machine/content specification; N = future native enforcement;
Q = device/durability qualification only if separately promised. Every negative uses
the C1 stable control with the same preconditions. Evidence means future observations,
not calculated goldens or measurements. Missing primitive means blocked, never pass.

| Cut / kind | Stable control or changed schedule | Marker, artifacts/side effects, reader and exit oracle |
| --- | --- | --- |
| C1 D + N | Fixed redacted schema-valid unknown bytes, stable owned root/mount, absent names, no competing writer; prepare then commit | Before commit: no final marker, owned artifacts only, reader rejects partial. After known successful commit: exactly one complete marker; reader verifies every byte/reference and accepts unknown; exit 2. N must independently prove binding/exclusion; D cannot. |
| C2 N | Against C1, preexist run/artifact/final marker or have two publishers claim the same absent name; substitute a run between mkdir and open | Preexisting entries byte-identical, no overwrite or false ownership/cleanup; loser exits 3. No marker attributable to loser (an existing marker may remain); reader may accept only an independently valid original bundle. Substituted run must not receive writes; missing exclusion blocks the candidate. |
| C3 N | Move a parent or replace selected root after binding, before artifact creation or marker commit; stable-object control remains C1 | No new-root/underlying writes or fallback. Under proposed predicate, suppress new marker, retain only safely owned partials, reader rejects partial, exit 3. Successful writes through old fd are not proof of location validity; predicate decision still required. |
| C4 N | Detach/replace mount after preflight, during writes, after last identity sample or immediately before commit; also detach/restore between samples | Required: no completion marker for affected run, no fallback/recreation/new-root writes; redacted diagnostic/exit 3, reader cannot accept partial. Observe both old and replacement locations independently. Inability to couple loss and commit is a blocked oracle, not solved by polling. |
| C5 D + N | Against C1, uncompleted short/zero-progress write, disk-full or precommit flush error; competitor changes artifact or temporary marker after validation | Exact completed byte counts and identity-bound consumed bytes required; incomplete/corrupt/substituted content must not produce an accepted new marker. Partial retained safely, reader rejects, exit 3. Rehash then rename still leaves a race without exclusion; no automatic rewrite. |
| C6 D + N | Cancel before commit versus during commit/result delivery, using C1 as no-cancel control | Precommit cancel: no marker, partial/exit 3. In-flight: no claim that cancellation removed an effective marker; record uncertain outcome if alive. Required ordering/reader policy unresolved; gate remains blocked rather than falsely asserting guaranteed absence. |
| C7 D + N | C1 rename succeeds, then a later required IO operation reports failure or acknowledgement is lost; contrast documented rename failure before effect | Confirmed no-effect failure: no new marker, reader rejects partial, exit 3. Possibly effective commit: marker may exist, artifacts may validate, exit 3 if failed/alive or no observed exit if killed. Reader cannot infer writer outcome from bytes; retain evidence, no retry/rollback. This exposes the unresolved contract boundary. |
| C8 D + N; Q separate | C1 reader accepts intact completed bundle; then remove/change an artifact or truncate marker, including possible post-crash partial persistence | Reader rejects missing/malformed/hash-mismatched data and displays no completed result. Original writer's already-issued exit is historical, not rewritten; later validation failure is not SDK incompatibility. Any CLI failed validation uses existing exit 3. Q needs target/device evidence, not inferred from rename/fsync or simulated damage. |

Reader correctness requires a stable set of actually consumed bytes; reopening after
hashing or comparing only stored digest strings fails C5/C8. Hashes establish relative
byte identity, not origin, absence of competing writers or valid commit-time attachment.

## A5–A6: capability result, burden and next decision

| Required capability | Result at this evidence boundary |
| --- | --- |
| Relative directory operations and exclusive names | **Supported at source-spec level**, conditional on documented flags/filesystem support; target build/Node exposure **unknown**. |
| Non-replacing marker rename | **Supported at source-spec level** by P4's conditional RENAME_EXCL; target support **unknown**, full source-entry ownership/visibility composition **blocked**. |
| Created-run identity and mutation exclusion | **Blocked**: no proven creation-to-handle binding or continuing exclusion across validation/rename. |
| Continuous root/mount predicate with marker commit | **Blocked**: precise predicate undecided, no documented atomic guard for the proposed predicate. |
| Cancellation / ambiguous-result agreement with reader | **Blocked**: strict suppression and effective-but-unacknowledged completion not reconciled. |
| Reader byte/closure rejection and status rules | **Supported at contract-spec level**; stable filesystem read/render enforcement **unknown**, not implemented/tested. |
| Power-loss durability | **Unknown and not newly promised**; no target/device/order qualification. It cannot be used to excuse mount-loss publication. |

Recommendation: **stop publisher implementation/qualification at this frontier**.
Confidence high that these six records do not prove the composition; confidence low
in target API applicability. A current-build authoritative source plus an explicit
identity/commit semantic decision and enforceable exclusion could change the result;
merely finding a renamed API or passing a content validator cannot.

Smallest later task: one **commit-boundary decision table**, under unchanged OP/EC,
covering which root/mount events invalidate publication and how cancellation or lost
acknowledgement is classified relative to an effective commit. Prerequisites: founder/
coordinator interpretation of the existing clauses, explicit failure ordering and the
strict no-marker-on-loss oracle. Stop if the desired result requires weakening that
oracle, new schema/permissions or unavailable current-build evidence; return a separate
decision request, not an implementation workaround. No approval is requested by R04.

Ranked follow-ons, coordinator dispatch only:
1. Resolve that single commit-boundary table or record its incompatible obligations;
   do not spend another round surveying APIs without a decidable predicate.
2. Specify truthful source/lock/doc identity after redaction, separating valid unknown
   evidence from publication refusal; this remains distinct from the exhausted API frontier.

Operators would need owned output roots, explicit conflict handling and safe partial/
uncertain-run inspection. A possible native dependency adds build/signing/distribution,
ABI/flag compatibility and runtime error-translation maintenance; none is selected.
OS/filesystem/device changes require fresh evidence for supported promises. Recovery
must never remove a competing run or recreate a mount path. Costs/timings and customer
value are unmeasured; a safe transaction alone proves no incremental review decision.
New paid spend: $0. No code, native bridge design, SDK/filesystem probes, mount tests,
fixtures, installs, customer operations/accounts/outreach or environment changes.
Replay stays **disabled / unknown / ISOLATION_UNAVAILABLE**. ReleaseLens #17 remains
the sole approval turn. Required checks, exact head/base, failure history and literal
Sourcery state are in the PR handoff; all prior bytes/55 headings/branches are preserved.
