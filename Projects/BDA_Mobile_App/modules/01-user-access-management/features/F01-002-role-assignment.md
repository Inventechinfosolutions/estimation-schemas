# F01-002 — Role Assignment

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-002 |
| Feature Name | Role Assignment |
| Module | 01 — User & Access Management |
| Description | Assign each user one of Engineer, CAO, or Super Admin roles controlling channel and functions. |
| Business Objective | Ensure each user has the correct role for mobile or web duties. |
| Actors | Super Admin |

### User Journey

- Super Admin opens user → assigns/changes role → saves; effective access updates on next login.

### Functional Capabilities

- Assign Engineer / CAO / Super Admin to user
- Prevent role-less active users

### Inputs

- User
- Role

### Outputs

- User with role

### Business Rules

- Active user must have exactly one baseline role
- Engineer role required for geo binding

### Validations

- Role mandatory for active users

### Calculations

- None

### Workflow

- Role change effective on next session

### Search Requirements

- Filter users by role

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Super Admin only

### Integrations

- None

### Dependencies

- F01-001

### Assumptions

- Baseline roles fixed to three

### Risks

- Wrong role grants excess access

### Non Functional Requirements

- Immediate effect after re-login

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Role assignment on user form | Easy | 4 |
| API | Assign/update user role | Easy | 4 |
| Database | Persistence / constraints for this feature | Simple | 1 |
| Testing | Feature test coverage | Easy | 4 |
| Documentation | Feature documentation | Simple | 1 |

**Feature Total: 14 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
