# F12-001 — Import Templates & Bulk Product Import

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-001 |
| Feature Name | Import Templates & Bulk Product Import |
| Module | 12 — Catalogue Data Import & Bulk Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Generate category-specific import templates (spreadsheet with template columns, permitted value lists, unit guidance and provenance columns) and import product records in bulk into a staging area with row-level validation against templates, masters, dimension parser, code uniqueness and duplicates.

### Business Objective
Load the initial catalogue (and future batches) quickly and accurately, as the core tooling of the population workstream.

### Actors
- Catalogue Administrator
- Data population team (with Catalogue Administrator access)

### User Journey
1. **Who creates:** The Catalogue Administrator or the population team creates import batches.
2. **How they create:** In the Import centre they download the template for a category, fill it offline, then use the Upload wizard to upload the file, map optional columns and start validation.
3. **How they edit:** They correct errors by fixing the file and re-uploading, or by correcting rows in staging (F12-003).
4. **How they send for approval:** Import does not publish; committed records become Draft products that follow the normal review workflow (Module 06).
5. **How the approver sees pending items:** There is no approver inbox for batches; reviewers see committed products in the review queue after submission.
6. **How the approver decides:** No decision applies on the batch; decisions are made per product in F06-003.
7. **How the maker sees history:** Importers see batch history with status, counts and error reports.
8. **How the approver / auditor sees history:** Auditors see batch uploads and commits in the audit log.

### Functional Capabilities
- Template generation per category from the published attribute template (columns, list validations, help row)
- Provenance and relationship columns
- Upload wizard for XLSX/CSV with column mapping
- Row-level validation: mandatory fields, permitted values, master lookups (material, finish, style), dimension parsing, code uniqueness, duplicates
- Validation error report (downloadable with row and column references)
- Import centre listing batches with status
- Background processing for large files

### UI Screens
- Import centre batch list
- Import template download by category
- Upload import file wizard
- Validation error report viewer

### Logical API Operations
- Generate category import template
- Upload and parse import file
- Validate staged rows against templates and masters
- Get batch status and errors
- Download validation error report

### Inputs
- Category, completed import file, column mappings

### Outputs
- Staged rows with validation results
- Error report

### Business Rules
- Import never overwrites Published content directly; updates create working drafts
- Rows failing validation cannot be committed
- Master values must exist (no auto-creation unless enabled by the Super Administrator)

### Validations
- File type XLSX/CSV; max 10 MB or 5,000 rows
- Header matches template version

### Calculations
- Row counts: total, valid, warnings, errors

### Workflow
Uploaded → Validated → Staged (→ F12-003 Commit)

### Search Requirements
- Batch list by category, user, status, date

### Documents
- Import templates, error reports

### Reports
- Batch validation report

### Notifications
- Import completed email (F06-005)

### Security
- Import permission (Super Administrator, Catalogue Administrator)
- Uploaded files scanned (F13-002)

### Integrations
- None

### Dependencies
- F03-002
- F03-004
- F02-003
- F06-001
- F12-003
- F13-002

### Assumptions
- Population team prepares data in templates; extraction from PDF catalogue is manual work in the population workstream

### Risks
- Source data inconsistencies produce many errors; normalisation rules agreed early

### Non Functional Requirements
- Validation of 2,000 rows under 2 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Import centre batch list | Medium | 6 |
| UI | Import template download by category | Medium | 6 |
| UI | Upload import file wizard | Very High | 16 |
| UI | Validation error report viewer | Complex | 12 |
| API | Generate category import template | Complex | 8 |
| API | Upload and parse import file | Very High | 16 |
| API | Validate staged rows against templates and masters | Very High | 16 |
| API | Get batch status and errors | Medium | 6 |
| API | Download validation error report | Easy | 4 |
| Database | Import batch and staging rows | Medium | 4 |
| Testing | Template generation per category | Medium | 6 |
| Testing | Validation rules on 2,000-row files | Complex | 8 |
| Testing | Malformed file handling | Easy | 4 |
| Documentation | Import template guide and field dictionary | Medium | 3 |

**Feature Total: 115 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 40 | 50 | 4 | 0 | 18 | 3 | **115** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- File parsing and validation are Very High import APIs
- Upload wizard with mapping is Very High UI
- No external integration channel in this feature; Integration row omitted.
