# F09-003 — Server-Synchronised Timer & Disruption Compensation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-003 |
| Feature Name | Server-Synchronised Timer & Disruption Compensation |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Countdown timer driven by SDC server time with drift correction, per-candidate remaining time tracking, pause on disconnect, automatic compensation for disruptions (power, network, terminal change) approved by proctor / EMU, extra time for differently-abled candidates, and late-entry rule with no compensation; warnings at configured intervals and auto-submit at zero.

### Business Objective
Ensure fair time for all candidates as required by the RFP.

### Actors
- Candidate
- Proctor
- EMU

### User Journey
1. **Who creates:** The timer starts when the candidate acknowledges instructions.
2. **How they create:** The system tracks remaining time centrally.
3. **How they edit:** Compensation requests are raised by the proctor for affected candidates.
4. **How they send for approval:** Compensation above a threshold needs EMU approval.
5. **How the approver sees pending items:** EMU sees compensation requests.
6. **How the approver decides:** EMU approves or rejects.
7. **How the applicant / maker sees history:** Candidates see remaining time including compensation.
8. **How the approver / auditor sees history:** Auditors see time adjustments with reasons.

### Functional Capabilities
- Server time synchronisation
- Central remaining-time ledger
- Disconnect pause and resume
- Compensation requests and approval
- Extra time for supported candidates
- Late entry rule
- Warnings and auto-submit

### UI Screens
- Timer component
- Proctor compensation panel
- EMU compensation approval

### Logical API Operations
- Server time sync
- Remaining time ledger
- Pause / resume on disconnect
- Compensation request and approval
- Auto-submit at time end

### Inputs
- Disruption events

### Outputs
- Adjusted time

### Business Rules
- No compensation for late entry
- Session end time extended only for compensated candidates

### Validations
- Reason mandatory

### Calculations
- Remaining = allotted + extra + compensation − elapsed

### Workflow
Running → Paused → Running → Ended

### Search Requirements
- None

### Documents
- None

### Reports
- Compensation report

### Notifications
- Time warnings

### Security
- Client clock ignored

### Integrations
- SDC NTP

### Dependencies
- F04-006
- F12-002

### Assumptions
- SDC provides NTP

### Risks
- Mass disruption handling

### Non Functional Requirements
- Drift under 1 second

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Timer component | Medium | 6 |
| UI | Proctor compensation panel | Medium | 6 |
| UI | EMU compensation approval | Easy | 4 |
| API | Server time sync | Medium | 6 |
| API | Remaining time ledger | Complex | 8 |
| API | Pause / resume on disconnect | Medium | 6 |
| API | Compensation request and approval | Medium | 6 |
| API | Auto-submit at time end | Medium | 6 |
| Database | Time ledger and adjustments | Easy | 2 |
| Testing | Timer and compensation tests | Complex | 8 |
| Documentation | Timing rules note | Easy | 2 |

**Feature Total: 60 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 32 | 2 | 0 | 8 | 2 | **60** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Central ledger rated Complex
- No external integration channel in this feature; Integration row omitted.
