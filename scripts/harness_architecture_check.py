#!/usr/bin/env python3
"""Check whether the review harness has the required architecture files."""
from pathlib import Path
import json
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "context": [
        "memory/project-status.md",
        "memory/active-focus.md",
        "scripts/process_integrity_check.py",
    ],
    "search_screening": [
        "harness/search-screening-protocol.md",
        "docs/search-results/search-protocol.md",
        "docs/search-results/screening-decisions.csv",
        "docs/search-results/fulltext-access-log.csv",
        "docs/search-results/vpn-download-checklist.md",
        "scripts/materialize_search_screening_logs.py",
        "scripts/gate_search_check.py",
        "scripts/gate_screening_check.py",
    ],
    "quality": [
        "harness/quality-gate.md",
        "scripts/audit_manuscript.py",
    ],
    "revision": [
        "harness/review-revision-protocol.md",
        "docs/review/review-action-log.json",
        "docs/review/response-to-reviewers.md",
        "manuscript/CHANGELOG.md",
        "manuscript/REVISION_MAP.md",
        "scripts/review_revision_check.py",
    ],
    "evaluation": [
        "harness/metrics.md",
        "harness/test-scenarios.md",
        "harness/consistency-benchmarks.md",
        "scripts/harness_test_inventory.py",
        "scripts/run_harness_checks.py",
        "progress/metrics-raw.json",
    ],
    "safety": [
        "harness/safety-policy.md",
    ],
    "submission": [
        "harness/submission-compliance.md",
        "harness/journal-profiles.md",
        "scripts/gen_word_full.py",
    ],
    "evolution": [
        "memory/workflow-evolution.md",
        "features/FEATURE_LIST.md",
        "progress/SESSION_LOG.md",
    ],
}

RECOMMENDED = [
    "harness/architecture.md",
    "knowledge/domain-ontology.md",
    "knowledge/pre-writing-plan.md",
]


def nonempty(rel):
    path = ROOT / rel
    return path.exists() and path.stat().st_size > 0


def metrics_schema_ok():
    path = ROOT / "progress/metrics-raw.json"
    if not path.exists():
        return False, "missing"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return False, f"invalid json: {exc}"
    if "records" not in data or not isinstance(data["records"], list):
        return False, "missing records[]"
    return True, f"{len(data['records'])} record(s)"


def main():
    missing = []
    empty = []
    print("Harness Architecture Check")

    for layer, files in REQUIRED.items():
        layer_missing = []
        for rel in files:
            path = ROOT / rel
            if not path.exists():
                layer_missing.append(rel)
                missing.append(rel)
            elif path.stat().st_size == 0:
                empty.append(rel)
        status = "PASS" if not layer_missing else "FAIL"
        print(f"- {layer}: {status}")
        for rel in layer_missing:
            print(f"  missing: {rel}")

    rec_missing = [rel for rel in RECOMMENDED if not (ROOT / rel).exists()]
    if rec_missing:
        print("\nRecommended files not found:")
        for rel in rec_missing:
            print(f"- {rel}")

    ok, msg = metrics_schema_ok()
    print(f"\nmetrics-raw.json: {'PASS' if ok else 'FAIL'} ({msg})")
    if not ok:
        missing.append("progress/metrics-raw.json schema")

    if empty:
        print("\nEmpty required files:")
        for rel in empty:
            print(f"- {rel}")

    print(f"\nSummary: {len(missing)} missing/schema issue(s), {len(empty)} empty required file(s)")
    return 1 if missing or empty else 0


if __name__ == "__main__":
    sys.exit(main())
