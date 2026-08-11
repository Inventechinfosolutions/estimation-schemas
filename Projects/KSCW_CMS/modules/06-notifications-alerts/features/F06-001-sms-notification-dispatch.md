# F06-001 — SMS Notification Dispatch

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-001 |
| Feature Name | SMS Notification Dispatch |
| Module | 06 — Notifications & Alerts (SMS / Email) |
| Description | Dispatch SMS alerts for configured complaint lifecycle events using templates. |
| Business Objective | Reach complainants/staff quickly on key events. |
| Actors | System; Admin (templates via Module 02) |

### User Journey

- Domain event occurs → template resolved → SMS sent via gateway → status logged.

### Functional Capabilities

- Event-driven SMS send
- Template merge
- Delivery status capture

### Inputs

- Event payload
- Mobile number
- Template

### Outputs

- SMS submit to gateway
- Log entry

### Business Rules

- Only configured events
- Suppress if no mobile / invalid number

### Validations

- Mobile format
- Template active

### Calculations

- None

### Workflow

- Event → render → dispatch → log

### Search Requirements

- Via F06-003 log

### Documents

- None

### Reports

- None

### Notifications

- This feature is the SMS channel

### Security

- Gateway credentials secured; PII minimization

### Integrations

- SMS gateway (KSCW/KEONICS facilitated)

### Dependencies

- F02-004
- Modules 03–05 events

### Assumptions

- Gateway account available before UAT

### Risks

- Gateway downtime impacts ack perception

### Non Functional Requirements

- Retry policy coordinated with F06-003

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | SMS dispatch status peek on notification admin | Easy | 4 |
| API | SMS render-and-dispatch service | Complex | 8 |
| Integration | SMS gateway connector | Medium | 16 |
| Database | SMS dispatch attempt records | Easy | 2 |
| Testing | Template merge and gateway mock cases | Complex | 8 |
| Documentation | SMS dispatch notes | Easy | 2 |

**Feature Total: 40 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
