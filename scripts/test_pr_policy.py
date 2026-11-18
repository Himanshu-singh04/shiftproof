from copy import deepcopy
from pathlib import Path
import unittest

from check_pr import APP_LOGIN, BOT_EMAIL, SECTIONS, validate


class PRPolicyTests(unittest.TestCase):
    def setUp(self):
        self.trailer = f"Co-authored-by: GPT-6 Astra (OpenCode) <{BOT_EMAIL}>"
        self.pr = {"title": "chore: establish foundation", "commits": 1, "user": {"login": APP_LOGIN},
                   "body": "\n\n".join(f"## {section}\nRecorded evidence." for section in SECTIONS)
                   + "\nAI-Assisted: yes\nCoding-Agent: GPT-6 Astra / OpenCode\n\n" + self.trailer}
        self.commits = [{"sha": "abc123", "commit": {"message": "chore: foundation\n\n" + self.trailer}}]

    def test_assisted_record_passes(self):
        self.assertEqual(validate(self.pr, self.commits), [])

    def test_missing_verification_fails(self):
        self.pr["body"] = self.pr["body"].replace("## Verification\nRecorded evidence.", "## Verification\n")
        self.assertTrue(any("Verification" in e for e in validate(self.pr, self.commits)))

    def test_missing_commit_attribution_fails(self):
        self.commits[0]["commit"]["message"] = "chore: foundation"
        self.assertTrue(any("abc123" in e for e in validate(self.pr, self.commits)))

    def test_missing_squash_attribution_fails(self):
        self.pr["body"] = self.pr["body"].replace(self.trailer, "")
        self.assertTrue(validate(self.pr, self.commits))

    def test_app_cannot_declare_unassisted(self):
        self.pr["body"] = self.pr["body"].replace("AI-Assisted: yes", "AI-Assisted: no")
        self.assertTrue(any("disclose" in e for e in validate(self.pr, self.commits)))

    def test_native_dependabot_preserves_own_attribution(self):
        self.pr["user"]["login"] = "dependabot[bot]"
        self.pr["body"] = "Bumps actions/checkout; upstream release notes."
        self.commits[0]["author"] = {"login": "dependabot[bot]"}
        self.commits[0]["committer"] = {"login": "dependabot[bot]"}
        self.commits[0]["commit"]["verification"] = {"verified": True, "reason": "valid"}
        self.assertEqual(validate(self.pr, self.commits), [])

    def test_modified_dependabot_needs_full_record(self):
        self.pr["user"]["login"] = "dependabot[bot]"
        self.pr["body"] = "Bumps actions/checkout; upstream release notes."
        self.assertTrue(validate(self.pr, self.commits))

    def test_unassisted_human_contribution(self):
        self.pr["user"]["login"] = "contributor"
        self.pr["body"] = self.pr["body"].replace("AI-Assisted: yes", "AI-Assisted: no").replace(self.trailer, "")
        self.commits[0]["commit"]["message"] = "chore: unassisted maintenance"
        self.assertEqual(validate(self.pr, self.commits), [])

    def native_dependency(self, committer="web-flow"):
        self.pr["user"]["login"] = "dependabot[bot]"
        self.pr["title"] = "Bump actions/checkout from 6 to 7"
        self.pr["body"] = "Native dependency update with upstream release notes."
        self.commits[0].update(author={"login": "dependabot[bot]"}, committer={"login": committer})
        self.commits[0]["commit"].update(message="Bump actions/checkout", verification={"verified": True, "reason": "valid"})

    def test_signed_native_dependabot_title_and_committers(self):
        for committer in ("dependabot[bot]", "web-flow"):
            with self.subTest(committer=committer):
                self.native_dependency(committer)
                self.assertEqual(validate(self.pr, self.commits), [])

    def test_amended_dependabot_requires_record(self):
        self.native_dependency("human-editor")
        self.pr["title"] = "chore(deps): update dependency"
        self.assertTrue(validate(self.pr, self.commits))

    def test_unsigned_dependabot_identity_is_not_exempt(self):
        self.native_dependency()
        self.pr["title"] = "chore(deps): update dependency"
        self.commits[0]["commit"]["verification"]["verified"] = False
        self.assertTrue(validate(self.pr, self.commits))

    def test_assisted_amendment_cannot_keep_bot_author_to_skip_attribution(self):
        self.commits[0].update(author={"login": "dependabot[bot]"}, committer={"login": "human-editor"})
        self.commits[0]["commit"]["message"] = "chore: amended dependency update"
        self.assertTrue(validate(self.pr, self.commits))

    def test_all_agent_trailers_must_survive_squash(self):
        second = "Co-authored-by: Second agent <second@example.invalid>"
        self.commits[0]["commit"]["message"] += "\n" + second
        self.assertTrue(validate(self.pr, self.commits))
        self.pr["body"] += "\n" + second
        self.assertEqual(validate(self.pr, self.commits), [])

    def test_unrelated_shared_trailer_does_not_replace_portfolio_agent(self):
        other = "Co-authored-by: Contributor <contributor@example.invalid>"
        self.pr["body"] += "\n" + other
        self.commits[0]["commit"]["message"] = "chore: foundation\n\n" + other
        self.assertTrue(validate(self.pr, self.commits))

    def test_unchanged_evidence_template_is_rejected(self):
        template = (Path(__file__).resolve().parents[1] / ".github/PULL_REQUEST_TEMPLATE.md").read_text()
        self.pr["body"] = template.replace("AI-Assisted: choose yes or no", "AI-Assisted: yes").replace(
            "Coding-Agent: replace with actual model and harness (or none for unassisted work)",
            "Coding-Agent: GPT-6 Astra / OpenCode").replace(
            "Replace this line with the truthful Co-authored-by trailer for assisted work.", self.trailer)
        errors = validate(self.pr, self.commits)
        for section in ("Task", "Changes", "Verification", "Documentation"):
            self.assertTrue(any(section in error for error in errors), section)

    def test_assistance_requires_explicit_choice(self):
        self.pr["body"] = self.pr["body"].replace("AI-Assisted: yes", "AI-Assisted: choose yes or no")
        self.assertTrue(validate(self.pr, self.commits))

    def test_lf_and_crlf_with_final_newlines(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=repr(newline)):
                pr, commits = deepcopy(self.pr), deepcopy(self.commits)
                pr["body"] = (pr["body"] + "\n").replace("\n", newline)
                commits[0]["commit"]["message"] = (commits[0]["commit"]["message"] + "\n").replace("\n", newline)
                self.assertEqual(validate(pr, commits), [])

    def test_appended_summary_requires_restoring_final_trailer(self):
        self.pr["body"] += "\n\n## Summary by reviewer\nAdditional summary.\n"
        self.assertTrue(validate(self.pr, self.commits))
        self.pr["body"] += "\n" + self.trailer + "\n"
        self.assertEqual(validate(self.pr, self.commits), [])

    def test_trailer_in_commit_prose_is_not_attribution(self):
        self.commits[0]["commit"]["message"] += "\n\nUnrelated paragraph after the trailer."
        self.assertTrue(validate(self.pr, self.commits))

    def test_incomplete_commit_list_is_rejected(self):
        self.pr["commits"] = 251
        self.assertTrue(validate(self.pr, self.commits * 250))

    def test_missing_count_and_empty_commits_are_rejected(self):
        self.pr.pop("commits")
        self.assertTrue(validate(self.pr, self.commits))
        self.pr["commits"] = 0
        self.assertTrue(validate(self.pr, []))


if __name__ == "__main__":
    unittest.main()
