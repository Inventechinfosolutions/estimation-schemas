# F08-006 — Attendance Sheets, Scans & Centre Incident Records

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-006 |
| Feature Name | Attendance Sheets, Scans & Centre Incident Records |
| Module | 08 — Test Centre Operations & Candidate Validation |
| Module Type | Business |
| Release | Go-live |

### Description
Digital attendance from validation and login, printable attendance sheet with signatures, upload of scanned commission copy of admission certificates and signed attendance sheets after the session, centre incident log (power, network, malpractice, health), and session closure report.

### Business Objective
Keep complete session records as required by the RFP.

### Actors
- Proctor
- Centre Operator
- EMU

### User Journey
1. **Who creates:** The proctor records attendance and incidents during the session.
2. **How they create:** The proctor logs incidents with time and affected candidates; prints attendance sheet.
3. **How they edit:** Incidents can be updated until closure.
4. **How they send for approval:** Session closure with uploads goes to EMU.
5. **How the approver sees pending items:** EMU sees closure reports.
6. **How the approver decides:** EMU accepts or asks for missing uploads.
7. **How the applicant / maker sees history:** The proctor sees closure status.
8. **How the approver / auditor sees history:** Auditors see scans and incidents.

### Functional Capabilities
- Digital attendance
- Attendance sheet PDF
- Scan uploads
- Incident log with categories
- Closure report
- Missing upload reminders

### UI Screens
- Attendance and incident console
- Scan upload
- Closure report

### Logical API Operations
- Attendance summary
- Generate attendance sheet
- Upload scans
- Log incident
- Close session

### Inputs
- Incidents
- Scans

### Outputs
- Closure report

### Business Rules
- Closure requires scans

### Validations
- File types

### Calculations
- Present / absent counts

### Workflow
Open → Closed → Accepted

### Search Requirements
- Incidents

### Documents
- Attendance sheets
- Admission certificates

### Reports
- Attendance
- Incidents

### Notifications
- Missing upload reminders

### Security
- Centre scope

### Integrations
- None

### Dependencies
- F08-003
- F12-004

### Assumptions
- Scanners at centres

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Attendance and incident console | Medium | 6 |
| UI | Scan upload | Easy | 4 |
| UI | Closure report | Easy | 4 |
| API | Attendance summary | Easy | 4 |
| API | Generate attendance sheet | Easy | 4 |
| API | Upload scans | Easy | 4 |
| API | Log incident | Easy | 4 |
| API | Close session | Medium | 6 |
| Database | Attendance, incidents and scans | Easy | 2 |
| Testing | Closure tests | Easy | 4 |
| Documentation | Session closure SOP | Easy | 2 |

**Feature Total: 44 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 22 | 2 | 0 | 4 | 2 | **44** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
