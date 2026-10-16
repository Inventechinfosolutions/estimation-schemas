# F12-001 — Real-Time Centre & Session Monitoring

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-001 |
| Feature Name | Real-Time Centre & Session Monitoring |
| Module | 12 — Central Monitoring Centre & Examination Monitoring Unit |
| Module Type | Business |
| Release | Go-live |

### Description
Central monitoring dashboard for the Examination Monitoring Unit, KEONICS and competent authorities: map and grid of centres with session state, readiness, proctor presence, validated / logged-in / submitted counts, average progress, alert counts, recording health, network status, and drill-down to seat level; auto-refresh by websocket.

### Business Objective
Give live visibility of every session as required by the RFP.

### Actors
- EMU Monitor
- KEONICS
- Competent Authority

### User Journey
1. **Who creates:** The dashboard populates automatically from session events.
2. **How they create:** Users filter by district, centre or session.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Users see exceptions highlighted.
6. **How the approver decides:** Users drill down and act via F12-002.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see monitoring access logs.

### Functional Capabilities
- Centre map and grid
- Session state tiles
- Counts and progress
- Alert and recording health
- Seat-level drill-down
- Websocket refresh
- Exception highlighting

### UI Screens
- Monitoring wall (map and grid)
- Centre drill-down
- Seat-level view

### Logical API Operations
- Aggregate live session metrics
- Real-time push of metrics
- Centre and seat drill-down

### Inputs
- Session events

### Outputs
- Live dashboard

### Business Rules
- Scope by role

### Validations
- None

### Calculations
- Progress %, counts

### Workflow
Not applicable

### Search Requirements
- Centres

### Documents
- None

### Reports
- Snapshots

### Notifications
- Exception alerts

### Security
- Read-only for authorities

### Integrations
- None

### Dependencies
- Modules 08–10

### Assumptions
- None

### Risks
- Event volume

### Non Functional Requirements
- Update within 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Monitoring wall (map and grid) | Very High | 16 |
| UI | Centre drill-down | Complex | 12 |
| UI | Seat-level view | Medium | 6 |
| API | Aggregate live session metrics | Complex | 8 |
| API | Real-time push of metrics | Complex | 8 |
| API | Centre and seat drill-down | Medium | 6 |
| Database | Live metrics store | Medium | 4 |
| Testing | Monitoring accuracy and latency tests | Complex | 8 |
| Documentation | Monitoring guide | Easy | 2 |

**Feature Total: 70 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 22 | 4 | 0 | 8 | 2 | **70** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Real-time aggregation rated Complex
- No external integration channel in this feature; Integration row omitted.
