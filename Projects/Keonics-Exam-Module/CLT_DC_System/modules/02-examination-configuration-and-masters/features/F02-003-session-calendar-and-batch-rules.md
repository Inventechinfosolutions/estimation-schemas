# F02-003 — Session Calendar & Batch Rules

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-003 |
| Feature Name | Session Calendar & Batch Rules |
| Module | 02 — Examination Configuration & Masters |
| Module Type | Business |
| Release | Go-live |

### Description
Creation of the test calendar: working Saturdays for government employees and Sundays for prospective candidates, 4 sessions per day with an optional 5th, multiple sessions per centre per day with one active at a time, minimum batch size, booking open / close dates and conversion of Sunday batches to Saturday.

### Business Objective
Publish bookable sessions that follow RFP rules and adjust to booking demand.

### Actors
- KEONICS Administrator
- Approving Authority

### User Journey
1. **Who creates:** The KEONICS Administrator creates the calendar.
2. **How they create:** The administrator generates sessions for a period from templates (days, timings, centres, category) and adjusts individual sessions.
3. **How they edit:** The administrator edits draft sessions; published sessions with bookings can only be moved through rescheduling.
4. **How they send for approval:** The calendar is submitted for approval before publication.
5. **How the approver sees pending items:** The Approving Authority sees the calendar summary.
6. **How the approver decides:** The Approving Authority approves; sessions open for booking.
7. **How the applicant / maker sees history:** Candidates see published sessions in booking.
8. **How the approver / auditor sees history:** Auditors see calendar changes.

### Functional Capabilities
- Session templates (timings, sessions per day)
- Category per day: employees (Saturday) / prospective (Sunday)
- Optional 5th session
- One active session per centre at a time
- Minimum batch size per session
- Booking window and cut-off
- Holiday calendar
- Sunday-to-Saturday conversion

### UI Screens
- Calendar view by month
- Session generator
- Session detail
- Calendar approval

### Logical API Operations
- Generate sessions from template
- Maintain session
- Validate overlaps and category rules
- Approve and publish calendar
- Convert batch category / day

### Inputs
- Period, templates, centres

### Outputs
- Published sessions

### Business Rules
- No mixing of employees and prospective candidates in a session
- No overlapping sessions at a centre

### Validations
- Dates in future
- Not on holidays

### Calculations
- Seats per session = centre capacity

### Workflow
Draft → Approved → Published → Closed

### Search Requirements
- Sessions by date, centre

### Documents
- None

### Reports
- Calendar

### Notifications
- Calendar publication notice

### Security
- Admin only

### Integrations
- None

### Dependencies
- F02-002
- F05-001
- F05-006

### Assumptions
- Working Saturdays defined by holiday master

### Risks
- Late calendar changes

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Calendar view by month | Medium | 6 |
| UI | Session generator | Medium | 6 |
| UI | Session detail | Easy | 4 |
| UI | Calendar approval | Easy | 4 |
| API | Generate sessions from template | Complex | 8 |
| API | Maintain session | Medium | 6 |
| API | Validate overlaps and category rules | Medium | 6 |
| API | Approve and publish calendar | Easy | 4 |
| API | Convert batch category / day | Medium | 6 |
| Database | Session calendar | Medium | 4 |
| Testing | Calendar generation and rule tests | Medium | 6 |
| Documentation | Calendar guide | Easy | 2 |

**Feature Total: 62 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 30 | 4 | 0 | 6 | 2 | **62** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Generator rated Complex
- No external integration channel in this feature; Integration row omitted.
