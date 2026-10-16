# F12-003 — Email, SMS & WhatsApp Gateway Connectors

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-003 |
| Feature Name | Email, SMS & WhatsApp Gateway Connectors |
| Module | 12 — Notification Service |
| Module Type | Shared |
| Release | Go-live |

### Description
Connectors to BDA's SMTP / e-mail service, SMS gateway (DLT compliant) and WhatsApp Business API provider, with retries, throttling, delivery receipts, failover and a switch to enable / disable each channel.

### Business Objective
Deliver messages reliably through BDA's channels.

### Actors
- System
- Super Admin (configuration)

### User Journey
1. **Who creates:** Messages are sent by the system.
2. **How they create:** The dispatcher picks queued messages and sends them through the channel connector.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** The Super Admin sees channel health.
6. **How the approver decides:** The Super Admin enables or disables channels.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see sends in the delivery log.

### Functional Capabilities
- E-mail connector with attachments
- SMS connector with DLT parameters
- WhatsApp connector with template messages
- Delivery receipt callbacks
- Retries and throttling
- Channel switches

### UI Screens
- Channel configuration and health

### Logical API Operations
- Dispatch e-mail
- Dispatch SMS
- Dispatch WhatsApp
- Delivery receipt callback
- Retry and throttle

### Inputs
- Queued messages

### Outputs
- Sent messages
- Delivery status

### Business Rules
- WhatsApp only for opted-in recipients

### Validations
- Channel enabled

### Calculations
- None

### Workflow
Queued → Sent → Delivered / Failed

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- All

### Security
- Credentials in vault

### Integrations
- E-mail, SMS, WhatsApp gateways

### Dependencies
- F13-001
- F12-004

### Assumptions
- BDA provides accounts

### Risks
- Gateway outages

### Non Functional Requirements
- 1,000 SMS per minute throughput

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Channel configuration and health | Easy | 4 |
| API | Dispatch e-mail | Medium | 6 |
| API | Dispatch SMS | Medium | 6 |
| API | Dispatch WhatsApp | Medium | 6 |
| API | Delivery receipt callback | Medium | 6 |
| API | Retry and throttle | Easy | 4 |
| Integration | E-mail (SMTP / API) connector | Simple | 4 |
| Integration | SMS gateway connector with DLT | Medium | 16 |
| Integration | WhatsApp Business API connector | Medium | 16 |
| Testing | Channel integration tests | Medium | 6 |
| Documentation | Gateway configuration note | Easy | 2 |

**Feature Total: 76 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 28 | 0 | 36 | 6 | 2 | **76** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Three integration rows
