# F01-005 — Role & Permission Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-005 |
| **Feature Name** | Role & Permission Management |
| **Module** | 01 — User & Role Management |

### Description
Define roles and maintain a module-and-action permission matrix so users only access authorized functions, satisfying SOW RBAC and least-privilege requirements.

### Business Objective
Implement role-based access control for all CPMS modules with an administrable permission model and a BDA-signoff-ready role–permission matrix.

### Actors
- Super Administrator
- Auditor (read-only matrix view)
- All users (consumers of enforced permissions)

### User Journey
1. Admin opens Roles.
2. Creates or edits a role (e.g., Estate Officer, Accounts Officer).
3. Opens permission matrix and grants View/Create/Update/Approve/Export (and similar actions) per module.
4. Saves matrix; changes apply on next authorization check / session refresh policy.
5. Assigns roles to users (via F01-004).

### Functional Capabilities
- CRUD for roles (system roles vs custom roles)
- Permission catalog by module and action
- Matrix UI to grant/revoke permissions
- Clone role
- Activate/deactivate role (cannot assign inactive roles)
- Seed baseline roles from SOW indicative list (see also F01-010)

### Inputs
- Role code, name, description, status
- Permission checks (module, action, allow/deny)

### Outputs
- Saved role and matrix
- Effective permissions for authorization service
- Matrix export for BDA sign-off (Excel/PDF)

### Business Rules
- Least privilege default (no implicit all-access except Super Administrator).
- Super Administrator role is protected from permission stripping that would lock out administration.
- Deactivated roles cannot be newly assigned.
- Permission changes are audited.
- Segregation-of-duties constraints (F01-007) validated when saving user-role combinations and optionally when editing matrix pairs.

### Validations
- Unique role code
- At least one permission for activatable custom roles (configurable)
- Prevent empty Super Admin matrix

### Calculations
None.

### Workflow
Optional approval for changes to privileged finance permissions (if Module 02 workflow configured). Baseline: Super Admin direct with audit.

### Search Requirements
- Search roles by name/code/status
- Filter permissions by module in matrix

### Documents
Role–permission matrix export for design sign-off.

### Reports
Role Register; Permission Matrix export.

### Notifications
Optional alert to auditors when privileged matrix changes.

### Security
- Matrix admin restricted to Super Administrator (or equivalent permission)
- Authorization enforced server-side on every operation (not UI-only hiding)

### Integrations
None.

### Dependencies
- Module catalog aligned to CPMS modules 01–11
- F01-004 for assignment
- F01-007 for SoD checks
- Consumed by all business modules

### Assumptions
- Actions standardized (View, Create, Update, Delete/Deactivate, Approve, Export, Configure) unless BDA finalizes a richer set during design.
- Indicative SOW roles used as baseline seed.
- Dynamic matrix UI justifies Very High UI complexity.
- Enterprise RBAC enforcement and tests included.

### Risks
- Incomplete module action catalog early in project causes matrix rework.
- Over-permissive defaults increase audit findings.

### Non Functional Requirements
- Matrix usable for ~12 modules × standard actions without critical performance issues
- Export to Excel/PDF
- English UI mandatory

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: dynamic permission matrix UI, authorization model, protected system roles, exportable matrix deliverable.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Role list screen | UI | Easy | 4 |
| Role create / edit form | UI | Medium | 6 |
| Permission matrix (module × action) screen | UI | Very High | 16 |
| Role CRUD operations | API | Medium | 6 |
| Permission matrix load/save operations | API | Complex | 8 |
| Role, permission, mapping schema | Database | Complex | 6 |
| RBAC matrix tests | Testing | Very High | 12 |
| Role–permission matrix deliverable docs | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
- Permission matrix UI classified Very High (dynamic UI per Estimation Master).
- Testing Very High due to cross-module authorization scenarios.
