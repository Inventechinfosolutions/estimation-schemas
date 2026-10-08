# F12-004 — Catalogue Export & Bulk Update

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-004 |
| Feature Name | Catalogue Export & Bulk Update |
| Module | 12 — Catalogue Data Import & Bulk Operations |
| Module Type | Technical |
| Release | Optional |

### Description
Export catalogue data (filtered products with core, attribute, material, finish, length and provenance columns) to a spreadsheet, edit offline, and re-upload as a bulk update with diff preview, validation and audit. Recommended for post-launch normalisation and large-scale corrections.

### Business Objective
Allow Garrison to make large-scale corrections (for example renaming a finish across 300 products) efficiently after launch.

### Actors
- Catalogue Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates exports and bulk update jobs.
2. **How they create:** They export the filtered product set, edit the spreadsheet, then upload it in the Bulk update wizard and review the field-level diff.
3. **How they edit:** They exclude rows from the update or re-upload a corrected file before applying.
4. **How they send for approval:** Bulk updates to Published products create working drafts that follow the review workflow; Draft products are updated directly.
5. **How the approver sees pending items:** Reviewers see the resulting working drafts in the review queue.
6. **How the approver decides:** Reviewers approve or request changes per product (bulk approve available).
7. **How the maker sees history:** The administrator sees bulk update job history.
8. **How the approver / auditor sees history:** Auditors see per-product changes from bulk updates in the audit log.

### Functional Capabilities
- Filtered export with column selection
- Bulk update upload with field-level diff preview
- Validation identical to import
- Working drafts for Published products
- Job history

### UI Screens
- Catalogue export dialog with column selection
- Bulk update wizard with diff preview

### Logical API Operations
- Export catalogue to spreadsheet
- Parse and validate bulk update file
- Apply bulk update with audit

### Inputs
- Filters, columns, edited spreadsheet

### Outputs
- Export file
- Updated drafts
- Job log

### Business Rules
- Product code is the immutable key
- Published products are never changed directly

### Validations
- Same validation as import

### Calculations
- Diff counts

### Workflow
Exported → Edited offline → Uploaded → Previewed → Applied

### Search Requirements
- Job history by date and user

### Documents
- Export files

### Reports
- Bulk update job report

### Notifications
- Job completion email

### Security
- Import permission

### Integrations
- None

### Dependencies
- F12-001
- F12-003
- F06-002

### Assumptions
- Optional; reuses import validation

### Risks
- Mass changes need careful review; diff preview mitigates

### Non Functional Requirements
- Export of 10,000 products under 2 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Catalogue export dialog with column selection | Medium | 6 |
| UI | Bulk update wizard with diff preview | Very High | 16 |
| API | Export catalogue to spreadsheet | Complex | 8 |
| API | Parse and validate bulk update file | Very High | 16 |
| API | Apply bulk update with audit | Complex | 8 |
| Database | Bulk update job log | Easy | 2 |
| Testing | Export completeness | Easy | 4 |
| Testing | Bulk update diff, validation and audit | Medium | 6 |
| Documentation | Bulk update guide | Easy | 2 |

**Feature Total: 68 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 32 | 2 | 0 | 10 | 2 | **68** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Bulk update parsing reuses import validators but is still a Very High import API
- No external integration channel in this feature; Integration row omitted.
