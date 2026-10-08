# F06-001 — Data Completeness & Duplicate Validation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-001 |
| Feature Name | Data Completeness & Duplicate Validation |
| Module | 06 — Content Governance & Publishing Workflow |
| Module Type | Business |
| Release | Go-live |

### Description
Evaluate each product and combination against baseline mandatory rules (code, name, category, description, applicable dimensions, profile drawing where available, source and source reference for external products) and template-driven conditional rules (material, finish, length, applications, related products, technical documents). Calculate a completeness score and detect probable duplicates by code, normalised name and dimension similarity.

### Business Objective
Stop incomplete or duplicate profiles reaching the public catalogue, and give Garrison visibility of data quality during population.

### Actors
- Catalogue Administrator
- Catalogue Reviewer
- Super Administrator

### User Journey
1. **Who creates:** Completeness results are produced automatically by the system whenever a product or combination is saved; baseline rule settings are maintained by the Catalogue Administrator.
2. **How they create:** The completeness checklist in the workspace lists each rule as pass/fail with jump-to-field; a duplicate warning appears when a probable duplicate is found.
3. **How they edit:** Makers fix failing items; they mark a duplicate warning as 'Not a duplicate' with a reason, or abandon the record.
4. **How they send for approval:** Submission for review is blocked until all mandatory rules pass and duplicate warnings are resolved (F06-002).
5. **How the approver sees pending items:** Reviewers see the completeness score and duplicate resolution in the review workspace.
6. **How the approver decides:** Reviewers may request changes if they disagree with a 'Not a duplicate' resolution.
7. **How the maker sees history:** Makers see completeness history and resolutions on the record.
8. **How the approver / auditor sees history:** Auditors and the Super Administrator see the data quality dashboard and rule setting changes in the audit log.

### Functional Capabilities
- Baseline mandatory rules (configurable list)
- Template-driven conditional rules
- External-product rules (source and source reference mandatory)
- Completeness score (percentage of applicable rules met) and band (Complete, Nearly complete, Incomplete)
- Duplicate detection: exact code, code without punctuation, normalised name similarity, same category plus dimensions within tolerance
- Duplicate comparison dialog and 'Not a duplicate' resolution
- Data quality dashboard (by category, band, top missing fields, unresolved duplicates)

### UI Screens
- Completeness checklist panel with jump-to-field
- Completeness rule settings
- Duplicate warning dialog with side-by-side comparison
- Data quality dashboard

### Logical API Operations
- Evaluate completeness for product or combination
- Calculate completeness score
- Detect probable duplicates
- Get data quality dashboard aggregates
- Save completeness rule settings
- Resolve duplicate warning

### Inputs
- Product/combination data
- Rule settings
- Duplicate tolerance (default ±1/32 inch on all dimensions)

### Outputs
- Pass/fail per rule
- Completeness score and band
- Duplicate warnings and resolutions
- Dashboard aggregates

### Business Rules
- Products failing mandatory rules cannot be submitted for review
- Unresolved duplicate warnings block submission
- Rules are re-evaluated on every save and before publish

### Validations
- Tolerance values positive

### Calculations
- Completeness score = rules passed ÷ applicable rules × 100
- Name similarity on normalised tokens (case, punctuation and stop-word insensitive)

### Workflow
Evaluated continuously; gate applied at submission and publish

### Search Requirements
- Dashboard filters by category, band, missing field

### Documents
- None

### Reports
- Data quality dashboard
- Incomplete products export

### Notifications
- None

### Security
- Rule settings: Catalogue Administrator; dashboard: all admin roles

### Integrations
- None

### Dependencies
- F03-002
- F04-001
- F04-002
- F07-002
- F06-002

### Assumptions
- Duplicate detection runs within the catalogue only (not against external websites)

### Risks
- False-positive duplicates on very similar profiles; resolution is quick and remembered

### Non Functional Requirements
- Evaluation under 300 ms per save; dashboard under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Completeness checklist panel with jump-to-field | Complex | 12 |
| UI | Completeness rule settings | Medium | 6 |
| UI | Duplicate warning dialog with side-by-side comparison | Complex | 12 |
| UI | Data quality dashboard | Very High | 16 |
| API | Evaluate completeness for product or combination | Complex | 8 |
| API | Calculate completeness score | Medium | 6 |
| API | Detect probable duplicates | Complex | 8 |
| API | Get data quality dashboard aggregates | Medium | 6 |
| API | Save completeness rule settings | Easy | 4 |
| API | Resolve duplicate warning | Easy | 4 |
| Database | Completeness snapshot and score | Easy | 2 |
| Database | Duplicate resolution decisions | Easy | 2 |
| Testing | Baseline and conditional rules per category | Complex | 8 |
| Testing | Duplicate detection accuracy cases | Medium | 6 |
| Testing | External product source rules | Easy | 4 |
| Documentation | Data quality rules reference | Medium | 3 |

**Feature Total: 107 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 46 | 36 | 4 | 0 | 18 | 3 | **107** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Dashboard is a Very High UI
- Duplicate similarity logic drives a Complex API row
- No external integration channel in this feature; Integration row omitted.
