import json, os, subprocess, sys, tempfile, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class KitTests(unittest.TestCase):
    def test_licenses_script_runs_and_writes_json(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "licenses.json")
            r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts/dependency_licenses.py"), "--out", out], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            with open(out) as f: data = json.load(f)
            self.assertIn("packages", data); self.assertIsInstance(data["packages"], list)

    def test_licenses_deny_detects(self):
        r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts/dependency_licenses.py"), "--deny", "MIT"], capture_output=True, text=True)
        self.assertIn("interdits", r.stdout)   # au moins la ligne de synthèse ; le code de sortie dépend de l'environnement

    def test_sbom_is_cyclonedx(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "sbom.cdx.json")
            r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts/sbom_cyclonedx.py"), "--out", out], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            with open(out) as f: bom = json.load(f)
            self.assertEqual(bom["bomFormat"], "CycloneDX"); self.assertEqual(bom["specVersion"], "1.5")
            self.assertTrue(all(c["purl"].startswith("pkg:pypi/") for c in bom["components"]))

if __name__ == "__main__":
    unittest.main()
