# Local operations and deployment proposal

Status: proposed operating model; no product runtime, package, server or worker exists.
Only the foundation commands in [CONTRIBUTING](../CONTRIBUTING.md) are available.
All product installation, execution and recovery steps below describe future work.

## Storage and execution reality

| Resource | Current reality / proposed boundary |
| --- | --- |
| Source and documentation | Pendrive checkout `/Volumes/AIWorkspace/projects/shiftproof`; all planning artifacts live here |
| CPU and RAM | Mac executes processes; observed 16 GiB RAM and eight logical CPUs, not a benchmark |
| Coordinator and current session history | Mac `/Users/himanshusingh/.local/share/opencode/opencode.db`; changing checkout directory does not relocate it |
| Credentials | Mac owner-controlled storage outside Git; not moved to the pendrive by this work |
| Models and caches | Directories exist, but model/cache routing is not configured; no model selected or benchmarked |
| Persistent project server/workers | Not provisioned; this planning work uses temporary specialists, not persistent workers |
| GitHub | Remote copies of pushed source/docs and CI/review records; unpushed local changes are not remotely backed up |
| Runtime evidence | Proposed user-selected local directory outside Git; artifacts/local citations are run-bundle-relative; host roots are operational metadata, with explicit retention and capacity |

Do not call the pendrive “all memory”: it stores files, while compute, current
history and credentials remain on the Mac. Future per-project history, model
weights and caches need explicit routing, permissions, backup and recovery tests.
Do not copy a live OpenCode database as an assumed consistent backup or claim a
new session service exists merely because a directory was created.

## Proposed install and startup

1. Confirm ADRs: exact runtime/package manager, selected SDK pair, supported platform,
   isolation mechanism and evidence schema. Until then no install command is published.
2. Build a versioned local CLI artifact from a reviewed revision; pin the complete
   dependency tree and record integrity metadata. Provision reviewed packages with
   install scripts disabled; an essential script requires explicit investigation.
3. Verify artifact contents against the release manifest and declared runtime.
   Integrity checks detect mismatch; they do not establish publisher authenticity.
4. Choose read-only source/lockfile snapshots, reviewed fixtures and a writable
   evidence directory outside Git. Check free space, path containment and mount identity.
   Hold verified directory/mount handles for publication; a preflight pathname check
   alone is insufficient. All creation, writes, renames and completion publication
   must remain bound to those identities, including across mount removal/replacement.
5. Preflight adapter support, exact installed identities, scope and isolation.
   If replay enforcement is unavailable, allow only discovery and an unknown report
   when publication safety is independently available.
6. Run offline with filtered environment and no production credentials; inspect
   status, coverage, gaps and completion manifest before using the report.

Proposed command surface, **not available**:
`shiftproof analyze --manifest <run.json> --output <new-directory>`.
The JSON manifest carries source root, source/target locks, pair, adapter, fixture
bundle and frozen scope; it does not carry credentials or executable hooks.
Unknown fields and unsafe paths fail validation. No shell strings are accepted.
Manifest path inputs resolve relative to the manifest directory unless absolute;
`--output` resolves relative to the invocation directory unless absolute. Validate
each against its designated source/provisioning/output base. Persist source paths
relative to the source snapshot and artifact/local citation paths relative to the
run bundle, with containment enforced separately. Never interpret stored references
relative to the current working directory or persist host roots as report links.
Proposed exit codes: `0` complete compatible-within-tested-scope; `1` complete
incompatible; `2` complete unknown; `3` invalid input or failed/incomplete execution.
An incomplete run exits `3` even if its report retains a validated incompatibility.
No install, dev, build, release or product-test commands exist today.

## Execution controls and observability

Initial deployment is one local CLI with one worker, not a hosted service. Network
may be used deliberately to provision reviewed artifacts/docs before a run; replay
must not fetch missing dependencies or call a remote API. No paid fallback exists.
Child processes separate SDK module state but are not a security sandbox. B03 must
choose and test enforceable network denial, filesystem confinement, descendant
cleanup and resource limits. Unsupported platforms stay discovery-only.

Publication feasibility is a separate ADR-04/B09 platform gate: demonstrate that
the chosen Node/runtime APIs or an explicitly reviewed platform mechanism bind
directory operations and the final marker to verified handles/mount identity.
Do not assume Node can enforce this. If identity is lost or binding cannot be
guaranteed, stop publication with exit 3, retain no completion marker, and report
the failure through stderr. Never recreate a missing mount directory, reopen its
pathname as a substitute, or fall back to the Mac's underlying directory. Polling
mount identity before ordinary pathname writes is not sufficient. No platform
ships report publication until this gate passes; no mechanism is selected yet.

Proposed limits are in [testing](testing.md); they are unmeasured. Logs contain
run ID, stage, duration, input hashes, counts, reason codes and redacted diagnostics.
Do not log raw headers, tokens, complete customer source, prompts containing secrets
or full fixture bodies by default. No telemetry, background upload or external
monitoring service is required. Report stages pending/running/complete/failed/cancelled
so an operator can distinguish a stopped worker from a completed unknown result.

## Recovery and retention

| Failure | Proposed response and recovery |
| --- | --- |
| Wrong/missing lock or artifact | Stop preflight; correct explicit identity and start a new run; never resolve latest silently |
| Network attempted in offline mode | Block it; emit isolation/adapter gap; review fixture seam before rerun |
| Timeout/crash/nondeterminism | Preserve redacted diagnostic/attempt evidence; mark unknown; reset both environments and rerun with a new ID |
| Disk full, pendrive removed or mount identity changed | Fail handle-bound publication; suppress completion manifest; no pathname fallback/recreation; reconnect and verify a fresh mount/output handle before a new run |
| Interrupted process | Terminate descendants; mark leftover run partial; inspect then delete only its owned scratch directory |
| Corrupt/missing report artifacts | Reader rejects digest/reference mismatch; regenerate from pinned inputs, never repair status manually |
| Model absent or overloaded later | Skip explanation with reason; preserve deterministic report; no paid or network substitute |
| Faulty release | Reinstall prior reviewed CLI artifact and matching adapter; keep old evidence immutable and generate new runs |

No automatic resume combining partial observations is proposed. Retry a complete
scenario on both sides so clocks, state and fixture identity match. Preserve previous
run directories for diagnosis until the operator chooses to delete them.
Proposed default retention: local only, no automatic deletion in MVP; show artifact
size/location and provide documented manual cleanup. Scratch data is removed after
completion or explicit recovery. Customer evidence is never committed by default.
Filesystem permissions restrict casual access, not encryption or backup assurance.
Any sharing requires operator review/redaction; deleted local files may remain in backups.

## Packaging, release and deployment gates

M3 proposes a versioned local archive plus manifest, usage documentation and schema
revision. Public registry publication, installer signing and supported OS matrix
remain decisions; do not assume an npm release exists. No web deployment, database
migration, daemon or remote hosting is needed for the initial CLI.
Releases require foundation checks plus product corpus, install/recovery rehearsal,
measured limits and human-reviewed evidence at an exact revision. Owner approval
and coordinator submission follow [development](development.md); workers do not
self-approve. New heads invalidate earlier review/approval according to that policy.

Keep founder expenditure at $0 in the initial phase: existing local or explicitly
customer-owned compute only, no new paid inference/hosting/API credits. Proposed
AI tooling is read-only and bounded; credentials remain outside evidence manifests.
Before persistent workers are provisioned, agree session storage/routing, startup,
backup/restore and ownership separately; no provisioning is part of this plan.
