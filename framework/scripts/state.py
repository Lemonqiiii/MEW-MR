#!/usr/bin/env python3
"""Read and update project state (state.json).

Usage:
  python3 state.py                           # Print current state
  python3 state.py get project.phase          # Get a specific key
  python3 state.py set project.phase "writing" # Set a specific key
  python3 state.py set metrics.words_written 2500
  python3 state.py gate 4 pass                # Mark gate as passed
  python3 state.py gate 4 fail                # Mark gate as failed
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = ROOT / "state.json"


def load():
    if STATE_PATH.exists():
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(state):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def get_nested(data, path):
    keys = path.split(".")
    current = data
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return None
    return current


def set_nested(data, path, value):
    keys = path.split(".")
    current = data
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
    # Try to convert value to appropriate type
    try:
        if "." in str(value):
            current[keys[-1]] = float(value)
        else:
            current[keys[-1]] = int(value)
    except (ValueError, TypeError):
        current[keys[-1]] = value
    return data


def main():
    if len(sys.argv) < 2:
        state = load()
        print(json.dumps(state, indent=2, ensure_ascii=False))
        return

    cmd = sys.argv[1]

    if cmd == "get":
        if len(sys.argv) < 3:
            print("Usage: python3 state.py get <key.path>")
            sys.exit(1)
        state = load()
        val = get_nested(state, sys.argv[2])
        if val is not None:
            print(json.dumps(val, indent=2, ensure_ascii=False) if isinstance(val, (dict, list)) else val)
        else:
            print(f"null (key not found: {sys.argv[2]})")
            sys.exit(1)

    elif cmd == "set":
        if len(sys.argv) < 4:
            print("Usage: python3 state.py set <key.path> <value>")
            sys.exit(1)
        state = load()
        state = set_nested(state, sys.argv[2], sys.argv[3])
        state["project"]["last_updated"] = datetime.now().isoformat()
        save(state)
        print(f"Set {sys.argv[2]} = {sys.argv[3]}")

    elif cmd == "gate":
        if len(sys.argv) < 4:
            print("Usage: python3 state.py gate <N> <pass|fail>")
            sys.exit(1)
        gate_id = sys.argv[2]
        gate_status = sys.argv[3]
        state = load()
        if "gates" not in state:
            state["gates"] = {}
        state["gates"][gate_id] = {
            "status": "passed" if gate_status == "pass" else "failed",
            "last_run": datetime.now().isoformat(),
        }
        state["project"]["last_updated"] = datetime.now().isoformat()
        save(state)
        print(f"Gate {gate_id}: {gate_status.upper()}")

    else:
        print(f"Unknown command: {cmd}")
        print("Commands: get, set, gate")
        sys.exit(1)


if __name__ == "__main__":
    main()
