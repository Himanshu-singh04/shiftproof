# B02: isolated runtime/toolchain validation

Status: implementation checkpoint for [issue #11](https://github.com/Himanshu-singh04/shiftproof/issues/11).
Candidates: Node 26.13.1, TypeScript 7.0.2, standalone npm 12.2.3, package-lock v3.
Not yet approved; final offline replay and independent review remain pending.

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
The first scope checkpoint preceded provisioning. Selected candidate archives now
match upstream checksums; reviewed metadata and license hashes are retained in
`experiments/b02-runtime-validation/pins.json` and `inventory.ndjson`.
There are no preinstall/install/postinstall hooks. Publish/prepare hooks are
inventoried but never executed; all npm operations disable scripts/audit/funding.

The initial compile attempt succeeded for good.ts and correctly diagnosed TS2322
for bad.ts, but the experiment expected exit 2 rather than TypeScript 7's observed
exit 1. The raw failed run is retained outside Git at
`/Volumes/AIWorkspace/caches/shiftproof/b02/run-5x0byznm/commands.ndjson`.
The assertion now requires exit 1 AND TS2322; fresh final captures are pending.

## Maintenance boundary

The scoped npm Dependabot entry uses lockfile-only and ignores `typescript` and
`@typescript/*`: these exact toolchain experiment inputs cannot change without
new provenance, hook/license review, offline captures and coordinator review.
The ignore applies to security updates too. Review their advisories and the Node
and standalone npm release/security feeds weekly and before reuse; explicitly
retain, retire or re-scope affected pins through a bounded issue. Do not interpret
ignored automatic upgrades or a disabled npm audit as security clearance.
Node/npm archives are outside npm manifest coverage and need that manual review.
B01 historical aliases and their existing advisory-triage policy are unchanged.
