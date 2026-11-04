"""Tests for test-suite-synthesizer."""
import unittest
from test_suite_synthesizer.synthesizer import TestSuiteSynthesizer


class TestTestSuiteSynthesizer(unittest.TestCase):
    def setUp(self):
        self.s = TestSuiteSynthesizer()

    def test_scaffold_generation(self):
        code = "def parse_data(raw): pass"
        out = self.s.synthesize_tests_for_code("parser", code)
        self.assertIn("class TestParser(unittest.TestCase):", out)
        self.assertIn("def test_parse_data_basic", out)


if __name__ == "__main__":
    unittest.main()
