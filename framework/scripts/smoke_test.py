#!/usr/bin/env python3
"""
Smoke test — verify the framework is correctly set up.
Run this FIRST after cloning. Takes ~3 seconds.

Usage:
    python3 scripts/smoke_test.py
"""

import sys
import os
from pathlib import Path

# Fix Windows terminal encoding
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PASS, FAIL, WARN, SKIP = 0, 0, 0, 0
ROOT = Path(__file__).resolve().parent.parent

def ok(msg):
    global PASS
    PASS += 1
    print(f"  ✅  {msg}")

def bad(msg, detail=""):
    global FAIL
    FAIL += 1
    print(f"  ❌  {msg}")
    if detail:
        print(f"      {detail}")

def warn(msg, detail=""):
    global WARN
    WARN += 1
    print(f"  ⚠️  {msg}")
    if detail:
        print(f"      {detail}")

def skip(msg):
    global SKIP
    SKIP += 1
    print(f"  ⬜  {msg}")

# ════════════════════════════════════════════════════════════
print("=" * 60)
print("Medical Review Framework — Smoke Test")
print("=" * 60)

# ── 1. Python version ─────────────────────────────────────
print("\n── 1. Python Environment ──")
py_ver = sys.version_info
if py_ver >= (3, 10):
    ok(f"Python {py_ver.major}.{py_ver.minor}.{py_ver.micro}")
else:
    bad(f"Python {py_ver.major}.{py_ver.minor}.{py_ver.micro} — need 3.10+",
        "Install Python 3.10 or newer: https://python.org/downloads/")

# ── 2. Dependencies ───────────────────────────────────────
print("\n── 2. Dependencies ──")
deps = {
    "yaml": "pip install pyyaml",
    "docx": "pip install python-docx",
    "requests": "pip install requests",
    "PIL": "pip install Pillow",
}
for mod, install_cmd in deps.items():
    try:
        __import__(mod)
        ok(f"{mod}")
    except ImportError:
        bad(f"{mod} — not installed", f"Run: {install_cmd}")

# ── 3. Required files ─────────────────────────────────────
print("\n── 3. Required Files ──")
required = [
    ("config.yaml", "Project configuration"),
    ("state.json", "Progress tracking"),
    ("CLAUDE.md", "Claude Code orchestrator"),
    ("claude/CLAUDE.md", "Agent dispatch reference"),
    ("claude/gates/gates.md", "Gate definitions"),
    ("scripts/verify_gates.py", "Gate verification runner"),
    ("scripts/state.py", "State management"),
    ("scripts/gen_word.py", "Word document generator"),
]
for path, desc in required:
    full = ROOT / path
    if full.exists():
        ok(f"{path} ({desc})")
    else:
        bad(f"{path} — missing ({desc})",
            f"Expected at: {full}")

# ── 4. Config validity ────────────────────────────────────
print("\n── 4. Configuration ──")
try:
    import yaml
    with open(ROOT / "config.yaml", "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if cfg is None:
        bad("config.yaml is empty", "Edit config.yaml with your project settings")
    else:
        ok("config.yaml is valid YAML")
        topic = cfg.get("project", {}).get("topic", "")
        if topic and topic != "Your Review Topic Here":
            ok(f"Topic configured: {topic[:60]}")
        else:
            warn("Topic not configured",
                 'Edit config.yaml → project.topic: "Your Topic Here"')
except Exception as e:
    bad(f"config.yaml error: {e}", "Check config.yaml syntax")

# ── 5. Agent definitions ──────────────────────────────────
print("\n── 5. Agent Definitions ──")
agents_dir = ROOT / "claude" / "agents"
expected_agents = [
    "0-coder", "1-search", "2-analysis", "3-writing",
    "4-review", "5-evaluation", "6-screening", "7-synthesis",
    "8-submission", "peer-review", "sr-systematic-review"
]
found = 0
for name in expected_agents:
    path = agents_dir / f"{name}.md"
    if path.exists():
        found += 1
    else:
        bad(f"Agent {name} — claude/agents/{name}.md not found")
if found == len(expected_agents):
    ok(f"All {found} agent definitions present")
elif found > 0:
    warn(f"{found}/{len(expected_agents)} agent definitions found")

# ── 6. Scripts (syntax check) ─────────────────────────────
print("\n── 6. Script Syntax ──")
scripts_dir = ROOT / "scripts"
py_scripts = sorted(scripts_dir.glob("*.py"))
for script in py_scripts:
    name = script.name
    try:
        with open(script, "r", encoding="utf-8") as f:
            compile(f.read(), name, "exec")
        ok(name)
    except SyntaxError as e:
        bad(f"{name} — syntax error at line {e.lineno}", str(e))

# ── 7. Directory structure ────────────────────────────────
print("\n── 7. Directory Structure ──")
dirs = [
    ("manuscript/", "Your manuscript lives here"),
    ("data/", "Search results and screening data"),
    ("docs/", "Paper notes and methods"),
    ("manuscript/figures/", "Generated figures"),
    ("progress/", "Session logs"),
]
for dirpath, desc in dirs:
    full = ROOT / dirpath
    if full.exists():
        ok(f"{dirpath} ({desc})")
    else:
        warn(f"{dirpath} — not created yet",
             f"Will be created automatically during first run")

# ── 8. Claude Code availability ───────────────────────────
print("\n── 8. Claude Code ──")
import shutil
claude_path = shutil.which("claude")
if claude_path:
    ok(f"claude found: {claude_path}")
else:
    warn("claude command not found in PATH",
         "Install Claude Code: https://docs.anthropic.com/en/docs/claude-code/overview")
    skip("Cannot verify Claude Code version")

# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
total = PASS + FAIL + WARN + SKIP
print(f"  Passed:  {PASS}/{total}")
if FAIL > 0:
    print(f"  Failed:  {FAIL}/{total}  ← fix these first")
if WARN > 0:
    print(f"  Warnings: {WARN}/{total}  ← recommended")
if SKIP > 0:
    print(f"  Skipped: {SKIP}/{total}")

if FAIL == 0:
    print(f"\n  🎉  All checks passed!")
    print(f"  Next: Edit config.yaml → set your topic")
    print(f"        Then run: claude")
    print(f"        Then say: 1  (to begin literature search)")
else:
    print(f"\n  ❌  {FAIL} issue(s) need attention before proceeding.")
    print(f"  See messages above for fix instructions.")

print()
sys.exit(0 if FAIL == 0 else 1)
