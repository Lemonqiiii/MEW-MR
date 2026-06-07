"""Shared configuration loader for all framework scripts.

Reads config.yaml from the project root directory.
Usage:
    from config_loader import load_config
    config = load_config()
    src = config["paths"]["manuscript_src"]
"""

import yaml
from pathlib import Path


def find_project_root():
    """Find the project root by looking for config.yaml upward.

    Searches from current working directory first (supports test projects
    with their own config.yaml), then falls back to the framework location.
    """
    # Priority 1: search from CWD (supports test projects and sub-projects)
    cwd = Path.cwd().resolve()
    current = cwd
    while current != current.parent:
        if (current / "config.yaml").exists():
            return current
        current = current.parent

    # Priority 2: search from script location (framework default)
    script_dir = Path(__file__).resolve().parent
    current = script_dir
    while current != current.parent:
        if (current / "config.yaml").exists():
            return current
        current = current.parent

    raise FileNotFoundError("config.yaml not found from CWD or script location")


def load_config():
    """Load config.yaml from project root."""
    root = find_project_root()
    with open(root / "config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_path(config, key):
    """Resolve a path from config relative to project root."""
    root = find_project_root()
    return str(root / config["paths"][key])
