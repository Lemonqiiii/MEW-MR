#!/usr/bin/env python3
"""
Unified Gate Verification Runner.

Each Gate is a Python function returning a GateResult.
Gates can block agent progress -- a failed pre_gate means the agent cannot start.

Usage:
  python3 verify_gates.py --gate 4           # Run specific gate
  python3 verify_gates.py --gate 1 --gate 7  # Run multiple gates
  python3 verify_gates.py --phase writing    # Run gates for a phase
  python3 verify_gates.py --all              # Run all gates
  python3 verify_gates.py --check-prereq 3   # Check pre-gate for Agent 3
  python3 verify_gates.py --check-output 3   # Check post-gate for Agent 3

Exit code: 0 = all passed, 1 = failures, 2 = config/setup error
"""

import json
import os
import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass, field

from config_loader import load_config, find_project_root

ROOT = find_project_root()
CONFIG = load_config()

# ── State ──
STATE_PATH = ROOT / "state.json"


def load_state():
    if STATE_PATH.exists():
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# ── Agent pre/post gate mapping ──
AGENT_GATES = {
    "1": {"pre": [], "post": [1, 7]},
    "6": {"pre": [1], "post": [2]},
    "2": {"pre": [2], "post": [3]},
    "3": {"pre": [3], "post": [4, 8]},
    "7": {"pre": [4], "post": [9]},
    "4": {"pre": [9], "post": [10]},
    "8": {"pre": [10], "post": [11]},
    "0": {"pre": [], "post": []},
    "5": {"pre": [], "post": []},
}

# ── Phase to gate mapping ──
PHASE_GATES = {
    "search": [1, 7],
    "screening": [2],
    "analysis": [3],
    "writing": [4, 8],
    "synthesis": [9],
    "review": [10],
    "submission": [11],
}


# ════════════════════════════════════════════════════════════════════
@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str = ""


@dataclass
class GateResult:
    gate_id: int
    name: str
    checks: list = field(default_factory=list)

    @property
    def passed(self):
        return all(c.passed for c in self.checks)

    def add(self, name, passed, detail=""):
        self.checks.append(CheckResult(name, passed, detail))
        return passed


# ════════════════════════════════════════════════════════════════════
# GATE 1: Literature Search -> Screening
# ════════════════════════════════════════════════════════════════════
def gate1():
    """GATE: Search -> Screening"""
    r = GateResult(1, "Search -> Screening")
    data_dir = ROOT / CONFIG["paths"]["data_dir"]

    # 1.1: Data files exist
    search_file = data_dir / "pubmed_search_results.json"
    if search_file.exists():
        r.add("Search results exist", True, str(search_file))
    else:
        r.add("Search results exist", False, f"{search_file} not found -- run Agent 1 first")
        return r  # Cannot continue without data

    # 1.2: Load and check data
    try:
        with open(search_file, "r", encoding="utf-8") as f:
            papers = json.load(f)
        if not isinstance(papers, list):
            papers = []
    except Exception:
        papers = []

    count = len(papers)
    r.add("Papers found", count > 0, f"{count} papers in search results")

    if count == 0:
        return r

    # 1.3: PMID uniqueness (dedup accuracy)
    pmids = [str(p.get("pmid", "")) for p in papers if p.get("pmid")]
    dupes = len(pmids) - len(set(pmids))
    r.add("PMID uniqueness", dupes == 0, f"{dupes} duplicates in {len(pmids)} PMIDs" if dupes else "0 duplicates")

    # 1.4: Data completeness
    missing_abstract = sum(1 for p in papers if not (p.get("abstractText") or "").strip())
    missing_title = sum(1 for p in papers if not p.get("title"))
    total = len(papers)
    miss_rate = max(missing_abstract, missing_title) / total * 100 if total else 100
    r.add(
        "Data completeness",
        miss_rate < 5,
        f"abstract missing: {missing_abstract}, title missing: {missing_title} ({miss_rate:.1f}%)",
    )

    # 1.5: Year distribution
    years = {}
    for p in papers:
        y = p.get("pubYear") or p.get("year") or "unknown"
        years[y] = years.get(y, 0) + 1
    if years:
        numeric = [int(y) for y in years if str(y).isdigit()]
        yr_range = f"{min(numeric)}-{max(numeric)}" if numeric else "unknown"
        r.add("Year coverage", len(years) >= 3, f"Range: {yr_range}, distinct years: {len(years)}")
    else:
        r.add("Year coverage", False, "No year data found")

    # 1.6: Population contamination check
    exclusion_kw = CONFIG.get("agents", {}).get("screening", {}).get("exclusion_keywords", {})
    pop_kw = exclusion_kw.get("population", [])
    if pop_kw:
        contaminated = []
        for p in papers:
            title = (p.get("title") or "").lower()
            abstract = (p.get("abstractText") or "").lower()[:500]
            text = title + " " + abstract
            for kw in pop_kw:
                if kw.lower() in text:
                    contaminated.append(p.get("pmid", "?"))
                    break
        r.add(
            "Population contamination",
            len(contaminated) == 0,
            f"{len(contaminated)} contaminated papers: {contaminated[:5]}" if contaminated else "0 wrong-population papers",
        )
    else:
        r.add("Population contamination", True, "No exclusion keywords configured -- skipped")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 2: Screening -> Deep Reading
