# B03: local replay isolation feasibility

Status: measured **no-go / replay-disabled / unknown** for
[issue #13](https://github.com/Himanshu-singh04/shiftproof/issues/13).
Worker probe/oracle checks pass. No mechanism is selected for product replay;
the [coordinator independently verified the historical head](https://github.com/Himanshu-singh04/shiftproof/pull/14#issuecomment-7004162398)
`b1ce6c40b2f5d08c7d70a63c582a88256a9bf103` and recommended research acceptance.
The integration revision awaits coordinator re-review and later founder approval.

## Original request and bounded scope

Founder instruction: “ok proceed with the further tasks”, authorizing rolling
independent work after the B02 worker handoff. Same persistent ShiftProof worker,
GPT-6 Astra / OpenCode; no subagents or concurrent editor.

The historical probe base was approved main `6efbbd35398dd08a9232bd24cffda0d84fdb474b`.
At that time, [B02 PR #12](https://github.com/Himanshu-singh04/shiftproof/pull/12)
was pending at `8a0f40c5a44844e08010d143ecd7ac86ae7eb8de`; its code and candidate
runtime were not used for these probes. B01's historical Stripe pair is approved
for research. Accepted B02 main `68cd7a7b6139383391ffdb8bf0f3ad7ac28fac2b` is now
merged into this branch without rebasing the independently reviewed B03 history.

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
Raw attempts and explicit oracles are retained below; these findings are not
claims that a supported macOS boundary is impossible under a different assignment.

Any feasibility must be rerun against the separately approved B02 runtime before
product replay. B04, adapter and product gates remain unresolved.

## Actors, authority and supported boundary

- The operator, approved checkout, Python supervisor, observed runtime and OS are
  trusted to run the experiment. A malicious same-user host process, compromised
  kernel or modified supervisor is outside this measurement. No new UID, VM,
  entitlement, daemon or system policy is created.
- The synthetic Node child stands in for buggy or compromised SDK/harness behavior
  trying to exceed its intended file/network/process authority. It executes only
  the reviewed probe source; no customer module or downloaded code is introduced.
- The desired replay boundary would allow reviewed code/artifacts and per-run
  scratch only, deny network acquisition and unauthorized children/exec, filter
  environment and bound whole-tree resources. **No complete supported boundary
  meeting that requirement was established.**
- All probe targets are owned: sibling `inside`/`outside` directories inside each
  B03 run, synthetic text sentinels, one relative directory symlink, ephemeral IPv4
  loopback TCP/UDP listeners, and at most one bounded child per tree control.
  `outside` means outside the proposed child's grant, not outside authorized storage.
  System executables/manuals/libraries were inspected as tooling, never used as
  confidential-data or filesystem-denial sentinels.

The working diagnostic Seatbelt policy is **targeted deny**, not an allowlist:
`(allow default)`, deny `file-read*`/`file-write*` beneath the owned outside directory,
deny `network*`, deny `process-fork`/`process-exec`, then allow entry exec of the
exact observed Node binary. Unmentioned paths, file metadata elsewhere, IPC and
other capabilities remain permitted/unverified. Passing its targeted probes
cannot justify product replay. No fallback silently labels this policy complete.

## Two-mechanism comparison and primary sources

[`sources.json`](../experiments/b03-isolation-feasibility/sources.json) contains
current-host manual locations, version-specific URLs, read date, complete-source
SHA-256 values and excerpts. Public documentation retrieval is distinct from
network **probes**, whose only targets were self-owned loopback listeners.

| Mechanism | Present / support evidence | Measured result / disposition |
| --- | --- | --- |
| macOS `/usr/bin/sandbox-exec` (Seatbelt profiles) | Present. Installed Apple `sandbox-exec(1)` says **DEPRECATED**, directing developers to App Sandbox. Installed `sandbox(7)` says child processes inherit restrictions and explains that already-open file descriptors retain authority. | Targeted filesystem/network/process denials work in measured scope. Complete restrictive startup profiles fail; deprecated CLI and unvalidated policy leave product replay disabled. |
| Node v26.13.0 `--permission` | Present/stable runtime feature. [Exact-version docs](https://nodejs.org/download/release/v26.13.0/docs/api/permissions.html) explicitly deny malicious-code security guarantees and document relative-symlink and inherited-FD limitations. | Direct API denials work; relative symlink permits outside read/write. Not OS isolation; rejected as the replay security boundary. |

Apple's [current App Sandbox documentation](https://developer.apple.com/documentation/security/app-sandbox)
describes macOS app resource access through entitlements. This experiment does not
adopt/sign an App Sandbox app or evaluate it as a third mechanism. Likewise a Docker
CLI appeared in read-only executable discovery, but no daemon, VM, container or
image was inspected, started or installed. Presence of a CLI establishes no isolation.

Version/support observations are limited to macOS **27.2.1, build 26B131, arm64**;
Node **v26.13.0**, resolved path
`/opt/homebrew/Cellar/node/26.13.0_2/bin/node`; Python **3.13.4**. The system sandbox
binary has no separately claimed semantic version; OS build, binary and manual
hashes identify the observation. Node is dynamically linked Homebrew tooling, not
a standalone authenticated B02 artifact. `otool -L` was inspected read-only;
[host inventory](../experiments/b03-isolation-feasibility/evidence/host.json) retains
OS/build, Node component versions, linked-library listing and the exact final policy.

| Identity | SHA-256 |
| --- | --- |
| Observed Node executable | `64e4f47aef084a288c443ebe9a0091a34acba03ad176fb612b6e7d90784ff93d` |
| Installed sandbox-exec executable | `10cf4a46a575e4747d2419cf343800db0d11ae6e6e9b8415998d3d8f336b2a92` |
| Final raw observations | `5d909bf4d8883a1112b518e2372e144cfdb412b977900b64a65e1f103502d2db` |
| Earlier complete exploratory observations | `72a22cb8b5fdf1e84b43ba1f9fe20d23cdbdbab0db01577a6da0e650c1a06093` |
| Startup profile attempts | `f5c99ea690df8af7a6217f591e6c58027fec34096a488817f0d877d0b2a762b1` |

Hashes detect identity changes, not publisher authenticity. Linked libraries are
not pinned/authenticated by the Node executable hash. This limitation further
precludes treating the observed runtime as an approved product pin.

## Actual attack matrix and oracles

[`probe.cjs`](../experiments/b03-isolation-feasibility/probe.cjs) uses built-in Node
APIs only. [`run.py`](../experiments/b03-isolation-feasibility/run.py) retains argv,
cwd, direct-child PID, status/signal, output, timing, cap/cleanup state, listener
counters and independent filesystem side-effect checks. It does not run B01 SDKs.

Final run: **48 operation probes** (16 per baseline/mechanism), **6 cap controls**,
**9 tree controls**, plus environment-positive, independent filesystem-state and
positive/denied-launch controls. The earlier exploratory run is preserved too.

| Operation | Unrestricted synthetic positive | Targeted sandbox-exec | Node permission model |
| --- | --- | --- | --- |
| Startup, inside read/write | Works | Works | Works |
| Outside synchronous/async read, write, directory listing | Works | EPERM | ERR_ACCESS_DENIED |
| Raw `inside/../outside` traversal | Reads sentinel | EPERM | ERR_ACCESS_DENIED |
| Relative symlink `inside/escape → ../outside`, read/write | Works | EPERM; no outside write | **Escapes grant**; outside bytes read/file created |
| Spawn exact observed Node child | Child marker returned | EPERM | ERR_ACCESS_DENIED |
| Replace owned process with `/bin/sh -c 'printf B03_EXEC'` | Exec marker returned | EPERM | ERR_ACCESS_DENIED |
| TCP `net.connect`, HTTP `http.get`, UDP `dgram.send` | Exact nonce returned by owned listener | EPERM; no delivery | ERR_ACCESS_DENIED; no delivery |
| Filtered synthetic environment | Canary removed, explicit public key kept | Same | Same |

The network positive controls made two TCP/HTTP deliveries and one UDP delivery;
restricted attempts added zero. Both listeners bound **127.0.0.1 port 0**, accepted
only the synthetic nonce for the oracle, and closed/joined at run end. No named-host
lookup, external DNS/egress target, scan or remote service was used. Actual external
DNS/egress, IPv6, Unix sockets, inherited sockets, raw sockets and IPC-mediated
network access remain **unverified**. Local denials are not promoted to proof of
every network path, particularly with the undocumented/deprecated profile surface.

An `allowed` probe needs exit 0 and the exact positive value/marker. A `denied`
probe needs the expected API denial code and a completed structured result; the
runner's independent checks confirm outside writes did not occur under the targeted
policy. A missing result, crash or timeout is a **harness/enforcement failure or
limit**, never an SDK error or semantic incompatibility. There are no SDK outcomes
in these records. Error text is not broadly reclassified as a denial.

The [portable checker](../experiments/b03-isolation-feasibility/check.py) asserts
complete unique probe coverage, exact positive/denial codes, listener increments,
filesystem side effects, caps and child states. The Node symlink escape is an
expected **negative finding**, not a security pass. Counterexamples remove required
network evidence, turn a completed probe into a crash, or inject a compatible result;
all must be rejected. Passing checks mean the no-go evidence is internally consistent.

### Environment and resource/cleanup findings

The launcher constructs an environment from synthetic input only; it does not copy
host credentials. Its allowlist retains `B03_KEEP`, sets HOME/TMPDIR to owned inside
scratch and drops `B03_SYNTHETIC_SECRET`. A separately executed positive passes
that synthetic canary deliberately, proving its detection works. Logs contain only
the presence boolean, never any host environment enumeration. No inherited PATH,
NODE_OPTIONS or NODE_PATH is supplied; executables use explicit paths. Unintended
file descriptors are closed; stdin is `/dev/null`, stdout/stderr are supervised pipes.
Filtering is a launcher behavior, not an OS confidentiality boundary.

- Output emitter is bounded to **128 KiB**, not an endless flood. Supervisor reads
  at most **8,193 bytes** to detect crossing an **8,192-byte combined capture cap**,
  retains at most 8,192, records `output-limit`, and kills its own process group.
  Final output-limit runs completed in approximately 103–111 ms with exit -9.
  This bounds captured pipe bytes, not all kernel-buffered writes or filesystem output.
- The wait probe sleeps only **2.5 seconds**. A **0.4-second** wall deadline is checked
  by the supervisor; observed total termination was approximately 426–438 ms,
  including scheduling/cleanup. Records say `wall-limit`, not SDK failure. Normal
  probes have a 2-second wall bound; tree controls have a 0.5-second bound.
- Parent-failure controls exit **23** intentionally. The same-group child is gone
  after group cleanup. A child using Node `detached: true` survives both parent
  failure/group cleanup and parent timeout/group cleanup: **process-parent or
  process-group timeout is insufficient** for general descendant cleanup.
- Each positive tree control creates only one child, has a unique synthetic token,
  and independently self-expires after 3 seconds. The runner inspects only that
  reported PID with `ps -ww`, checks the owned probe/token before individually
  signaling a still-live child, and records it gone/zombie afterward. No unrelated
  PID is signaled. This cooperative identity/expiry scheme is a bounded experiment
  cleanup backstop, not a malicious-descendant containment mechanism or PID-race proof.
- With either restriction enabled, all three child/detach attempts are denied
  before child creation. This establishes measured prevention for those APIs,
  not inherited-policy enforcement on descendants that never existed.
- Group signals against already-exited leaders returned EPERM in 56 final records.
  The runner records this instead of asserting cleanup. It uses `waitid(WNOWAIT)`
  so the leader PID cannot be reused before group signaling/reaping. Live cap-control
  group signals succeeded; owned-child state is checked separately.

**Not enforced:** whole-tree memory ceiling, cumulative CPU, general process count,
disk quota, reliable cleanup after supervisor death, arbitrary double-fork/reparent
trees, native-code/IPC bypasses, hostile PID reuse or authority through inherited
handles. No exhaustion/fork-bomb probes were attempted. These gaps alone prevent
claiming the planned SP-09/SP-11 resource boundary.

## Startup failures, preserved attempts and no-go launch gate

[`startup-attempts.json`](../experiments/b03-isolation-feasibility/evidence/startup-attempts.json)
retains exact profile strings, arguments, statuses and empty stderr/stdout where
observed. A default-deny profile, a global file-read/write restriction with explicit
library/tool/scratch allowances, its file-only diagnostic variant, and a read-data-only
variant exited **-6 (SIGABRT)** before the Node marker. Cause was not established;
they are startup/enforcement failures, **not successful denials**. Allow-default
controls (`/usr/bin/true` and Node startup) succeeded; separate network-only and
process-only restrictions allowed startup. No extra permissions or tools were
installed to pursue a general policy after this bounded investigation.

An initial runner attempt stopped on an unhandled group-signal EPERM; its
[incomplete record](../experiments/b03-isolation-feasibility/evidence/initial-incomplete.ndjson)
contains inventory only and is not passed as a completed probe run; the
[console failure excerpt](../experiments/b03-isolation-feasibility/evidence/initial-failure.txt)
retains the exit/error. The corrected
supervisor retains signal errors and checks actual owned-child state. The
[exploratory complete capture](../experiments/b03-isolation-feasibility/evidence/preliminary-observations.ndjson)
preceded the final committed-source run, which added independent filesystem state
confirmation and raw traversal input. No earlier capture was overwritten.

`run.py --decision` performs read-only mechanism presence/deprecation detection and
returns `replay: disabled`, `status: unknown`, `reason: ISOLATION_UNAVAILABLE`.
The branch implements no approved complete boundary, so there is no auto-enable
path based on probe success. The denied-launch control first executes a tiny owned
marker-writing command successfully, removes the marker, then passes the same
launch callback to the no-go gate: **zero dispatches and no marker**. This is an
actual executable positive and withheld launch, not an SDK run outside isolation.

**B01 execution inside isolation was not attempted.** There is no accepted complete
boundary to place it in. B01 source/fixtures/lock/captures remain byte-unchanged;
there is no compatible/incompatible result or product RunRecord from B03.

## Reproduction, cleanup and exact evidence

The final run used committed source at
`efec00317127657a884fb330e856dda84574f79e` and created
`/Volumes/AIWorkspace/caches/shiftproof/b03/run-un5mds7z`.
Scratch creation checks the mounted APFS volume UUID
`EAD8504C-B540-47B5-95EA-FBA54591ACAC`; missing/replaced mount or redirected cache
means stop, never Mac fallback. This preflight is not a mount-removal race defense.

```sh
# Manual macOS measurements; creates a new run directory and ephemeral listeners.
python3 -B experiments/b03-isolation-feasibility/run.py
# Check the printed run path, or omit it to verify retained final evidence.
python3 -B experiments/b03-isolation-feasibility/check.py
# Read-only no-go result; no child/SDK launch.
python3 -B experiments/b03-isolation-feasibility/run.py --decision
```

All three commands passed. [Final observations](../experiments/b03-isolation-feasibility/evidence/observations.ndjson)
have 70 raw records; [check output](../experiments/b03-isolation-feasibility/evidence/checks.txt)
and [decision output](../experiments/b03-isolation-feasibility/evidence/decision.json)
are retained. `argv` contains all actual sandbox profile paths/Node flags; the
diagnostic profile is deterministically generated by `profile()` in the source.
Node flags were `--permission --allow-fs-read=<inside> --allow-fs-write=<inside>`;
no network/child/worker/native-addon grants were passed. The other mechanism used
`/usr/bin/sandbox-exec -f <diagnostic.sb> <exact-node> <owned-probe> ...`.

Raw directories, profiles and sentinels remain for review. Listener sockets/threads
close in `finally`; live owned children are individually checked/cleaned as recorded.
After evidence review, remove only an explicitly inspected `run-*` child of B03
scratch with `shutil.rmtree`; validate the mount and direct parent, reject symlinks.
Do not remove B01/B02 caches or coordinator worktrees. No global installation,
profile/service/system policy exists to undo. The no-go gate must be revisited in
a separately bounded task, then rerun against approved B02 tooling before replay.

## Acceptance and check results

| Criterion | Worker verdict | Evidence / limitation |
| --- | --- | --- |
| A1 | Met | Two mechanisms, explicit actors/boundary, current installed Apple manuals and exact Node docs; present/enforced/deprecated/untested separated. |
| A2 | Met for feasibility investigation | Actual owned-file/escape/process/loopback probes with working positives; no complete OS boundary selected. |
| A3 | Met for investigation; product limits unmet | Actual filtered-environment/cap/tree controls demonstrate both bounded cleanup and detachment gap. Whole-tree memory/CPU/descendant enforcement unverified. |
| A4 | Met via no-go path | Explicit oracles, raw failures and successful controls; deterministic disabled/unknown gate and denied launch; no SDK outside isolation. |
| A5 | Met | Exact observed tooling, support/attack matrix, residual risk and mandatory approved-B02 rerun; B04/product gates visible. |
| A6 | Met at worker verification | Probe/evidence checker, repository checker, 25 policy tests, actionlint and full-diff checks pass; historical head independently verified, integration re-review pending. |

Required commands:

```sh
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -p 'test_*.py'
/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=
git diff --check origin/main
git diff --exit-code origin/main -- experiments/b01-sdk-selection
```

No CI sandbox execution is added: Linux foundation CI does not prove macOS
enforcement. CI runs both B02 portable identity controls and B03's portable
raw-evidence checker without Node, privileges or network for those controls;
final PR checks/URLs and exact head are in the handoff comment.

Unsupported/prohibited/unrun: external DNS/egress, credential/customer-file access,
unrelated process signals, privilege changes, hypervisor/image/tool installs,
system policy changes, resource exhaustion, broader runtime/OS testing, App Sandbox
deployment, arbitrary customer modules, B01 SDK execution and product replay.
No paid service was used. Historical independent coordinator probes reproduced
the findings; integration re-review is pending. This result authorizes no product
replay or architecture approval.

## Accepted-main integration

The integration-only assignment preserves issue #13 A1–A6 and the original probes.
B02 accepts Node **26.13.1**, standalone npm **12.2.3**, TypeScript **7.0.2** and
package-lock v3 for research. B03 captures still describe Node **26.13.0**.
There were no textual merge conflicts. Status documentation and CI were reconciled
to retain both portable checkers and accepted B01/B02 scoped maintenance.

B01/B02 experiment files match accepted main; B03 code, fixtures and all captures
match the independently reviewed historical head. Portable controls recheck those
identities and retained observations. Coordinator historical checkout/captures
remain preserved; its independently reproduced observations support the historical
NO-GO, not Node 26.13.1 containment. No new host isolation probes, selected-runtime
execution, provisioning or dependency acquisition belong to this integration.
Future replay requires separately authorized validation against accepted B02 tooling;
the integration keeps **NO-GO / replay disabled / unknown / ISOLATION_UNAVAILABLE**.
