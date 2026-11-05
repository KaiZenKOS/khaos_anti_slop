"""Local smoke tests for the optional heuristic scanner."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'scripts' / 'audit_slop.py'
spec = importlib.util.spec_from_file_location('khaos_audit', MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class AuditTests(unittest.TestCase):
    def test_finds_generic_copy(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'page.tsx').write_text('Unlock the future with our revolutionary product', encoding='utf-8')
            findings = module.scan(Path(d))
            self.assertTrue(any(f['rule'] == 'generic-copy' for f in findings))

    def test_accepts_brand_purple(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'style.css').write_text('body { color: #5A3FFF; }', encoding='utf-8')
            self.assertEqual(module.scan(Path(d)), [])

    def test_skips_dependencies(self):
        with tempfile.TemporaryDirectory() as d:
            package = Path(d) / 'node_modules'
            package.mkdir()
            (package / 'x.js').write_text('revolutionize the future', encoding='utf-8')
            self.assertEqual(module.scan(Path(d)), [])

if __name__ == '__main__':
    unittest.main()
