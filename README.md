# ShiftProof

**Upgrade with behavioral evidence.**

Local-first analysis of behavioral compatibility when upgrading a third-party SDK.

## Initial goal

Inspect one TypeScript SDK migration using versioned documentation, affected call sites, and behavioral checks. Produce evidence-backed findings and reviewable patch proposals, keeping unresolved capability gaps visible.

## Status

Repository initialized. The first SDK/version pair, implementation, and dedicated OpenCode project session are pending. No application or test commands exist yet.

## Development workspace

Local checkout: `/Volumes/AIWorkspace/projects/shiftproof`.

Execution will use existing local or customer-owned resources, with no new initial founder hosting or inference expenditure. This product has an independent repository and release lifecycle.

## Git workflow

- Commit source, documentation, reviewed fixtures, and dependency lockfiles.
- Keep credentials, OpenCode databases, model weights, caches, and raw customer evidence outside Git.
- Complete a bounded task, run its relevant checks, inspect the diff, then commit and push the intended files.
- Report the commit and push result to the coordinator. A local commit is not a remote backup until the push succeeds.
- Use task branches for substantive implementation work and preserve unrelated changes.

Detailed plans and project-specific working instructions will follow during project planning.
