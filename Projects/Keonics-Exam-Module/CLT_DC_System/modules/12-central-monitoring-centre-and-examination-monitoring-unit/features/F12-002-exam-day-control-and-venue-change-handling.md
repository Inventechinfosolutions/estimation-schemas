# F12-002 — Exam-Day Control & Venue Change Handling

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-002 |
| Feature Name | Exam-Day Control & Venue Change Handling |
| Module | 12 — Central Monitoring Centre & Examination Monitoring Unit |
| Module Type | Business |
| Release | Go-live |

### Description
Control console for EMU: hold / resume a session or candidate, approve compensation, restart a centre, move candidates to another terminal or centre on venue failure with booking and hall ticket updates, handle exceptions communicated by venue, and broadcast messages to centre consoles.

### Business Objective
Allow controlled interventions with full traceability.

### Actors
- EMU Monitor
- Proctor
- KEONICS

### User Journey
1. **Who creates:** EMU initiates control actions.
2. **How they create:** EMU selects targets and action with reason.
3. **How they edit:** Actions can be reversed where safe.
4. **How they send for approval:** Venue changes need KEONICS approval.
5. **How the approver sees pending items:** KEONICS sees venue change requests.
6. **How the approver decides:** KEONICS approves.
7. **How the applicant / maker sees history:** Proctors see instructions.
8. **How the approver / auditor sees history:** Auditors see interventions.

### Functional Capabilities
- Hold / resume
- Bulk compensation
- Centre restart
- Candidate move across terminals / centres
- Venue change with booking update
- Broadcast to consoles

### UI Screens
- Control console
- Venue change wizard
- Broadcast message

### Logical API Operations
- Hold / resume
- Bulk compensation
- Move candidates
- Venue change with rebooking
- Broadcast

### Inputs
- Actions

### Outputs
- Interventions

### Business Rules
- Every action requires reason

### Validations
- Target state

### Calculations
- Compensation minutes

### Workflow
Requested → Executed

### Search Requirements
- Interventions

### Documents
- None

### Reports
- Intervention report

### Notifications
- Candidate notices on venue change

### Security
- EMU only

### Integrations
- None

### Dependencies
- F09-003
- F05-004
- F12-001

### Assumptions
- None

### Risks
- Mass disruption

### Non Functional Requirements
- Action under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Control console | Complex | 12 |
| UI | Venue change wizard | Complex | 12 |
| UI | Broadcast message | Easy | 4 |
| API | Hold / resume | Medium | 6 |
| API | Bulk compensation | Medium | 6 |
| API | Move candidates | Complex | 8 |
| API | Venue change with rebooking | Complex | 8 |
| API | Broadcast | Easy | 4 |
| Database | Intervention log | Easy | 2 |
| Testing | Control action tests | Complex | 8 |
| Documentation | Exam-day control SOP | Easy | 2 |

**Feature Total: 72 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 32 | 2 | 0 | 8 | 2 | **72** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
