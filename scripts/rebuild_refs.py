#!/usr/bin/env python3
"""Deprecated legacy reference-rebuild entry point.

The previous version of this script was tied to an archived manuscript and
contained a hard-coded reference list. Reference rebuilding must now be done
with a topic-specific script that accepts an explicit manuscript path and
reference source.
"""
raise SystemExit(
    "scripts/rebuild_refs.py is deprecated. Create a topic-specific reference "
    "rebuild script that accepts explicit input/output paths."
)
