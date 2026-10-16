# F15-004 — Support Helpdesk & Ticket Tracking

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F15-004 |
| Feature Name | Support Helpdesk & Ticket Tracking |
| Module | 15 — Platform Operations & Support |
| Module Type | Technical |
| Release | Go-live |

### Description
Helpdesk for BDA users and bidders to raise issues, severity classification (Critical / High / Medium / Low), assignment, resolution tracking against response and resolution SLAs, escalation and monthly reports.

### Business Objective
Track support and meet the RFP support SLAs.

### Actors
- BDA users
- Successful Bidder
- Support team

### User Journey
1. **Who creates:** Users raise tickets.
2. **How they create:** The user selects category, describes the issue and attaches screenshots.
3. **How they edit:** The user can add comments.
4. **How they send for approval:** Tickets are triaged by support.
5. **How the approver sees pending items:** Support sees tickets by severity and SLA.
6. **How the approver decides:** Support resolves or escalates.
7. **How the applicant / maker sees history:** Users see ticket status.
8. **How the approver / auditor sees history:** BDA sees reports.

### Functional Capabilities
- Ticket creation
- Severity and SLA
- Assignment and escalation
- Reports

### UI Screens
- Raise ticket
- Ticket list and detail
- Support queue

### Logical API Operations
- Create ticket
- Update / assign / escalate
- SLA timer
- Ticket reports

### Inputs
- Issue details

### Outputs
- Tickets

### Business Rules
- SLA per severity

### Validations
- Mandatory fields

### Calculations
- SLA due

### Workflow
Open → In Progress → Resolved → Closed

### Search Requirements
- Tickets

### Documents
- Attachments

### Reports
- Monthly support report

### Notifications
- Ticket updates

### Security
- Users see own tickets

### Integrations
- None

### Dependencies
- F12-002

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Raise ticket | Easy | 4 |
| UI | Ticket list and detail | Medium | 6 |
| UI | Support queue | Easy | 4 |
| API | Create ticket | Easy | 4 |
| API | Update / assign / escalate | Easy | 4 |
| API | SLA timer | Easy | 4 |
| API | Ticket reports | Easy | 4 |
| Database | Ticket store | Easy | 2 |
| Testing | Ticket flow tests | Easy | 4 |
| Documentation | Support process note | Simple | 1 |

**Feature Total: 37 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 16 | 2 | 0 | 4 | 1 | **37** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
