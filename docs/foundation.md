# Foundation delivery record

## Request and scope

Establish a public, independently operated repository with agent-authored PRs,
authenticated human review, Dependabot, CI, agent co-authorship, and durable
delivery evidence before application development. Founder expenditure starts
at $0; required checks must not depend on paid inference or hosting.

## Changes

- Contributor and agent instructions, issue/PR templates, and human CODEOWNERS.
- Read-only, time-bounded CI with pinned checkout and checksum-verified actionlint.
- Formatting/local-link checks and tested PR evidence/attribution policy.
- Weekly GitHub Actions dependency updates; runtime updates follow manifests.
- Delivery, authentication, attribution, and recovery documentation.

## Verification procedure

Run the four commands in `CONTRIBUTING.md`. Policy tests cover acceptance,
missing verification, missing commit/squash attribution, concealed App assistance,
native Dependabot attribution, and unassisted human work. Actual local and remote
outcomes, commit SHAs, and CI URLs are recorded in the foundation PR timeline.

## Current gates

Public visibility, PR-only main, one approval after the latest push, stale-review
dismissal, code-owner review, resolved conversations, squash-only linear history,
and no bypass are configured in GitHub. Required-check binding must be verified
after the first workflow run. CODEOWNERS and Dependabot become default-branch
configuration after the human-approved foundation merge.

No application, product tests, release artifacts, or dedicated project server
have been created. Those are subsequent milestones, not implied by green CI.
