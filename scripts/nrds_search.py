"""NRDS Life-Course Review — Tier 1 search using Python urllib (no shell curl dependency)."""
import json, os, time, urllib.request, urllib.parse, ssl

OUTPUT_DIR = "E:/medical-review/data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Focused short queries (5-8 keywords each) ──
QUERIES = [
    ("Q1 NRDS+vent+outcome", "neonatal RDS ventilation long-term pulmonary outcome follow-up"),
    ("Q2 Preterm+steroid+neuro", "preterm dexamethasone postnatal corticosteroid neurodevelopment cognitive follow-up"),
    ("Q3 Surfactant+long-term", "surfactant replacement neonatal RDS long-term childhood adolescent outcome"),
    ("Q4 CPAP+NIV+lung", "preterm CPAP non-invasive ventilation childhood lung function asthma FEV1"),
    ("Q5 DOHaD+respiratory", "DOHaD life-course preterm birth lung respiratory adult COPD"),
    ("Q6 BPD+trajectory", "bronchopulmonary dysplasia neonatal long-term pulmonary outcome trajectory school-age"),
    ("Q7 NRDS+cerebral palsy", "neonatal respiratory distress preterm cerebral palsy cognitive IQ school performance"),
    ("Q8 Systematic review NRDS", "systematic review meta-analysis neonatal respiratory distress long-term outcome"),
    ("Q9 NICU QoL follow-up", "neonatal intensive care quality of life HRQOL adolescent adult follow-up respiratory"),
    ("Q10 LISA surfactant less invasive", "less invasive surfactant LISA MIST preterm neonatal outcome follow-up"),
    ("Q11 Oxygen target preterm long-term", "oxygen saturation target preterm neonatal long-term outcome BPD ROP"),
    ("Q12 Antenatal corticosteroid long-term", "antenatal corticosteroid betamethasone dexamethasone preterm long-term child outcome"),
    ("Q13 HFOV ventilation preterm", "high-frequency oscillatory ventilation preterm neonatal long-term pulmonary outcome"),
    ("Q14 NRDS respiratory morbidity childhood", "neonatal RDS respiratory morbidity childhood wheezing asthma hospitalization"),
    ("Q15 INSURE surfactant ventilation", "INSURE intubation surfactant extubation preterm neonatal outcome"),
    ("Q16 Volume-targeted ventilation preterm", "volume-targeted ventilation volume guarantee preterm long-term outcome BPD"),
    ("Q17 Preterm adult lung function", "preterm birth adult lung function FEV1 spirometry COPD respiratory epidemiology"),
    ("Q18 Early hydrocortisone preterm neuro", "hydrocortisone preterm neonatal hypotension neurodevelopment long-term follow-up"),
]

EPMC_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
ctx = ssl.create_default_context()

def search_epmc(query, label, max_results=300):
    """Search Europe PMC using urllib (no curl/subprocess dependency)."""
    all_results = []
    cursor = None
    seen_ids = set()

    for batch in range(6):
        params = {
            "query": query,
            "resultType": "core",
            "pageSize": 100,
            "format": "json"
        }
        if cursor:
            params["cursorMark"] = cursor

        url = EPMC_URL + "?" + urllib.parse.urlencode(params)

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NRDS-Review/1.0"})
            with urllib.request.urlopen(req, timeout=45, context=ctx) as resp:
                response = resp.read().decode("utf-8")
        except Exception as e:
            print(f"  [{label}] Batch {batch+1}: HTTP error - {e}")
            break

        if not response.strip():
            print(f"  [{label}] Batch {batch+1}: empty response")
            break

        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            print(f"  [{label}] Batch {batch+1}: JSON error, response[:200]={response[:200]}")
            break

        hit_count = data.get("hitCount", 0)
        if batch == 0:
            print(f"  [{label}] Hits: {hit_count}")

        results = data.get("resultList", {}).get("result", [])
        if not results:
            break

        next_cursor = data.get("nextCursorMark")
        new_count = 0
        for r in results:
            rid = r.get("id", "")
            if rid and rid not in seen_ids:
                seen_ids.add(rid)
                journal_info = r.get("journalInfo") or {}
                journal_data = journal_info.get("journal", {}) or {}
                pub_type_data = r.get("pubTypeList") or {}

                all_results.append({
                    "id": rid,
                    "pmid": r.get("pmid", ""),
                    "pmcid": r.get("pmcid", ""),
                    "doi": r.get("doi", ""),
                    "title": r.get("title", ""),
                    "authorString": r.get("authorString", ""),
                    "journal": journal_data.get("title", ""),
                    "pubYear": r.get("pubYear", ""),
                    "abstractText": r.get("abstractText", ""),
                    "pubTypeList": pub_type_data.get("pubType", []) if isinstance(pub_type_data, dict) else [],
                    "source": r.get("source", ""),
                    "citedByCount": r.get("citedByCount", 0),
                    "query_label": label,
                })
                new_count += 1

        print(f"  [{label}] B{batch+1}: +{new_count} (total {len(all_results)})")

        if len(all_results) >= max_results:
            break
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
        time.sleep(0.35)

    return all_results

# ── Main ──
print("=" * 60)
print("NRDS Life-Course Review - Tier 1 Search (urllib)")
print("=" * 60)

all_papers = {}

for label, query in QUERIES:
    print(f"\n-- {label} --")
    results = search_epmc(query, label, max_results=200)
    new = 0
    for p in results:
        key = p["pmid"] or p["doi"] or p["id"]
        if key not in all_papers:
            all_papers[key] = p
            new += 1
    print(f"  >> Added {new} new (total unique: {len(all_papers)})")
    time.sleep(0.4)

# ── Save ──
output_path = os.path.join(OUTPUT_DIR, "pubmed_search_results.json")
papers_list = list(all_papers.values())
papers_list.sort(key=lambda x: (-int(x.get("pubYear") or 0), -int(x.get("citedByCount") or 0)))

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(papers_list, f, ensure_ascii=False, indent=2)

print(f"\n{'=' * 60}")
print(f"Search complete: {len(papers_list)} unique papers -> {output_path}")

# Stats
years = [p.get("pubYear") for p in papers_list if p.get("pubYear")]
if years:
    print(f"Year range: {min(years)}-{max(years)}")
    year_dist = {}
    for y in years:
        year_dist[y] = year_dist.get(y, 0) + 1
    for y in sorted(year_dist.keys(), reverse=True):
        print(f"  {y}: {year_dist[y]}")

has_pmid = sum(1 for p in papers_list if p.get("pmid"))
has_abs = sum(1 for p in papers_list if p.get("abstractText"))
print(f"With PMID: {has_pmid} | With abstract: {has_abs}")
print(f"Total: {len(papers_list)}")
