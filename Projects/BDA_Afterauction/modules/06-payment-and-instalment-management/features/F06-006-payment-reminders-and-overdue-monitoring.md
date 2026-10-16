# F06-006 — Payment Reminders & Overdue Monitoring

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-006 |
| Feature Name | Payment Reminders & Overdue Monitoring |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Automatic reminders to bidders before and after each due date by e-mail, SMS and WhatsApp (where enabled), with configurable reminder points, overdue status computation, overdue lists for Finance and DS offices, and escalation into default proceedings when overdue exceeds the configured limit.

### Business Objective
Reduce delays and defaults through timely, automatic reminders and visibility of overdue sites.

### Actors
- System
- Finance Officer
- Auction Admin
- Successful Bidder

### User Journey
1. **Who creates:** The scheduler creates reminders automatically.
2. **How they create:** Daily jobs evaluate due dates and send reminders at configured points (e.g., T−7, T−2, T+1, T+7).
3. **How they edit:** The Auction Admin edits reminder points through configuration.
4. **How they send for approval:** No approval for reminders.
5. **How the approver sees pending items:** The Finance Officer sees overdue sites with days overdue and amount.
6. **How the approver decides:** The Finance Officer can trigger default proceedings (F06-008) for sites past the limit.
7. **How the applicant / maker sees history:** The bidder sees reminders in the portal inbox.
8. **How the approver / auditor sees history:** Auditors see reminder dispatch logs.

### Functional Capabilities
- Configurable reminder points
- Daily reminder job with holiday awareness
- Overdue computation and buckets (0–15, 16–30, 31–60, >60 days)
- Overdue lists by DS, layout, auction
- Automatic flag for default eligibility

### UI Screens
- Overdue monitoring list
- Reminder configuration
- Reminder history per site

### Logical API Operations
- Daily reminder job
- Compute overdue and buckets
- Flag default eligibility
- List overdue
- Reminder history

### Inputs
- Due dates
- Reminder points

### Outputs
- Reminders
- Overdue lists

### Business Rules
- No reminders for paid instalments
- Reminders stop on extension approval and restart on revised date

### Validations
- Reminder points valid

### Calculations
- Days overdue = today − due date

### Workflow
Upcoming → Due → Overdue → Default-eligible

### Search Requirements
- Overdue by filters

### Documents
- None

### Reports
- Overdue ageing report

### Notifications
- Reminders by e-mail, SMS, WhatsApp

### Security
- DS isolation on lists

### Integrations
- Through F12

### Dependencies
- F06-001
- F12-002
- F02-004

### Assumptions
- None

### Risks
- Message costs; frequency configurable

### Non Functional Requirements
- Daily job completes within 15 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Overdue monitoring list | Medium | 6 |
| UI | Reminder configuration | Easy | 4 |
| UI | Reminder history per site | Easy | 4 |
| API | Daily reminder job | Medium | 6 |
| API | Compute overdue and buckets | Medium | 6 |
| API | Flag default eligibility | Easy | 4 |
| API | List overdue | Easy | 4 |
| API | Reminder history | Easy | 4 |
| Database | Reminder schedule and log | Easy | 2 |
| Testing | Reminder timing tests | Medium | 6 |
| Testing | Overdue bucket tests | Easy | 4 |
| Documentation | Reminder configuration note | Simple | 1 |

**Feature Total: 51 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 24 | 2 | 0 | 10 | 1 | **51** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Scheduler embedded
- No external integration channel in this feature; Integration row omitted.
