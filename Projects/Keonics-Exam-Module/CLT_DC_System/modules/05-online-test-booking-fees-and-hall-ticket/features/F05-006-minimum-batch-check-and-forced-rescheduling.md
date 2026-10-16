# F05-006 — Minimum Batch Check & Forced Rescheduling

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-006 |
| Feature Name | Minimum Batch Check & Forced Rescheduling |
| Module | 05 — Online Test Booking, Fees & Hall Ticket |
| Module Type | Business |
| Release | Go-live |

### Description
Scheduled check of sessions against minimum batch size before cut-off; administrator selects target sessions; system moves candidates in bulk, regenerates hall tickets and triggers e-mail, SMS and a helpdesk outbound call list with acknowledgement tracking; supports converting Sunday batches to Saturday.

### Business Objective
Run economical sessions and communicate changes reliably.

### Actors
- KEONICS Administrator
- Helpdesk Executive
- Candidate

### User Journey
1. **Who creates:** The system flags sessions below minimum size; the administrator creates a move plan.
2. **How they create:** The administrator selects target sessions; the system proposes candidate moves.
3. **How they edit:** The administrator adjusts the plan.
4. **How they send for approval:** The plan is approved by the Approving Authority.
5. **How the approver sees pending items:** The approver sees the plan and impact.
6. **How the approver decides:** The approver approves; moves are executed.
7. **How the applicant / maker sees history:** Candidates see the new booking and notices; helpdesk sees call list.
8. **How the approver / auditor sees history:** Auditors see the plan, approvals and acknowledgements.

### Functional Capabilities
- Below-minimum detection job
- Move plan with target sessions
- Bulk move with seat checks
- Hall ticket regeneration
- Outbound call list with outcomes
- Acknowledgement tracking
- Sunday-to-Saturday conversion

### UI Screens
- Below-minimum sessions
- Move plan builder
- Plan approval
- Outbound call list

### Logical API Operations
- Detect below-minimum sessions
- Propose move plan
- Approve and execute moves
- Record call outcome and acknowledgement

### Inputs
- Target sessions

### Outputs
- Moved bookings
- Notices

### Business Rules
- Forced moves do not consume the candidate's one-time reschedule
- Category rules respected

### Validations
- Capacity in targets

### Calculations
- Shortfall = minimum − booked

### Workflow
Draft → Approved → Executed

### Search Requirements
- Plans

### Documents
- New hall tickets

### Reports
- Forced reschedules

### Notifications
- E-mail and SMS notice
- Helpdesk call

### Security
- Admin only

### Integrations
- None

### Dependencies
- F02-003
- F05-004
- F14-003

### Assumptions
- Helpdesk staffed by KEONICS / vendor

### Risks
- Candidate non-response

### Non Functional Requirements
- Bulk move of 500 candidates under 2 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Below-minimum sessions | Easy | 4 |
| UI | Move plan builder | Complex | 12 |
| UI | Plan approval | Easy | 4 |
| UI | Outbound call list | Medium | 6 |
| API | Detect below-minimum sessions | Medium | 6 |
| API | Propose move plan | Complex | 8 |
| API | Approve and execute moves | Complex | 8 |
| API | Record call outcome and acknowledgement | Easy | 4 |
| Database | Move plans and acknowledgements | Easy | 2 |
| Testing | Forced reschedule tests | Complex | 8 |
| Documentation | Batch management guide | Easy | 2 |

**Feature Total: 64 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 26 | 2 | 0 | 8 | 2 | **64** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Plan builder rated Complex
- No external integration channel in this feature; Integration row omitted.