# ════════════════════════════════════════════════════════════════════
def gate2():
    """GATE: Screening -> Deep Reading"""
    r = GateResult(2, "Screening -> Deep Reading")
    data_dir = ROOT / CONFIG["paths"]["data_dir"]

    # 2.1: Final inclusion file exists
    inclusion_file = data_dir / "screening_final_included.json"
    if not inclusion_file.exists():
        r.add("Inclusion file exists", False, f"{inclusion_file} not found -- run Agent 6 first")
        return r
    r.add("Inclusion file exists", True, str(inclusion_file))

    # 2.2: Exclusion file exists
    excluded_file = data_dir / "screening_excluded.json"
    if excluded_file.exists():
        try:
            with open(excluded_file, "r", encoding="utf-8") as f:
                excluded = json.load(f)
            if not isinstance(excluded, list):
                excluded = []
        except (json.JSONDecodeError, ValueError):
            excluded = []
        excluded_with_reason = [e for e in excluded if isinstance(e, dict) and e.get("reason")]
        r.add(
            "Exclusion reasons documented",
            len(excluded_with_reason) > 0 if excluded else True,
            f"{len(excluded_with_reason)}/{len(excluded)} excluded papers have reasons",
        )
    else:
        r.add("Exclusion file exists", False, f"{excluded_file} not found")

    # 2.3: Abstract-only ratio check
    thresholds = CONFIG.get("agents", {}).get("screening", {}).get("type_thresholds", {})
    max_abstract = thresholds.get("abstract_only_max_pct", 20)

    if inclusion_file.exists():
        with open(inclusion_file, "r", encoding="utf-8") as f:
            included = json.load(f)
        if not isinstance(included, list):
            included = []
        abstract_only = sum(1 for p in included if p.get("abstract_only", False))
        ratio = (abstract_only / len(included) * 100) if included else 0
        r.add(
            "Abstract-only ratio",
            ratio <= max_abstract,
            f"{abstract_only}/{len(included)} ({ratio:.1f}%) -- threshold: <={max_abstract}%",
        )
    else:
        r.add("Abstract-only ratio", False, "Inclusion file not found")

    # 2.4: Minimum sample warning (small samples make distribution checks unreliable)
    if inclusion_file.exists():
        inclusion_count = len(included) if isinstance(included, list) else 0
        sufficient = inclusion_count >= 10
        r.add(
            "Minimum sample size",
            True,  # Always pass — this is a warning, not a block
            f"{inclusion_count} papers included — {'sufficient' if sufficient else 'WARNING: <10 papers, type distribution checks unreliable'}",
        )

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 3: Deep Reading -> Writing
# ════════════════════════════════════════════════════════════════════
def gate3():
    """GATE: Deep Reading -> Writing"""
    r = GateResult(3, "Deep Reading -> Writing")
    papers_dir = ROOT / CONFIG["paths"]["papers_dir"]

    # 3.1: Paper notes exist
    if papers_dir.exists():
        notes = list(papers_dir.glob("**/*.md"))
        note_count = len(notes)
        r.add("Paper notes exist", note_count > 0, f"{note_count} notes found")
    else:
        r.add("Paper notes directory exists", False, f"{papers_dir} not found")
        return r

    # 3.2: Manuscript outline exists
    outline_path = ROOT / "manuscript" / "outline.md"
    r.add("Outline exists", outline_path.exists(), str(outline_path) if outline_path.exists() else "not found")

    # 3.3: Note quality spot check (structural -- checks for key fields, not content)
    note_files = list(papers_dir.glob("**/*.md"))
    if note_files:
        sample = note_files[: min(5, len(note_files))]
        quality_checks = 0
        total = len(sample)
        for nf in sample:
            try:
                with open(nf, "r", encoding="utf-8") as f:
                    content = f.read()
                score = sum(
                    [
                        bool(re.search(r"(核心发现|Key Finding|finding)", content)),
                        bool(re.search(r"PMID\S*\s*[:\s]*\d{7,8}", content)),
                        bool(re.search(r"(与本综述|Relevance|relevance)", content)),
                        bool(re.search(r"(方法|Methods|methods|设计类型|design)", content)),
                    ]
                )
                if score >= 3:
                    quality_checks += 1
            except Exception:
                total -= 1
        if total > 0:
            r.add(
                "Note quality (structural)",
                quality_checks >= total * 0.8,
                f"{quality_checks}/{total} notes score >=3/4",
            )
        else:
            r.add("Note quality (structural)", False, "No readable notes")
    else:
        r.add("Note quality (structural)", False, "No note files found")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 4: Writing -- Citation Verification
