#!/usr/bin/env python3
"""
Generate a review pack (Disclosure Packet) from a manuscript.

Parses the manuscript and extracts the 6 categories of permitted information.
Outputs to review-pipeline/context/disclosure-packet.md
"""

import re
import sys
import json
from pathlib import Path


def parse_manuscript(filepath):
    """Parse manuscript into structured components."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract title (first substantive line)
    lines = text.strip().split("\n")
    title = ""
    for line in lines:
        cleaned = re.sub(r'^\[\d+\]\[.*?\]\s*', '', line).strip()
        cleaned = re.sub(r'^#+\s*', '', cleaned).strip()
        if cleaned and len(cleaned) > 20:
            title = cleaned
            break

    # Try to identify sections
    sections = []
    current_section = None
    current_content = []

    for line in lines:
        heading_match = re.match(r'^\[\d+\]\[Heading (\d)\]\s*(.+)', line)
        markdown_heading = re.match(r'^(#{1,3})\s+(.+)', line)
        if heading_match or markdown_heading:
            if current_section:
                sections.append({
                    "title": current_section,
                    "content": "\n".join(current_content)
                })
            current_section = heading_match.group(2) if heading_match else markdown_heading.group(2)
            current_content = []
        elif current_section:
            cleaned = re.sub(r'^\[\d+\]\[.*?\]\s*', '', line)
            current_content.append(cleaned)

    if current_section:
        sections.append({
            "title": current_section,
            "content": "\n".join(current_content)
        })

    # Count words (excluding paragraph markers)
    cleaned_text = re.sub(r'^\[\d+\]\[.*?\]\s*', '', text, flags=re.MULTILINE)
    word_count = len(cleaned_text.split())

    # Count references
    ref_count = len(re.findall(r'^\[\d+\]\[Normal\]\s*\[\d+\]', text, re.MULTILINE))
    if ref_count == 0:
        ref_text = text.split("## References", 1)[1] if "## References" in text else text
        ref_count = len(re.findall(r'^\s*\d+\.\s+', ref_text, re.MULTILINE))

    return {
        "title": title,
        "word_count": word_count,
        "sections": sections,
        "reference_count": ref_count
    }


def build_disclosure_packet(parsed, journal="Target Journal"):
    """Build the Disclosure Packet following the 6-category standard."""
    return {
        "category_a": {
            "manuscript_title": parsed["title"],
            "word_count": parsed["word_count"],
            "section_count": len(parsed["sections"]),
            "reference_count": parsed["reference_count"]
        },
        "category_b": {
            "journal": journal,
            "journal_type": "To be inferred from journal requirements",
            "if_range": "To be verified"
        },
        "category_c": {
            "declared_review_type": "To be inferred from manuscript",
            "methodology_standard": "To be selected after review-type detection"
        },
        "category_d": {
            "pico": {
                "population": "To be inferred from manuscript",
                "intervention": "To be inferred from manuscript",
                "comparison": "To be inferred from manuscript",
                "outcome": "To be inferred from manuscript"
            }
        },
        "category_e": {
            "search_strategy": {
                "databases": "To be verified from manuscript",
                "search_date_range": "To be verified from manuscript"
            }
        },
        "category_f": {
            "citation_count": parsed["reference_count"],
            "citation_breakdown": "To be extracted by Agent P"
        }
    }


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('--help', '-h'):
        print("Usage: python3 gen-review-pack.py <manuscript_path> [journal_name]")
        print("  Parses manuscript and generates a disclosure packet (JSON)")
        print("  for the peer review pipeline.")
        sys.exit(0 if len(sys.argv) >= 2 and sys.argv[1] in ('--help', '-h') else 1)

    filepath = sys.argv[1]
    journal = sys.argv[2] if len(sys.argv) > 2 else "Target Journal"

    parsed = parse_manuscript(filepath)
    packet = build_disclosure_packet(parsed, journal)

    output_dir = Path("review-pipeline/context")
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_dir / "disclosure-packet.json", "w", encoding="utf-8") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)

    print(f"Disclosure Packet generated: {output_dir / 'disclosure-packet.json'}")
    print(f"  Manuscript: {parsed['title'][:80]}...")
    print(f"  Words: {parsed['word_count']:,}")
    print(f"  Sections: {len(parsed['sections'])}")
    print(f"  References: {parsed['reference_count']}")


if __name__ == "__main__":
    main()
