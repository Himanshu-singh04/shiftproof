# B02: isolated runtime/toolchain validation

Status: investigation in progress for [issue #11](https://github.com/Himanshu-singh04/shiftproof/issues/11).
No runtime, compiler or npm selection is approved yet.

## Request and scope

Original founder instruction: “ok then proceed with the further tasks”, following
the merged first research round. The coordinator assigned B02 to the existing
ShiftProof worker, GPT-6 Astra / OpenCode, without subagents.

Compare Node 24 and 26 only. Select exact supported Node, TypeScript, npm and lock
format for darwin-arm64 only after artifact verification and isolated provisioning.
Retain provenance, licenses, lifecycle-hook review, fresh offline installation,
ordinary compile/type-error controls, repeated B01 semantic captures and fail-closed
identity controls. Return specific blockers rather than substitute unavailable pins.

Acceptance is issue #11 A1–A6, unchanged: version-specific primary evidence;
verified task-local prebuilt tools; fresh offline compile and B01 replay; pre-load
identity checks with negative controls; reproducible commands/maintenance; reconciled
research status and required checks. The final record will mark each criterion.

All provisioning/execution scratch belongs under
`/Volumes/AIWorkspace/caches/shiftproof`. No global tools, profile/PATH changes,
install hooks or source builds. B01 experiment files remain immutable. The accepted
Stripe 12.18.0 → 13.0.0 pair is selected for research, not shipped support.
B03 isolation and B04 schema/adapter remain separate gates. Offline npm flags and
the synthetic transport are not an egress/filesystem/process sandbox.

## Initial checkpoint

Clean fetched base: `6efbbd35398dd08a9232bd24cffda0d84fdb474b`.
The mounted external APFS volume reports UUID
`EAD8504C-B540-47B5-95EA-FBA54591ACAC`; missing mount means stop, no fallback.
Artifact and experiment checks have not run at this checkpoint.
