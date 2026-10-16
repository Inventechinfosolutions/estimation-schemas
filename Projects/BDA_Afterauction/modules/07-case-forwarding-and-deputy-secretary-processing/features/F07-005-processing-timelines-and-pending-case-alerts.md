# F07-005 — Processing Timelines & Pending Case Alerts

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-005 |
| Feature Name | Processing Timelines & Pending Case Alerts |
| Module | 07 — Case Forwarding & Deputy Secretary Processing |
| Module Type | Business |
| Release | Go-live |

### Description
Tracking of time spent at each stage and task against configured limits, red / amber / green indicators, reminders to the responsible officer, escalation to the next level, and pendency reports by DS office, officer and stage.

### Business Objective
Make delays visible and ensure accountability for processing within timelines.

### Actors
- System
- Deputy Secretary
- Case Worker
- Commissioner / Read-only Viewer

### User Journey
1. **Who creates:** Timers are created automatically when tasks start.
2. **How they create:** The timer engine computes due dates and sends reminders and escalations.
3. **How they edit:** Timers are not edited; pauses happen through rules.
4. **How they send for approval:** No approval.
5. **How the approver sees pending items:** Officers see RAG status in queues; supervisors see escalated cases.
6. **How the approver decides:** Supervisors act on escalated cases.
7. **How the applicant / maker sees history:** Officers see their pendency.
8. **How the approver / auditor sees history:** Auditors see timer events.

### Functional Capabilities
- Timer per task and stage
- RAG status
- Reminders and escalation
- Pendency views and reports

### UI Screens
- Pendency view by DS / officer / stage
- Escalated cases list

### Logical API Operations
- Start / stop / pause timer
- Timer evaluation job
- Escalate
- Pendency aggregation

### Inputs
- Configured limits

### Outputs
- Reminders
- Escalations
- Pendency

### Business Rules
- Working-day calculation

### Validations
- None

### Calculations
- Elapsed working days

### Workflow
Running → Paused → Running → Completed | Breached

### Search Requirements
- Escalated by filters

### Documents
- None

### Reports
- Pendency report

### Notifications
- Reminders and escalations

### Security
- DS isolation

### Integrations
- None

### Dependencies
- F02-004
- F12-002

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Job completes within 10 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Pendency view by DS / officer / stage | Medium | 6 |
| UI | Escalated cases list | Easy | 4 |
| API | Start / stop / pause timer | Medium | 6 |
| API | Timer evaluation job | Medium | 6 |
| API | Escalate | Easy | 4 |
| API | Pendency aggregation | Medium | 6 |
| Database | Timer store | Easy | 2 |
| Testing | Timer and escalation tests | Medium | 6 |
| Documentation | Timeline note | Simple | 1 |

**Feature Total: 41 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 22 | 2 | 0 | 6 | 1 | **41** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Uses F02-004 date engine
- No external integration channel in this feature; Integration row omitted.
