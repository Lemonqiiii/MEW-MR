#!/usr/bin/env python3
"""Inventory robustness scenarios and consistency benchmarks."""
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "harness/test-scenarios.md"
BENCHMARKS = ROOT / "harness/consistency-benchmarks.md"


def read(path):
    return path.read_text(encoding="utf-8", errors="replace")


def main():
    errors = []
    scenario_text = read(SCENARIOS) if SCENARIOS.exists() else ""
    bench_text = read(BENCHMARKS) if BENCHMARKS.exists() else ""

    levels = sorted(set(re.findall(r"^## (L\d+):", scenario_text, re.MULTILINE)))
    scenario_ids = sorted(set(re.findall(r"^### (L\d+-\d+):", scenario_text, re.MULTILINE)))
    bench_ids = sorted(set(re.findall(r"^### (Bench-\d+):", bench_text, re.MULTILINE)))

    for required in ["L6", "L7", "L8"]:
        if required not in levels:
            errors.append(f"Missing robustness level {required}")
    for required in ["Bench-006", "Bench-007", "Bench-008"]:
        if required not in bench_ids:
            errors.append(f"Missing consistency benchmark {required}")

    print("Harness Test Inventory")
    print(f"Robustness levels: {', '.join(levels) or 'none'}")
    print(f"Robustness scenarios: {len(scenario_ids)}")
    print(f"Consistency benchmarks: {len(bench_ids)}")
    print(f"Errors: {len(errors)}")
    for item in errors:
        print(f"ERROR: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
