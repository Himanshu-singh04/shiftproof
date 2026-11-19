# B03: local replay isolation feasibility

Status: preliminary **no-go / replay-disabled / unknown** for
[issue #13](https://github.com/Himanshu-singh04/shiftproof/issues/13).
Final evidence/oracle checks and coordinator review remain pending.

## Original request and bounded scope

Founder instruction: “ok proceed with the further tasks”, authorizing rolling
independent work after the B02 worker handoff. Same persistent ShiftProof worker,
GPT-6 Astra / OpenCode; no subagents or concurrent editor.

Base is approved main `6efbbd35398dd08a9232bd24cffda0d84fdb474b`.
[B02 PR #12](https://github.com/Himanshu-singh04/shiftproof/pull/12) remains pending
at `8a0f40c5a44844e08010d143ecd7ac86ae7eb8de`; its code and candidate runtime are
not incorporated here. B01's historical Stripe pair is approved for research.

Compare at most two installed mechanisms: macOS `sandbox-exec` and observed Node's
permission model. Use tiny reviewed synthetic probes only, owned sentinel files
and ephemeral loopback listeners. No credentials, customer code, external probe
targets, privileged changes, downloads or VM setup. All scratch stays under
`/Volumes/AIWorkspace/caches/shiftproof/b03` on the verified external volume.

Issue #13 A1–A6 are unchanged: define actors/authority and support; measure actual
filesystem/network/process enforcement with positive controls; test environment,
output/wall bounds and owned-child cleanup; retain explicit success/denial/no-go
oracles; document attack matrix and residual limits; run required checks. Unsupported
enforcement yields replay-disabled/unknown, never a compatibility result.

## Initial observations

Read-only inventory: macOS 27.2.1 arm64; `/opt/homebrew/bin/node` resolves to
`/opt/homebrew/Cellar/node/26.13.0_2/bin/node`, reports v26.13.0. This is observed
installed tooling, not an approved B02 pin. `/usr/bin/sandbox-exec` exists; its
installed Apple manual explicitly marks it deprecated. Node's versioned permission
documentation says it does not protect against malicious code. Presence and
documentation alone do not establish measured isolation.

Initial actual probes show Node permission-model relative-symlink read/write escapes.
A diagnostic sandbox-exec policy denies the owned outside sentinel paths, loopback
network and subprocess/exec probes. It is not a full filesystem allowlist: broader
restrictive profiles aborted before the Node startup marker, and the command remains
deprecated. Baseline detached children survive process-group cleanup; separately
identified owned children are then terminated, without claiming general containment.
All raw attempts will be retained with explicit oracles in the final record.

Any feasibility must be rerun against the separately approved B02 runtime before
product replay. B04, adapter and product gates remain unresolved.
