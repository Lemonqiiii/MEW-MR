#!/usr/bin/env python3
"""Generate a structured peer review report template from a manuscript.

Reads a manuscript, extracts metadata and structure, and produces a
pre-filled review report template ready for reviewer input.

Usage:
  python3 peer_review.py manuscript/submission.md
  python3 peer_review.py manuscript/submission.md --output my_review.md
  python3 peer_review.py manuscript/submission.md --json  # structured output
"""

import re
import sys
import json
from pathlib import Path
from datetime import datetime


def detect_manuscript_type(text):
    """Auto-detect manuscript type from title and abstract only.

    Only checks the first 1500 characters (title + abstract) to avoid being
    misled by mentions of study designs in the body text of narrative reviews.
    """
    # Check title + abstract only (body text of narrative reviews discusses other study types)
    header = text[:1500].lower()

    # Look for explicit self-identification in title or abstract
    title_line = ""
    for line in text[:500].split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            title_line = line.lower()
            break

    # If title explicitly says "systematic review" or "meta-analysis"
    if "systematic review" in title_line or "meta-analysis" in title_line:
        if "meta-analysis" in title_line:
            return "meta_analysis"
        return "systematic_review"

    # If abstract mentions "systematic review" or "meta-analysis" as the study type
    abstract_section = text[text.find("## Abstract"):text.find("## 1.")] if "## Abstract" in text and "## 1." in text else header
    abstract_lower = abstract_section.lower()

    if "we conducted a systematic review" in abstract_lower or "this systematic review" in abstract_lower:
        return "systematic_review"
    if "we conducted a meta-analysis" in abstract_lower or "this meta-analysis" in abstract_lower:
        return "meta_analysis"

    # For review papers without systematic methodology
    if "narrative review" in title_line or "narrative review" in abstract_lower:
        return "narrative_review"
    if "review" in title_line and "narrative" not in title_line:
        # Could be narrative or systematic — check for PRISMA in methods
        if "prisma" in header or "search strategy" in header or "inclusion criteria" in header:
            return "systematic_review"
        return "narrative_review"

    # Original research
    if any(kw in title_line for kw in ["trial", "cohort", "case-control", "cross-sectional"]):
        return "original_research"

    return "narrative_review"  # Default for review-like content


def extract_sections(text):
    """Extract section headings and word counts."""
    sections = []
    for m in re.finditer(r"^#{1,3}\s+(.+)$", text, re.MULTILINE):
        level = len(m.group(0).split()[0])  # count # symbols
        title = m.group(1)
        start = m.end()
        sections.append({"level": level, "title": title, "start": start})
    # Add word counts between sections
    for i, s in enumerate(sections):
        end = sections[i + 1]["start"] if i + 1 < len(sections) else len(text)
        s["word_count"] = len(re.findall(r"\b\w+\b", text[s["start"] : end]))
    return sections


def extract_references(text):
    """Extract reference list."""
    refs = []
    if "## References" in text:
        ref_section = text.split("## References")[1]
        for m in re.finditer(r"^(\d+)\.\s*(.+)$", ref_section, re.MULTILINE):
            refs.append({"number": int(m.group(1)), "text": m.group(2).strip()[:120]})
    return refs


def count_issues(text):
    """Count potential issues for the reviewer to check."""
    issues = {
        "claims_to_verify": len(re.findall(r"\[\d+(?:,\d+)*\]", text.split("## References")[0] if "## References" in text else text)),
        "sentences": len(re.findall(r"[.!?]+\s", text)),
        "figures": len(re.findall(r"Figure\s+\d+", text)),
        "tables": len(re.findall(r"Table\s+\d+", text)),
    }
    return issues


