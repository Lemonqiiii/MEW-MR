"""PubMed/Europe PMC supplemental search for 2020-2024 papers by individual year."""
import json, os, time, subprocess

OUTPUT_DIR = "E:/medical-review/data"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pubmed_search_supplement.json")

BASE_QUERY = "squamous+NSCLC+immunotherapy+resistance"

# Search each year individually
YEARS = ["2020", "2021", "2022", "2023", "2024"]

BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

all_results = []
seen_ids = set()

# Load existing IDs from main search
main_file = os.path.join(OUTPUT_DIR, "pubmed_search_results.json")
if os.path.exists(main_file):
    with open(main_file, "r", encoding="utf-8") as f:
        existing = json.load(f)
    for r in existing:
        seen_ids.add(r.get("id", ""))
    print(f"Loaded {len(seen_ids)} existing IDs from main search")

for year in YEARS:
    cursor = None
    print(f"\n=== Year: {year} ===")

    for batch in range(5):
        q_encoded = f"{BASE_QUERY}+AND+PUB_YEAR:{year}"
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
            print(f"  Batch {batch+1}: empty response")
            break

        try:
            data = json.loads(response)
        except json.JSONDecodeError as e:
            print(f"  Batch {batch+1}: JSON parse error - {e}")
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
        print(f"  Batch {batch+1}: {hit_count} hits, +{new_count} new, total={len(all_results)}")

        if new_count < 5 or not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
        time.sleep(0.3)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"\n{'='*60}")
print(f"SUPPLEMENTAL SEARCH COMPLETE")
print(f"Total unique papers (2020-2024): {len(all_results)}")
print(f"Saved to: {OUTPUT_FILE}")

years = {}
for r in all_results:
    y = r.get("pubYear", "unknown")
    years[y] = years.get(y, 0) + 1
print("\nYear distribution:")
for y in sorted(years.keys(), reverse=True):
    print(f"  {y}: {years[y]}")

review_count = sum(1 for r in all_results if any(
    "review" in str(pt).lower() or "Review" in str(pt)
    for pt in r.get("pubTypeList", [])
))
print(f"\nReview articles: {review_count}")
print(f"Other articles: {len(all_results) - review_count}")
