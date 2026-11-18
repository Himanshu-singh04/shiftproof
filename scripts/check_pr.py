"""Validate the review record; human review still establishes truth and adequacy."""
import json
import re
import sys

APP_LOGIN = "himanshu-portfolio-agent[bot]"
BOT_EMAIL = "358166722+himanshu-portfolio-agent[bot]@users.noreply.github.com"
TRAILER = re.compile(r"^Co-authored-by: .+ <[^<>\s]+@[^<>\s]+>$", re.MULTILINE)
SECTIONS = ("Task", "Changes", "Verification", "Documentation", "Agent attribution")


def validate(pr, commits):
    errors = []
    if not re.match(r"^(feat|fix|docs|chore|ci|test|refactor|perf|build|revert)(\([^\n)]+\))?!?: .+", pr["title"]):
        errors.append("Use a conventional PR title.")
    # Native dependency PRs have their own release notes and commit attribution.
    if pr["user"]["login"] == "dependabot[bot]" and commits and all(
        (commit.get("author") or {}).get("login") == "dependabot[bot]" for commit in commits
    ):
        return errors
    body = pr.get("body") or ""
    for section in SECTIONS:
        match = re.search(r"^## " + re.escape(section) + r"\s*\n(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL)
        if not match or not match[1].strip():
            errors.append(f"Missing content under ## {section}.")
    assisted = re.search(r"^AI-Assisted: (yes|no)\s*$", body, re.MULTILINE)
    agent = re.search(r"^Coding-Agent: (.+)$", body, re.MULTILINE)
    if not assisted or not agent or "replace with" in agent[1].lower():
        errors.append("Declare AI-Assisted: yes/no and the actual Coding-Agent (or none).")
    if pr["user"]["login"] == APP_LOGIN:
        if not assisted or assisted[1] != "yes":
            errors.append("Portfolio App PRs must disclose AI assistance.")
        if not any(f"<{BOT_EMAIL}>" in line for line in TRAILER.findall(body)):
            errors.append("Portfolio App PRs must preserve the owned bot's co-author trailer.")
    if assisted and assisted[1] == "yes":
        trailers = set(TRAILER.findall(body))
        if not trailers or not agent or agent[1].strip().lower() == "none":
            errors.append("Assisted PRs require a named coding agent and co-author trailer.")
        if not commits:
            errors.append("No PR commits found.")
        for commit in commits:
            if (commit.get("author") or {}).get("login") == "dependabot[bot]":
                continue
            committed = set(TRAILER.findall(commit["commit"]["message"]))
            if not committed.intersection(trailers):
                errors.append(f"Commit {commit['sha'][:12]} lacks a co-author trailer preserved in the PR body.")
    return errors


if __name__ == "__main__":
    with open(sys.argv[1]) as event_file, open(sys.argv[2]) as commits_file:
        pr = json.load(event_file)["pull_request"]
        commits = [commit for page in json.load(commits_file) for commit in page]
    errors = validate(pr, commits)
    if errors:
        raise SystemExit("\n".join(errors))
    print("PR record and attribution checks passed; human review is still required.")
