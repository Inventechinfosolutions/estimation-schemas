# F08-005 — Seat Allocation & Hall Ticket Login Control

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-005 |
| Feature Name | Seat Allocation & Hall Ticket Login Control |
| Module | 08 — Test Centre Operations & Candidate Validation |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic random allocation of verified candidates to working terminals (accessible seats for supported candidates), seat display and print, binding of hall ticket to terminal so that login works only at the designated seat, and seat change by proctor with reason.

### Business Objective
Enforce designated seating and prevent proxy logins.

### Actors
- Proctor
- Candidate
- System

### User Journey
1. **Who creates:** The system allocates seats when the session opens.
2. **How they create:** Seats are shown to the proctor and candidate.
3. **How they edit:** The proctor can change seat for faulty terminals with reason.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** EMU sees seat changes.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate logs in at the assigned seat with hall ticket number.
8. **How the approver / auditor sees history:** Auditors see seat map and changes.

### Functional Capabilities
- Random allocation
- Accessible seats
- Seat map display / print
- Terminal binding
- Seat change with reason
- Login rejection at wrong terminal

### UI Screens
- Seat map
- Seat change dialog

### Logical API Operations
- Allocate seats
- Bind hall ticket to terminal
- Change seat
- Validate login terminal

### Inputs
- Verified candidates
- Terminals

### Outputs
- Seat map

### Business Rules
- Login only from assigned terminal

### Validations
- Terminal registered

### Calculations
- Random allocation

### Workflow
Allocated → Changed

### Search Requirements
- By candidate

### Documents
- Seat map

### Reports
- Seat changes

### Notifications
- None

### Security
- Terminal identity

### Integrations
- None

### Dependencies
- F02-002
- F08-003
- F09-001

### Assumptions
- Terminals registered

### Risks
- None

### Non Functional Requirements
- Allocation under 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Seat map | Medium | 6 |
| UI | Seat change dialog | Easy | 4 |
| API | Allocate seats | Medium | 6 |
| API | Bind hall ticket to terminal | Medium | 6 |
| API | Change seat | Easy | 4 |
| API | Validate login terminal | Medium | 6 |
| Database | Seat allocation | Easy | 2 |
| Testing | Seat allocation and binding tests | Medium | 6 |
| Documentation | Seating SOP | Simple | 1 |

**Feature Total: 41 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 22 | 2 | 0 | 6 | 1 | **41** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
