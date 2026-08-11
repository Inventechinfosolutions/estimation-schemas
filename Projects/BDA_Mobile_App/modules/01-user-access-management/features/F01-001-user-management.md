# F01-001 — User Management

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-001 |
| Feature Name | User Management |
| Module | 01 — User & Access Management |
| Description | Create, update, search, activate and deactivate BDA users who will use CDRMS (Engineers, CAO, Super Admin). |
| Business Objective | Maintain a controlled user register for CDRMS access. |
| Actors | Super Admin |

### User Journey

- Super Admin opens User register → searches/filters → creates or edits user profile → activates/deactivates as needed.

### Functional Capabilities

- User list with search/filter
- User create/edit form (name, mobile, email, employee/BDA ID, status)
- Activate/deactivate without deleting history

### Inputs

- Name
- Mobile
- Email
- Employee/BDA ID
- Status

### Outputs

- Saved user record
- Updated list

### Business Rules

- Only Super Admin may manage users
- Mobile unique per active user
- Deactivated users cannot log in

### Validations

- Mandatory name and mobile
- Valid mobile/email format

### Calculations

- None

### Workflow

- Create → Active; deactivate → Inactive

### Search Requirements

- Search by name, mobile, employee ID, status

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Super Admin only
- Audit create/update/deactivate

### Integrations

- None

### Dependencies

- None

### Assumptions

- User list provided by BDA for initial load

### Risks

- Duplicate mobiles in legacy lists

### Non Functional Requirements

- Web responsive; audit of changes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | User list screen | Easy | 4 |
| UI | User create/edit form | Medium | 6 |
| API | User CRUD with search | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 26 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
