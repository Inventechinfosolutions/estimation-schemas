# F08-002 — Communication Service Adapter

| Field | Value |
|-------|-------|
| Feature ID | F08-002 |
| Feature Name | Communication Service Adapter |
| Module | 08 — Integration Hub |
| Type | Technical |
| Notes | Go-live |

## Feature Specification

### Description
Integrates SMS/email providers for outbound notifications used by OTP, confirmation, and credentials.

### Business Objective
Abstract communication providers for the Notification Service.

### Actors
- Platform Administrator
- System

### User Journey
1. Administrator configures SMS/email provider settings.
2. System sends messages through adapter and receives status.
3. Admin updates templates routing via provider accounts.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Admin sees provider health.
8. Auditor sees config history masked.

### Functional Capabilities
- Configure SMS provider
- Configure email provider
- Send message
- Status callback/poll
- Health panel

### UI Screens
- Communication provider configuration screen
- Provider health panel
- Test SMS/email dialog

### Logical API Operations
- Save comms config
- Adapter send SMS
- Adapter send email
- Adapter status callback

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- All outbound comms via adapter
- Rate limit at adapter

### Validations
- Sender IDs configured

### Calculations
- None beyond display counters

### Workflow
Configured → Healthy | Degraded

### Search Requirements
Error log

### Documents
Runbook

### Reports
None

### Notifications
N/A

### Security
- API keys vaulted

### Integrations
SMS/email providers

### Dependencies
- None

### Assumptions
- Transactional SMS DLT/compliance handled by client/provider

### Risks
- SMS DLT template mismatch

### Non Functional Requirements
- Send latency acceptable for OTP

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Communication provider configuration screen | Complex | 12 |
| UI | Provider health panel | Easy | 4 |
| UI | Test SMS/email dialog | Easy | 4 |
| API | Save comms config | Medium | 6 |
| API | Adapter send SMS | Complex | 8 |
| API | Adapter send email | Complex | 8 |
| API | Adapter status callback | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Integration | External channel adapter work | Medium | 16 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 77 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Transactional SMS DLT/compliance handled by client/provider / SMS DLT template mismatch.
