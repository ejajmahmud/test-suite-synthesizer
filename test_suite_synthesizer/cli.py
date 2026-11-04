"""CLI for test-suite-synthesizer."""
import sys
import argparse
from .synthesizer import TestSuiteSynthesizer


def main():
    parser = argparse.ArgumentParser(description="Test Suite Synthesizer")
    parser.add_argument("--demo", action="store_true", help="Generate sample test")
    args = parser.parse_args()

    s = TestSuiteSynthesizer()
    code = "def add(a, b): return a + b\ndef sub(a, b): return a - b"
    test_code = s.synthesize_tests_for_code("calc", code)
    print(test_code)
    sys.exit(0)


if __name__ == "__main__":
    main()
