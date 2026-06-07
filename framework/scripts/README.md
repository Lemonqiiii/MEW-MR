# Scripts

## Framework Infrastructure (project-agnostic)
| Script | Purpose |
|--------|---------|
| `config_loader.py` | Load config.yaml from project root |
| `state.py` | Read/write state.json |
| `verify_gates.py` | Unified gate verification runner (11 gates) |
| `gen_word.py` | Generate Word document from markdown manuscript |
| `audit_manuscript.py` | Structural integrity audit before Word generation |
| `rebuild_refs.py` | Rebuild reference section from body citations |

## Domain-Specific Examples (customize for your review)
| Script | Purpose | Customization Needed |
|--------|---------|---------------------|
| `pubmed_search.py` | PubMed/Europe PMC multi-query search | Replace QUERIES list with your search terms |
| `screen_abstracts.py` | Title/abstract PICO screening | Replace PICO criteria and exclusion keywords |
| `fulltext_screening.py` | Full-text evaluation and mechanism classification | Replace MECHANISM_CATEGORIES and scoring criteria |
| `gate123_verify.py` | Gates 1-3 verification (deprecated) | Use `verify_gates.py --gate 1 --gate 2 --gate 3` instead |
| `generate_figures.py` | Generate PNG figures using PIL | Replace figure specifications |
