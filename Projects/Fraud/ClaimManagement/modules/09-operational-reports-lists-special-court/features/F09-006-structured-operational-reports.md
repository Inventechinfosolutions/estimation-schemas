# F09-006 — Structured operational reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-006 |
| **Feature Name** | Structured operational reports |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
The Officer chooses a report type (depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, user/activity), sets filters, and generates it from structured records. Publishing a PDF on a home page is not the way these reports are produced.

### Business Objective
Produce operational reports from structured depositor, asset and claim data rather than PDF publishing on a website.

### Actors
Officer; Administrator; auditor as authorised.

### User Journey
1. Officer chooses a report type: depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, or user/activity.
2. Officer sets filters and generates the report from structured records.
3. Publishing a PDF on a home page is not how the report is produced.

### Functional Capabilities
- Report catalogue of the SOW types including FE-wise views on imported FE references.
- Filter and generate from structured records.
- Authorised export.

### Inputs
Report type, filters (FE, scheme, dates, status, Post).

### Outputs
Structured operational report.

### Business Rules
- PDF publishing alone is not sufficient.
- Role/Post mapping reports are F09-007.
- Visibility follows Module 01.

### Validations
- Report type from the catalogue.
- Filters cannot return unauthorised KYC packs as a dump if the Post lacks rights.

### Calculations
Aggregations per report type.

### Workflow
Choose type → filter → generate → export if allowed.

### Search Requirements
Report runs by type, date, user.

### Documents
Generated report files as exports, not homepage content.

### Reports
Depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, user/activity, FE-wise.

### Notifications
None.

### Security
Need-to-know. User/activity reports are auditor/Administrator class.

### Integrations
None.

### Dependencies
Structured data from Modules 02–08; F01.

### Assumptions
- Website review requirement for automated reports from structured data applies.

### Risks
- Reverting to homepage PDFs would fail acceptance criterion 15.

### Non Functional Requirements
Structured data; searchable filters; not .org homepage publishing as the method.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Report catalogue and filters | UI | Complex | 12 |
| Report generate and export | UI | Medium | 6 |
| Structured report engine | API | Very High | 16 |
| Report query support | DB | Complex | 6 |
| Structured report tests | Testing | Very High | 12 |
| Operational reports guide | Documentation | Complex | 4 |
| **Total** | | | **56** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Court-facing ED/Special Court formats are F09-001/F09-002, not this catalogue.
