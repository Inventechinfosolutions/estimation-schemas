# F01-003 — Data Normalisation & Validation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-003 |
| Feature Name | Data Normalisation & Validation |
| Module | 01 — Catalogue Data Extraction & Preparation |
| Module Type | Technical |
| Release | Go-live |

### Description
Transform raw records into the master dataset: parse fractional dimensions (for example 5 1/2, 3 11/16) into numeric values while keeping display text, map source categories and styles to Garrison names, normalise species, detect duplicates and conflicts, generate slugs and SEO defaults, and produce a validation report.

### Business Objective
Produce one clean, consistent product dataset that drives all website pages and filters.

### Actors
- Delivery developer
- Delivery lead

### User Journey
1. **Who creates:** The delivery developer builds the master dataset from raw records.
2. **How they create:** Scripts apply parsing, mapping tables and validation, and write the master dataset and report.
3. **How they edit:** Mapping tables are adjusted after Garrison review (F01-004) and the build is re-run.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees validation reports per run.
8. **How the approver / auditor sees history:** The delivery lead reviews the validation report before the review workbook is issued.

### Functional Capabilities
- Fraction and mixed-number dimension parsing with numeric and display values
- Category, style and species mapping tables
- Duplicate and conflict detection (same code, same dimensions in the same category)
- Slug and default title/meta generation
- Validation report
- Master dataset in CSV and JSON

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Parse fractional dimensions to numeric values
- Map categories and styles to Garrison taxonomy
- Normalise species values
- Detect duplicates and conflicts
- Generate slugs and SEO defaults
- Produce validation report
- Build master dataset

### Inputs
- Raw dataset
- Mapping tables

### Outputs
- Master dataset
- Validation report

### Business Rules
- Product code plus category is the unique key
- Unmapped categories or styles block the build
- Display text for dimensions keeps the source fraction

### Validations
- Thickness and width parse to positive numbers
- Every product has a mapped category and an image

### Calculations
- Numeric dimension = whole + numerator ÷ denominator

### Workflow
Raw → Normalised → Validated → Master

### Search Requirements
- None

### Documents
- Data dictionary

### Reports
- Validation report

### Notifications
- None

### Security
- None specific

### Integrations
- None

### Dependencies
- F01-001
- F01-002

### Assumptions
- Garrison keeps Brenlo category names unless renamed in the review workbook

### Risks
- Ambiguous or missing dimensions on a few products; flagged for manual fix

### Non Functional Requirements
- Build runs in minutes and is repeatable

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Parse fractional dimensions to numeric values | Medium | 6 |
| API | Map categories and styles to Garrison taxonomy | Medium | 6 |
| API | Normalise species values | Easy | 4 |
| API | Detect duplicates and conflicts | Medium | 6 |
| API | Generate slugs and SEO defaults | Easy | 4 |
| API | Produce validation report | Easy | 4 |
| API | Build master dataset | Medium | 6 |
| Database | Master dataset schema | Easy | 2 |
| Database | Category, style and species mapping tables | Easy | 2 |
| Testing | Normalisation and mapping rules | Medium | 6 |
| Testing | Reconciliation of master dataset against raw extraction | Easy | 4 |
| Documentation | Data dictionary and taxonomy mapping sheet | Medium | 3 |

**Feature Total: 53 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 36 | 4 | 0 | 10 | 3 | **53** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Scripted transformations; mapping tables keep rules data-driven
- No external integration channel in this feature; Integration row omitted.
