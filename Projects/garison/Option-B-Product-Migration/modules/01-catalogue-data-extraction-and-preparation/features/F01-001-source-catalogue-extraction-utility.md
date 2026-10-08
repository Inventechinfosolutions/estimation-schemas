# F01-001 — Source Catalogue Extraction Utility

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-001 |
| Feature Name | Source Catalogue Extraction Utility |
| Module | 01 — Catalogue Data Extraction & Preparation |
| Module Type | Technical |
| Release | Go-live |

### Description
Command-line utility that walks the source catalogue's moulding categories and styles, reads each listing and product view, and captures product code, category, style, thickness, width, species options and image URL into a raw dataset with a run log. It can alternatively ingest a supplier-provided data file if Brenlo supplies one.

### Business Objective
Collect the full product list accurately and repeatably, without manual copy-paste.

### Actors
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer runs the extraction; no Garrison user operates it.
2. **How they create:** They configure the category and style list, request throttle and output folder, then run the utility; it writes raw records and a run log.
3. **How they edit:** They re-run for failed or newly found categories; runs resume from the last checkpoint.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees each run's log (pages fetched, products found, errors).
8. **How the approver / auditor sees history:** The delivery lead reviews run logs and the per-category counts used in the reconciliation report.

### Functional Capabilities
- Category and style traversal of the public moulding catalogue
- Parsing of listing markup (code, thickness, width, style, species, image)
- Product view fetch for species options
- Throttling (for example one request every 1–2 seconds), retries, resume from checkpoint
- Raw dataset (JSON/CSV) and run log with per-category counts
- Alternative input adapter for a supplier data file

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Crawl category and style listing pages
- Extract product attributes from listing markup
- Fetch product view and species options
- Throttle, retry and resume extraction
- Ingest supplier-provided data file
- Write raw dataset and run log

### Inputs
- Category and style list
- Throttle and retry settings
- Optional supplier data file

### Outputs
- Raw product records
- Image URL list
- Run log with per-category counts

### Business Rules
- Only publicly accessible pages are read; no login and no circumvention of blocks
- Requests are throttled to avoid load on the source site
- Every record keeps its source URL and capture date

### Validations
- Each record has code, category and image URL; missing fields are flagged

### Calculations
- Per-category product counts

### Workflow
Configured → Running → Completed | Partially completed (resume)

### Search Requirements
- None

### Documents
- Run logs

### Reports
- Per-category extraction counts

### Notifications
- None

### Security
- Runs from the delivery environment; no credentials stored

### Integrations
- Brenlo public catalogue (read-only)

### Dependencies
- Garrison confirmation of Brenlo permission (before publication)

### Assumptions
- Source markup stays stable during the project
- Some category URLs currently return access errors remotely; these are captured by browser-based or manual capture within the per-product contingency

### Risks
- Source site blocks automated access; supplier data file or manual capture used instead

### Non Functional Requirements
- Full extraction completes within a few hours at a polite request rate

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Crawl category and style listing pages | Complex | 8 |
| API | Extract product attributes from listing markup | Medium | 6 |
| API | Fetch product view and species options | Medium | 6 |
| API | Throttle, retry and resume extraction | Medium | 6 |
| API | Ingest supplier-provided data file | Medium | 6 |
| API | Write raw dataset and run log | Easy | 4 |
| Database | Raw extraction dataset structure | Simple | 1 |
| Integration | Source catalogue read-only web access (markup parsing) | Medium | 16 |
| Testing | Extraction accuracy against sampled pages | Medium | 6 |
| Testing | Resilience to failed or blocked requests | Easy | 4 |
| Documentation | Extraction run guide | Easy | 2 |

**Feature Total: 65 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 36 | 1 | 16 | 10 | 2 | **65** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Markup-parsing source treated as a Medium integration (mapping and retry)
- No user interface; command-line utility
