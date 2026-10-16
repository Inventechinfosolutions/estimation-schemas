# F11-005 — Configurable Report Builder

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-005 |
| Feature Name | Configurable Report Builder |
| Module | 11 — Dashboards, MIS & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Report builder for authorised users to choose a data set (sites, payments, cases, notifications), select columns, filters, grouping and totals, save reports privately or share by role, and export, with DS isolation enforced.

### Business Objective
Let BDA create new reports without vendor changes.

### Actors
- Auction Admin
- Finance Officer
- Commissioner / Read-only Viewer

### User Journey
1. **Who creates:** Authorised users create reports.
2. **How they create:** The user selects a data set, columns, filters and grouping and previews.
3. **How they edit:** The user edits and saves versions.
4. **How they send for approval:** Sharing to roles can require Auction Admin approval (configurable).
5. **How the approver sees pending items:** The Auction Admin sees share requests.
6. **How the approver decides:** The Auction Admin approves or rejects sharing.
7. **How the applicant / maker sees history:** Users see their saved and shared reports.
8. **How the approver / auditor sees history:** Auditors see report definitions and runs.

### Functional Capabilities
- Curated data sets
- Column, filter, group and total selection
- Preview
- Save and share
- Export

### UI Screens
- Report builder
- Saved reports
- Share approval

### Logical API Operations
- Data set metadata
- Build and run dynamic query with isolation
- Save / share report
- Approve share
- Export

### Inputs
- Selections

### Outputs
- Custom reports

### Business Rules
- Only curated data sets; no free SQL
- Masked fields stay masked

### Validations
- Row limits

### Calculations
- Group totals

### Workflow
Draft → Saved → Shared

### Search Requirements
- Saved reports

### Documents
- Exports

### Reports
- Custom

### Notifications
- Share approval

### Security
- DS isolation and masking

### Integrations
- None

### Dependencies
- F01-003
- F11-004

### Assumptions
- None

### Risks
- Performance of ad hoc queries; row limits

### Non Functional Requirements
- Query timeout 60 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Report builder | Complex | 12 |
| UI | Saved reports | Easy | 4 |
| UI | Share approval | Easy | 4 |
| API | Data set metadata | Medium | 6 |
| API | Build and run dynamic query with isolation | Very High | 16 |
| API | Save / share report | Easy | 4 |
| API | Approve share | Easy | 4 |
| API | Export | Easy | 4 |
| Database | Saved report definitions | Easy | 2 |
| Testing | Builder and isolation tests | Complex | 8 |
| Documentation | Report builder guide | Easy | 2 |

**Feature Total: 66 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 34 | 2 | 0 | 8 | 2 | **66** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Dynamic query with isolation rated Very High
- No external integration channel in this feature; Integration row omitted.
