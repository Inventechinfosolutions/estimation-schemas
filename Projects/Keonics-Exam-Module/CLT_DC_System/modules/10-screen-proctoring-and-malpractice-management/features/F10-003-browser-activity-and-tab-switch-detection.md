# F10-003 — Browser Activity & Tab-Switch Detection

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-003 |
| Feature Name | Browser Activity & Tab-Switch Detection |
| Module | 10 — Screen Proctoring & Malpractice Management |
| Module Type | Business |
| Release | Go-live |

### Description
Client-side detection of focus loss, tab or window switching, blocked key combinations, multiple displays, new USB devices, VM and remote desktop, with events sent immediately; configurable responses (warn, count, lock terminal pending proctor unlock, auto-submit after N events).

### Business Objective
Detect and respond to suspicious browser activity immediately.

### Actors
- System
- Candidate
- Proctor

### User Journey
1. **Who creates:** Detection runs during the test.
2. **How they create:** Events are sent and policies applied.
3. **How they edit:** Policies configured by administrator.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Proctor sees events per seat.
6. **How the approver decides:** Proctor unlocks or escalates.
7. **How the applicant / maker sees history:** Candidate sees warnings.
8. **How the approver / auditor sees history:** Auditors see events.

### Functional Capabilities
- Focus and tab-switch events
- Blocked shortcut attempts
- Multi-monitor detection
- USB / VM / remote desktop detection
- Configurable responses
- Proctor unlock

### UI Screens
- Activity policy configuration
- Candidate warning overlay

### Logical API Operations
- Activity event intake
- Policy evaluation
- Lock / unlock terminal

### Inputs
- Client events

### Outputs
- Flags, actions

### Business Rules
- Auto-submit only if policy enabled

### Validations
- Event signature

### Calculations
- Event counts

### Workflow
Event → Warn / Lock / Submit

### Search Requirements
- Events

### Documents
- None

### Reports
- Activity report

### Notifications
- Real-time alerts

### Security
- Signed events

### Integrations
- None

### Dependencies
- F09-007
- F10-004

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Event delivery under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Activity policy configuration | Easy | 4 |
| UI | Candidate warning overlay | Easy | 4 |
| API | Activity event intake | Medium | 6 |
| API | Policy evaluation | Medium | 6 |
| API | Lock / unlock terminal | Easy | 4 |
| Database | Activity events | Easy | 2 |
| Testing | Detection tests | Complex | 8 |
| Documentation | Activity policy note | Simple | 1 |

**Feature Total: 35 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 16 | 2 | 0 | 8 | 1 | **35** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Capture hooks in F09-007
- No external integration channel in this feature; Integration row omitted.
