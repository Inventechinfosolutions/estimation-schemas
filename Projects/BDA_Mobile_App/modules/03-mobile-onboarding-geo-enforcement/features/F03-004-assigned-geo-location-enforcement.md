# F03-004 — Assigned Geo-Location Enforcement

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-004 |
| Feature Name | Assigned Geo-Location Enforcement |
| Module | 03 — Mobile Onboarding & Geo Enforcement |
| Description | Prevent capture/submit outside the engineer’s assigned geo-location with server-side enforcement. |
| Business Objective | Stop cross-location CDR data entry. |
| Actors | Engineer; System |

### User Journey

- On save/submit, system checks assigned geo vs selected/current location → deny with message if mismatch; log attempt.

### Functional Capabilities

- Server-side geo check on save/submit
- Clear denial message
- Auditable denial

### Inputs

- Assigned geo
- Attempted site geo/context

### Outputs

- Allow or deny save/submit

### Business Rules

- Client checks insufficient alone
- Deny other locations

### Validations

- Mandatory geo context on submit

### Calculations

- None

### Workflow

- Validate → Allow/Deny

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Enforce for Engineer role

### Integrations

- None

### Dependencies

- F01-003
- F02-001
- F03-003

### Assumptions

- Geo masters meaningful for field

### Risks

- GPS drift near boundaries

### Non Functional Requirements

- Denial audited

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Geo violation messaging on mobile | Medium | 6 |
| API | Server geo enforcement on save/submit | Complex | 8 |
| Database | Persistence / constraints for this feature | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 29 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
