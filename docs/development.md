# Development and delivery

## Ownership and authentication

`Himanshu-singh04` is the human reviewer and code owner. The private GitHub App
`himanshu-portfolio-agent` (App ID `5812624`, installation `183214958`) authors
agent PRs. It is installed only on ReleaseLens, ShiftProof, and HookTrace.
It can write contents, issues, PRs, and workflows, and read Actions and checks.
The App has no rule bypass. Actions tokens are read-only by default.

The local credential helper is outside Git:

```sh
python3 /Volumes/AIWorkspace/portfolio/tools/agent-auth.py shiftproof git push -u origin HEAD
python3 /Volumes/AIWorkspace/portfolio/tools/agent-auth.py shiftproof gh pr create --draft --body-file /path/to/pr.md
```

The helper creates a token scoped to one repository, passes it through process
environment, and revokes it when the command finishes. Never print tokens or put
them in remote URLs. The owner-only App key lives on the Mac outside the projects.
Human `gh` authentication is reserved for repository administration; approvals
must be submitted by the human reviewer, not an agent using that login.

## Attribution

Git commit authorship and authenticated PR authorship are distinct. Preserve
the human's configured Git identity and credit the actual contributing agent.
For the foundation work, use:

```text
Co-authored-by: GPT-6 Astra (OpenCode) <358166722+himanshu-portfolio-agent[bot]@users.noreply.github.com>
```

This is our owned bot's verified GitHub email, not an OpenAI email or separate
model account. A different model uses its own truthful display name and the same
portfolio bot email. List multiple agents when each actually contributed.
Copy all relevant trailers into the PR body as plain text. Squash defaults use
the PR title and body; inspect the final message and verify the resulting commit.
Do not add AI co-authorship to unchanged automated Dependabot commits. If an
agent contributes to a dependency PR, disclose that work and attribute its commits.

## Evidence for each action

| Action | Durable record |
| --- | --- |
| Work begins | Linked issue with scope and observable acceptance criteria |
| Commit | Descriptive message, associated documentation, agent trailer |
| Push | Remote commit SHA; PR comment with change summary, commands/results, and CI URL |
| PR | Completed template; actual model/harness, documentation impact, relevant trailers |
| Review | Coordinator findings plus human authenticated approval after latest push |
| Merge | Squash SHA and attribution, linked PR, default-branch CI result, follow-up comment |

Do not claim a push or merge succeeded until the remote state confirms it.
The PR timeline and CI logs record operations; repository docs explain behavior
and decisions. Avoid commits whose only purpose is recording their own push.

## Checks and maintenance

- `foundation`: tracked text formatting, relative Markdown file existence,
  PR-policy unit tests, and checksum-verified actionlint workflow validation.
- `pr-record`: conventional title, filled evidence sections, and assisted commit /
  squash-body attribution. This validates structure, not the truth of evidence.
- CI runs on branch pushes and PR changes, including body edits. It has no paid
  API calls, deployment credentials, or model downloads. Hosted runners still
  download pinned tooling. Product correctness checks arrive with implementation.
- Require both check names from GitHub Actions once observed on the first PR.
  All workflow/policy changes remain subject to human code-owner review.
- Dependabot checks GitHub Actions weekly with at most three open version PRs.
  Add runtime ecosystems when manifests exist. Security updates and secret
  scanning/push protection are enabled in repository settings.
- Review dependency changes through the same CI and human approval process.
  Release publishing and CodeQL follow the first supported runtime and package.

## Recovery

Failed CI: inspect logs, fix on the same branch, push, and request fresh approval.
Rejected push: report it; do not weaken protections. Expired token: rerun the
helper for a fresh scoped token. Lost App key: generate a replacement in App
settings, replace the local key, verify authentication, then revoke the old key.
An interrupted helper may leave a token valid until its normal expiration.

The project checkout is on `/Volumes/AIWorkspace`. Dedicated project-session
database placement and routing are pending; changing directory alone does not
move OpenCode history. The coordinator remains on the Mac.
