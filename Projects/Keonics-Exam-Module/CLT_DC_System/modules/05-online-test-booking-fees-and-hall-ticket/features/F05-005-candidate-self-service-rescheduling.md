# F05-005 — Candidate Self-Service Rescheduling

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-005 |
| Feature Name | Candidate Self-Service Rescheduling |
| Module | 05 — Online Test Booking, Fees & Hall Ticket |
| Module Type | Business |
| Release | Go-live |

### Description
Self-service rescheduling allowed once per booking, at least 7 days before the session, to another session of the same category with available seats, without fee; new hall ticket issued; no cancellation.

### Business Objective
Implement the RFP rescheduling rules without manual intervention.

### Actors
- Candidate

### User Journey
1. **Who creates:** The candidate requests rescheduling from My Bookings.
2. **How they create:** The candidate selects a new eligible session; a seat is held.
3. **How they edit:** The candidate confirms or abandons.
4. **How they send for approval:** No approval when rules are met.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees the new booking and history.
8. **How the approver / auditor sees history:** Auditors see reschedule events.

### Functional Capabilities
- Eligibility check (once, ≥ 7 days)
- Eligible session list
- Seat swap with hold
- New hall ticket
- Reschedule history
- No cancellation option

### UI Screens
- Reschedule eligibility and session choice
- Reschedule confirmation

### Logical API Operations
- Check reschedule eligibility
- Swap booking seat
- Record reschedule

### Inputs
- New session

### Outputs
- Updated booking

### Business Rules
- Once per booking
- At least 7 days before
- Same category

### Validations
- Seat available

### Calculations
- Days to session

### Workflow
Booked → Rescheduled

### Search Requirements
- None

### Documents
- New hall ticket

### Reports
- Reschedules

### Notifications
- Reschedule confirmation

### Security
- Own booking

### Integrations
- None

### Dependencies
- F05-001
- F05-004

### Assumptions
- No fee for rescheduling

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Reschedule eligibility and session choice | Medium | 6 |
| UI | Reschedule confirmation | Easy | 4 |
| API | Check reschedule eligibility | Medium | 6 |
| API | Swap booking seat | Medium | 6 |
| API | Record reschedule | Easy | 4 |
| Database | Reschedule history | Simple | 1 |
| Testing | Reschedule rule tests | Medium | 6 |
| Documentation | Reschedule guide | Simple | 1 |

**Feature Total: 34 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 16 | 1 | 0 | 6 | 1 | **34** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
