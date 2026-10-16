# F12-004 — Post-Test Wrap-Up & Archival

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-004 |
| Feature Name | Post-Test Wrap-Up & Archival |
| Module | 12 — Central Monitoring Centre & Examination Monitoring Unit |
| Module Type | Business |
| Release | Go-live |

### Description
Wrap-up after each session: closure checklist per centre, completeness checks (all responses, recordings, scans, attendance), archival of session data to long-term storage with checksums, terminal data wipe confirmation, and status report.

### Business Objective
Close every session cleanly and preserve records.

### Actors
- EMU
- Service Provider operations

### User Journey
1. **Who creates:** Wrap-up starts when all candidates submit.
2. **How they create:** Checks run; gaps listed.
3. **How they edit:** Gaps resolved by centre uploads.
4. **How they send for approval:** Archival approved by EMU.
5. **How the approver sees pending items:** EMU sees wrap-up status.
6. **How the approver decides:** EMU approves archival.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see archival records.

### Functional Capabilities
- Closure checklist
- Completeness checks
- Archival with checksums
- Terminal wipe confirmation
- Status report

### UI Screens
- Wrap-up console
- Archival status

### Logical API Operations
- Completeness checks
- Archive session
- Wipe confirmation
- Status report

### Inputs
- Session data

### Outputs
- Archive

### Business Rules
- Archive only when complete or exceptions approved

### Validations
- Checksums

### Calculations
- Completeness %

### Workflow
Open → Wrapped → Archived

### Search Requirements
- Archives

### Documents
- Status report

### Reports
- Wrap-up status

### Notifications
- Gap alerts

### Security
- Immutable archives

### Integrations
- None

### Dependencies
- F08-006
- F10-006
- F17-003

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Wrap-up console | Medium | 6 |
| UI | Archival status | Easy | 4 |
| API | Completeness checks | Medium | 6 |
| API | Archive session | Medium | 6 |
| API | Wipe confirmation | Easy | 4 |
| API | Status report | Easy | 4 |
| Database | Archive catalogue | Easy | 2 |
| Testing | Wrap-up tests | Medium | 6 |
| Documentation | Wrap-up SOP | Easy | 2 |

**Feature Total: 40 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 20 | 2 | 0 | 6 | 2 | **40** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
