#!/usr/bin/env python3
"""
稿件结构检查脚本

Checklist:
- 章节完整性
- 引用格式一致性
- 字数统计
- 引用密度
"""

import re
import sys
import io

# Fix Windows GBK encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def analyze_manuscript(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")

    # 字数统计
    words = len(text.split())
    chars = len(text)

    # 章节统计
    sections = re.findall(r'^#{1,3}\s+(.+)$', text, re.MULTILINE)

    # 引用统计
    ref_section = text.split("## References")[-1] if "## References" in text else ""
    refs = re.findall(r'^(\d+)\.\s', ref_section, re.MULTILINE)

    # 文中引用标记
    citation_markers = re.findall(r'\[[\d,\-–\s]+\]', text.split("## References")[0] if "## References" in text else text)

    print(f"[Structure Report] Manuscript Analysis")
    print(f"=" * 50)
    print(f"File: {filepath}")
    print(f"Word count: {words:,}")
    print(f"Character count: {chars:,}")
    print(f"Line count: {len(lines):,}")
    print(f"")
    print(f"[Sections] ({len(sections)} sections):")
    for s in sections:
        indent = "  " * (s.count("#") - 1) if s.startswith("#") else ""
        print(f"  {indent}- {s.strip('#').strip()}")
    print(f"")
    print(f"[Citations]:")
    print(f"  Total references: {len(refs)}")
    print(f"  In-text citation markers: {len(citation_markers)}")
    print(f"  Citation density: {len(citation_markers) / max(words/1000, 1):.1f} per 1k words")
    print(f"")

    # Check issues
    issues = []

    # Check reference number continuity
    ref_nums = [int(r) for r in refs]
    if ref_nums:
        expected = list(range(1, max(ref_nums) + 1))
        missing = set(expected) - set(ref_nums)
        if missing:
            issues.append(f"[!] Non-contiguous reference numbers, missing: {sorted(missing)}")

    if not refs:
        issues.append("[!] No reference list found")

    if not sections:
        issues.append("[!] No section structure detected")

    if issues:
        print("[Issues Found]:")
        for i in issues:
            print(f"  {i}")
    else:
        print("[OK] No obvious structure issues found")

    return {"words": words, "sections": len(sections), "refs": len(refs), "issues": issues}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check-structure.py <manuscript_path>")
        sys.exit(1)
    analyze_manuscript(sys.argv[1])
