"""PubMed/Europe PMC multi-query literature search using curl for reliable HTTP."""

from config_loader import load_config, find_project_root
config = load_config()
ROOT = find_project_root()

import json, os, time, subprocess

OUTPUT_DIR = str(ROOT / config["paths"]["data_dir"])
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pubmed_search_results.json")

print("WARNING: pubmed_search.py is a domain-specific example. Edit QUERIES before using it for a new review.")

QUERIES = [
    "squamous carcinoma NSCLC immunotherapy resistance",
    "squamous NSCLC PD-1 resistance immune mechanism",
    "squamous cell lung cancer immune checkpoint resistance TME",
    "LUSC immunotherapy resistance immune evasion",
    "squamous NSCLC anti-PD-L1 non-response tumor microenvironment",
    "squamous NSCLC CTLA-4 resistance",
    "squamous lung cancer T cell exhaustion resistance",
]

BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

all_results = []
seen_ids = set()

for q_idx, query in enumerate(QUERIES):
    cursor = None  # Don't send cursorMark on first request
    print(f"\n=== Query {q_idx+1}/{len(QUERIES)}: {query} ===")

    for batch in range(5):
        q_encoded = query.replace(" ", "%20")
        url = f"{BASE_URL}?query={q_encoded}&resultType=core&pageSize=100&format=json"
        if cursor:
            url += f"&cursorMark={cursor}"

        try:
            result = subprocess.run(
                ["curl", "-s", "--connect-timeout", "15", "--max-time", "60", url],
                capture_output=True, timeout=90
            )
            response = result.stdout.decode("utf-8")
        except Exception as e:
            print(f"  Batch {batch+1}: curl error - {e}")
            break

        if not response.strip():
            print(f"  Batch {batch+1}: empty response (rc={result.returncode}, stderr={result.stderr[:100]})")
            break

        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            print(f"  Batch {batch+1}: JSON parse error, response[:200]={response[:200]}")
            break

        hit_count = data.get("hitCount", 0)
        if hit_count == 0:
            print(f"  Batch {batch+1}: 0 hits, stopping")
            break

        results = data.get("resultList", {}).get("result", [])
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
                    "pubTypeList": pub_type_data.get("pubType", []),
                    "source": r.get("source", ""),
                    "citedByCount": r.get("citedByCount", 0),
                })
                new_count += 1

        next_cursor = data.get("nextCursorMark", "")
        print(f"  Batch {batch+1}: {hit_count} total hits, +{new_count} new, cumulative={len(all_results)}")

        if new_count < 5 or not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
        time.sleep(0.3)

# Save
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"SEARCH COMPLETE")
print(f"Total unique papers: {len(all_results)}")
print(f"Saved to: {OUTPUT_FILE}")

# Year distribution
years = {}
for r in all_results:
    y = r.get("pubYear", "unknown")
    years[y] = years.get(y, 0) + 1
print("\nYear distribution:")
for y in sorted(years.keys(), reverse=True)[:10]:
    print(f"  {y}: {years[y]}")

# Article types
review_count = sum(1 for r in all_results if any(
    "review" in str(pt).lower() or "Review" in str(pt)
    for pt in r.get("pubTypeList", [])
))
print(f"\nReview articles: {review_count}")
print(f"Other articles: {len(all_results) - review_count}")
print(f"Review ratio: {review_count/max(len(all_results),1)*100:.1f}%")
