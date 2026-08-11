# F01-001 — User Lifecycle Management

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-001 |
| Feature Name | User Lifecycle Management |
| Module | 01 — User Access & Role Management |
| Description | Create, update, search, activate and deactivate CMS users who access the KSCW Complaint Management System. |
| Business Objective | Maintain a controlled user register for secure CMS operations. |
| Actors | Admin |

### User Journey

- Admin opens User register → searches/filters users → creates or edits profile → activates or deactivates as needed.

### Functional Capabilities

- User list with search and filter
- User create/edit form (name, mobile, email, employee ID, status)
- Activate/deactivate without deleting history

### Inputs

- Name
- Mobile
- Email
- Employee / staff ID
- Status

### Outputs

- Saved user record
- Updated user list

### Business Rules

- Only Admin may manage users
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

- Admin only
- Audit create/update/deactivate

### Integrations

- None

### Dependencies

- None (foundation)

### Assumptions

- Initial user list provided by KSCW for load

### Risks

- Duplicate mobiles in legacy staff lists

### Non Functional Requirements

- Web responsive; audit of changes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | CMS User register list with search/filter | Easy | 4 |
| UI | User create/edit profile form | Medium | 6 |
| API | User CRUD with search and activate/deactivate | Medium | 6 |
| Database | User entity persistence and unique mobile constraint | Easy | 2 |
| Testing | User lifecycle happy-path and negative cases | Medium | 6 |
| Documentation | User admin feature notes | Easy | 2 |

**Feature Total: 26 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
