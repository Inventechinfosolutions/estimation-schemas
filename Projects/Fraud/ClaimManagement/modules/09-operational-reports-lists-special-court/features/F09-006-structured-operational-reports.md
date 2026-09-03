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
1. Who creates: Officer
2. How they create: Officer chooses a report type: depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, or user/activity.
3. How they edit: Officer sets filters and generates the report from structured records.
4. How they send for approval: Publishing a PDF on a home page is not how the report is produced. Choose type → filter → generate → export if allowed.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Report catalogue of the SOW types including FE-wise views on imported FE references.
- Filter and generate from structured records.
- Authorised export.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Report catalogue and filters | Complex |
| Report generate and export | Medium |
| Structured operational reports history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Structured report engine | Very High |
| Update structured operational reports | Medium |
| Search structured operational reports | Medium |
| Read structured operational reports history | Easy |

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
| Structured operational reports history | UI | Medium | 6 |
| Structured report engine | API | Very High | 16 |
| Update structured operational reports | API | Medium | 6 |
| Search structured operational reports | API | Medium | 6 |
| Read structured operational reports history | API | Easy | 4 |
| Report query support | DB | Complex | 6 |
| Structured operational reports feature tests | Testing | Very High | 12 |
| Structured operational reports implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
