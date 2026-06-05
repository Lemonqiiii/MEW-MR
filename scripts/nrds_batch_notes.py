"""NRDS Life-Course Review — Batch note generation for Phase 4 deep reading."""
import json, os, re, urllib.request, urllib.parse, ssl, time

OUTPUT_DIR = "E:/medical-review/docs/papers/nrds_lifecourse"
DATA_DIR = "E:/medical-review/data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(DATA_DIR, "screening_final_included.json"), "r", encoding="utf-8") as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} included papers")

# Composite scoring
import math
for p in papers:
    score = float(p.get("relevance_score", 0.5))
    citations = int(p.get("citedByCount", 0))
    year_str = p.get("pubYear", "")
    year = int(year_str) if year_str.isdigit() else 2020
    paper_type = p.get("paper_type", "G")
    type_boost = {"F": 0.15, "D": 0.10, "H": 0.08, "B": 0.07, "A": 0.10, "E": 0.03, "G": 0.0, "I": -0.05, "J": -0.10}
    boost = type_boost.get(paper_type, 0)
    citation_score = math.log(citations + 1) / math.log(2) * 0.02
    recency = min((year - 2010) / 16, 1.0) * 0.03 if year >= 2010 else 0
    p["composite_score"] = score + boost + citation_score + recency

papers.sort(key=lambda x: -x["composite_score"])
P1 = [p for p in papers if p["composite_score"] >= 0.75]
P2 = [p for p in papers if 0.55 <= p["composite_score"] < 0.75]
P3 = [p for p in papers if p["composite_score"] < 0.55]

print(f"P1: {len(P1)}, P2: {len(P2)}, P3: {len(P3)}")

def sanitize_filename(s):
    s = re.sub(r'[<>:"/\\|?*]', '', s)
    return re.sub(r'\s+', '_', s)[:80]

EPMC_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/article"
ctx = ssl.create_default_context()

ptype_map = {"A": "机制实验", "B": "转化研究", "C": "多组学+验证", "D": "临床+机制终点",
    "E": "观察性/关联研究", "F": "系统综述/荟萃分析", "G": "叙述性综述",
    "H": "临床疗效", "I": "病例报告", "J": "方法/方案"}

scope_map = {
    "A": {"mechanism": True, "clinical": True, "primary": True, "abstract_ok": False},
    "B": {"mechanism": True, "clinical": True, "primary": True, "abstract_ok": False},
    "C": {"mechanism": False, "clinical": True, "primary": True, "abstract_ok": False},
    "D": {"mechanism": "needs_experimental", "clinical": True, "primary": True, "abstract_ok": False},
    "E": {"mechanism": False, "clinical": "hypothesis_only", "primary": "auxiliary_only", "abstract_ok": True},
    "F": {"mechanism": False, "clinical": True, "primary": "consensus_only", "abstract_ok": False},
    "G": {"mechanism": False, "clinical": "background_only", "primary": False, "abstract_ok": True},
    "H": {"mechanism": False, "clinical": True, "primary": True, "abstract_ok": False},
    "I": {"mechanism": False, "clinical": False, "primary": False, "abstract_ok": True},
    "J": {"mechanism": False, "clinical": False, "primary": "info_only", "abstract_ok": True},
}

