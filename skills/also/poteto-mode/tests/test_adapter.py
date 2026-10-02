"""Behavioral integration checks. Run with --work-dir pointing at disposable scratch."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
HELPER = SKILL / "scripts/poteto.py"
parser = argparse.ArgumentParser()
parser.add_argument("--work-dir", required=True)
options, remaining = parser.parse_known_args()
WORK = str(Path(options.work_dir).resolve())


class AdapterTests(unittest.TestCase):
    def call(self, *args, env=None, success=True):
        result = subprocess.run([sys.executable, str(HELPER), *args], capture_output=True, text=True, env=env)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def orch(self, store, *args, env=None, success=True):
        result = self.call("run", "--work-dir", WORK, "orch", "--store", str(store), "--json", *args, env=env, success=success)
        return json.loads(result.stdout) if success else result

    def test_resolver_keeps_dependency_names_in_the_bundle(self):
        path = Path(self.call("resolve", "tdd").stdout.strip())
        self.assertIn("refs/cursor-plugins/pstack/skills/tdd", str(path))
        self.assertTrue(path.is_file())
        self.call("resolve", "invented-skill", success=False)

    def test_preparation_does_not_write_into_canonical_skills(self):
        self.call("prepare", "--work-dir", str(SKILL), success=False)
        self.call("verify")

    def test_frontier_cli_uses_github_and_preserves_store_on_invalid_input(self):
        with tempfile.TemporaryDirectory(prefix="frontier-", dir=WORK) as directory:
            root = Path(directory)
            bindir = root / "bin"
            bindir.mkdir()
            fixture = root / "github.json"
            rows = {
                "12": dict(number=12, headRefName="base", baseRefName="main", headRefOid="a" * 40, state="OPEN"),
                "13": dict(number=13, headRefName="tip", baseRefName="base", headRefOid="b" * 40, state="OPEN"),
            }
            fixture.write_text(json.dumps(rows))
            fake = bindir / "gh"
            fake.write_text('#!' + sys.executable + '\nimport json,os,sys\nassert sys.argv[1:3] == ["pr", "view"]\nprint(json.dumps(json.load(open(os.environ["POTETO_TEST_GITHUB"]))[sys.argv[3]]))\n')
            fake.chmod(0o755)
            env = {**os.environ, "PATH": str(bindir) + os.pathsep + os.environ["PATH"], "POTETO_TEST_GITHUB": str(fixture)}
            store = root / "store"
            self.orch(store, "init", env=env)
            self.orch(store, "frontier", "set", "--repo", str(root), "--prs", "12,13", env=env)
            before = json.loads((store / "frontier.json").read_text())
            self.assertEqual(before["generation"], 1)
            self.assertEqual([row["pr"] for row in before["prs"]], [12, 13])
            self.assertEqual(before["lowestUnmerged"], 12)
            rows["12"]["state"] = "MERGED"
            rows["13"]["baseRefName"] = "main"
            rows["13"]["headRefOid"] = "c" * 40
            fixture.write_text(json.dumps(rows))
            self.orch(store, "frontier", "set", "--repo", str(root), "--prs", "12,13", env=env)
            updated = json.loads((store / "frontier.json").read_text())
            self.assertEqual(updated["generation"], 2)
            self.assertEqual(updated["lowestUnmerged"], 13)
            self.assertEqual(updated["prs"][1]["sha"], "c" * 40)
            rows["13"]["state"] = "CLOSED"
            fixture.write_text(json.dumps(rows))
            failure = self.orch(store, "frontier", "set", "--repo", str(root), "--prs", "12,13", env=env, success=False)
            self.assertIn("closed without merge", failure.stderr)
            self.assertEqual(json.loads((store / "frontier.json").read_text()), updated)
            self.orch(store, "frontier", "set", "--repo", str(root), env=env, success=False)
            self.assertEqual(json.loads((store / "frontier.json").read_text()), updated)

    def test_decision_log_treats_generated_text_as_data(self):
        with tempfile.TemporaryDirectory(prefix="log-", dir=WORK) as directory:
            path = Path(directory) / "decisions.tsv"
            self.call("run", "--work-dir", WORK, "log", str(path), "verify", "=not a formula", "a\tb\nc", "$(do-not-run)", "PASS")
            rows = path.read_text().splitlines()
            self.assertEqual(len(rows), 2)
            cells = rows[1].split("\t")
            self.assertEqual(len(cells), 6)
            self.assertTrue(cells[2].startswith("'="))
            self.assertEqual(cells[4], "$(do-not-run)")


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0], *remaining])
