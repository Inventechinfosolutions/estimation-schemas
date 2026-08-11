# F06-002 — Email Notification Dispatch

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-002 |
| Feature Name | Email Notification Dispatch |
| Module | 06 — Notifications & Alerts (SMS / Email) |
| Description | Dispatch Email alerts for configured complaint events using templates. |
| Business Objective | Provide richer written notifications for events. |
| Actors | System; Admin |

### User Journey

- Event occurs → email template rendered → email sent → status logged.

### Functional Capabilities

- Event-driven email send
- Subject/body template merge
- Delivery/accept status logging

### Inputs

- Event payload
- Email address
- Template

### Outputs

- Outbound email
- Log entry

### Business Rules

- Configured events only
- Skip if no email

### Validations

- Email format
- Active template

### Calculations

- None

### Workflow

- Event → render → send → log

### Search Requirements

- Via F06-003

### Documents

- None

### Reports

- None

### Notifications

- This feature is the Email channel

### Security

- SMTP credentials secured

### Integrations

- SMTP / email gateway

### Dependencies

- F02-004
- Modules 03–05

### Assumptions

- Mail relay provided by KSCW

### Risks

- Spam filtering blocks complainant mail

### Non Functional Requirements

- Async send; bounded retries

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Email template preview from dispatch admin | Medium | 6 |
| API | Email render-and-dispatch service | Complex | 8 |
| Integration | SMTP/email gateway connector | Easy | 8 |
| Database | Email dispatch attempt records | Easy | 2 |
| Testing | Email merge and send mock cases | Medium | 6 |
| Documentation | Email dispatch notes | Easy | 2 |

**Feature Total: 32 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
