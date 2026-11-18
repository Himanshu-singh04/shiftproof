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
Human `gh` authentication is used for authorized repository administration and
explicitly delegated approval submissions. The founder reviews the linked PR
and coordinator briefing, then approves the identified revision in coordinator
chat. Only after that decision may the coordinator submit an `APPROVE` review
through the founder's existing account, using the review API's explicit
`commit_id`. The review must quote or faithfully record the authorization, link
the briefing, name the founder as decision-maker, and disclose submission by
the coordinator on their behalf. Workers cannot submit approvals.

Verify the recorded review's owner, state, and commit. Recheck required CI,
unresolved threads, current head, and final squash trailers immediately before
merge. A changed head requires renewed review and explicit approval; general
workflow consent never approves a future PR. Do not duplicate an existing valid
owner approval or treat a bot review as the founder's decision. This protocol,
authorized on 2026-11-18, supersedes the earlier personal-click-only rule.

Use the scoped App helper's guarded merge command after approval:

```sh
python3 /Volumes/AIWorkspace/portfolio/tools/agent-auth.py shiftproof gh pr merge NUMBER --squash
```

Replace `NUMBER` with the approved PR number. The helper verifies an actual
current-head owner approval and pins the merge head; it is an operator guard,
not a GitHub-wide permissions boundary. Record approval ID, merge SHA,
attribution, and main CI in the PR timeline. Preserve prior review comments.

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
Copy every co-author trailer into a final plain-text trailer block in the PR body,
separated from the preceding prose by a blank line. Keep this block after any
automated summaries. Squash defaults use the PR title and body. The validator
uses `git interpret-trailers --parse`, so a co-author line in the middle of prose
does not count. Inspect the exact final squash message immediately before merge
and verify the resulting commit; body edits after CI can invalidate attribution.
Do not add AI co-authorship to unchanged automated Dependabot commits. If an
agent contributes to a dependency PR, disclose that work and attribute its commits.

The native Dependabot exception requires API author `dependabot[bot]`, committer
`dependabot[bot]` or `web-flow`, and a valid verified signature. It permits the
bot's generated title and release notes. Unsigned or differently committed updates
need the normal review record. These checks catch ordinary amendments retaining
the bot author; metadata/signature matching is not proof against all deliberate
identity spoofing. Human review remains responsible for truthful attribution.

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

## Coordinator and worker review loop

Preserve the founder's original prompt beside a refined task: intended outcome,
bounded scope, acceptance criteria, assumptions, and verification expectations.
Clarify material ambiguities one question at a time. Do not silently change the
goal or weaken criteria to fit an implementation. Reuse the project's dedicated
worker session once provisioned; keep one editing task active per checkout.

The worker implements, tests, documents, and reports the exact pushed SHA. The
coordinator reviews the delivered behavior against each criterion, independently
exercises relevant behavior, and records met/unmet/unverified results. Green CI
alone is not acceptance. Give findings stable IDs and leave them on the PR,
inline where appropriate. Workers reply to each finding with fixing commits,
commands/results, and CI links; blocked or disputed findings need explanations.
Only resolve a thread after coordinator verification. Append corrections and
verification replies so earlier findings and decisions remain readable.

Label comments `Coordinator review`, `Implementation response`, or `Coordinator
verification`, with actual model and task/session references. Both roles use the
same portfolio App; role labels are not independent authenticated approvals.
Until project workers are provisioned, bootstrap corrections identify the
coordinator as their implementer instead of claiming a worker did the work.

Before requesting human approval, brief one PR at a time: original/refined task,
actual delivery, reviewed SHA, acceptance evidence, checks run/not run, resolved
findings, and remaining limitations. Request approval only after required checks
pass and blocking findings are verified. Recheck new revisions before handing
them back to the founder. Record merge SHA, attribution, and main CI afterward.

## Checks and maintenance

- `foundation`: tracked text formatting, relative Markdown file existence,
  PR-policy unit tests, and checksum-verified actionlint workflow validation.
- `pr-record`: conventional title, filled evidence sections, and assisted commit /
  squash-body attribution. This validates structure, not the truth of evidence.
- Replace template prompts with actual evidence and explicitly choose assisted
  or unassisted work. All co-authors must survive in the final squash trailer block.
- Incomplete commit metadata fails closed: the fetched list must match the PR's
  reported commit count. Split PRs exceeding the REST endpoint's 250-commit cap.
- API retrieval runs before checkout with a step-scoped read token; the Python
  validator receives no `GH_TOKEN`. Checkout does not persist credentials.
- Concurrency includes the checked SHA so an older revision cannot cancel a
  newer revision's checks. Re-run checks if metadata changed during a run.
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

Actions read-only repository settings are defaults, not an immutable maximum:
workflow `permissions` can request additional access. Same-repository workflow
authors are trusted automation operators, not sandboxed adversaries. These
workflows and App-authored policy changes require human review; the App key is
never a CI secret. Main protections have no App/Actions bypass. Token isolation
here reduces unnecessary exposure but does not make arbitrary workflow edits
safe. See [GitHub token permissions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication).

## Recovery

Failed CI: inspect logs, fix on the same branch, push, and request fresh approval.
Rejected push: report it; do not weaken protections. Expired token: rerun the
helper for a fresh scoped token. Lost App key: generate a replacement in App
settings, replace the local key, verify authentication, then revoke the old key.
An interrupted helper may leave a token valid until its normal expiration.

The project checkout is on `/Volumes/AIWorkspace`. Dedicated project-session
database placement and routing are pending; changing directory alone does not
move OpenCode history. The coordinator remains on the Mac.
