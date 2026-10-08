# F04-004 — Garrison Review Workbook & Sign-off

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-004 |
| Feature Name | Garrison Review Workbook & Sign-off |
| Module | 04 — One-time Product Data Migration |
| Module Type | Technical |
| Release | Go-live |

### Description
Export the master dataset to an Excel review workbook (thumbnail link, code, category, style, dimensions, species, include/exclude and rename columns), import Garrison's decisions, apply them to the dataset and record a change log per round until sign-off. This replaces an admin portal for the one-time catalogue set-up.

### Business Objective
Give Garrison control over which products appear and how they are named, without an admin portal.

### Actors
- Garrison catalogue owner
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer creates the review workbook from the master dataset.
2. **How they create:** Garrison marks each product Include/Exclude and can rename categories or display names.
3. **How they edit:** Garrison can return the workbook more than once; each round is re-imported and compared with the previous one.
4. **How they send for approval:** Garrison emails the completed workbook back as its approval submission.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's sign-off email on the final round is the approval decision; the dataset is then frozen.
7. **How the maker sees history:** Garrison sees the change log of applied decisions per round.
8. **How the approver / auditor sees history:** The delivery lead keeps workbooks, change logs and the sign-off email as the audit record.

### Functional Capabilities
- Review workbook export with image links and decision columns
- Import and validation of decisions
- Application of include/exclude and renames
- Change log per round
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
- Reviewed and frozen master dataset
- Change log

### Business Rules
- Excluded products are never published
- Renames apply to display fields, not the product code
- Dataset frozen after sign-off

### Validations
- Decision values limited to Include/Exclude
- Workbook rows match dataset keys

### Calculations
- Included product count for reconciliation

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
- F04-003

### Assumptions
- At most two review rounds

### Risks
- Late review rounds delay publishing

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
