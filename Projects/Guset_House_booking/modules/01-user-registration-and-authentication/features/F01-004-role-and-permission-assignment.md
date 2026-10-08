# F01-004 — Role and Permission Assignment

| Field | Value |
|-------|-------|
| Feature ID | F01-004 |
| Feature Name | Role and Permission Assignment |
| Module | 01 — User Registration & Authentication |
| Type | Shared |
| Notes | Go-live |

## Feature Specification

### Description
Lets Platform Administrators assign User→Role→Permissions so employees and administrators receive appropriate access.

### Business Objective
Enforce least-privilege access across employee and admin functions.

### Actors
- Platform Administrator
- Auditor

### User Journey
1. Platform Administrator creates/maintains roles and assigns them to users.
2. Administrator opens role catalogue, defines permissions, and maps users to roles.
3. Administrator edits role permissions or user-role mappings; changes take effect on next authorisation check.
4. Approval does not apply unless client later mandates maker-checker; Phase 1 is direct admin apply with audit.
5. No approver inbox in Phase 1.
6. No approver decision in Phase 1.
7. Administrator sees change history on role/user mapping screens.
8. Auditor views permission change history.

### Functional Capabilities
- Maintain roles
- Assign permissions to roles
- Assign roles to users
- Disable role assignment
- Audit permission changes

### UI Screens
- Role catalogue register
- Role permission matrix screen
- User-role assignment screen
- Permission change history screen

### Logical API Operations
- List roles
- Save role permissions
- Assign roles to user
- Get permission change history

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Permissions granted only via roles
- Platform Administrator cannot be lockout-orphaned (break-glass policy)
- Site Administrator scoped where configured

### Validations
- Role name unique
- At least one permission or explicit empty denied
- User must exist

### Calculations
- None beyond display counters

### Workflow
RoleDraft → Active → Inactive; UserRoleAssigned → Effective

### Search Requirements
Search users by name/mobile; filter roles

### Documents
None

### Reports
None

### Notifications
None

### Security
- Only Platform Administrator manages roles
- All changes audited

### Integrations
None

### Dependencies
- F01-003

### Assumptions
- Indicative roles: Employee Guest, Site Administrator, Platform Administrator, Auditor

### Risks
- Over-privileged roles if matrix is coarse

### Non Functional Requirements
- Authorisation checks enforced server-side on every operation

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Role catalogue register | Medium | 6 |
| UI | Role permission matrix screen | Complex | 12 |
| UI | User-role assignment screen | Medium | 6 |
| UI | Permission change history screen | Easy | 4 |
| API | List roles | Easy | 4 |
| API | Save role permissions | Complex | 8 |
| API | Assign roles to user | Medium | 6 |
| API | Get permission change history | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 63 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Indicative roles: Employee Guest, Site Administrator, Platform Administrator, Auditor / Over-privileged roles if matrix is coarse.
