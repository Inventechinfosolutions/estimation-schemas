# F03-002 — Mandatory OTP Login (Every Session)

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-002 |
| Feature Name | Mandatory OTP Login (Every Session) |
| Module | 03 — Mobile Onboarding & Geo Enforcement |
| Description | Require OTP validation on every login before establishing a session; fresh OTP after logout/expiry. |
| Business Objective | Ensure every engineer session is OTP-verified. |
| Actors | Engineer |

### User Journey

- After identity → OTP sent to registered mobile → engineer enters OTP → session starts; logout requires new OTP.

### Functional Capabilities

- OTP entry
- Resend with cooldown
- Session only after success
- No remembered OTP-once login

### Inputs

- OTP code

### Outputs

- Authenticated session

### Business Rules

- OTP every login
- Single-use, time-bound
- Max attempts/resend cooldown

### Validations

- OTP format/length
- Expiry check

### Calculations

- None

### Workflow

- Send OTP → Validate → Session

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- SMS OTP

### Security

- Block after max failures per policy

### Integrations

- SMS gateway via F07-001

### Dependencies

- F03-001
- F07-001
- F02-004

### Assumptions

- Registered mobile reachable

### Risks

- SMS delay in field

### Non Functional Requirements

- Session timeout from parameters

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Mobile OTP entry & resend screens | Complex | 8 |
| API | Issue/validate OTP session | Complex | 8 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Integration | External/internal integration for this feature | Simple | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 33 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