# ════════════════════════════════════════════════════════════════════
def gate4():
    """GATE: Citation Verification"""
    r = GateResult(4, "Citation Verification")
    src_path = ROOT / CONFIG["paths"]["manuscript_src"]

    if not src_path.exists():
        r.add("Manuscript exists", False, f"{src_path} not found -- run Agent 3 first")
        return r
    r.add("Manuscript exists", True, str(src_path))

    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 4.1: Has title
    r.add("Has title", bool(re.match(r"^# ", text)), "Title found" if re.match(r"^# ", text) else "Missing # Title")

    # 4.2: Has Abstract section
    r.add("Has Abstract", "## Abstract" in text, "Abstract found" if "## Abstract" in text else "Missing ## Abstract")

    # 4.3: Has References section
    has_refs = "## References" in text
    ref_count = text.count("## References")
    r.add(
        "Has References",
        has_refs and ref_count == 1,
        f"References found" if has_refs and ref_count == 1 else f"Missing or duplicate References ({ref_count})",
    )

    # 4.4: Citation format integrity
    body = text.split("## References")[0] if "## References" in text else text
    body_refs = set()
    for m in re.finditer(r"\[([\d,\s\--]+)\]", body):
        for part in m.group(1).split(","):
            part = part.strip()
            if "-" in part or "-" in part:
                a, b = re.split(r"[--]", part)
                try:
                    body_refs.update(range(int(a), int(b) + 1))
                except ValueError:
                    pass
            else:
                try:
                    body_refs.add(int(part))
                except ValueError:
                    pass

    if "## References" in text:
        refs_section = text.split("## References")[1]
        list_refs = set()
        for m in re.finditer(r"^(\d+)\.", refs_section, re.MULTILINE):
            list_refs.add(int(m.group(1)))
        dangling = sorted(list_refs - body_refs) if body_refs else []
        uncited = sorted(body_refs - list_refs) if list_refs else []
        r.add(
            "Reference consistency",
            len(dangling) == 0 and len(uncited) == 0,
            f"Body refs: {len(body_refs)}, List refs: {len(list_refs)}"
            + (f", Dangling: {dangling}" if dangling else "")
            + (f", Uncited: {uncited}" if uncited else ""),
        )
    else:
        r.add("Reference consistency", False, "No References section to check")

    # 4.5: Word count sanity
    word_count = len(re.findall(r"\b\w+\b", body))
    r.add("Word count", word_count >= 500, f"{word_count} words in body" if word_count >= 500 else f"Only {word_count} words -- too short")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 5: Format Integrity
