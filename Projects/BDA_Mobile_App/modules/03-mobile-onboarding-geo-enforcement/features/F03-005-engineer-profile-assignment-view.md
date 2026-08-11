# F03-005 — Engineer Profile & Assignment View

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-005 |
| Feature Name | Engineer Profile & Assignment View |
| Module | 03 — Mobile Onboarding & Geo Enforcement |
| Description | Show engineer identity and assigned geo-location on mobile. |
| Business Objective | Let engineers confirm who they are and which location they may work in. |
| Actors | Engineer |

### User Journey

- Engineer opens profile → sees name, role, assigned geo.

### Functional Capabilities

- Read-only profile and assignment summary

### Inputs

- Authenticated engineer

### Outputs

- Profile display

### Business Rules

- Read-only

### Validations

- None

### Calculations

- None

### Workflow

- None

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Own profile only

### Integrations

- None

### Dependencies

- F03-002

### Assumptions

- Profile data from user master

### Risks

- Stale assignment display if not refreshed

### Non Functional Requirements

- Available online after login

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Mobile profile screen | Simple | 2 |
| API | Get engineer profile | Simple | 2 |
| Database | Persistence / constraints for this feature | Simple | 1 |
| Testing | Feature test coverage | Simple | 2 |
| Documentation | Feature documentation | Simple | 1 |

**Feature Total: 8 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
