# F14-002 — E-mail & SMS Gateway Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F14-002 |
| Feature Name | E-mail & SMS Gateway Integration |
| Module | 14 — Notifications & Helpdesk |
| Module Type | Shared |
| Release | Go-live |

### Description
Integration with the state / KEONICS SMS gateway (DLT compliant) and SMTP e-mail service, queue-based sending with retries, throttling for bulk, delivery receipt processing, and failover between providers if configured.

### Business Objective
Deliver OTPs and notifications reliably.

### Actors
- System

### User Journey
1. **Who creates:** Messages are queued by the engine.
2. **How they create:** Connectors send and process receipts.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Operations see queue health.
6. **How the approver decides:** Operations retry failures.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see delivery logs.

### Functional Capabilities
- SMS connector with DLT
- SMTP connector
- Queue with priority (OTP first)
- Retries
- Delivery receipts
- Throttling

### UI Screens
- Gateway health

### Logical API Operations
- Send SMS
- Send e-mail
- Process delivery receipts
- Priority queue management

### Inputs
- Messages

### Outputs
- Delivered messages

### Business Rules
- OTP priority

### Validations
- DLT IDs

### Calculations
- None

### Workflow
Queued → Sent → Delivered / Failed

### Search Requirements
- None

### Documents
- None

### Reports
- Delivery rates

### Notifications
- None

### Security
- Credentials in vault

### Integrations
- SMS, SMTP

### Dependencies
- F14-001

### Assumptions
- Gateway accounts provided by KEONICS

### Risks
- Gateway throughput

### Non Functional Requirements
- OTP dispatched within 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Gateway health | Easy | 4 |
| API | Send SMS | Easy | 4 |
| API | Send e-mail | Easy | 4 |
| API | Process delivery receipts | Medium | 6 |
| API | Priority queue management | Medium | 6 |
| Database | Message queue | Easy | 2 |
| Integration | SMS gateway (DLT) | Medium | 16 |
| Integration | SMTP e-mail service | Easy | 8 |
| Testing | Gateway tests | Medium | 6 |
| Documentation | Gateway configuration note | Simple | 1 |

**Feature Total: 57 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 20 | 2 | 24 | 6 | 1 | **57** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
