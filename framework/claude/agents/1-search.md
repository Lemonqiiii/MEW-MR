# Agent 1: Literature Search

## Metadata
- **id**: 1
- **type**: execution (horizontal)
- **triggers**: `1` `search` `搜索` `检索` `find papers`
- **pre_gate**: none
- **post_gate**: Gate 1, Gate 7

## Input
- `state.json` → `active_focus` — PICO framework, search keywords, inclusion/exclusion criteria
- `config.yaml` → `paper_type_system` — paper classification system to use
- `docs/methods/database-coverage.md` — database activation decision table
- Optional: user-specified additional search parameters

## Output Schema
```json
{
  "databases_searched": ["pubmed", "semantic_scholar", ...],
  "total_hits": 1205,
  "deduplicated_count": 1100,
  "layer_validation": {
    "l1_multi_strategy": "PASS",
    "l2_citation_diffusion": "PASS",
    "l3_external_gold_standard": "92%",
    "l4_grey_literature": "PASS",
    "l5_saturation_adversarial": "PASS"
  },
  "full_text_estimate": {
    "oa_auto": "40%",
    "vpn_manual": "30%",
    "paywall": "15%",
    "abstract_only": "15%"
  },
  "domain_ontology_built": true,
  "handoff_path": "docs/search-results/handoff.md"
}
```

---

## Steps

### Step 0: Database Requirements Assessment (MANDATORY — GATEKEEPING)
1. Read `state.json` → `active_focus` for PICO and study design types
2. Read `docs/methods/database-coverage.md` activation decision table
3. Determine databases to activate:

| Condition | Activate |
|-----------|----------|
| All reviews | PubMed + Semantic Scholar + Europe PMC (Tier 1 auto) |
| Drug/biologic topic | Embase (Tier 2 high priority) |
| RCT/clinical trial topic | Cochrane CENTRAL + ClinicalTrials.gov |
| Chinese population/TCM | CNKI + Wanfang (Tier 2 required) |
| TCM/integrative medicine | + SinoMed (Tier 2 required) |
| Recent advances | Europe PMC preprint mode (auto) |
| Systematic review/meta-analysis | Embase + Cochrane (strongly recommended) |

4. Output database list with priority and access method
5. **DO NOT skip this step.** It is the gatekeeping step.

### Step 1: Tier 1 Automated Search (MANDATORY)
1. **PubMed**: Construct MeSH + free-text search → E-utilities API or WebFetch → PMID list + abstracts
   - **FALLBACK**: If WebFetch to pubmed.ncbi.nlm.nih.gov is blocked, use WebSearch with `site:pubmed.ncbi.nlm.nih.gov` or Semantic Scholar as primary source
2. **Semantic Scholar**: Keyword + semantic search → API → paper details (TLDR abstracts, citation counts)
3. **Europe PMC**: Free-text + preprint → API → paper details (OA full-text links)
   - **FALLBACK**: If europepmc.org is blocked, use WebSearch or rely on Semantic Scholar + PubMed results
4. **ClinicalTrials.gov** (if activated): API → completed/ongoing trial records
5. **Search Query Diagnostics** (before submitting):
   - Sensitivity test: verify known must-hit terms
   - Precision test: random sample of 20 hits → agent judges relevance (target ≥85%)
   - Gap analysis: check for missing synonyms/hypernyms
6. Merge Tier 1 results into initial PMID list

### Step 2: Generate Tier 2 Manual Search Checklist (MANDATORY)
1. Pre-compile search queries for each database (Embase/Emtree, Cochrane, CNKI, Wanfang, SinoMed)
2. Write `docs/search-results/manual-search-checklist.md`:
   - Complete step-by-step instructions per database
   - Pre-compiled query (paste-ready)
   - Export format instructions (RIS) and file naming conventions
   - Estimated time
3. Prompt user:
   > "Tier 1 automated search complete, ~N hits. Please connect to institutional VPN and execute Tier 2 searches following the checklist. Place RIS files in docs/search-results/ and say 'ready' when done."

### Step 3: Merge and Deduplicate (MANDATORY)
User triggers after Tier 2 completion:
1. Read all RIS files in `docs/search-results/`
2. Parse PMID/DOI/title
3. Unified dedup: PMID exact match → DOI match → title similarity >95%
4. Generate deduplicated master list

### Step 4: Five-Layer Comprehensiveness Validation (MANDATORY)
#### Layer 1: Multi-Strategy Search Coverage
- Four independent search paths executed (PubMed + S2 + EPMC + optional ClinicalTrials.gov)
- Confirm successful response status for each database