def generate_template(manuscript_path):
    """Generate a structured peer review report template."""
    with open(manuscript_path, "r", encoding="utf-8") as f:
        text = f.read()

    mtype = detect_manuscript_type(text)
    sections = extract_sections(text)
    refs = extract_references(text)
    stats = count_issues(text)

    # Extract title
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(manuscript_path).stem

    report = {
        "metadata": {
            "manuscript": str(Path(manuscript_path).resolve()),
            "title": title,
            "type": mtype,
            "review_date": datetime.now().isoformat(),
            "total_words": len(re.findall(r"\b\w+\b", text)),
            "reference_count": len(refs),
        },
        "structure": {
            "sections": [{"title": s["title"], "level": s["level"], "words": s["word_count"]} for s in sections],
        },
        "references": refs,
        "stats": stats,
        "review_dimensions": {
            "scientific_validity": {"score": None, "issues": [], "checks": stats["claims_to_verify"]},
            "methodology": {"score": None, "issues": []},
            "data_interpretation": {"score": None, "issues": []},
            "novelty_impact": {"score": None, "issues": []},
            "presentation": {"score": None, "issues": []},
        },
        "recommendation": None,
        "must_fix": [],
        "nice_to_have": [],
    }

    # Add SR-specific dimensions if applicable
    if mtype in ("systematic_review", "meta_analysis"):
        report["review_dimensions"]["sr_specific"] = {
            "prisma_compliance": {"score": None, "items_passed": 0, "items_total": 27},
            "search_strategy": {"score": None, "issues": []},
            "screening_selection": {"score": None, "issues": []},
            "risk_of_bias": {"score": None, "issues": []},
            "synthesis_method": {"score": None, "issues": []},
            "grade_certainty": {"score": None, "issues": []},
            "protocol_fidelity": {"score": None, "issues": []},
        }

    # Add verification items (auto-generated grep checks for common issues)
    report["verification_items"] = generate_verifications(text, refs, report)

    return report


def generate_verifications(text, refs, report):
    """Generate grep-verifiable checks for common manuscript issues."""
    items = []
    body = text.split("## References")[0] if "## References" in text else text

    # V1: All cited references appear in reference list
    body_refs = set()
    for m in re.finditer(r"\[([\d,\s\-–]+)\]", body):
        for part in m.group(1).split(","):
            part = part.strip()
            if "-" in part or "–" in part:
                a, b = re.split(r"[-–]", part)
                try:
                    body_refs.update(range(int(a), int(b) + 1))
                except ValueError:
                    pass
            else:
                try:
                    body_refs.add(int(part))
                except ValueError:
                    pass
    list_nums = {r["number"] for r in refs}
    dangling = sorted(body_refs - list_nums)
    uncited = sorted(list_nums - body_refs)
    if dangling:
        ref_str = ",".join(str(d) for d in dangling[:3])
        items.append({"id": "V-REF-001", "description": f"Dangling references in body: {dangling}", "severity": "MUST_FIX", "command": f"grep -n '[{ref_str}]' manuscript/submission.md", "expected": "No matches (dangling refs removed or added to reference list)"})
    if uncited:
        ref_str = "|".join(str(u) for u in uncited[:3])
        items.append({"id": "V-REF-002", "description": f"Uncited references in list: {uncited}", "severity": "SHOULD_FIX", "command": f"grep -n '^({ref_str})\\.' manuscript/submission.md", "expected": "No matches (uncited refs removed or cited in body)"})

    # V2: No editor placeholders
    placeholders = re.findall(r"\[(To be completed|TBD|待完成)\]", body)
    if placeholders:
        items.append({"id": "V-PH-001", "description": f"Editor placeholders found: {placeholders}", "severity": "MUST_FIX", "command": "grep -n -E 'To be completed|TBD' manuscript/submission.md", "expected": "No matches"})

    # V3: Abstract exists and has minimum length
    if "## Abstract" in text:
        abstract_start = text.find("## Abstract")
        abstract_end = text.find("## ", abstract_start + 10)
        abstract_text = text[abstract_start:abstract_end] if abstract_end > 0 else text[abstract_start:abstract_start + 500]
        abstract_words = len(re.findall(r"\b\w+\b", abstract_text))
        if abstract_words < 50:
            items.append({"id": "V-ABS-001", "description": f"Abstract too short: {abstract_words} words (minimum 50)", "severity": "MUST_FIX", "command": f"grep -c '\\w' manuscript/submission.md # abstract word count was {abstract_words}", "expected": ">=50 words in Abstract"})

    # V4: Figure/table references match available files
    fig_refs = set(re.findall(r"Figure\s+(\d+)", text))
    tab_refs = set(re.findall(r"Table\s+(\d+)", text))
    if fig_refs:
        items.append({"id": "V-FIG-001", "description": f"Figure references in text: {sorted(fig_refs)}", "severity": "SHOULD_FIX", "command": f"ls manuscript/figures/Figure*", "expected": f"Files matching: {sorted(fig_refs)}"})
    if tab_refs:
        items.append({"id": "V-TAB-001", "description": f"Table references in text: {sorted(tab_refs)}", "severity": "SHOULD_FIX", "command": f"ls manuscript/figures/Table*", "expected": f"Files matching: {sorted(tab_refs)}"})

    # V5: No HTML comments left from synthesis/review passes
    if "<!--" in text:
        html_comments = re.findall(r"<!-- (.*?) -->", text)
        if html_comments:
            items.append({"id": "V-HTML-001", "description": f"HTML audit comments remaining: {len(html_comments)}", "severity": "MUST_FIX", "command": "grep -c '<!--' manuscript/submission.md", "expected": "0 HTML comments"})

    return items


