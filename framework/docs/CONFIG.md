# Configuration Reference

All project-specific settings live in `config.yaml`. This is the single source of truth — no settings are hardcoded in scripts or agent definitions.

## Project Identity

```yaml
project:
  topic: "Your Review Topic"         # e.g. "NRDS Life-Course Outcomes"
  domain: "your-field"               # e.g. "neonatology, respiratory medicine"
  review_type: "narrative"           # narrative | systematic | meta-analysis
  target_journal: "Journal Name"     # e.g. "Pediatric Research"
  language: "en"                     # en | zh (manuscript language)
```

## File Paths

All paths are relative to the project root.

```yaml
paths:
  manuscript_src: "manuscript/submission.md"   # Single source of truth
  figures_dir: "manuscript/figures"            # Figure image files
  data_dir: "data"                             # Search results, screening data
  papers_dir: "docs/papers"                    # Paper notes
  search_results_dir: "docs/search-results"    # Search handoff files
  output_dir: "manuscript"                     # Generated outputs
```

## Agent Configuration

### Screening (Agent 6)

```yaml
agents:
  screening:
    # Paper classification system
    paper_type_system: "default-a-j"    # From templates/paper-types/

    # Domain-specific exclusion keywords
    exclusion_keywords:
      population: []                    # e.g. ["laryngeal", "head and neck"]
      intervention: []
      other: []

    # Type distribution health check thresholds
    type_thresholds:
      mechanism_types_min_pct: 20       # A+B+C minimum %
      bioinformatics_max_pct: 50        # E type maximum %
      secondary_source_max_pct: 30      # F+G maximum %
      abstract_only_max_pct: 20         # Maximum abstract-only %
```

### Submission (Agent 8)

```yaml
agents:
  submission:
    target_journal_profile: ""          # e.g. "pediatric-research"
```

## Script Configuration

### Word Generation

```yaml
scripts:
  gen_word:
    output_filename: "manuscript/output.docx"
    font: "Times New Roman"
    font_size: 12
    line_spacing: 2.0
    margin_top_cm: 2.54
    margin_bottom_cm: 2.54
    margin_left_cm: 3.18
    margin_right_cm: 3.18
```

### Manuscript Audit

```yaml
scripts:
  audit:
    checks:
      - title_exists
      - abstract_exists
      - references_exist
      - sections_sequential
      - citation_integrity
```

## Custom Paper Type Systems

Create new `.md` files in `templates/paper-types/` following the format of `default-a-j.md`. Reference them in config:

```yaml
agents:
  screening:
    paper_type_system: "my-custom-system"
```

This loads `templates/paper-types/my-custom-system.md`.

## Custom Domain Templates

Replace any file in `templates/` to customize the framework for your domain:
- `paper-note.md` — paper note structure
- `domain-ontology.md` — intervention inventory template
- `clinical-decision-framework.md` — decision framework format
