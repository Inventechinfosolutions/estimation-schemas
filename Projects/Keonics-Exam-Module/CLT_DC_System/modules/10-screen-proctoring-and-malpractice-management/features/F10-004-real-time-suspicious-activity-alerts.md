# F10-004 — Real-Time Suspicious Activity Alerts

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-004 |
| Feature Name | Real-Time Suspicious Activity Alerts |
| Module | 10 — Screen Proctoring & Malpractice Management |
| Module Type | Business |
| Release | Go-live |

### Description
Real-time alert service consolidating webcam, activity, recording and network events into alerts with severity, candidate, seat and evidence; pushed to proctor console and EMU dashboard via websockets with acknowledgement, escalation if unacknowledged, and live view of candidate screen snapshot.

### Business Objective
Allow immediate intervention.

### Actors
- Proctor
- EMU

### User Journey
1. **Who creates:** Alerts are created by detection services.
2. **How they create:** Alerts appear on consoles.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Unacknowledged alerts escalate to EMU.
5. **How the approver sees pending items:** Proctor and EMU see live alert lists.
6. **How the approver decides:** They acknowledge, act or escalate to case.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see alert handling times.

### Functional Capabilities
- Alert correlation
- Severity rules
- Websocket push
- Acknowledgement and escalation
- Live snapshot view
- Alert-to-case conversion

### UI Screens
- Proctor alert console
- EMU alert wall
- Alert detail with evidence

### Logical API Operations
- Alert correlation service
- Real-time push channel
- Acknowledge / escalate
- Live snapshot fetch

### Inputs
- Detection events

### Outputs
- Alerts

### Business Rules
- High severity unacknowledged in 2 minutes escalates

### Validations
- None

### Calculations
- Response time

### Workflow
New → Acknowledged → Closed / Case

### Search Requirements
- Alerts

### Documents
- Evidence

### Reports
- Alert response times

### Notifications
- Console alerts

### Security
- Scope by centre

### Integrations
- None

### Dependencies
- F10-002
- F10-003
- F12-001

### Assumptions
- None

### Risks
- Alert fatigue

### Non Functional Requirements
- Alert within 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Proctor alert console | Complex | 12 |
| UI | EMU alert wall | Complex | 12 |
| UI | Alert detail with evidence | Medium | 6 |
| API | Alert correlation service | Complex | 8 |
| API | Real-time push channel | Complex | 8 |
| API | Acknowledge / escalate | Easy | 4 |
| API | Live snapshot fetch | Medium | 6 |
| Database | Alerts | Easy | 2 |
| Testing | Alert latency and load tests | Complex | 8 |
| Documentation | Alert handling SOP | Easy | 2 |

**Feature Total: 68 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 26 | 2 | 0 | 8 | 2 | **68** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Real-time channel rated Complex
- No external integration channel in this feature; Integration row omitted.
