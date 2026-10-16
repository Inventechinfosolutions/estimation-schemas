# F06-006 — Excel / CSV Question Import

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-006 |
| Feature Name | Excel / CSV Question Import |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Template-based bulk import of bilingual items with metadata, media references in a zip, validation report, staging, duplicate detection and submission into the review workflow.

### Business Objective
Avoid double entry of items prepared offline.

### Actors
- Question Bank Administrator
- SME Author

### User Journey
1. **Who creates:** The administrator or author uploads a file.
2. **How they create:** The system validates and shows a staging report.
3. **How they edit:** The uploader fixes errors and re-uploads.
4. **How they send for approval:** Valid items go to review.
5. **How the approver sees pending items:** Reviewers see imported items in the queue.
6. **How the approver decides:** As in F06-003.
7. **How the applicant / maker sees history:** The uploader sees import history.
8. **How the approver / auditor sees history:** Auditors see import logs.

### Functional Capabilities
- Downloadable template
- Excel / CSV parsing with Kannada Unicode
- Media zip mapping
- Validation report
- Duplicate detection
- Submit to review

### UI Screens
- Import upload
- Validation and staging report
- Import history

### Logical API Operations
- Parse and stage file
- Validate rows
- Commit to review

### Inputs
- Excel / CSV, media zip

### Outputs
- Items in review

### Business Rules
- Imported items still need review and committee

### Validations
- Mandatory columns

### Calculations
- None

### Workflow
Uploaded → Staged → Committed

### Search Requirements
- Imports

### Documents
- Template

### Reports
- Import report

### Notifications
- Import complete

### Security
- Encrypted staging

### Integrations
- None

### Dependencies
- F06-003

### Assumptions
- None

### Risks
- Unicode issues in Excel

### Non Functional Requirements
- 1,000 rows under 2 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Import upload | Easy | 4 |
| UI | Validation and staging report | Medium | 6 |
| UI | Import history | Easy | 4 |
| API | Parse and stage file | Complex | 8 |
| API | Validate rows | Medium | 6 |
| API | Commit to review | Medium | 6 |
| Database | Import staging | Easy | 2 |
| Testing | Import tests with Kannada data | Medium | 6 |
| Documentation | Import template guide | Easy | 2 |

**Feature Total: 44 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 20 | 2 | 0 | 6 | 2 | **44** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard import
- No external integration channel in this feature; Integration row omitted.
