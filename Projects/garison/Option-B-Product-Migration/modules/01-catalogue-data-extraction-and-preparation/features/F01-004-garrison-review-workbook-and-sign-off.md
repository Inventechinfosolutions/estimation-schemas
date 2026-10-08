# F01-004 — Garrison Review Workbook & Sign-off

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-004 |
| Feature Name | Garrison Review Workbook & Sign-off |
| Module | 01 — Catalogue Data Extraction & Preparation |
| Module Type | Technical |
| Release | Go-live |

### Description
Export the master dataset to an Excel review workbook (thumbnail link, code, category, style, dimensions, species, include/exclude, rename columns), import Garrison's decisions back, apply them to the dataset, and record a change log per review round until sign-off.

### Business Objective
Give Garrison control over which products appear and how they are named, without an admin portal.

### Actors
- Garrison catalogue owner
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer creates the review workbook from the master dataset.
2. **How they create:** Garrison opens the workbook and marks each product Include/Exclude, optionally renaming the category or display name.
3. **How they edit:** Garrison can return the workbook several times; each round is re-imported and compared with the previous round.
4. **How they send for approval:** Garrison sends the completed workbook back by email as its approval submission.
5. **How the approver sees pending items:** The delivery lead tracks review rounds in the change log; there is no in-system inbox.
6. **How the approver decides:** Garrison's sign-off email on the final round is the approval decision; the dataset is then frozen.
7. **How the maker sees history:** Garrison sees the change log summarising applied decisions per round.
8. **How the approver / auditor sees history:** The delivery lead keeps workbooks, change logs and the sign-off email as the audit record.

### Functional Capabilities
- Review workbook export with image links and decision columns
- Import and validation of Garrison decisions
- Application of include/exclude and renames to the dataset
- Change log per review round
- Dataset freeze on sign-off

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Export review workbook
- Import and apply Garrison decisions
- Generate change log between review rounds

### Inputs
- Master dataset
- Completed review workbook

### Outputs
- Reviewed master dataset
- Change log
- Frozen dataset on sign-off

### Business Rules
- Excluded products are never loaded
- Renames apply only to display fields, not the product code
- Dataset frozen after sign-off; later changes go through a refresh

### Validations
- Decision column values limited to Include/Exclude
- Workbook rows match dataset keys

### Calculations
- Included product count for the reconciliation report

### Workflow
Issued → Returned → Applied → (repeat) → Signed off

### Search Requirements
- None

### Documents
- Review workbooks, sign-off email

### Reports
- Change log per round

### Notifications
- Email exchange with Garrison (outside the system)

### Security
- Workbooks shared through an agreed secure channel

### Integrations
- None

### Dependencies
- F01-003

### Assumptions
- At most two review rounds

### Risks
- Late review rounds delay loading

### Non Functional Requirements
- Workbook opens in standard Excel

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Export review workbook | Complex | 8 |
| API | Import and apply Garrison decisions | Complex | 8 |
| API | Generate change log between review rounds | Easy | 4 |
| Database | Review decision log | Simple | 1 |
| Testing | Round-trip of review decisions | Easy | 4 |
| Documentation | Review instructions for Garrison | Easy | 2 |

**Feature Total: 27 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 1 | 0 | 4 | 2 | **27** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Workbook export with thumbnails and decision import are Complex scripts
- No external integration channel in this feature; Integration row omitted.
