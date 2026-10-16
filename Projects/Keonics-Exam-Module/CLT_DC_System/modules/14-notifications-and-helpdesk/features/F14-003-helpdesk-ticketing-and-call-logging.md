# F14-003 — Helpdesk Ticketing & Call Logging

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F14-003 |
| Feature Name | Helpdesk Ticketing & Call Logging |
| Module | 14 — Notifications & Helpdesk |
| Module Type | Shared |
| Release | Go-live |

### Description
Helpdesk module for the need-based offsite helpdesk: logging of inbound calls and e-mails as tickets with candidate look-up, categories, priority and SLA timers, assignment and escalation, outbound call campaigns (forced reschedules, reminders) with outcomes, knowledge base of answers, and candidate ticket status on portal.

### Business Objective
Support candidates and stakeholders with traceable resolution.

### Actors
- Helpdesk Executive
- Candidate
- KEONICS
- Support Engineer

### User Journey
1. **Who creates:** Helpdesk executives create tickets; candidates may raise online.
2. **How they create:** The executive logs call details with candidate look-up.
3. **How they edit:** Tickets updated with notes until resolution.
4. **How they send for approval:** Escalations go to support engineers or KEONICS.
5. **How the approver sees pending items:** Assignees see queues.
6. **How the approver decides:** Assignees resolve or escalate.
7. **How the applicant / maker sees history:** Candidates see ticket status.
8. **How the approver / auditor sees history:** Auditors see ticket history and SLA.

### Functional Capabilities
- Ticket logging with candidate look-up
- Categories and priority
- SLA timers and escalation
- Outbound campaigns
- Knowledge base
- Online ticket raising
- Helpdesk reports

### UI Screens
- Ticket console
- Ticket detail
- Outbound campaign list
- Knowledge base
- Candidate ticket page

### Logical API Operations
- Ticket CRUD and assignment
- SLA timer and escalation
- Outbound campaign
- Knowledge base search

### Inputs
- Calls
- E-mails

### Outputs
- Resolved tickets

### Business Rules
- Every call logged

### Validations
- Category mandatory

### Calculations
- SLA elapsed

### Workflow
Open → Assigned → Resolved → Closed

### Search Requirements
- Tickets by candidate, status

### Documents
- None

### Reports
- Ticket SLA report

### Notifications
- Ticket updates

### Security
- Masked candidate data

### Integrations
- Telephony not integrated (manual logging)

### Dependencies
- F05-006

### Assumptions
- Telephony integration not required

### Risks
- Volume spikes

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Ticket console | Medium | 6 |
| UI | Ticket detail | Medium | 6 |
| UI | Outbound campaign list | Medium | 6 |
| UI | Knowledge base | Easy | 4 |
| UI | Candidate ticket page | Easy | 4 |
| API | Ticket CRUD and assignment | Medium | 6 |
| API | SLA timer and escalation | Medium | 6 |
| API | Outbound campaign | Medium | 6 |
| API | Knowledge base search | Easy | 4 |
| Database | Tickets, campaigns and knowledge base | Medium | 4 |
| Testing | Helpdesk tests | Medium | 6 |
| Documentation | Helpdesk SOP | Easy | 2 |

**Feature Total: 60 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 22 | 4 | 0 | 6 | 2 | **60** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
