# Agent 2: Paper Analysis

## Metadata
- **id**: 2
- **type**: execution (horizontal)
- **triggers**: `3` `analyze` `分析` `读` `take notes`
- **pre_gate**: Gate 2
- **post_gate**: Gate 3

## Input
- Paper PMID/DOI/URL or existing PDF
- `templates/paper-note.md` — note template
- Screening Agent Handoff — paper type code (A-J) and citation scope labels

## Output Schema
```json
{
  "note_path": "docs/papers/topic/AuthorYear-Keyword.md",
  "pmid": "12345678",
  "paper_type": "A",
  "importance": "★★★ | ★★ | ★",
  "key_finding": "one-sentence summary",
  "citation_scope": {
    "can_support_mechanism": true,
    "can_support_clinical": true,
    "can_be_primary_ref": true,
    "abstract_only_ok": false
  }
}
```

---

## Steps

### Step 1: Fetch Paper Metadata (MANDATORY)
1. Retrieve paper metadata and abstract via PMID/DOI
2. If full-text access available, read full text; otherwise base initial notes on abstract
3. Mark `abstract_only: true` if full text unavailable

### Step 2: Confirm Paper Type (MANDATORY)
1. Read paper type code (A-J) from Screening Agent Handoff
2. Read citation scope labels from Handoff
3. Fill both fields in note template

### Step 3: Structured Extraction (MANDATORY)
Follow `templates/paper-note.md` template:
- **Metadata**: PMID, journal, year, authors, citation count, **paper type**, **citation scope**
- **PICO** (clinical studies) or **Research Framework** (basic research)
- **Core Methods**: design type, sample size, key techniques
- **Key Findings & Data**: specific numbers, effect sizes, confidence intervals
- **Limitations**: stated and unstated
- **Relevance to Review**: specific connections to review themes

### Step 4: Write Note (MANDATORY)
Write to `docs/papers/[topic]/[FirstAuthor][Year]-[Keyword].md`

### Step 5: Update Index (MANDATORY)
Update literature statistics (including paper type field)

### Step 6: Flag Key Findings (CONDITIONAL)
If paper contains important arguments → flag for `state.json` key findings update

### Output
- Note file path
- One-sentence key finding summary
- Importance rating: ★★★ Core / ★★ Important / ★ Auxiliary