#### Layer 2: Multi-Point Citation Diffusion
- **Anchor A — Consensus**: Top 5 most-cited papers in three-way consensus set (PubMed ∩ S2 ∩ EPMC) → backward references + forward citations
- **Anchor B — Temporal**: Most recent 5 papers (current-2 years) in three-way consensus → their references
- **Anchor C — Methodological**: 2 papers each from different study designs (RCT×2, cohort×2, systematic review×2, basic experiment×2) → cross-validate different citation circles
- **Anchor D — Geographic**: If metadata supports, 1 paper from different countries → non-Anglosphere researcher citation networks

#### Layer 3: External Gold Standard Validation
1. Identify 2-3 recent high-quality systematic reviews/meta-analyses in results (published current-3 years, highly cited)
2. Extract their included paper lists (references)
3. Cross-validate: what % of published SR references did our search hit?
   - ≥90% → ✅ Acceptable coverage
   - 85-90% → ⚠️ Flag, analyze missed paper characteristics
   - <85% → ❌ Major search strategy gap → report to user

#### Layer 4: Grey Literature Supplement
1. If clinical trial topic: check ClinicalTrials.gov for completed unpublished trials
2. Conference abstracts: Europe PMC auto-covered
3. Preprints: Europe PMC bioRxiv/medRxiv auto-covered
4. Grey literature tagged separately — not primary evidence for core claims

#### Layer 5: Saturation + Adversarial Verification
1. **Saturation**: Iteratively expand search (add synonyms, hypernyms) → PMID increment <5% → search saturated
2. **Adversarial**: Randomly sample 5 included papers → read Discussion sections → verify key prior works cited in Discussion are in our search results → ≥2 missing → 🔴 potential search blind spot

### Step 5: Full-Text Access Triage (MANDATORY)

| Tier | Source | Agent Action | Estimated Coverage |
|------|--------|-------------|-------------------|
| Tier 1 | PMC OA, Europe PMC OA, bioRxiv/medRxiv | Auto-fetch full text | 30-50% |
| Tier 2 | VPN required (institutional subscription) | Generate download list → user VPN batch download | 20-30% |
| Tier 3 | Paywall | Generate list → note access pathways → user decides | 10-20% |
| Tier 4 | No full text available | Mark as abstract-only → downgrade | remainder |

**Abstract-only ratio control**:
- Target: abstract-only ≤20% of final inclusion
- Estimate ratio at Step 5 completion
- If predicted >20% → ⚠️ warn → recommend prioritizing Tier 2 full-text acquisition

### Step 6: Update Index (MANDATORY)
1. Update literature statistics
2. Generate Handoff to Screening Agent (see Handoff Schema below)

### Step 7: Domain Ontology Construction (MANDATORY — Module A gatekeeping)
See `claude/gates/gates.md` → Gate 7 for pass criteria.

1. **Guideline Discovery**: WebSearch for clinical practice guidelines → extract all mentioned interventions
2. **Completeness Check**: WebSearch standard-of-care interventions → cross-check against extracted list → flag missing interventions
3. **Evidence Gap Grading**: For each intervention, determine max follow-up horizon → assign G0-G4 grade per `claude/gates/gates.md`
4. **Clinical Urgency Scoring**: Score each intervention on 4 dimensions (frequency 0.30, adoption trend 0.25, clinical stakes 0.25, knowledge gap risk 0.20)
5. **Interaction Map**: For all intervention pairs, search for combined/interaction evidence → label KNOWN/UNEXPLORED
6. **Write Domain Ontology**: Fill `templates/domain-ontology.md` with all collected data

**Post-condition**: `python3 scripts/verify_gates.py --gate 7` must pass.

---

## Handoff Schema (to Screening Agent)
```json
{
  "search_topic": "string",
  "date": "YYYY-MM-DD",
  "databases": [
    {"name": "pubmed", "hits": 0, "status": "PASS"},
    {"name": "semantic_scholar", "hits": 0, "status": "PASS"}
  ],
  "total_deduplicated": 0,
  "layer_validation": {
    "l1": "PASS",
    "l2": "PASS",
    "l3_hit_rate_pct": 0,
    "l4": "PASS",
    "l5": "PASS"
  },
  "full_text_triage": {
    "oa_auto_pct": 0,
    "vpn_manual_pct": 0,
    "estimated_abstract_only_pct": 0
  },
  "domain_ontology_path": "knowledge/domain-ontology.md",
  "known_issues": ["string"],
  "recommendations": ["string"]
}
```
