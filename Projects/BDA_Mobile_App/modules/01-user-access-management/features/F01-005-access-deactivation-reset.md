# F01-005 — Access Deactivation & Reset

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-005 |
| Feature Name | Access Deactivation & Reset |
| Module | 01 — User & Access Management |
| Description | Deactivate users and support secure credential reset when access must be revoked or recovered. |
| Business Objective | Keep access current when staff leave or credentials are compromised. |
| Actors | Super Admin |

### User Journey

- Super Admin deactivates user or initiates reset → user cannot log in until reactivated / reset completed.

### Functional Capabilities

- Deactivate/reactivate
- Secure credential reset

### Inputs

- User
- Reset request

### Outputs

- Inactive user / new credentials

### Business Rules

- Deactivated users blocked at login
- Historical applications remain visible to authorized roles

### Validations

- Confirm before deactivate

### Calculations

- None

### Workflow

- Active ↔ Inactive; Reset flow

### Search Requirements

- List inactive users

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Super Admin only
- Audit deactivate/reset

### Integrations

- None

### Dependencies

- F01-001

### Assumptions

- Reset channel agreed operationally

### Risks

- Delayed deactivation leaves open access

### Non Functional Requirements

- Immediate login block on deactivate

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Deactivate action | Simple | 2 |
| UI | Credential reset dialog | Easy | 4 |
| API | Deactivate and reset credential | Easy | 4 |
| Database | Persistence / constraints for this feature | Simple | 1 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Simple | 1 |

**Feature Total: 16 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
