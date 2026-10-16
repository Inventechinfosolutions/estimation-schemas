# F12-002 — Stage Event Notification Engine

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-002 |
| Feature Name | Stage Event Notification Engine |
| Module | 12 — Notification Service |
| Module Type | Shared |
| Release | Go-live |

### Description
Engine that subscribes to stage and business events (result approved, intimation, demand, payment, reminders, forwarding, document requests, draft deed, completion, defaults, disputes) and scheduled triggers, resolves recipients and preferences, and queues messages per channel.

### Business Objective
Send the right message to the right person at every stage automatically.

### Actors
- System

### User Journey
1. **Who creates:** The system creates notifications from events.
2. **How they create:** Event handlers create notification jobs with recipients and data.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Recipients see messages.
8. **How the approver / auditor sees history:** Auditors see jobs in the delivery log.

### Functional Capabilities
- Event subscription catalogue (30+ events)
- Recipient resolution by role and case
- Language and channel preference
- Quiet hours for SMS / WhatsApp
- Queue with priority

### UI Screens
- Event-to-notification mapping

### Logical API Operations
- Publish event
- Resolve recipients
- Queue messages
- Scheduled trigger runner
- Event mapping configuration

### Inputs
- Events

### Outputs
- Queued messages

### Business Rules
- No duplicates for same event and recipient
- Quiet hours respected

### Validations
- Recipient contact present

### Calculations
- None

### Workflow
Event → Queued → Sent (F12-003)

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- All

### Security
- System

### Integrations
- None

### Dependencies
- F12-001
- F12-003

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Queue latency under 1 minute

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Event-to-notification mapping | Medium | 6 |
| API | Publish event | Medium | 6 |
| API | Resolve recipients | Medium | 6 |
| API | Queue messages | Medium | 6 |
| API | Scheduled trigger runner | Medium | 6 |
| API | Event mapping configuration | Easy | 4 |
| Database | Notification queue | Easy | 2 |
| Database | Event mapping | Easy | 2 |
| Testing | Event coverage tests | Complex | 8 |
| Documentation | Event catalogue | Easy | 2 |

**Feature Total: 48 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 28 | 4 | 0 | 8 | 2 | **48** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Event coverage testing rated Complex
- No external integration channel in this feature; Integration row omitted.