# P1 notes
print("\nGenerating P1 notes...")
p1_notes_list = []
for idx, p in enumerate(P1):
    pmid = p.get("pmid", "")
    doi = p.get("doi", "")
    title = p.get("title", "Unknown")
    journal = p.get("journal", "Unknown")
    year = p.get("pubYear", "?")
    authors = p.get("authorString", "Unknown")
    abstract = p.get("abstractText", "") or ""
    paper_type = p.get("paper_type", "G")
    ptype_name = ptype_map.get(paper_type, "未分类")
    scope = scope_map.get(paper_type, {})

    first_author = authors.split(",")[0].strip() if authors else "Unknown"
    first_author = re.sub(r'\s+.*', '', first_author)
    composite = p.get("composite_score", 0)
    importance = "core" if composite >= 0.85 else "important"

    # Relevance areas
    text = (title + " " + abstract[:3000]).lower()
    areas = []
    if any(kw in text for kw in ["ventilat", "cpap", "hfov", "nippv", "respiratory support"]): areas.append("ventilation")
    if any(kw in text for kw in ["corticosteroid", "dexamethasone", "betamethasone", "hydrocortisone", "steroid", "antenatal corticosteroid"]): areas.append("steroids")
    if any(kw in text for kw in ["surfactant", "lisa", "mist", "insure", "beractant", "poractant"]): areas.append("surfactant")
    if any(kw in text for kw in ["oxygen therap", "saturation target", "hyperoxi", "hypoxi"]): areas.append("oxygen")
    if any(kw in text for kw in ["neurodevelopment", "cognitive", "cerebral palsy", "bayley", "iq", "intelligence"]): areas.append("neurodevelopment")
    if any(kw in text for kw in ["pulmonary function", "lung function", "fev1", "spirometry", "asthma", "wheez", "respiratory morbidity"]): areas.append("lung_function")
    if any(kw in text for kw in ["quality of life", "hrqol", "functional outcome", "functional status"]): areas.append("qol")
    if any(kw in text for kw in ["bpd", "bronchopulmonary", "chronic lung disease"]): areas.append("bpd")
    if any(kw in text for kw in ["life course", "dohad", "developmental origin", "adulthood", "adult outcome", "adolescen"]): areas.append("lifecourse")

    # Extract stats from abstract
    pval_matches = re.findall(r'[pP]\s*[<≤=]\s*0\.\d+', abstract)
    stat_matches = re.findall(r'(?:OR|RR|HR|aOR)\s*[=：:]\s*[0-9.]+', abstract, re.IGNORECASE)
    n_match = re.search(r'(?:n\s*[=：:]\s*|N\s*[=：:]\s*|included\s+|enrolled\s+|total\s+of\s+)(\d{2,6})', abstract)
    sample_size = n_match.group(1) if n_match else "?"

    note = f"""# {title}

## 元数据
- **PMID**: {pmid}
- **DOI**: {doi}
- **期刊**: {journal}
- **年份**: {year}
- **引用次数**: {p.get("citedByCount", 0)}
- **论文类型**: {paper_type} — {ptype_name}
- **引用范围**: mechanism={scope.get("mechanism")} | clinical={scope.get("clinical")} | primary={scope.get("primary")}

## 研究问题
[TBD]

## 方法
- **样本量**: {sample_size}
- **统计显著**: {', '.join(pval_matches[:3]) if pval_matches else 'N/A'}
- **效应量**: {', '.join(stat_matches[:3]) if stat_matches else 'N/A'}

## 核心发现
[TBD — requires deep reading]

## 与本综述的关系
- **关联领域**: {', '.join(areas) if areas else 'TBD'}
- **重要性**: {'★★★ 核心' if importance == 'core' else '★★ 重要'} (score={composite:.3f})

## 摘要
{abstract[:2000]}

## 笔记日期
2026-06-05 | Agent 2 (batch)
"""
    fname = sanitize_filename(f"{first_author}_{year}_{pmid}")
    with open(os.path.join(OUTPUT_DIR, f"{fname}.md"), "w", encoding="utf-8") as f:
        f.write(note)

    p1_notes_list.append({"pmid": pmid, "file": f"{fname}.md", "title": title[:80], "importance": importance, "type": paper_type, "areas": areas})
    if (idx+1) % 20 == 0:
        print(f"  {idx+1}/{len(P1)}...")
    time.sleep(0.15)

print(f"P1 done: {len(p1_notes_list)} notes")

# P2 abbreviated
print("\nGenerating P2 abbreviated notes...")
p2_notes_list = []
for idx, p in enumerate(P2):
    pmid = p.get("pmid", "")
    title = p.get("title", "Unknown")
    abstract = (p.get("abstractText", "") or "")[:800]
    year = p.get("pubYear", "?")
    paper_type = p.get("paper_type", "G")
    authors = p.get("authorString", "Unknown")
    first_author = authors.split(",")[0].strip() if authors else "Unknown"
    first_author = re.sub(r'\s+.*', '', first_author)

    note = f"""# {title}
- **PMID**: {pmid} | **Year**: {year} | **Type**: {paper_type} | **Importance**: ★★
## Abstract
{abstract}
---
*Abbreviated note | 2026-06-05*
"""
    fname = sanitize_filename(f"{first_author}_{year}_{pmid}_abbrev")
    with open(os.path.join(OUTPUT_DIR, f"{fname}.md"), "w", encoding="utf-8") as f:
        f.write(note)
    p2_notes_list.append({"pmid": pmid, "file": f"{fname}.md", "title": title[:80], "type": paper_type})
    if (idx+1) % 50 == 0:
        print(f"  {idx+1}/{len(P2)}...")

print(f"P2 done: {len(p2_notes_list)} abbreviated notes")

# Save index
with open(os.path.join(OUTPUT_DIR, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write(f"# NRDS Life-Course Review — Paper Index\n\n")
    f.write(f"**Total**: {len(papers)} | **P1**: {len(P1)} | **P2**: {len(P2)} | **P3**: {len(P3)}\n\n")
    f.write("## Priority 1 (Full Notes)\n\n")
    for n in p1_notes_list:
        f.write(f"- [{n['type']}] {'★★★' if n['importance']=='core' else '★★'} [{n['pmid']}] {n['title']} → `{n['file']}`\n")
    f.write("\n## Priority 2 (Abbreviated)\n\n")
    for n in p2_notes_list:
        f.write(f"- [{n['type']}] [{n['pmid']}] {n['title']} → `{n['file']}`\n")
    f.write(f"\n## Priority 3 (Index Only, n={len(P3)})\n\n")
    for p in P3:
        f.write(f"- [{p.get('paper_type','?')}] [{p.get('pmid','N/A')}] {p.get('title','Unknown')[:80]}\n")

# Save P1/P2/P3 splits
for label, data in [("p1_core", P1), ("p2_important", P2), ("p3_auxiliary", P3)]:
    with open(os.path.join(DATA_DIR, f"screening_{label}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone. Index: {os.path.join(OUTPUT_DIR, 'INDEX.md')}")
print(f"P1: {len(P1)} | P2: {len(P2)} | P3: {len(P3)}")

# Stats
from collections import Counter
p1_types = Counter(n["type"] for n in p1_notes_list)
print("P1 types:", dict(p1_types))
all_areas = Counter()
for n in p1_notes_list:
    for a in n.get("areas", []):
        all_areas[a] += 1
print("P1 areas:", dict(all_areas.most_common()))
