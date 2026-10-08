# F05-002 — Credential Delivery

| Field | Value |
|-------|-------|
| Feature ID | F05-002 |
| Feature Name | Credential Delivery |
| Module | 05 — Access Credentials & Guest Check-in |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Shares access credentials with the user through SMS or other configured communication channels.

### Business Objective
Ensure the employee receives entry credentials without relying solely on portal login at arrival.

### Actors
- System
- Employee Guest

### User Journey
1. System creates delivery request after credential generation.
2. Notification Service dispatches SMS/email; status recorded.
3. Resend allowed with rate limits; content not freely editable by employee.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Employee sees delivery status (Sent/Failed) on booking.
8. Admin sees dispatch history and can resend.

### Functional Capabilities
- Dispatch credential message
- Resend credential
- Show delivery status
- Rate-limit resend

### UI Screens
- Credential delivery status panel
- Resend credential confirmation
- Admin dispatch history

### Logical API Operations
- Request credential dispatch
- Resend credential dispatch
- Get delivery status

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Dispatch only for active credential
- Mask credential partially in admin lists if required

### Validations
- User must have reachable mobile/email per channel

### Calculations
- None beyond display counters

### Workflow
CredentialActive → DispatchQueued → Sent | Failed → Resent

### Search Requirements
Admin find failed dispatches

### Documents
None

### Reports
None

### Notifications
Primary channel SMS/email

### Security
- No plaintext credential in broad admin grids if policy requires
- Rate limit

### Integrations
F07-002 / F08-002

### Dependencies
- F05-001
- F07-002

### Assumptions
- SMS is primary; email secondary

### Risks
- SMS failure near arrival time

### Non Functional Requirements
- Dispatch queued within seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Credential delivery status panel | Easy | 4 |
| UI | Resend credential confirmation | Simple | 2 |
| UI | Admin dispatch history | Medium | 6 |
| API | Request credential dispatch | Medium | 6 |
| API | Resend credential dispatch | Medium | 6 |
| API | Get delivery status | Easy | 4 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 38 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: SMS is primary; email secondary / SMS failure near arrival time.
