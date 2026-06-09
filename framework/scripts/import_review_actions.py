#!/usr/bin/env python3
"""Import audit/review-actions.json into a framework-side revision checklist.

This script validates the minimum MEW-MR review-actions contract and writes a
Markdown checklist. It intentionally does not edit the manuscript.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "manuscript" / "review-actions-import.md"
SEVERITY_ORDER = {"critical": 0, "major": 1, "minor": 2, "suggestion": 3}
REQUIRED_TOP = {"review_id", "manuscript", "meta_reviewer_summary", "actions"}
REQUIRED_ACTION = {"id", "severity", "reviewer", "location", "problem_type", "problem", "suggested_fix", "verifier"}


def fail(message: str) -> int:
    print(f"ERROR: {message}")
    return 1


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    missing_top = REQUIRED_TOP - set(data)
    if missing_top:
        errors.append(f"missing top-level fields: {sorted(missing_top)}")

    actions = data.get("actions")
    if not isinstance(actions, list):
        errors.append("actions must be a list")
        return errors

    seen = set()
    for idx, action in enumerate(actions):
        if not isinstance(action, dict):
            errors.append(f"actions[{idx}] must be an object")
            continue
        label = action.get("id", f"actions[{idx}]")
        if action.get("id") in seen:
            errors.append(f"duplicate action id: {action.get('id')}")
        seen.add(action.get("id"))
        missing = REQUIRED_ACTION - set(action)
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
        severity = action.get("severity")
        if severity not in SEVERITY_ORDER:
            errors.append(f"{label}: invalid severity {severity!r}")
        if not isinstance(action.get("location"), dict):
            errors.append(f"{label}: location must be an object")
    return errors


def action_sort_key(action: dict) -> tuple[int, str]:
    return (SEVERITY_ORDER.get(action.get("severity"), 99), str(action.get("id", "")))


def render(data: dict) -> str:
    actions = sorted(data["actions"], key=action_sort_key)
    lines = [
        "# Imported Review Actions",
        "",
        f"- Review ID: `{data['review_id']}`",
        f"- Manuscript reviewed: `{data['manuscript']}`",
        f"- Actions: {len(actions)}",
        "",
        "## Meta Reviewer Summary",
        "",
        data["meta_reviewer_summary"].strip(),
        "",
        "## Checklist",
        "",
    ]
    for action in actions:
        location = action.get("location", {})
        section = location.get("section", "unspecified")
        paragraph = location.get("paragraph")
        where = f"{section}" + (f", paragraph {paragraph}" if paragraph is not None else "")
        lines.extend([
            f"### {action['id']} — {action['severity'].upper()}",
            "",
            f"- [ ] Status: open",
            f"- Reviewer: {action['reviewer']}",
            f"- Location: {where}",
            f"- Problem type: {action['problem_type']}",
            f"- Problem: {action['problem']}",
            f"- Suggested fix: {action['suggested_fix']}",
            f"- Verifier: `{action['verifier']}`",
            "",
        ])
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: python scripts/import_review_actions.py <review-actions.json> [output.md]")
        return 0 if len(sys.argv) >= 2 else 1

    src = Path(sys.argv[1])
    if not src.is_absolute():
        src = Path.cwd() / src
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    if not out.is_absolute():
        out = Path.cwd() / out

    try:
        data = json.loads(src.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        return fail(f"cannot read JSON: {exc}")

    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(data), encoding="utf-8")
    print(f"Imported {len(data['actions'])} review action(s) -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
