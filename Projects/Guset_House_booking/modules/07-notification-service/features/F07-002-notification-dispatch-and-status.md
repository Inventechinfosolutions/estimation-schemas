# F07-002 — Notification Dispatch and Status

| Field | Value |
|-------|-------|
| Feature ID | F07-002 |
| Feature Name | Notification Dispatch and Status |
| Module | 07 — Notification Service |
| Type | Technical |
| Notes | Go-live |

## Feature Specification

### Description
Dispatches notifications through provisioned channels and records delivery/failure status.

### Business Objective
Reliably deliver OTP, confirmation, and credential messages with operational visibility.

### Actors
- System
- Platform Administrator

### User Journey
1. Upstream modules create dispatch requests.
2. Dispatch engine sends via Integration Hub and records status callbacks.
3. Admin may retry failed dispatches.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Admin sees dispatch register and statuses.
8. Auditor reviews dispatch audit.

### Functional Capabilities
- Queue dispatch
- Send via adapter
- Record status
- Retry failed
- Idempotent send keys

### UI Screens
- Dispatch register
- Dispatch detail view
- Retry dispatch confirmation

### Logical API Operations
- Enqueue notification
- Handle provider status callback
- List dispatches
- Retry dispatch

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Idempotent against duplicate events
- Retry limits
- Do not log full OTP/credential secrets

### Validations
- Template active for event
- Recipient present

### Calculations
- Retry backoff

### Workflow
Queued → Sent → Delivered | Failed → Retried

### Search Requirements
Filter by event, status, recipient masked

### Documents
None

### Reports
Failure rates to dashboard optional

### Notifications
This is the notification engine

### Security
- Secret redaction in logs
- Admin role for retries

### Integrations
F08-002

### Dependencies
- F07-001
- F08-002

### Assumptions
- Provider webhooks available or poll status

### Risks
- Provider outage

### Non Functional Requirements
- High throughput queue

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Dispatch register | Medium | 6 |
| UI | Dispatch detail view | Easy | 4 |
| UI | Retry dispatch confirmation | Simple | 2 |
| API | Enqueue notification | Complex | 8 |
| API | Handle provider status callback | Complex | 8 |
| API | List dispatches | Medium | 6 |
| API | Retry dispatch | Medium | 6 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 55 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Provider webhooks available or poll status / Provider outage.
