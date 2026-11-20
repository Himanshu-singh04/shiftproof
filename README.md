# ShiftProof

**Upgrade with behavioral evidence.**

Local-first analysis of behavioral compatibility when upgrading a third-party SDK.

## Initial goal

Inspect one TypeScript SDK upgrade using versioned documentation, affected call sites, and offline behavioral fixtures. Produce traceable local reports with explicit coverage gaps. Optional reviewable patch proposals and code transformations are deferred.

## Status

Foundation and planning [PR #5](https://github.com/Himanshu-singh04/shiftproof/pull/5) are merged; App-rename corrections [PR #7](https://github.com/Himanshu-singh04/shiftproof/pull/7) and persistent-worker [provisioning #8](https://github.com/Himanshu-singh04/shiftproof/issues/8) are complete. [B01 research](docs/b01-sdk-selection.md) selected Stripe 12.18.0 → 13.0.0 for research, accepted in PR #10. [B02 toolchain evidence](docs/b02-runtime-validation.md) is accepted in PR #12: Node 26.13.1, npm 12.2.3 and TypeScript 7.0.2 for research. [B03 isolation research](docs/b03-isolation-feasibility.md) is accepted in PR #14 and remains NO-GO / replay disabled; its historical probes used Node 26.13.0. The documentation-only [B03a path decision](docs/b03a-path-decision.md) proposes a pause on product-path adoption, pending review. No shipped SDK compatibility, product runtime or release artifact exists; technical ADRs remain gated. Existing foundation checks are in [CONTRIBUTING](CONTRIBUTING.md).

## Product planning

- [Product requirements](docs/product.md): users, scope, requirement IDs and pilot hypotheses.
- [Solution design](docs/specs/001-mvp/solution-design.md): proposed components, interfaces and pending ADRs.
- [Evidence contract](docs/evidence-contract.md): exact statuses, coverage, provenance and missing evidence.
- [Roadmap](docs/roadmap.md): bounded selection spike and dependency-ordered tasks.
- [Testing](docs/testing.md): planned product/evaluation gates and unmeasured targets.
- [Operations](docs/operations.md): storage reality, proposed install/run/recovery and deployment.

Compilation is not behavioral proof. Offline synthetic/mocked results do not establish actual remote-service compatibility or universal migration safety.

## Development workspace

Local checkout: `/Volumes/AIWorkspace/projects/shiftproof`.

Execution will use existing local or customer-owned resources, with no new initial founder hosting or inference expenditure. This product has an independent repository and release lifecycle.

## Git workflow

See [contributing](CONTRIBUTING.md), [development and delivery](docs/development.md),
and the [foundation record](docs/foundation.md) for checks, authenticated review,
agent attribution, and evidence requirements.

- Commit source, documentation, reviewed fixtures, and dependency lockfiles.
- Keep credentials, OpenCode databases, model weights, caches, and raw customer evidence outside Git.
- Complete a bounded task, run its relevant checks, inspect the diff, then commit and push the intended files.
- Report the commit and push result to the coordinator. A local commit is not a remote backup until the push succeeds.
- Use task branches for substantive implementation work and preserve unrelated changes.

Source, docs and the dedicated worker's history/OAuth database are on the pendrive; execution uses Mac CPU/RAM. Coordinator history and the GitHub App key remain on the Mac. Worker inference uses the existing subscription; product inference is not provisioned or required. See [operations](docs/operations.md) for the storage boundary.
