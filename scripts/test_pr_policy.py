import unittest

from check_pr import APP_LOGIN, BOT_EMAIL, SECTIONS, validate


class PRPolicyTests(unittest.TestCase):
    def setUp(self):
        self.trailer = f"Co-authored-by: GPT-6 Astra (OpenCode) <{BOT_EMAIL}>"
        self.pr = {"title": "chore: establish foundation", "user": {"login": APP_LOGIN},
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
        self.assertEqual(validate(self.pr, self.commits), [])

    def test_modified_dependabot_needs_full_record(self):
        self.pr["user"]["login"] = "dependabot[bot]"
        self.pr["body"] = "Bumps actions/checkout; upstream release notes."
        self.assertTrue(validate(self.pr, self.commits))

    def test_unassisted_human_contribution(self):
        self.pr["user"]["login"] = "contributor"
        self.pr["body"] = self.pr["body"].replace("AI-Assisted: yes", "AI-Assisted: no").replace(self.trailer, "")
        self.assertEqual(validate(self.pr, []), [])


if __name__ == "__main__":
    unittest.main()
