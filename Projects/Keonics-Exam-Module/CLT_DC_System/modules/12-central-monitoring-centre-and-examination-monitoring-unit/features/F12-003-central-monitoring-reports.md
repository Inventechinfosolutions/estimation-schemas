# F12-003 — Central Monitoring Reports

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-003 |
| Feature Name | Central Monitoring Reports |
| Module | 12 — Central Monitoring Centre & Examination Monitoring Unit |
| Module Type | Business |
| Release | Go-live |

### Description
Reports for each test day: start-of-test report (centres started on time, delays), exception report (incidents, alerts, compensations, rejections), completion report (attendance, submissions, scores summary), and session summary for KEONICS, exportable to PDF / Excel.

### Business Objective
Provide the reports required from the Central Monitoring Centre.

### Actors
- EMU
- KEONICS

### User Journey
1. **Who creates:** Reports generate automatically at session milestones.
2. **How they create:** Users run reports for dates.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Users see reports.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see report logs.

### Functional Capabilities
- Start-of-test report
- Exception report
- Completion report
- Session summary
- PDF / Excel export
- Scheduled distribution

### UI Screens
- Monitoring reports

### Logical API Operations
- Start report
- Exception report
- Completion report
- Scheduled distribution

### Inputs
- Session data

### Outputs
- Reports

### Business Rules
- Scope by role

### Validations
- None

### Calculations
- Delays, rates

### Workflow
Not applicable

### Search Requirements
- By date

### Documents
- Report PDFs

### Reports
- As listed

### Notifications
- Report e-mail

### Security
- Role scope

### Integrations
- None

### Dependencies
- F12-001

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Under 10 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Monitoring reports | Medium | 6 |
| API | Start report | Medium | 6 |
| API | Exception report | Medium | 6 |
| API | Completion report | Medium | 6 |
| API | Scheduled distribution | Easy | 4 |
| Database | Report snapshots | Easy | 2 |
| Testing | Report reconciliation tests | Medium | 6 |
| Documentation | Report catalogue | Simple | 1 |

**Feature Total: 37 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 22 | 2 | 0 | 6 | 1 | **37** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
