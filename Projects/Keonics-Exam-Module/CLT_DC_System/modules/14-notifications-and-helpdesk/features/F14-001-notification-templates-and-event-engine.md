# F14-001 — Notification Templates & Event Engine

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F14-001 |
| Feature Name | Notification Templates & Event Engine |
| Module | 14 — Notifications & Helpdesk |
| Module Type | Shared |
| Release | Go-live |

### Description
Template management (SMS with DLT template IDs, e-mail HTML) in Kannada and English, event catalogue (about 25 events), recipient rules, scheduled reminders (test day minus 2 days, mock availability), and enable / disable per event.

### Business Objective
Communicate consistently at every step.

### Actors
- KEONICS Administrator
- System

### User Journey
1. **Who creates:** Administrator creates templates and mappings.
2. **How they create:** Administrator writes bilingual templates and maps to events.
3. **How they edit:** Templates edited with versions.
4. **How they send for approval:** Templates approved before use.
5. **How the approver sees pending items:** Approver sees templates.
6. **How the approver decides:** Approver approves.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see template versions.

### Functional Capabilities
- SMS and e-mail templates
- DLT template IDs
- Event catalogue
- Recipient rules
- Scheduled reminders
- Per-event switches

### UI Screens
- Template list
- Template editor
- Event mapping

### Logical API Operations
- Template CRUD
- Event dispatch engine
- Scheduled reminder job
- Render template

### Inputs
- Templates

### Outputs
- Messages queued

### Business Rules
- Only approved templates

### Validations
- Placeholders

### Calculations
- None

### Workflow
Draft → Active

### Search Requirements
- Templates

### Documents
- None

### Reports
- Template list

### Notifications
- As configured

### Security
- Admin only

### Integrations
- None

### Dependencies
- F14-002

### Assumptions
- DLT registration by KEONICS

### Risks
- DLT approvals

### Non Functional Requirements
- Dispatch within 30 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template list | Easy | 4 |
| UI | Template editor | Medium | 6 |
| UI | Event mapping | Medium | 6 |
| API | Template CRUD | Easy | 4 |
| API | Event dispatch engine | Complex | 8 |
| API | Scheduled reminder job | Medium | 6 |
| API | Render template | Easy | 4 |
| Database | Templates and mappings | Easy | 2 |
| Testing | Event engine tests | Medium | 6 |
| Documentation | Notification catalogue | Easy | 2 |

**Feature Total: 48 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 22 | 2 | 0 | 6 | 2 | **48** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
