# F07-001 — SMS OTP Dispatch & Validation

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-001 |
| Feature Name | SMS OTP Dispatch & Validation |
| Module | 07 — Notification Service |
| Description | Send and validate OTP via SMS gateway for every engineer mobile login. |
| Business Objective | Deliver reliable OTP for mandatory every-login authentication. |
| Actors | System; Engineer |

### User Journey

- Login requests OTP → SMS sent to registered mobile → validation result returned to login flow; delivery logged.

### Functional Capabilities

- Dispatch SMS OTP
- Validate OTP
- Resend cooldown
- Delivery logging
- Honor OTP parameters

### Inputs

- Mobile number
- OTP request

### Outputs

- OTP delivery status
- Validation result

### Business Rules

- Single-use OTP
- Expiry and attempt limits from parameters

### Validations

- OTP match/expiry

### Calculations

- None

### Workflow

- Request → Send → Validate

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- SMS OTP

### Security

- Only for provisioned engineer mobiles

### Integrations

- SMS gateway

### Dependencies

- F02-004
- F03-002

### Assumptions

- SMS gateway credentials arranged

### Risks

- Gateway downtime blocks login

### Non Functional Requirements

- Retry/logging for support

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | OTP service admin/log view (minimal) | Simple | 2 |
| API | OTP issue/validate APIs | Complex | 8 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Integration | External/internal integration for this feature | Medium | 16 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 39 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
