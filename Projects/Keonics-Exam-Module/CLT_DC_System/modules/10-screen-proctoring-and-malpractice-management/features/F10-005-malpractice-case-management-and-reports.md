# F10-005 — Malpractice Case Management & Reports

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-005 |
| Feature Name | Malpractice Case Management & Reports |
| Module | 10 — Screen Proctoring & Malpractice Management |
| Module Type | Business |
| Release | Go-live |

### Description
Case management for malpractice: creation from alerts or proctor reports, evidence bundle (recording clips, snapshots, activity logs, incident notes), candidate explanation (optional), committee decision (no action, warning, result cancelled, debarred for period), effect on result and future bookings, and malpractice reports.

### Business Objective
Handle malpractice consistently with evidence.

### Actors
- Proctor
- EMU
- Malpractice Committee
- Candidate

### User Journey
1. **Who creates:** Proctor or EMU creates a case.
2. **How they create:** The case is created with evidence attached automatically.
3. **How they edit:** Evidence and notes can be added.
4. **How they send for approval:** The case is submitted to the committee.
5. **How the approver sees pending items:** Committee sees pending cases.
6. **How the approver decides:** Committee decides; result withheld or cancelled accordingly.
7. **How the applicant / maker sees history:** Candidate sees outcome where applicable.
8. **How the approver / auditor sees history:** Auditors see case history.

### Functional Capabilities
- Case creation from alert
- Evidence bundle with clip extraction
- Candidate explanation
- Committee decision
- Result hold / cancel
- Debarment
- Malpractice reports

### UI Screens
- Case list
- Case detail with evidence player
- Committee decision
- Malpractice report

### Logical API Operations
- Create case
- Build evidence bundle and clips
- Record decision and apply effects
- Debarment check in booking
- Malpractice reports

### Inputs
- Alerts
- Notes

### Outputs
- Decisions

### Business Rules
- Result withheld while case open
- Debarred candidates cannot book

### Validations
- Decision reason

### Calculations
- Debarment end date

### Workflow
Open → Under Review → Decided → Closed

### Search Requirements
- Cases

### Documents
- Evidence bundle
- Decision letter

### Reports
- Malpractice reports

### Notifications
- Decision notice

### Security
- Restricted access

### Integrations
- None

### Dependencies
- F10-004
- F11-003

### Assumptions
- Committee formed by KEONICS

### Risks
- Legal challenges

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Case list | Medium | 6 |
| UI | Case detail with evidence player | Complex | 12 |
| UI | Committee decision | Medium | 6 |
| UI | Malpractice report | Medium | 6 |
| API | Create case | Medium | 6 |
| API | Build evidence bundle and clips | Complex | 8 |
| API | Record decision and apply effects | Medium | 6 |
| API | Debarment check in booking | Easy | 4 |
| API | Malpractice reports | Medium | 6 |
| Database | Cases, evidence references and decisions | Medium | 4 |
| Testing | Case workflow tests | Medium | 6 |
| Documentation | Malpractice SOP | Easy | 2 |

**Feature Total: 72 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 30 | 4 | 0 | 6 | 2 | **72** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
