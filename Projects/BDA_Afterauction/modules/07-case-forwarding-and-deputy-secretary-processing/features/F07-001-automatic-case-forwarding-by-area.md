# F07-001 — Automatic Case Forwarding by Area

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-001 |
| Feature Name | Automatic Case Forwarding by Area |
| Module | 07 — Case Forwarding & Deputy Secretary Processing |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic forwarding of the case to the concerned Deputy Secretary queue (DS1 / DS2 / DS3) when 75% payment is confirmed, using the area allocation rule, with an exception queue for unmapped areas, forwarding note, and notification to the DS office and the bidder.

### Business Objective
Remove manual file movement and start DS processing on the same day the 75% milestone is reached.

### Actors
- System
- Auction Admin
- Deputy Secretary

### User Journey
1. **Who creates:** The system forwards the case automatically on the 75% milestone event.
2. **How they create:** The forwarding job resolves the DS office from F02-002, creates the DS task and records the forwarding note.
3. **How they edit:** Forwarding cannot be edited; changes are made through re-assignment (F07-002).
4. **How they send for approval:** No approval; unmapped cases go to the Auction Admin's exception queue.
5. **How the approver sees pending items:** The Deputy Secretary sees new cases in the DS queue with forwarding date.
6. **How the approver decides:** The Auction Admin resolves exceptions by selecting the DS office with reason.
7. **How the applicant / maker sees history:** The bidder sees the stage 'Forwarded to Deputy Secretary' in the tracker.
8. **How the approver / auditor sees history:** Auditors see forwarding events with rule version.

### Functional Capabilities
- Event-driven forwarding on 75% milestone
- DS resolution using area rules
- Exception queue for unmapped or ambiguous areas
- Forwarding note with case summary
- Notifications to DS office and bidder

### UI Screens
- Forwarding exception queue
- Forwarding log

### Logical API Operations
- Handle 75% milestone event
- Resolve DS office
- Create DS task
- Resolve forwarding exception
- Forwarding log

### Inputs
- Milestone event
- Area rule

### Outputs
- DS task
- Forwarding note

### Business Rules
- Forward only on confirmed 75% credit
- Exactly one DS office per case

### Validations
- Area mapped

### Calculations
- None

### Workflow
Milestone → Forwarded | Exception → Resolved → Forwarded

### Search Requirements
- Forwarded cases by DS and date

### Documents
- Forwarding note

### Reports
- Forwarding report

### Notifications
- DS office and bidder

### Security
- DS isolation applies after forwarding

### Integrations
- None

### Dependencies
- F06-005
- F02-002
- F12-002

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Forwarding within 5 minutes of milestone

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Forwarding exception queue | Easy | 4 |
| UI | Forwarding log | Easy | 4 |
| API | Handle 75% milestone event | Medium | 6 |
| API | Resolve DS office | Easy | 4 |
| API | Create DS task | Medium | 6 |
| API | Resolve forwarding exception | Easy | 4 |
| API | Forwarding log | Simple | 2 |
| Database | Forwarding log | Simple | 1 |
| Testing | Forwarding and exception tests | Medium | 6 |
| Documentation | Forwarding rules note | Simple | 1 |

**Feature Total: 38 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 22 | 1 | 0 | 6 | 1 | **38** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small event handler
- No external integration channel in this feature; Integration row omitted.
