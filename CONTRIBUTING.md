# Contributing

ShiftProof is at the repository-foundation stage. No application commands or release artifacts exist yet.

1. Open an issue with the problem, scope, acceptance criteria, and verification plan.
2. Branch from current `main`, using `feat/`, `fix/`, `docs/`, or `chore/`.
3. Make a focused change with its documentation and relevant verification.
4. Use a conventional title such as `chore: establish repository foundation`.
5. Open a draft PR early; complete the PR template before requesting review.
6. Require passing checks and an approval from `Himanshu-singh04` after the latest push. Squash merge only.

AI assistance is welcome and must be disclosed. Use the actual model name in the
commit trailer and PR body. Do not invent vendor email addresses. Our portfolio
uses its owned App identity for agent attribution; see [development](docs/development.md).
Unmodified Dependabot updates retain Dependabot attribution.

## Local checks

Requires Git, Python 3.11+, and [actionlint](https://github.com/rhysd/actionlint) 1.7.12.

```sh
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -p 'test_*.py'
actionlint -shellcheck= -pyflakes=
git diff --check
```

These check the foundation and PR-record policy. Product tests will accompany product code.