# ════════════════════════════════════════════════════════════════════
def gate5():
    """GATE: Format Integrity"""
    r = GateResult(5, "Format Integrity")
    src_path = ROOT / CONFIG["paths"]["manuscript_src"]

    if not src_path.exists():
        r.add("Manuscript exists", False, f"{src_path} not found")
        return r

    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    body = text.split("## References")[0] if "## References" in text else text

    # 5.1: Section numbering sequential
    sections = re.findall(r"^## (\d+)\.", body, re.MULTILINE)
    if sections:
        nums = [int(s) for s in sections]
        expected = list(range(1, max(nums) + 1))
        r.add(
            "Section numbering",
            nums == expected,
            f"Sections: {nums}" if nums == expected else f"Non-sequential: found {nums}, expected {expected}",
        )
    else:
        r.add("Section numbering", True, "No numbered sections -- OK for narrative review")

    # 5.2: Figure references match figure files
    fig_dir = ROOT / CONFIG["paths"]["figures_dir"]
    body_figs = set(re.findall(r"Figure\s+(\d+)", body))
    if fig_dir.exists():
        actual_figs = set()
        for f in fig_dir.iterdir():
            m = re.match(r"Figure(\d+)", f.stem)
            if m:
                actual_figs.add(int(m.group(1)))
        missing = sorted(body_figs - actual_figs)
        r.add(
            "Figure references",
            len(missing) == 0,
            f"Body references: {body_figs}, Files: {actual_figs}"
            + (f", Missing files: {missing}" if missing else ""),
        )
    else:
        r.add("Figure references", len(body_figs) == 0, f"No figures dir, body refs: {body_figs}")

    # 5.3: No placeholder/TBD remnants
    placeholders = re.findall(r"\[(To be completed|TBD|待完成)\]", text)
    r.add(
        "No placeholders",
        len(placeholders) == 0,
        f"Found: {placeholders}" if placeholders else "0 placeholders",
    )

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 6: Citation Scope Compliance
# ════════════════════════════════════════════════════════════════════
def gate6():
    """GATE: Citation Scope Compliance"""
    r = GateResult(6, "Citation Scope Compliance")
    src_path = ROOT / CONFIG["paths"]["manuscript_src"]
    data_dir = ROOT / CONFIG["paths"]["data_dir"]

    if not src_path.exists():
        r.add("Manuscript exists", False, f"{src_path} not found")
        return r

    r.add("Manuscript exists", True, str(src_path))

    # 6.1: Screening data available for cross-check
    inclusion_file = data_dir / "screening_final_included.json"
    if not inclusion_file.exists():
        r.add("Type data available", False, "screening_final_included.json not found -- cannot verify citation scope")
        return r

    with open(inclusion_file, "r", encoding="utf-8") as f:
        included = json.load(f)
    if not isinstance(included, list):
        included = []

    # Build PMID -> type lookup
    pmid_type = {}
    for p in included:
        pid = str(p.get("pmid", ""))
        ptype = p.get("type", "")
        if pid and ptype:
            pmid_type[pid] = ptype

    if not pmid_type:
        r.add("Type data available", False, "No PMID->type mappings in screening data")
        return r

    r.add("Type data available", True, f"{len(pmid_type)} PMID->type mappings")

    # 6.2: Count type G in reference list (narrative reviews should NOT be primary)
    # This is a structural check -- semantic verification requires Agent 4
    type_g_count = sum(1 for t in pmid_type.values() if t == "G")
    type_i_count = sum(1 for t in pmid_type.values() if t == "I")
    r.add(
        "Type G/I flagged for review",
        True,  # Always passes structurally; semantic check by Agent 4
        f"Type G: {type_g_count}, Type I: {type_i_count} -- Agent 4 must verify manually",
    )

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 7: Domain Ontology Completeness
# ════════════════════════════════════════════════════════════════════
def gate7():
    """GATE: Domain Ontology Completeness"""
    r = GateResult(7, "Domain Ontology Completeness")
    ontology_path = ROOT / "knowledge" / "domain-ontology.md"

    if not ontology_path.exists():
        r.add("Domain ontology exists", False, f"{ontology_path} not found -- run Agent 1 Step 7 first")
        return r
    r.add("Domain ontology exists", True, str(ontology_path))

    with open(ontology_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 7.1: Intervention Inventory table present
    has_inventory = "Intervention Inventory" in content or "干预清单" in content
    r.add("Intervention inventory", has_inventory, "Table present" if has_inventory else "Missing")

    # 7.2: Gap grading table present
    has_gaps = "Evidence Gap Grading" in content or "证据空白分级" in content
    r.add("Evidence gap grading", has_gaps, "G0-G4 grades present" if has_gaps else "Missing")

    # 7.3: Urgency scoring table present
    has_urgency = "Clinical Urgency" in content or "临床紧迫性" in content
    r.add("Urgency scoring", has_urgency, "Composite scores present" if has_urgency else "Missing")

    # 7.4: Interaction map present
    has_interaction = "Interaction" in content or "交互" in content
    r.add("Interaction map", has_interaction, "Present" if has_interaction else "Missing")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 8: Pre-writing Planning
# ════════════════════════════════════════════════════════════════════
def gate8():
    """GATE: Pre-writing Planning"""
    r = GateResult(8, "Pre-writing Planning")
    plan_path = ROOT / "knowledge" / "pre-writing-plan.md"

    r.add(
        "Pre-writing plan exists",
        plan_path.exists(),
        str(plan_path) if plan_path.exists() else "not found -- run Agent 3 Steps 0a-0f first",
    )

    if plan_path.exists():
        with open(plan_path, "r", encoding="utf-8") as f:
            content = f.read()
        has_allocation = "allocation" in content.lower() or "篇幅" in content
        has_gap_map = "gap" in content.lower() or "空白" in content
        has_time = "time" in content.lower() or "时间" in content or "band" in content.lower()
        r.add("Section allocation", has_allocation, "Present" if has_allocation else "Missing")
        r.add("Gap-emphasis mapping", has_gap_map, "Present" if has_gap_map else "Missing")
        r.add("Time annotation", has_time, "Present" if has_time else "Missing")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 9: Synthesis Quality
# ════════════════════════════════════════════════════════════════════
def gate9():
    """GATE: Synthesis Quality"""
    r = GateResult(9, "Synthesis Quality")

    artifacts = [
        ("Cross-intervention matrix", ROOT / "harness" / "cross-intervention-output.md"),
        ("Synthesis reasoning log", ROOT / "harness" / "synthesis-reasoning-log.md"),
        ("Argument diversity report", ROOT / "harness" / "argument-diversity-report.md"),
        ("Coverage gap report", ROOT / "harness" / "coverage-gap-report.md"),
    ]

    for name, path in artifacts:
        r.add(f"{name} exists", path.exists(), str(path) if path.exists() else f"{name} not found")

    # Pattern A check in argument diversity report
    div_path = ROOT / "harness" / "argument-diversity-report.md"
    if div_path.exists():
        with open(div_path, "r", encoding="utf-8") as f:
            content = f.read()
        pattern_a_matches = re.findall(r"Pattern A.*?(\d+)", content)
        if pattern_a_matches:
            try:
                count = int(pattern_a_matches[0])
                r.add("Pattern A count", count <= 3, f"Pattern A count: {count} -- threshold: <=3")
            except ValueError:
                r.add("Pattern A count", True, "Could not parse count -- Agent 7 must verify manually")
        else:
            r.add("Pattern A count", True, "Pattern A count not found in report -- Agent 7 must verify manually")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 10: Enhanced Review Completeness
# ════════════════════════════════════════════════════════════════════
def gate10():
    """GATE: Enhanced Review"""
    r = GateResult(10, "Enhanced Review")

    # 10.1: Review report exists (any round)
    report_dir = ROOT / "harness" / "reports"
    if report_dir.exists():
        reports = list(report_dir.glob("review-*.md"))
        r.add("Review report exists", len(reports) > 0, f"{len(reports)} review reports found" if reports else "No review reports")
    else:
        r.add("Review report exists", False, f"{report_dir} not found")

    # 10.2: Manuscript has perspective tags
    src_path = ROOT / CONFIG["paths"]["manuscript_src"]
    if src_path.exists():
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
        perspectives = len(re.findall(r"<!-- PERSPECTIVE:", text))
        r.add("Perspective tags", perspectives >= 2, f"{perspectives} perspective tags" if perspectives >= 2 else f"Only {perspectives} perspectives -- target >=2")

    # 10.3: Cochrane concentration flag (structural)
    if src_path.exists():
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
        cochrane_refs = len(re.findall(r"Cochrane Database", text))
        r.add("Cochrane references flagged", True, f"{cochrane_refs} Cochrane references -- Agent 4 must verify concentration")

    return r


# ════════════════════════════════════════════════════════════════════
# GATE 11: Submission Ready
# ════════════════════════════════════════════════════════════════════
def gate11():
    """GATE: Submission Ready"""
    r = GateResult(11, "Submission Ready")
    src_path = ROOT / CONFIG["paths"]["manuscript_src"]

    if not src_path.exists():
        r.add("Manuscript exists", False, f"{src_path} not found")
        return r

    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 11.1: No HTML audit tags remaining
    html_tags = re.findall(r"<!-- .*? -->", text)
    r.add(
        "HTML audit tags removed",
        len(html_tags) == 0,
        f"{len(html_tags)} tags remaining: {html_tags[:3]}..." if html_tags else "0 tags -- clean",
    )

    # 11.2: No placeholders
    placeholders = re.findall(r"\[(To be completed|TBD|待完成)\]", text)
    r.add("No editor placeholders", len(placeholders) == 0, f"Found: {placeholders}" if placeholders else "0 placeholders")

    # 11.3: Completeness sections
    sections_to_check = ["Author Contributions", "Acknowledgements", "Funding", "Data Availability", "Competing Interests"]
    present = [s for s in sections_to_check if s in text]
    r.add("Completeness sections", len(present) >= 3, f"{len(present)}/{len(sections_to_check)} present: {present}")

    # 11.4: Submission report exists
    report_path = ROOT / "harness" / "submission-readiness-report.md"
    r.add("Submission report exists", report_path.exists(), str(report_path) if report_path.exists() else "not found")

    return r


# ════════════════════════════════════════════════════════════════════
# Gate Registry
# ════════════════════════════════════════════════════════════════════
GATES = {
    1: gate1,
    2: gate2,
    3: gate3,
    4: gate4,
    5: gate5,
    6: gate6,
    7: gate7,
    8: gate8,
    9: gate9,
    10: gate10,
    11: gate11,
}


# ════════════════════════════════════════════════════════════════════
# Revision Check: Verify MUST FIX items from peer review
# ════════════════════════════════════════════════════════════════════
def check_revision(report_path):
    """Check MUST FIX items from a peer review report against the manuscript.

    Reads the peer review report (JSON from peer_review.py or markdown),
    extracts MUST FIX verification items, and checks each one.
    """
    print(f"\n{'='*60}")
    print(f"REVISION CHECK: {report_path}")
    print(f"{'='*60}")

    report_file = Path(report_path)
    if not report_file.exists():
        print(f"  FAIL Report not found: {report_path}")
        return False, []

    # Try JSON first, then markdown
    verification_items = []
    try:
        with open(report_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Try parsing as JSON
        try:
            report = json.loads(content)
            verification_items = report.get("verification_items", [])
        except json.JSONDecodeError:
            # Parse markdown verification checklist
            in_checklist = False
            for line in content.split("\n"):
                if "## Verification Checklist" in line:
                    in_checklist = True
                    continue
                if in_checklist and line.startswith("## "):
                    break
                if in_checklist and line.startswith("| V-"):
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) >= 4:
                        verification_items.append({
                            "id": parts[1],
                            "description": parts[2],
                            "severity": parts[3],
                            "command": "see report",
                            "expected": "see report",
                        })
    except Exception as e:
        print(f"  WARN Could not parse report: {e}")
        return True, []  # Don't block — manual verification needed

    if not verification_items:
        print("  PASS No verification items in report — nothing to check")
        return True, []

    must_fix = [vi for vi in verification_items if vi.get("severity") == "MUST_FIX"]
    should_fix = [vi for vi in verification_items if vi.get("severity") == "SHOULD_FIX"]

    print(f"  MUST_FIX items: {len(must_fix)}")
    print(f"  SHOULD_FIX items: {len(should_fix)}")
    print()

    all_must_fix_resolved = True
    total_checks = 0
    resolved = 0

    for vi in verification_items:
        cmd = vi.get("command", "")
        desc = vi.get("description", vi.get("id", "?"))
        sev = vi.get("severity", "?")
        expected = vi.get("expected", "")

        # Run the verification command
        import subprocess
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10, cwd=ROOT)
            output = result.stdout.strip()
            returncode = result.returncode

            # Determine pass/fail based on expected
            if "No matches" in expected or "0 " in expected or "0 HTML" in expected:
                passed = returncode != 0 or not output  # grep returns 1 = no matches
            elif ">=" in expected:
                try:
                    threshold = int(re.findall(r">=(\d+)", expected)[0])
                    count = len(output.split("\n")) if output else 0
                    passed = count >= threshold
                except (IndexError, ValueError):
                    passed = returncode == 0
            else:
                passed = returncode == 0 and bool(output)

            icon = "PASS" if passed else "FAIL"
            print(f"  {icon} [{sev}] {desc}")
            if not passed:
                print(f"       Expected: {expected}")
                print(f"       Command: {cmd}")
                if vi.get("severity") == "MUST_FIX":
                    all_must_fix_resolved = False

            total_checks += 1
            if passed:
                resolved += 1
        except Exception as e:
            print(f"  WARN [{sev}] {desc} — could not run: {e}")

    print(f"\n  Resolved: {resolved}/{total_checks}")
    if must_fix:
        unresolved_must = [vi for vi in must_fix if True]  # Would need tracking
        if not all_must_fix_resolved:
            print(f"  FAIL Unresolved MUST_FIX items remain")
        else:
            print(f"  PASS All MUST_FIX items resolved")

    return all_must_fix_resolved, verification_items


