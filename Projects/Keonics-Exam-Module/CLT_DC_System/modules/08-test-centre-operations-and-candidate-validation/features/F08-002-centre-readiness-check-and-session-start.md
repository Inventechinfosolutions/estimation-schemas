# F08-002 — Centre Readiness Check & Session Start

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-002 |
| Feature Name | Centre Readiness Check & Session Start |
| Module | 08 — Test Centre Operations & Candidate Validation |
| Module Type | Business |
| Release | Go-live |

### Description
Centre readiness console: terminal heartbeat and client version check, network latency test, candidate list availability, recording readiness, sanity check report sent to central control, and proctor-initiated start within the time window, with hold and restart options.

### Business Objective
Start each session only when the centre is ready.

### Actors
- Proctor
- Centre Operator
- Examination Monitoring Unit

### User Journey
1. **Who creates:** The centre operator runs readiness before the session.
2. **How they create:** Checks run automatically; failures are listed.
3. **How they edit:** Faulty terminals are marked and seats reallocated.
4. **How they send for approval:** Readiness is submitted to central control; start needs EMU green signal where configured.
5. **How the approver sees pending items:** EMU sees readiness of all centres.
6. **How the approver decides:** EMU allows start or holds.
7. **How the applicant / maker sees history:** Proctor sees readiness and starts the session.
8. **How the approver / auditor sees history:** Auditors see readiness reports.

### Functional Capabilities
- Terminal heartbeat and version check
- Network test
- Camera and recording check
- Candidate list sync
- Readiness report to central
- Proctor start with time window
- Hold and restart

### UI Screens
- Centre readiness console
- Session start panel

### Logical API Operations
- Terminal heartbeat
- Readiness evaluation
- Submit readiness
- Start session
- Hold / restart session

### Inputs
- Terminal status

### Outputs
- Started session

### Business Rules
- Start only within window and with proctor present
- No local database at centre

### Validations
- All checks green or overridden with reason

### Calculations
- Ready terminals vs booked candidates

### Workflow
Not Ready → Ready → Started → Closed

### Search Requirements
- None

### Documents
- Readiness report

### Reports
- Readiness

### Notifications
- Readiness failures to EMU

### Security
- Centre IP

### Integrations
- None

### Dependencies
- F02-002
- F07-003
- F12-001

### Assumptions
- Centres provide hardware and network

### Risks
- Centre network

### Non Functional Requirements
- Heartbeat every 15 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Centre readiness console | Complex | 12 |
| UI | Session start panel | Medium | 6 |
| API | Terminal heartbeat | Medium | 6 |
| API | Readiness evaluation | Medium | 6 |
| API | Submit readiness | Easy | 4 |
| API | Start session | Medium | 6 |
| API | Hold / restart session | Medium | 6 |
| Database | Readiness and session state | Easy | 2 |
| Testing | Readiness and start tests | Complex | 8 |
| Documentation | Centre readiness checklist | Easy | 2 |

**Feature Total: 58 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 28 | 2 | 0 | 8 | 2 | **58** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Real-time readiness rated Complex
- No external integration channel in this feature; Integration row omitted.
