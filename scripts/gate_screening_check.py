#!/usr/bin/env python3
"""Gate Screening: validate screening decisions and full-text access logs."""
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DECISIONS = ROOT / "docs/search-results/screening-decisions.csv"
DEFAULT_ACCESS = ROOT / "docs/search-results/fulltext-access-log.csv"

REQUIRED_DECISION_FIELDS = [
    "record_id", "title", "screening_round", "decision", "reason_code",
    "confidence", "reviewer", "conflict_status", "fulltext_status",
    "citation_scope",
]

REQUIRED_ACCESS_FIELDS = [
    "pmid", "doi", "title", "access_tier", "status", "pdf_path", "attempts",
]


def resolve(arg, default):
    path = Path(arg) if arg else default
    return path if path.is_absolute() else ROOT / path


def read_csv(path):
    if not path.exists():
        return [], []
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def missing_fields(fields, required):
    return [f for f in required if f not in fields]


def main():
    decision_path = resolve(sys.argv[1], DEFAULT_DECISIONS) if len(sys.argv) > 1 else DEFAULT_DECISIONS
    access_path = resolve(sys.argv[2], DEFAULT_ACCESS) if len(sys.argv) > 2 else DEFAULT_ACCESS

    errors = []
    warnings = []

    decision_fields, decisions = read_csv(decision_path)
    access_fields, access = read_csv(access_path)

    if not decision_fields:
        errors.append(f"Missing or empty decision log: {decision_path}")
    else:
        miss = missing_fields(decision_fields, REQUIRED_DECISION_FIELDS)
        if miss:
            errors.append(f"Decision log missing fields: {miss}")
        if not decisions:
            errors.append("Decision log has headers but no screening rows")

    if not access_fields:
        errors.append(f"Missing or empty access log: {access_path}")
    else:
        miss = missing_fields(access_fields, REQUIRED_ACCESS_FIELDS)
        if miss:
            errors.append(f"Access log missing fields: {miss}")
        if not access:
            warnings.append("Access log has headers but no full-text access rows")

    if decisions:
        incomplete = [
            r for r in decisions
            if not r.get("decision") or not r.get("reason_code") or not r.get("fulltext_status")
        ]
        if incomplete:
            errors.append(f"{len(incomplete)} decision row(s) missing decision/reason/fulltext_status")

        included = [r for r in decisions if r.get("decision", "").lower() in {"include", "maybe", "fulltext_required"}]
        abstract_only = [
            r for r in included
            if "abstract" in r.get("fulltext_status", "").lower()
        ]
        if included:
            ratio = len(abstract_only) / len(included)
            if ratio > 0.20:
                errors.append(f"Abstract-only ratio {ratio:.1%} exceeds 20%")

        conflicts = [r for r in decisions if r.get("conflict_status", "").lower() == "conflict"]
        if conflicts:
            errors.append(f"{len(conflicts)} unresolved conflict row(s)")

    if access:
        tier2 = [r for r in access if r.get("access_tier", "").lower() == "tier2"]
        unresolved_tier2 = [
            r for r in tier2
            if "available" not in r.get("status", "").lower() and not r.get("pdf_path")
        ]
        if unresolved_tier2:
            warnings.append(f"{len(unresolved_tier2)} Tier 2 record(s) still need VPN/PDF resolution")

    print("Gate Screening Check")
    print(f"Decision log: {decision_path}")
    print(f"Access log: {access_path}")
    print(f"Decision rows: {len(decisions)}")
    print(f"Access rows: {len(access)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
