#!/usr/bin/env python3
"""Gate Search: validate that the search protocol is reproducible enough."""
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = ROOT / "docs/search-results/search-protocol.md"


def read(path):
    return path.read_text(encoding="utf-8", errors="replace")


def count_tbd(text):
    return len(re.findall(r"\bTBD\b", text, flags=re.IGNORECASE))


def table_rows(section):
    return [
        line for line in section.splitlines()
        if line.startswith("|") and "---" not in line and "Database" not in line
    ]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PROTOCOL
    if not path.is_absolute():
        path = ROOT / path

    errors = []
    warnings = []

    if not path.exists():
        errors.append(f"Missing search protocol: {path}")
        text = ""
    else:
        text = read(path)

    required_headings = [
        "## Review Context",
        "## PICO / PECO / SPIDER",
        "## Databases",
        "## Search Strings",
        "## Seed Papers",
        "## Search Diagnostics",
        "## Change Log",
    ]
    for heading in required_headings:
        if heading not in text:
            errors.append(f"Missing heading: {heading}")

    if text:
        tbd = count_tbd(text)
        if tbd:
            warnings.append(f"{tbd} TBD placeholder(s) remain")

        search_blocks = re.findall(r"```text\s*(.*?)```", text, re.DOTALL)
        filled_blocks = [b.strip() for b in search_blocks if b.strip() and b.strip().upper() != "TBD"]
        if not filled_blocks:
            errors.append("No filled search string block found")

        seed_section = text.split("## Seed Papers", 1)[-1].split("## Search Diagnostics", 1)[0]
        seed_rows = [r for r in table_rows(seed_section) if "TBD" not in r]
        if len(seed_rows) < 1:
            warnings.append("No completed seed paper row found")

        db_section = text.split("## Databases", 1)[-1].split("## Search Strings", 1)[0]
        db_rows = [r for r in table_rows(db_section) if "TBD" not in r]
        if len(db_rows) < 2:
            warnings.append("Fewer than 2 completed database rows found")

    print("Gate Search Check")
    print(f"Protocol: {path}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
