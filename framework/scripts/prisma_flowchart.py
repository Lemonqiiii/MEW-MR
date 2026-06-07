#!/usr/bin/env python3
"""Generate PRISMA 2020 flowchart data from screening records.

Reads the screening output files and produces the standard PRISMA flowchart
numbers and a markdown template.

Usage:
  python3 scripts/prisma_flowchart.py           # Generate from current data
  python3 scripts/prisma_flowchart.py --json    # Output as JSON
  python3 scripts/prisma_flowchart.py --markdown # Output as markdown table
"""

import json
import sys
from pathlib import Path
from config_loader import load_config, find_project_root

ROOT = find_project_root()
CONFIG = load_config()
DATA_DIR = ROOT / CONFIG["paths"]["data_dir"]


def count_papers(filepath):
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return len(data)
        elif isinstance(data, dict):
            return len(data.get("papers", data.get("results", [])))
    return 0


def build_prisma():
    """Build PRISMA 2020 flowchart numbers from actual data files."""
    prisma = {}

    # Identification
    search_results = count_papers(DATA_DIR / "pubmed_search_results.json")
    # Try to read merged search results if available
    merged = DATA_DIR / "pubmed_merged_all.json"
    if merged.exists():
        total_identified = count_papers(merged)
        # If merged exists, use it as total; search_results as one source
        prisma["databases_searched"] = 3  # PubMed + S2 + EPMC minimum
        prisma["records_identified_databases"] = total_identified
        prisma["records_identified_registers"] = count_papers(
            DATA_DIR / "clinicaltrials_export.json"
        )
    else:
        prisma["records_identified_databases"] = search_results
        prisma["records_identified_registers"] = 0

    prisma["total_identified"] = (
        prisma["records_identified_databases"]
        + prisma["records_identified_registers"]
    )

    # Screening — duplicate removal
    # Estimate duplicates: if we have both search_results and merged, diff is approx duplicates
    relevant = DATA_DIR / "pubmed_relevant_for_screening.json"
    if relevant.exists():
        prisma["records_after_dedup"] = count_papers(relevant)
    else:
        prisma["records_after_dedup"] = prisma["total_identified"]  # assume no dupe file

    prisma["duplicates_removed"] = (
        prisma["total_identified"] - prisma["records_after_dedup"]
    )

    # Screening — title/abstract
    prisma["records_screened"] = prisma["records_after_dedup"]
    excluded_file = DATA_DIR / "screening_excluded.json"
    prisma["records_excluded_title_abstract"] = count_papers(excluded_file)

    # Full-text retrieval
    included_after_screening = (
        prisma["records_screened"] - prisma["records_excluded_title_abstract"]
    )
    prisma["full_text_sought"] = included_after_screening

    # Check for unavailable full-text
    unavailable = sum(
        1
        for p in _load_json(DATA_DIR / "screening_final_included.json")
        if p.get("full_text_available") is False
    )
    prisma["full_text_not_retrieved"] = unavailable
    prisma["full_text_assessed"] = included_after_screening - unavailable

    # Final inclusion
    final = DATA_DIR / "screening_final_included.json"
    if final.exists():
        prisma["studies_included"] = count_papers(final)
        prisma["full_text_excluded"] = (
            prisma["full_text_assessed"] - prisma["studies_included"]
        )
    else:
        prisma["studies_included"] = 0
        prisma["full_text_excluded"] = 0

    # Meta-analysis eligibility (subset of included)
    prisma["studies_in_meta_analysis"] = 0  # determined post-extraction

    return prisma


def _load_json(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    return []


def render_markdown(prisma):
    """Render PRISMA flowchart as markdown."""
    return f"""## PRISMA 2020 Flow Diagram

### Identification
- Records identified from databases (n = {prisma['records_identified_databases']})
- Records identified from registers (n = {prisma['records_identified_registers']})
- **Total records identified (n = {prisma['total_identified']})**

### Screening
- Duplicate records removed (n = {prisma['duplicates_removed']})
- Records after deduplication (n = {prisma['records_after_dedup']})
- Records screened by title/abstract (n = {prisma['records_screened']})
- Records excluded (n = {prisma['records_excluded_title_abstract']})

### Retrieval
- Reports sought for retrieval (n = {prisma['full_text_sought']})
- Reports not retrieved (n = {prisma['full_text_not_retrieved']})
- Reports assessed for eligibility (n = {prisma['full_text_assessed']})

### Inclusion
- Reports excluded with reasons (n = {prisma['full_text_excluded']})
- **Studies included in review (n = {prisma['studies_included']})**
- Studies included in meta-analysis (n = {prisma['studies_in_meta_analysis']})
"""


def render_ascii_flowchart(prisma):
    """Render PRISMA flowchart as ASCII art."""
    return f"""
IDENTIFICATION
  Records from databases (n={prisma['records_identified_databases']})
  Records from registers  (n={prisma['records_identified_registers']})
                           ───────────────
  Total identified         (n={prisma['total_identified']})
                              │
                              ▼
SCREENING                 Duplicates removed (n={prisma['duplicates_removed']})
                           ───────────────
  After dedup             (n={prisma['records_after_dedup']})
                              │
                              ▼
  Title/abstract screened  (n={prisma['records_screened']})
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
              Excluded             Sought for retrieval
          (n={prisma['records_excluded_title_abstract']})    (n={prisma['full_text_sought']})
                                        │
                              ┌─────────┴─────────┐
                              │                   │
                              ▼                   ▼
                        Not retrieved       Full-text assessed
                    (n={prisma['full_text_not_retrieved']})  (n={prisma['full_text_assessed']})
                                                  │
                                        ┌─────────┴─────────┐
                                        │                   │
                                        ▼                   ▼
                                  Excluded with       STUDIES INCLUDED
                                  reasons             (n={prisma['studies_included']})
                                  (n={prisma['full_text_excluded']})         │
                                                             ┌─────────┴─────────┐
                                                             │                   │
                                                             ▼                   ▼
                                                       In qualitative      In quantitative
                                                       synthesis           synthesis (meta-analysis)
                                                       (n={prisma['studies_included']})  (n={prisma['studies_in_meta_analysis']})
"""


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Generate PRISMA 2020 flowchart")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.add_argument("--markdown", action="store_true", help="Output as markdown")
    p.add_argument("--ascii", action="store_true", help="Output as ASCII art")
    p.add_argument("--output", "-o", help="Write to file")
    args = p.parse_args()

    prisma = build_prisma()

    if args.json:
        output = json.dumps(prisma, indent=2, ensure_ascii=False)
    elif args.ascii:
        output = render_ascii_flowchart(prisma)
    else:  # default: markdown
        output = render_markdown(prisma)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Written: {args.output}")
    else:
        print(output)
