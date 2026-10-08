# F08-003 — SMS notification provision

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F08-003 |
| Feature Name | SMS notification provision |
| Module | 08 — Notifications & Alerts |
| Description | Optional SMS alerts when gateway credentials are provided by DIPR |
| Business Objective | Provide SMS channel for critical alerts when DIPR supplies gateway access. |
| Actors | System; Admin |

### User Journey

- Admin enables SMS channel with DIPR credentials → eligible events send SMS → delivery status recorded → failures visible in delivery log.

### Functional Capabilities

- Optional SMS send for configured critical events
- Template-based short message body
- Feature disabled until credentials validated
- Graceful degradation when SMS unavailable

### Inputs

Mobile number; template; event context

### Outputs

SMS dispatch status

### Business Rules

SMS only when gateway configured and user policy allows
Rate limits per gateway policy

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

DIPR-provided SMS gateway (credentials external)

### Dependencies

F08-004; Module 02 templates

### Assumptions

DIPR provides sandbox and production SMS credentials

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | SMS channel enablement toggle admin | Easy | 4 |
| UI | SMS test send panel | Easy | 4 |
| UI | Provider credential masked form | Medium | 6 |
| API | SMS message render from template | Easy | 4 |
| API | SMS dispatch submit operation | Easy | 4 |
| API | Opt-out flag enforcement check | Medium | 6 |
| Integration | SMS gateway REST connector | Medium | 16 |
| Integration | Credential vault and rate limit | Easy | 8 |
| Database | SMS dispatch attempt log | Easy | 2 |
| Testing | Mock gateway send success | Medium | 6 |
| Testing | Opt-out suppression negative | Easy | 4 |
| Testing | Invalid MSISDN validation | Easy | 4 |
| Documentation | SMS provision checklist for DIPR | Easy | 2 |
| Documentation | Template length and encoding notes | Easy | 2 |

**Feature Total: 72 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