def render_markdown(report):
    """Render report as markdown."""
    m = report["metadata"]
    lines = [
        f"# Peer Review Report — {m['title'][:80]}",
        f"",
        f"**Manuscript Type**: {m['type'].replace('_', ' ').title()}",
        f"**Date**: {m['review_date'][:10]}",
        f"**Words**: {m['total_words']} | **References**: {m['reference_count']}",
        f"",
        f"## Overall Assessment",
        f"[To be completed by reviewer]",
        f"",
        f"## Recommendation",
        f"- [ ] Accept",
        f"- [ ] Minor Revision",
        f"- [ ] Major Revision",
        f"- [ ] Reject",
        f"",
        f"## Major Issues (Must Address)",
        f"| # | Section | Issue | Severity | Suggested Fix |",
        f"|---|---------|-------|----------|---------------|",
    ]

    # Auto-detect potential issues
    for i, ref in enumerate(report["references"][:3]):
        lines.append(f"| {i+1} | References | Verify claim-citation match for ref [{ref['number']}] | HIGH | Cross-check abstract |")

    lines += [
        f"",
        f"## Minor Issues (Should Address)",
        f"| # | Section | Issue | Suggestion |",
        f"|---|---------|-------|------------|",
    ]

    lines += [
        f"",
        f"## Dimension Scores",
        f"| Dimension | Score (1-5) | Key Concern |",
        f"|-----------|------------|-------------|",
    ]
    for dim in report["review_dimensions"]:
        if isinstance(report["review_dimensions"][dim], dict) and "score" in report["review_dimensions"][dim]:
            lines.append(f"| {dim.replace('_', ' ').title()} | /5 | |")

    lines += [
        f"",
        f"### Structure Overview",
    ]
    for s in report["structure"]["sections"]:
        indent = "  " * (s["level"] - 1)
        lines.append(f"{indent}- {s['title']} ({s['words']} words)")

    lines += [
        f"",
        f"## References to Verify",
        f"| Ref # | Citation |",
        f"|-------|----------|",
    ]
    for ref in report["references"]:
        lines.append(f"| [{ref['number']}] | {ref['text'][:100]} |")

    lines += [
        f"",
        f"## Verification Checklist (Auto-generated)",
        f"| ID | Check | Severity | Command |",
        f"|----|-------|----------|---------|",
    ]
    for vi in report.get("verification_items", []):
        lines.append(f"| {vi['id']} | {vi['description'][:60]} | {vi['severity']} | `{vi['command'][:50]}...` |")
    lines += [
        f"",
        f"Run `python3 scripts/verify_gates.py --check-revision manuscript/peer_review_report.md` to auto-verify.",
        f"",
        f"## Language Quality Assessment",
        f"[To be completed by reviewer — apply claude/disciplines/language-naturalness.md]",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Generate peer review report template from manuscript")
    p.add_argument("manuscript", help="Path to manuscript file")
    p.add_argument("--output", "-o", help="Output report path (default: manuscript/peer_review_report.md)")
    p.add_argument("--json", action="store_true", help="Output structured JSON instead of markdown")
    args = p.parse_args()

    report = generate_template(args.manuscript)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        output = render_markdown(report)
        out_path = args.output or "manuscript/peer_review_report.md"
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Peer review template: {out_path}")
        print(f"  Type: {report['metadata']['type']}")
        print(f"  Words: {report['metadata']['total_words']}")
        print(f"  References: {report['metadata']['reference_count']}")
        print(f"  Sections: {len(report['structure']['sections'])}")
