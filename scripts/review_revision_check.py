#!/usr/bin/env python3
"""Gate Revision: validate review action tracking and revision traceability."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTION_LOG = ROOT / "docs" / "review" / "review-action-log.json"
RESPONSE = ROOT / "docs" / "review" / "response-to-reviewers.md"
CHANGELOG = ROOT / "manuscript" / "CHANGELOG.md"
REVISION_MAP = ROOT / "manuscript" / "REVISION_MAP.md"

BLOCKING = {"critical", "must_fix"}
SEVERITIES = BLOCKING | {"major", "minor", "suggestion", "editorial"}
STATUSES = {"open", "in_progress", "resolved", "verified", "deferred", "rejected"}
REQUIRED_ACTION_FIELDS = {
    "id",
    "source",
    "severity",
    "status",
    "location",
    "problem_type",
    "problem",
    "suggested_fix",
    "resolution",
    "verifiers",
}


def current_manuscript_from_status() -> str:
    status_path = ROOT / "memory" / "project-status.md"
    text = status_path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"`(manuscript/[^`]+\.md)`", text)
    if match:
        return match.group(1).replace("\\", "/")
    raise SystemExit("Cannot resolve current manuscript from memory/project-status.md")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def check_action(action: dict, index: int) -> list[str]:
    errors: list[str] = []
    label = action.get("id") or f"actions[{index}]"

    missing = sorted(REQUIRED_ACTION_FIELDS - set(action))
    if missing:
        errors.append(f"{label}: missing fields {', '.join(missing)}")

    severity = action.get("severity")
    if severity not in SEVERITIES:
        errors.append(f"{label}: invalid severity {severity!r}")

    status = action.get("status")
    if status not in STATUSES:
        errors.append(f"{label}: invalid status {status!r}")

    location = action.get("location")
    if not isinstance(location, dict):
        errors.append(f"{label}: location must be an object")
    else:
        for field in ("file", "section", "anchor"):
            if field not in location:
                errors.append(f"{label}: location missing {field}")

    if severity in BLOCKING and status not in {"resolved", "verified"}:
        errors.append(f"{label}: unresolved blocking action ({severity}/{status})")

    if severity == "major" and status in {"deferred", "rejected"}:
        if not action.get("deferral_rationale"):
            errors.append(f"{label}: deferred/rejected major action lacks deferral_rationale")

    if status in {"resolved", "verified"}:
        verifiers = action.get("verifiers")
        if not isinstance(verifiers, list) or not verifiers:
            errors.append(f"{label}: resolved action has no verifier")
        elif not any(v.get("result") == "pass" for v in verifiers if isinstance(v, dict)):
            errors.append(f"{label}: resolved action has no passing verifier")

    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    current = current_manuscript_from_status()

    if not ACTION_LOG.exists():
        errors.append("missing docs/review/review-action-log.json")
    else:
        try:
            data = json.loads(ACTION_LOG.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid review-action-log.json: {exc}")
            data = {}

        logged_manuscript = str(data.get("current_manuscript", "")).replace("\\", "/")
        if logged_manuscript != current:
            errors.append(
                f"review-action-log current_manuscript mismatch: {logged_manuscript!r} != {current!r}"
            )

        actions = data.get("actions")
        if not isinstance(actions, list):
            errors.append("review-action-log actions must be a list")
            actions = []

        seen_ids = set()
        blocking_ids = []
        for i, action in enumerate(actions):
            if not isinstance(action, dict):
                errors.append(f"actions[{i}] must be an object")
                continue
            action_id = action.get("id")
            if action_id in seen_ids:
                errors.append(f"duplicate action id: {action_id}")
            seen_ids.add(action_id)
            if action.get("severity") in BLOCKING:
                blocking_ids.append(str(action_id))
            errors.extend(check_action(action, i))

        response_text = read_text(RESPONSE)
        if blocking_ids and not response_text:
            errors.append("missing docs/review/response-to-reviewers.md for blocking actions")
        for action_id in blocking_ids:
            if action_id and action_id not in response_text:
                warnings.append(f"blocking action {action_id} not referenced in response-to-reviewers.md")

    changelog_text = read_text(CHANGELOG)
    revision_text = read_text(REVISION_MAP)

    if not changelog_text:
        errors.append("missing or empty manuscript/CHANGELOG.md")
    elif current not in changelog_text:
        errors.append(f"CHANGELOG.md does not reference current manuscript {current}")

    if not revision_text:
        errors.append("missing or empty manuscript/REVISION_MAP.md")
    else:
        if current not in revision_text:
            errors.append(f"REVISION_MAP.md does not reference current manuscript {current}")
        if "Revision Map — jitc_submission.md" in revision_text:
            errors.append("REVISION_MAP.md still uses jitc_submission.md as the active title")

    print("Gate Revision Check")
    print(f"- current manuscript: {current}")
    print(f"- action log: {'present' if ACTION_LOG.exists() else 'missing'}")
    print(f"- errors: {len(errors)}")
    print(f"- warnings: {len(warnings)}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

