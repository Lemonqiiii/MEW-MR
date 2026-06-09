#!/usr/bin/env python3
"""Run the currently executable harness checks."""
import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BASE_CHECKS = [
    ["python", "scripts/process_integrity_check.py"],
    ["python", "scripts/gate_search_check.py"],
    ["python", "scripts/gate_screening_check.py"],
    ["python", "scripts/harness_architecture_check.py"],
    ["python", "scripts/harness_test_inventory.py"],
    ["python", "scripts/review_revision_check.py"],
    ["python", "scripts/audit_manuscript.py"],
]

OPTIONAL_GATE_CHECKS = [
]


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=ROOT, text=True)
    return result.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-search-screening",
        action="store_true",
        help="Deprecated: Gate Search and Gate Screening now run by default.",
    )
    args = parser.parse_args()

    checks = list(BASE_CHECKS)
    if args.include_search_screening:
        checks.extend(OPTIONAL_GATE_CHECKS)

    failures = 0
    for cmd in checks:
        if run(cmd) != 0:
            failures += 1

    print(f"\nHarness checks complete: {len(checks) - failures}/{len(checks)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
