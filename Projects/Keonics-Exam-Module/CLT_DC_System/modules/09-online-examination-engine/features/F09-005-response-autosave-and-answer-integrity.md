# F09-005 — Response Autosave & Answer Integrity

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-005 |
| Feature Name | Response Autosave & Answer Integrity |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Each answer change sent to the server with sequence number and signature, acknowledged and stored in an append-only response log with hash chain; client keeps a short encrypted buffer to survive brief network loss; on terminal failure the candidate resumes on another terminal with all responses intact; no data stored locally after session.

### Business Objective
Guarantee no answer is lost or altered.

### Actors
- Candidate
- System
- Proctor

### User Journey
1. **Who creates:** Responses are saved automatically as the candidate answers.
2. **How they create:** The client sends each change; server acknowledges.
3. **How they edit:** Resume on another terminal by proctor action.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Proctor sees sync status per seat.
6. **How the approver decides:** Proctor triggers terminal move.
7. **How the applicant / maker sees history:** Candidate sees saved indicator.
8. **How the approver / auditor sees history:** Auditors verify response log integrity.

### Functional Capabilities
- Per-change autosave
- Sequence numbers and ack
- Append-only hash-chained log
- Encrypted short buffer
- Terminal move and resume
- Local data wipe after session
- Sync status

### UI Screens
- Sync status indicator
- Proctor terminal move

### Logical API Operations
- Save response event
- Resume candidate state
- Terminal move
- Integrity verification

### Inputs
- Answer events

### Outputs
- Stored responses

### Business Rules
- Last acknowledged response is final
- No local storage after session

### Validations
- Sequence continuity

### Calculations
- Hash chain

### Workflow
Pending → Acknowledged

### Search Requirements
- None

### Documents
- None

### Reports
- Response integrity report

### Notifications
- Sync failure alerts to proctor

### Security
- AES-256 at rest; TLS

### Integrations
- None

### Dependencies
- F16-001
- F16-002

### Assumptions
- None

### Risks
- High write volume at 2,000 concurrent

### Non Functional Requirements
- Save ack under 500 ms at peak

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Sync status indicator | Simple | 2 |
| UI | Proctor terminal move | Easy | 4 |
| API | Save response event | Very High | 16 |
| API | Resume candidate state | Complex | 8 |
| API | Terminal move | Medium | 6 |
| API | Integrity verification | Medium | 6 |
| Database | Response event log (hash chained, encrypted) | Complex | 6 |
| Testing | Autosave, failure and resume tests | Complex | 8 |
| Testing | Integrity tests | Medium | 6 |
| Documentation | Response integrity note | Easy | 2 |

**Feature Total: 64 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 36 | 6 | 0 | 14 | 2 | **64** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- High-volume write path rated Very High
- No external integration channel in this feature; Integration row omitted.
