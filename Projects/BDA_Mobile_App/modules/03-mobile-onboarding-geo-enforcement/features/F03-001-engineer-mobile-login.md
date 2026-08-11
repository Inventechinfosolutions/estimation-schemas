# F03-001 — Engineer Mobile Login

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-001 |
| Feature Name | Engineer Mobile Login |
| Module | 03 — Mobile Onboarding & Geo Enforcement |
| Description | Initiate engineer mobile login using provisioned identity with no OTP-free access path. |
| Business Objective | Start a secure mobile session only for provisioned engineers. |
| Actors | Engineer |

### User Journey

- Engineer opens app → enters identity → proceeds to OTP step (F03-002).

### Functional Capabilities

- Identity entry screen
- Reject unknown/deactivated users

### Inputs

- Employee ID / registered mobile

### Outputs

- OTP challenge initiated

### Business Rules

- Only active Engineer role users
- Online-only

### Validations

- Identity required

### Calculations

- None

### Workflow

- Identity → OTP

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- Triggers OTP

### Security

- Active engineer only

### Integrations

- Uses notification service for OTP

### Dependencies

- F01-003
- F07-001

### Assumptions

- App installed and online

### Risks

- Shared devices

### Non Functional Requirements

- Works on Android and iOS

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Mobile login identity screen | Medium | 6 |
| API | Validate engineer identity & start login | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Integration | External/internal integration for this feature | Simple | 4 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 26 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
