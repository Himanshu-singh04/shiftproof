# B02: isolated runtime/toolchain validation

Status: accepted **Node 26.13.1, TypeScript 7.0.2, standalone npm 12.2.3,
package-lock v3** for the bounded darwin-arm64 research target in
[issue #11](https://github.com/Himanshu-singh04/shiftproof/issues/11).
Worker validation, coordinator review and founder approval completed in
[PR #12](https://github.com/Himanshu-singh04/shiftproof/pull/12), merged as
`68cd7a7b6139383391ffdb8bf0f3ad7ac28fac2b`.
This is not a product runtime release or a production SDK recommendation.
[B03's historical Node 26.13.0 probes](b03-isolation-feasibility.md) retain their
separate NO-GO result; accepting these tooling pins does not establish isolation.

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

## Selection and primary evidence

Observed target: macOS **27.2.1 (26B131), darwin arm64**, on the authorized external
APFS volume. [`sources.json`](../experiments/b02-runtime-validation/sources.json)
retains primary URLs, retrieval date, complete response SHA-256 values and selected
release/engine/platform evidence. Sources were retrieved on 2026-11-19 with TLS
verification enabled. Only these two Node lines were compared:

| Candidate | Primary release evidence | Lifecycle and decision |
| --- | --- | --- |
| Node 24.22.3 | [Release](https://nodejs.org/en/blog/release/v24.22.3), [versioned platform requirements](https://github.com/nodejs/node/blob/v24.22.3/BUILDING.md), official index marks security release 2026-11-10, bundled npm 11.19.1 | Maintenance LTS since 2026-10-20; scheduled end 2028-04-30. Credible alternative, metadata compared only; archive not downloaded/executed. |
| Node 26.13.1 | [Release](https://nodejs.org/en/blog/release/v26.13.1), [versioned platform requirements](https://github.com/nodejs/node/blob/v26.13.1/BUILDING.md), official index marks security release 2026-11-10, bundled npm 11.20.0 | Active LTS from 2026-10-28; maintenance 2027-10-20; end 2029-04-30. Selected for longer remaining support and verified prebuilt darwin-arm64 availability. |

Both versioned platform tables declare macOS arm64 Tier 1, minimum macOS 13.5.
Lifecycle dates come from the [Node release schedule](https://github.com/nodejs/Release/blob/main/schedule.json),
snapshotted in the source record. Node 26.13.1 was independently selected from
release/security evidence; B01's observed 26.13.0 was not inherited as a pin.

- **npm 12.2.3**, separately downloaded from the registry, is a stable
  [versioned upstream release](https://github.com/npm/cli/releases/tag/v12.2.3).
  Its engine range is `^22.22.2 || ^24.15.0 || >=26.0.0`, satisfied by selected Node.
  Choose the current stable npm release rather than silently inherit B01 npm or
  Node's bundled npm **11.20.0**. The bundled npm is inventoried but never invoked.
  npm's tarball bundles its transitive tree: the complete tarball integrity pins
  its bytes, and all 188 included package manifests have retained identities.
- **TypeScript 7.0.2** is the stable [versioned release](https://github.com/microsoft/TypeScript/releases/tag/v7.0.2),
  with Node engine `>=16.20.0`. This is a native compiler distribution, not Node's
  type stripper. Its exact optional `@typescript/typescript-darwin-arm64@7.0.2`
  package declares `os: darwin`, `cpu: arm64`; registry SHA-512 and the upstream
  GitHub release asset SHA-256 both match the actual native tarball bytes.
  Other platform optional packages are pinned in the lock but not provisioned or
  claimed tested. Node has a dated LTS schedule; npm/TypeScript stable-release and
  engine evidence is not a promised multi-year patch-support schedule.
- **Lock format 3** was explicitly generated with selected npm's
  `install --package-lock-only --lockfile-version=3 --ignore-scripts --no-audit --no-fund`
  in task-owned `b02/seed`, using the isolated environment below. Its identities
  were committed in `bb55de61fba20f148ec5740702f81aa2a4e78bf5` before the successful
  fresh offline run. B01's separate lock was copied byte-for-byte, never regenerated.

### Artifact and license identities

All 27 downloaded archives passed byte verification before their code executed.
[`pins.json`](../experiments/b02-runtime-validation/pins.json) retains **full SHA-256,
registry SHA-512 integrity, URLs and upstream hash sources** for every provisioned
archive, including all 23 B01 packages. npm/TypeScript also match registry SHA-1;
SHA-512 is the stronger registry check. Node matches the official HTTPS
`SHASUMS256.txt`. No detached GPG or registry-signature validation is claimed;
trust rests on reviewed HTTPS upstream metadata and the committed hashes.

| Artifact | SHA-256 |
| --- | --- |
| node-v26.13.1-darwin-arm64.tar.gz | `aec2514ea1ceb2ba52455e9ec65986f6749a06dd759e5db2a72e6889668c9735` |
| npm-12.2.3.tgz | `fa0711dd513fa1386bbad3962a292cb813461cb57dedf07d6eb7efe76dffe897` |
| typescript-7.0.2.tgz | `da2513f4b95176d6dde8b51aab7afe8a927656c9d277369793f77f7e59371c08` |
| typescript-darwin-arm64-7.0.2.tgz | `902e2fe1cf0799198ef902c6b8c310a450fef629a6baba41d45641ef75c04ebd` |
| B02 package-lock.json | `64b091d82229261d090b92e21e1a44261496095b2c5526df885b516c614be571` |
| Original B01 package-lock.json | `a296083b67e75cba062f981c18b3a10e86fe980de19e90921b144a18e9018412` |

[`inventory.ndjson`](../experiments/b02-runtime-validation/inventory.ndjson) records
archive-member paths, exact package.json hashes, names/versions/engines/license
declarations, lifecycle hooks and license/notice file hashes. Actual license text
remains in the verified archives under `b02/downloads` and extracted package trees.
Node is MIT with bundled third-party notices; npm is Artistic-2.0; TypeScript and
its native package are Apache-2.0. B01 package licenses remain as recorded in its
lock and original record. The repository's synthetic experiment is UNLICENSED.

Inspection covered 184 manifests in Node (including unused bundled npm), 188 in
standalone npm, two in TypeScript (including vendored vscode-jsonrpc), one in the
native compiler and all B01 tarballs, including nested module-type manifests.
**No preinstall/install/postinstall hooks occur in this inventory.** Publish and
prepare hooks do exist, including build commands, global-install commands in
vendored publish scripts and Git-push/config commands. They were read as data,
never invoked. Only prebuilt published tarballs are used; no pack/publish/source
build is run. Every npm operation disables scripts, audit, funding and update notices.

## Reproduction and storage

Clean fetched base: `6efbbd35398dd08a9232bd24cffda0d84fdb474b`.
The mounted external APFS volume reports UUID
`EAD8504C-B540-47B5-95EA-FBA54591ACAC`; missing mount means stop, no fallback.
The launcher checks this volume UUID, native host architecture and non-redirected
cache path before creating work directories. This operational check is not a
mount-removal race defense or filesystem sandbox.

From the repository root on this assigned host:

```sh
python3 -B experiments/b02-runtime-validation/validate.py provision
python3 -B experiments/b02-runtime-validation/validate.py run
python3 -B experiments/b02-runtime-validation/check.py --scratch /Volumes/AIWorkspace/caches/shiftproof/b02
```

The first command is the only network-allowed phase. It uses explicit
`/usr/bin/curl --fail --silent --show-error --location --proto =https --proto-redir =https --output PATH URL`
for missing archives, rejects changed bytes/inventory, safely extracts verified
prebuilt Node/npm archives (Python `tarfile` data filter), then seeds only the B02
npm cache with `npm cache add ABSOLUTE_TARBALL --offline --ignore-scripts --no-audit --no-fund`.
Python 3.11+ must include the standard-library tarfile data filter (backported in
3.11.8). Existing extracted metadata is checked; mismatches stop instead of being repaired silently.

All npm/compile commands are constructed with explicit paths, never PATH discovery:

```text
NODE=/Volumes/AIWorkspace/caches/shiftproof/b02/tools/node-v26.13.1-darwin-arm64/bin/node
NPM=/Volumes/AIWorkspace/caches/shiftproof/b02/npm-12.2.3/package/bin/npm-cli.js
TSC=<fresh-run>/b02/node_modules/typescript/bin/tsc
```

The Node executable SHA-256 is
`266dec4dce3a6cdcf5cdc38722a00cf5ae6a12cc51068d2a227655bbb75751ec`.
`NODE TSC` resolves the locked native compiler at
`<fresh-run>/b02/node_modules/@typescript/typescript-darwin-arm64/lib/tsc`.
The TypeScript 7 launcher uses an absolute native executable path, not a source build.

Each `run` creates a new `run-*` directory containing initially absent b01/b02
node_modules trees; it copies only the pinned inputs and calls the equivalent of:

```text
NODE NPM ci --offline --ignore-scripts --no-audit --no-fund
NODE TSC --version
NODE TSC good.ts --strict --target ES2022 --module commonjs --outDir out --noEmitOnError
NODE <fresh-run>/b02/out/good.js
NODE TSC bad.ts --strict --noEmit --pretty false
NODE <fresh-run>/b01/check.cjs
```

`NODE`/`NPM`/`TSC` above denote exact absolute arguments, not installed shell aliases.
Every actual argv, cwd, exit status, stdout and stderr is in the retained command
logs. The parent environment is replaced with task-local `HOME`, `TMPDIR`, empty
user/global npm config files, `NPM_CONFIG_CACHE=b02/npm-cache`, and explicit
ignore-scripts/audit/fund/update-notifier/engine-strict settings. No inherited
credentials, NODE_OPTIONS, NODE_PATH, PATH changes or user npm config are used.
B01's unchanged child harness still launches with its original empty environment;
it performs only the reviewed synthetic transport/clock experiment.

### Results and preserved attempts

Manual on darwin-arm64:

| Command / record | Exact outcome |
| --- | --- |
| `validate.py provision` | Exit 0; all 27 archives verified; 25 local package tarballs seeded into task-only cache. [Provision argv/results](../experiments/b02-runtime-validation/evidence/provision.ndjson) |
| First `validate.py run` | Exit 1: good.ts compiled and emitted JS ran; bad.ts correctly reported TS2322/exit 1, but initial harness expected exit 2. [Unmodified failed attempt](../experiments/b02-runtime-validation/evidence/initial-failed-run.ndjson) |
| Corrected `validate.py run` from committed lock | Exit 0: fresh offline B01 install added 23 packages; B02 added 2; Node/npm/TypeScript version probes passed; good.ts compile/emitted JS exit 0; bad.ts exit 1 with TS2322; B01 check exit 0. [Exact argv/results](../experiments/b02-runtime-validation/evidence/offline-run.ndjson) |
| `check.py --scratch /Volumes/AIWorkspace/caches/shiftproof/b02` | Positive and negative identity/semantic controls pass; synthetic dispatch only, no SDK/tooling loaded. [Exact control output](../experiments/b02-runtime-validation/evidence/identity-controls.txt). Also runs portably in CI. |

Successful directory: `/Volumes/AIWorkspace/caches/shiftproof/b02/run-2t4pj1a4`.
Earlier failed directory: `b02/run-5x0byznm`; cache-seeding directory:
`b02/provision-83rzv5t5`. No retained attempt was overwritten to obtain a pass.

[Raw B02 observations](../experiments/b02-runtime-validation/evidence/observations.ndjson)
contain three fresh processes per SDK version, three scenarios each: **18 scenario
executions**, with one-request source StripeAPIError versus two-request target success
and requested 500-ms sleep; equal 200 return and equal structured nonretryable 400 error.
SHA-256: `a0a0f9d7cb3282f66005986a18d8e472348e5fccd63e452242fab3bb1dc2853e`.
Original B01 observations remain
`dcbb84d75584697828fc5fe9c753a17823b67088fadc9d10e13dd254f49dd3a1`.

Raw captures differ, as expected. `compare()` permits only Node `v26.13.0 → v26.13.1`
in the provenance line and parsed `X-Stripe-Client-User-Agent.lang_version`; it
requires equality of every remaining field, including input hashes, package metadata,
ordered events, timing requests and outcomes. It never rewrites retained captures.
The changed npm is installation provenance in the command log; B01 does not capture
npm in its observation schema. The compiler is not part of B01's JavaScript execution.

## Identity gate and limits

`validate.py` verifies the Node executable hash before its built-in-only runtime
probe, then checks exact Node version/platform/architecture before loading npm,
compiler or SDK code. Before npm dispatch, every included npm package manifest
must match the reviewed tarball bytes. Before compiler/SDK dispatch, manifest/lock
and fixture/script hashes must match the committed inputs, direct manifest/lock
fields must agree, and every applicable installed package manifest must match its
verified archive. Missing native TypeScript is a failure even though npm calls it
optional; foreign platform optional packages are neither installed nor accepted
as a replacement. Exact npm/compiler CLI version probes are additional positive
controls after metadata gates.

`check.py` uses disposable copies of real inputs/locks, **explicitly synthetic
installed manifests and mocked dispatch**. Positives must reach dispatch once;
negative controls must fail before it is called. Cases cover wrong/missing Node
executable, wrong version/platform/architecture, wrong/missing npm/compiler/native
compiler, modified/missing SDK/transitive identity, modified/missing manifest/lock,
and manifest/lock disagreement even with a refreshed manifest hash. A changed
semantic capture must fail comparison. These are not actual executions of an
unsupported binary, malicious SDK or foreign architecture.

**Trust boundary:** tarball integrity authenticates downloaded bytes relative to
the reviewed upstream hash. Installed package.json checks detect identity drift;
they do **not** authenticate arbitrary implementation/native-binary edits, module
resolution redirection, concurrent mutation or a compromised trusted checkout.
An explicit implementation-only mutation control confirms that metadata checks
cannot detect it; that mock code is never executed. Only Node's executable has a
separate pre-execution binary hash check. Use fresh installs from verified cache
for reproduction. These are trusted-research entry points, not a host-wide
enforcement mechanism; direct invocation outside the launcher bypasses its gates.

No egress/filesystem/process isolation is established by offline flags, empty
environments, injected transport or timeouts. B03 remains unresolved; arbitrary
customer/module replay is not authorized. No product RunRecord or behavioral
compatibility claim beyond these reviewed synthetic fixtures is made.

### Platforms and cleanup

Manual positive result is limited to the observed native darwin-arm64 host. The
launcher refuses other OS/architectures and wrong/missing volume identity. Linux
CI runs only portable input/identity/capture checks with mocked dispatch; it does
not install Node/TypeScript, download large archives or claim Linux runtime support.
Other macOS versions, x64/Rosetta, Windows and Linux toolchain execution are unverified.

Runs and failed logs are intentionally retained for coordinator reproduction.
After required evidence has been preserved, remove only a specifically inspected
task-owned `run-*` or `provision-*` directory beneath `b02`; never B01 cache or shared
caches. Example cleanup, **not executed for the retained runs**:

```sh
python3 -B - <<'PY'
import sys, shutil
from pathlib import Path
sys.path.insert(0, 'experiments/b02-runtime-validation')
import validate as v
v.mount_check()
path = v.CACHE / 'run-2t4pj1a4'
v.require(path.resolve().parent == v.CACHE and not path.is_symlink(), 'unexpected cleanup target')
shutil.rmtree(path)
PY
```

`check.py` removes only its own temporary mock directory automatically. Keep
`downloads`, `tools`, `npm-12.2.3` and `npm-cache` for offline reproduction; deleting
them later requires re-provisioning verified artifacts. No profile/service/global
install was created to undo.

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

## Acceptance and verification record

| Criterion | Worker status | Evidence / limits |
| --- | --- | --- |
| A1 | Met | Two Node lines compared; exact four-part selection, primary versioned sources and actual selected artifact hashes above. |
| A2 | Met | Verified prebuilt archives, scoped environment/cache, complete lifecycle/license inventory, no hook/source-build execution; exact locks and bundled npm identities retained. |
| A3 | Met | Committed-lock fresh offline installs, real compile/TS2322, 18 repeated B01 scenarios, raw failed and successful attempts, explicitly constrained comparison. |
| A4 | Met within declared trust boundary | Pre-load gates; actual positive toolchain and portable disposable/mock negatives. Installed implementation authentication is expressly unverified. |
| A5 | Met | Commands, full hashes, limitations, cleanup and manual/Dependabot maintenance; B03 remains open. |
| A6 | Met at worker verification | B01 research approval reconciled; original experiment unchanged; portable CI checks added. Subsequent coordinator review and founder approval completed in PR #12. |

Required local commands: `python3 scripts/check_repository.py` PASS;
`python3 -m unittest discover -s scripts -p 'test_*.py'` PASS (25 tests);
`/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=` PASS;
`git diff --check` and full base-to-HEAD whitespace check PASS;
`git diff --exit-code origin/main -- experiments/b01-sdk-selection` PASS (empty).
The PR timeline records final head, exact rerun outcomes and CI URLs; green checks
do not replace coordinator reproduction and founder approval.

Other failures: a guessed `microsoft/typescript-go` release tag URL returned 404;
the canonical Microsoft TypeScript 7.0.2 release succeeded and links its original
tag. A guessed native `bin/` lookup was absent; the inspected published resolver
uses `lib/tsc`. An intermediate `pr-record` failed after a bot summary displaced
the final co-author block; restoring the block preserved the summary and the
subsequent check passed. No TLS/access protections were weakened.

Not run: Node 24 execution, other-platform toolchains, detached signature validation,
full advisory/security audit, hosted Dependabot update proposals, enforced B03
isolation, customer code, live Stripe calls, product tests, performance benchmarks
or pilot validation. Selection is accepted for the bounded research target only.