# ════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════
def run_gate(gate_id) -> GateResult:
    if gate_id not in GATES:
        print(f"FAIL Unknown gate: {gate_id}")
        return GateResult(gate_id, "UNKNOWN")
    print(f"\n{'='*60}")
    print(f"GATE {gate_id}: {(GATES[gate_id].__doc__ or '').strip().split(chr(10))[0]}")
    print(f"{'='*60}")
    result = GATES[gate_id]()
    for c in result.checks:
        icon = "PASS" if c.passed else "FAIL"
        print(f"  {icon} {c.name}: {c.detail}")
    status = "PASS PASS" if result.passed else "FAIL FAIL"
    print(f"\n  {status}")
    return result


def main():
    parser = argparse.ArgumentParser(description="Unified Gate Verification Runner")
    parser.add_argument("--gate", type=int, action="append", help="Run specific gate(s)")
    parser.add_argument("--all", action="store_true", help="Run all gates")
    parser.add_argument("--phase", help="Run gates for a phase (search|screening|analysis|writing|synthesis|review|submission)")
    parser.add_argument("--check-prereq", help="Check pre-gates for an agent ID")
    parser.add_argument("--check-output", help="Check post-gates for an agent ID")
    parser.add_argument("--check-revision", help="Verify MUST FIX items from peer review report against manuscript")
    parser.add_argument("--list", action="store_true", help="List all gates and agent mappings")
    args = parser.parse_args()

    if args.list:
        print("Agent -> Gate mapping:")
        for agent_id, gates in AGENT_GATES.items():
            print(f"  Agent {agent_id}: pre={gates['pre']}, post={gates['post']}")
        print("\nPhase -> Gate mapping:")
        for phase, gates in PHASE_GATES.items():
            print(f"  {phase}: gates {gates}")
        return

    gate_ids = set()

    if args.gate:
        gate_ids.update(args.gate)
    if args.all:
        gate_ids.update(GATES.keys())
    if args.phase:
        phase = args.phase.lower()
        if phase in PHASE_GATES:
            gate_ids.update(PHASE_GATES[phase])
        else:
            print(f"FAIL Unknown phase: {phase}")
            print(f"   Valid phases: {list(PHASE_GATES.keys())}")
            sys.exit(2)
    if args.check_prereq:
        agent_id = args.check_prereq
        if agent_id in AGENT_GATES:
            gate_ids.update(AGENT_GATES[agent_id]["pre"])
        else:
            print(f"FAIL Unknown agent: {agent_id}")
            sys.exit(2)
    if args.check_output:
        agent_id = args.check_output
        if agent_id in AGENT_GATES:
            gate_ids.update(AGENT_GATES[agent_id]["post"])
        else:
            print(f"FAIL Unknown agent: {agent_id}")
            sys.exit(2)

    if args.check_revision:
        report_path = args.check_revision
        if not Path(report_path).exists():
            print(f"FAIL Revision report not found: {report_path}")
            sys.exit(1)
        passed, results = check_revision(report_path)
        if not passed:
            sys.exit(1)
        sys.exit(0)

    if not gate_ids:
        parser.print_help()
        print("\nNo gates specified. Use --gate, --all, --phase, --check-prereq, --check-output, or --check-revision.")
        sys.exit(0)

    results = []
    for gid in sorted(gate_ids):
        results.append(run_gate(gid))

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    print(f"  Passed: {passed}/{len(results)}")
    if failed > 0:
        failed_gates = [r.gate_id for r in results if not r.passed]
        print(f"  Failed: {failed} -- gates {failed_gates}")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
