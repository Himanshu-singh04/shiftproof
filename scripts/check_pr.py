"""Validate the review record; human review still establishes truth and adequacy."""
import json
import re
import subprocess
import sys

APP_LOGIN = "code-daddy04[bot]"
BOT_USER_ID = 358166722
BOT_EMAIL = "358166722+code-daddy04[bot]@users.noreply.github.com"
LEGACY_BOT_EMAIL = "358166722+himanshu-portfolio-agent[bot]@users.noreply.github.com"
BOT_EMAILS = (BOT_EMAIL, LEGACY_BOT_EMAIL)
TRAILER = re.compile(r"^Co-authored-by: .+ <[^<>\s]+@[^<>\s]+>$", re.MULTILINE)
SECTIONS = ("Task", "Changes", "Verification", "Documentation", "Agent attribution")
PLACEHOLDERS = {
    "Task": "Link the issue and its acceptance criteria.",
    "Changes": "Describe the change and any compatibility impact.",
    "Verification": "List exact commands and results. Link CI after it runs; disclose checks not run.",
    "Documentation": "List updated documents, or explain why none are needed.",
}


def normalize(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")


def coauthors(message):
    """Use Git's final-trailer rules, including for the PR-title/body squash default."""
    parsed = subprocess.check_output(
        ["git", "interpret-trailers", "--parse"], input=normalize(message), text=True)
    return set(TRAILER.findall(parsed))


def native_dependabot(commit):
    # These API metadata/signature checks detect ordinary amendments, not all spoofing.
    verification = commit["commit"].get("verification") or {}
    return ((commit.get("author") or {}).get("login") == "dependabot[bot]"
            and (commit.get("committer") or {}).get("login") in {"dependabot[bot]", "web-flow"}
            and verification.get("verified") is True
            and verification.get("reason") == "valid")


def has_portfolio_agent(trailers):
    return any(line.endswith(f"<{email}>") for line in trailers for email in BOT_EMAILS)


def validate(pr, commits):
    errors = []
    author = pr.get("user") or {}
    if type(author.get("id")) is not int or author["id"] <= 0:
        return ["Missing valid PR author ID; fetch complete GitHub REST metadata."]
    # The REST PR commits endpoint caps results at 250 even with pagination.
    if not commits or pr.get("commits") != len(commits):
        return ["Incomplete PR commit list; fetch the full list or split the PR (REST limit: 250)."]
    # Native dependency updates retain their generated titles, notes, and attribution.
    if pr["user"]["login"] == "dependabot[bot]" and all(native_dependabot(c) for c in commits):
        return errors
    if not re.match(r"^(feat|fix|docs|chore|ci|test|refactor|perf|build|revert)(\([^\n)]+\))?!?: .+", pr["title"]):
        errors.append("Use a conventional PR title.")
    body = normalize(pr.get("body") or "")
    for section in SECTIONS:
        match = re.search(r"^## " + re.escape(section) + r"[ \t]*\n(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL)
        content = re.sub(r"<!--.*?-->", "", match[1], flags=re.DOTALL).strip() if match else ""
        if not content or (section in PLACEHOLDERS and PLACEHOLDERS[section] in content):
            errors.append(f"Missing completed content under ## {section}; replace template instructions.")
    assisted = re.search(r"^AI-Assisted: (yes|no)\s*$", body, re.MULTILINE)
    agent = re.search(r"^Coding-Agent: (.+)$", body, re.MULTILINE)
    if not assisted or not agent or "replace with" in agent[1].lower():
        errors.append("Declare AI-Assisted: yes/no and the actual Coding-Agent (or none).")
    trailers = coauthors(pr["title"] + "\n\n" + body)
    portfolio_pr = author["id"] == BOT_USER_ID
    if portfolio_pr:
        if not assisted or assisted[1] != "yes":
            errors.append("Portfolio App PRs must disclose AI assistance.")
        if not has_portfolio_agent(trailers):
            errors.append("Portfolio App PRs require the owned bot's co-author in the final Git trailer block.")
    if assisted and assisted[1] == "yes":
        if not trailers or not agent or agent[1].strip().lower() == "none":
            errors.append("Assisted PRs require a named coding agent and final co-author trailer block.")
        for commit in commits:
            if native_dependabot(commit):
                continue
            committed = coauthors(commit["commit"]["message"])
            if not committed or not committed.issubset(trailers):
                errors.append(f"Commit {commit['sha'][:12]} must preserve all co-authors in the PR's final trailer block.")
            if portfolio_pr and not has_portfolio_agent(committed):
                errors.append(f"Commit {commit['sha'][:12]} lacks the portfolio agent's final co-author trailer.")
    return errors


if __name__ == "__main__":
    with open(sys.argv[1]) as event_file, open(sys.argv[2]) as commits_file:
        pr = json.load(event_file)["pull_request"]
        commits = [commit for page in json.load(commits_file) for commit in page]
    errors = validate(pr, commits)
    if errors:
        raise SystemExit("\n".join(errors))
    print("PR record and attribution checks passed; human review is still required.")
