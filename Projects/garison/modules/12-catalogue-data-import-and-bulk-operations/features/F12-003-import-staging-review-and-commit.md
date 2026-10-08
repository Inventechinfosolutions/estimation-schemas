# F12-003 — Import Staging Review & Commit

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-003 |
| Feature Name | Import Staging Review & Commit |
| Module | 12 — Catalogue Data Import & Bulk Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Review staged import rows in a spreadsheet-like grid with inline correction and re-validation, compare rows that update existing products, commit valid rows as Draft products (create or update mode), and roll back a committed batch if needed.

### Business Objective
Give the population team a controlled checkpoint between raw data and catalogue records.

### Actors
- Catalogue Administrator
- Data population team

### User Journey
1. **Who creates:** The importer works on a staged batch created in F12-001.
2. **How they create:** In the Staging grid they filter to error rows, correct values inline (re-validated immediately) and open the compare view for updates to existing products.
3. **How they edit:** They continue correcting until rows are valid, then commit; a committed batch can be rolled back while its products remain Draft.
4. **How they send for approval:** Commit does not need approval; committed products follow the review workflow before publication.
5. **How the approver sees pending items:** There is no approver inbox for staging.
6. **How the approver decides:** No decision applies on the batch.
7. **How the maker sees history:** Importers see batch status and commit results.
8. **How the approver / auditor sees history:** Auditors see commit and rollback with counts in the audit log.

### Functional Capabilities
- Staging grid with filters (errors, warnings, valid) and inline editing
- Immediate row re-validation
- Compare view for update rows (existing versus staged)
- Commit modes: create only, update only, create and update
- Commit summary and confirmation
- Rollback of a committed batch (only while products are Draft)

### UI Screens
- Staging grid with inline correction
- Staged record compare with existing product
- Commit summary and confirmation

### Logical API Operations
- Get staged rows with filters
- Update staged row and re-validate
- Commit batch as Draft products
- Roll back committed batch

### Inputs
- Corrections, commit mode

### Outputs
- Draft products created or updated
- Commit report

### Business Rules
- Only valid rows commit
- Updates to Published products create working drafts
- Rollback blocked once any product from the batch is In Review or beyond

### Validations
- Inline edits validated with the same rules as import

### Calculations
- Commit counts

### Workflow
Staged → Committed → (optional) Rolled back

### Search Requirements
- Grid filters by status, code, category

### Documents
- None

### Reports
- Commit report

### Notifications
- Import completed email

### Security
- Import permission

### Integrations
- None

### Dependencies
- F12-001
- F12-002
- F04-001
- F06-002

### Assumptions
- Batches up to 5,000 rows

### Risks
- Large grids in the browser; virtualised grid used

### Non Functional Requirements
- Grid handles 5,000 rows smoothly (virtual scrolling)

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Staging grid with inline correction | Very High | 16 |
| UI | Staged record compare with existing product | Complex | 12 |
| UI | Commit summary and confirmation | Medium | 6 |
| API | Get staged rows with filters | Medium | 6 |
| API | Update staged row and re-validate | Complex | 8 |
| API | Commit batch as Draft products | Very High | 16 |
| API | Roll back committed batch | Complex | 8 |
| Database | Staging-to-product lineage | Easy | 2 |
| Testing | Commit create and update modes | Complex | 8 |
| Testing | Rollback integrity | Medium | 6 |
| Documentation | Population runbook | Medium | 3 |

**Feature Total: 91 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 38 | 2 | 0 | 14 | 3 | **91** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Editable staging grid is a Very High UI
- Batch commit is a Very High transactional API
- No external integration channel in this feature; Integration row omitted.
