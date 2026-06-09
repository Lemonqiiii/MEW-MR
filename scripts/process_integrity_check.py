#!/usr/bin/env python3
"""Gate 0 process-integrity check for multi-review project reuse."""
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "memory" / "project-status.md"

PROCESS_FILES = [
    "AGENTS.md",
    "memory/agent-specializations.md",
    "harness/quality-gate.md",
    "harness/submission-compliance.md",
    "scripts/gen_word_full.py",
    "scripts/audit_manuscript.py",
    "scripts/rebuild_refs.py",
]

OLD_DEFAULTS = [
    "manuscript/jitc_submission.md",
    "screening_final_40.json",
    "Journal for ImmunoTherapy of Cancer",
    "JITC",
    "LUSC",
    "ICI resistance",
]


def read(path):
    return path.read_text(encoding="utf-8", errors="replace")


def current_manuscript():
    if not STATUS.exists():
        return None
    text = read(STATUS)
    m = re.search(r"`(manuscript/[^`]+\.md)`", text)
    return m.group(1) if m else None


def classify_hit(rel_path, line, token):
    path = rel_path.replace("\\", "/")
    lower_line = line.lower()
    explanatory_markers = [
        "histor", "archive", "legacy", "旧", "上一轮", "历史", "禁止",
        "不得", "替换为", "current_manuscript", "示例", "example"
    ]
    if any(marker in lower_line or marker in line for marker in explanatory_markers):
        return "INFO"
    if path.startswith("scripts/") and token in line:
        return "BLOCK"
    if token == "manuscript/jitc_submission.md" and "current_manuscript" not in line:
        return "WARN"
    return "WARN"


def main():
    errors = []
    warnings = []
    infos = []

    manuscript = current_manuscript()
    if not manuscript:
        errors.append("Cannot resolve current manuscript from memory/project-status.md")
    else:
        manuscript_path = ROOT / manuscript
        if not manuscript_path.exists():
            errors.append(f"Current manuscript does not exist: {manuscript}")

    for rel in PROCESS_FILES:
        path = ROOT / rel
        if not path.exists():
            warnings.append(f"Missing process file: {rel}")
            continue
        text = read(path)
        for lineno, line in enumerate(text.splitlines(), 1):
            for token in OLD_DEFAULTS:
                if token in line:
                    msg = f"{rel}:{lineno}: contains historical token `{token}`"
                    level = classify_hit(rel, line, token)
                    if level == "BLOCK":
                        errors.append(msg)
                    elif level == "WARN":
                        warnings.append(msg)
                    else:
                        infos.append(msg)

    print("Gate 0 Process Integrity")
    print(f"Current manuscript: {manuscript or 'UNRESOLVED'}")
    print(f"Blocking issues: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Historical/info hits: {len(infos)}")

    if errors:
        print("\nBLOCKING")
        for item in errors:
            print(f"- {item}")
    if warnings:
        print("\nWARNINGS")
        for item in warnings[:30]:
            print(f"- {item}")
        if len(warnings) > 30:
            print(f"- ... {len(warnings) - 30} more")
    if infos:
        print("\nINFO")
        for item in infos[:20]:
            print(f"- {item}")
        if len(infos) > 20:
            print(f"- ... {len(infos) - 20} more")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
