# F01-002 — Role & Permission Assignment

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-002 |
| Feature Name | Role & Permission Assignment |
| Module | 01 — User Access & Role Management |
| Description | Assign roles and permissions (Admin, Supervisor, Operator, and FRS-defined roles) to CMS users under User → Role → Permissions model. |
| Business Objective | Enforce least-privilege access aligned to CMS duties. |
| Actors | Admin |

### User Journey

- Admin opens role/permission screens → defines or selects role → maps permissions → assigns role to user.

### Functional Capabilities

- Role list and create/edit
- Permission matrix per role
- Assign one or more roles to a user as FRS defines

### Inputs

- Role name
- Permission set
- User–role mapping

### Outputs

- Role definitions
- Effective permissions for user

### Business Rules

- Access model is User → Role → Permissions
- Only Admin may change roles/permissions
- FRS-approved roles only

### Validations

- Role name required
- Cannot remove last Admin role without replacement

### Calculations

- None

### Workflow

- Define role → map permissions → assign to user

### Search Requirements

- Filter roles; find users by role

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Admin only
- Audit role and permission changes

### Integrations

- None

### Dependencies

- F01-001 User Lifecycle Management

### Assumptions

- FRS locks final permission catalogue

### Risks

- Late FRS role changes expand matrix scope

### Non Functional Requirements

- Permission checks on every protected action

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Role list and role create/edit form | Medium | 6 |
| UI | Permission matrix grid for role mapping | Complex | 8 |
| API | Role/permission CRUD and user–role assignment with rules | Complex | 8 |
| Database | Role, permission, and mapping entities with constraints | Medium | 4 |
| Testing | Permission matrix and assignment scenarios | Medium | 6 |
| Documentation | Role & permission admin notes | Easy | 2 |

**Feature Total: 34 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
