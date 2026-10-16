# F07-003 — Sealed Paper Storage & Session Release

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-003 |
| Feature Name | Sealed Paper Storage & Session Release |
| Module | 07 — Question Paper Generation & Mock Test |
| Module Type | Business |
| Release | Go-live |

### Description
Paper sets encrypted with session keys protected by HSM; release only when the session is started by the authorised proctor at the scheduled time from a registered centre; content never viewable by any staff; automatic closure after session.

### Business Objective
Ensure papers are not viewable except by candidates during the test.

### Actors
- System
- Proctor
- Examination Monitoring Unit

### User Journey
1. **Who creates:** The system seals sets after generation.
2. **How they create:** Keys are wrapped by HSM.
3. **How they edit:** No edit after seal.
4. **How they send for approval:** Release requires proctor start within the time window (F08-002).
5. **How the approver sees pending items:** EMU sees release status.
6. **How the approver decides:** EMU can hold release in emergencies.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see seal, release and close events.

### Functional Capabilities
- Session key per set
- HSM key wrapping
- Time-window release
- Centre and proctor checks
- Emergency hold
- Auto-close

### UI Screens
- Release status monitor

### Logical API Operations
- Seal with session key
- Release key at session start
- Hold / resume release
- Close session set

### Inputs
- Sealed set

### Outputs
- Released paper

### Business Rules
- Release only within ± 15 minutes of scheduled start
- No staff view

### Validations
- Proctor authenticated

### Calculations
- None

### Workflow
Sealed → Released → Closed

### Search Requirements
- None

### Documents
- None

### Reports
- Release log

### Notifications
- Release failure alert

### Security
- HSM protected

### Integrations
- HSM via F15-005

### Dependencies
- F07-001
- F08-002
- F15-005

### Assumptions
- None

### Risks
- HSM latency

### Non Functional Requirements
- Release under 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Release status monitor | Easy | 4 |
| API | Seal with session key | Complex | 8 |
| API | Release key at session start | Complex | 8 |
| API | Hold / resume release | Easy | 4 |
| API | Close session set | Easy | 4 |
| Database | Key references and release log | Easy | 2 |
| Testing | Release control tests | Complex | 8 |
| Documentation | Paper security note | Easy | 2 |

**Feature Total: 40 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 24 | 2 | 0 | 8 | 2 | **40** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Security-critical
- No external integration channel in this feature; Integration row omitted.
