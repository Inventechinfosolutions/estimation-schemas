# F01-002 — Roles & Permission Sets

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Roles & Permission Sets |
| **Module** | 01 — User & Role Management |

### Description
Define **Roles** and their module/action **permission sets**. In the BDA model, a Role is attached to a **Post** (F01-003), not directly to a Person. Persons inherit permissions only through Person–Post mapping (F01-001).

### Business Objective
Enforce least-privilege access through reusable roles that posts carry.

### Actors
Super Administrator; Auditor (read-only).

### User Journey
Administrator creates a Role, selects permitted modules and actions in the permission matrix, activates the Role, then attaches it to Posts in F01-003 (not to persons).

### Functional Capabilities
- Create, edit, clone, activate/deactivate Roles  
- Module/action permission matrix  
- Role register and matrix export  
- View which Posts currently use a Role (read-only reference)

### Inputs
Role name, description, module/action selections, status.

### Outputs
Configured Role, permission matrix, Role Register.

### Business Rules
- A Role grants only explicitly selected actions.  
- Inactive Roles cannot be newly attached to Posts.  
- Persons do not receive Role assignment in this feature.  
- Changing permissions on a Role affects all Posts carrying that Role (and thus all mapped persons).  
- Access changes are auditable.

### Validations
Unique role name; at least one permission for active roles; no duplicate permission entries.

### Calculations
None.

### Workflow
Direct configuration with audit.

### Search Requirements
Role name, status, module, action, Post using the role.

### Documents
None.

### Reports
Role–Permission Matrix; Role Register; Role-to-Post usage list.

### Notifications
Optional notice to administrators after material permission changes.

### Security
Super Administrator only for edits; permission changes logged; read-only auditor access.

### Integrations
Internal authorisation policy handoff (Simple).

### Dependencies
F01-003 consumes Roles on Posts; F01-001 persons inherit via Posts.

### Assumptions
Permissions are module-plus-action based; record-level ACL authoring is out of scope unless added later.

### Risks
Over-broad Roles propagate widely through Posts that use them.

### Non Functional Requirements
Fast permission evaluation at session/request time; immutable audit events.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Role Register + filters | UI | Medium | 6 |
| Role editor and permission matrix | UI | Very High | 16 |
| Role-to-Post usage view | UI | Easy | 4 |
| Role and permission operations | API | Complex | 8 |
| Role-permission persistence | Database | Complex | 6 |
| Authorisation policy handoff | Integration | Simple | 4 |
| Role security tests | Testing | Very High | 12 |
| Role configuration guide | Documentation | Medium | 3 |
| **Total** | | | **59** |

### Estimation Assumptions
- Uses Estimation Master values only.  
- Post attachment of Roles is estimated in F01-003.  
