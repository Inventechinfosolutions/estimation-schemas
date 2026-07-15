# F01-002 — Roles & Permission Sets
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Roles & Permission Sets |
| **Module** | 01 — User & Role Management |
### Description
Configure officer roles and module/action permission sets used throughout LMS.
### Business Objective
Enforce least-privilege access without code changes.
### Actors
Super Administrator; Auditor (read-only).
### User Journey
Administrator creates or updates a role, selects permitted modules and actions, reviews assigned users, and activates the role.
### Functional Capabilities
- Role CRUD and activation control.
- Configure module and action permissions.
- View role-to-user assignments and change history.
### Inputs
Role name, description, permission selections, status.
### Outputs
Active permission set and role matrix export.
### Business Rules
Only active roles may be assigned; protected administrator access cannot be removed without authorised replacement.
### Validations
Unique role name; at least one action for an active role.
### Calculations
None.
### Workflow
Direct configuration with audited changes.
### Search Requirements
Role name, module, action, status.
### Documents
None.
### Reports
Role–permission matrix.
### Notifications
Optional notification to impacted administrators.
### Security
Only Super Administrator changes permissions; all changes audited.
### Integrations
Internal authorisation service (Simple).
### Dependencies
F01-001 officer users; all consuming modules.
### Assumptions
Permission model is module plus action, as stated in the SOW.
### Risks
Overly broad permissions can compromise confidential operational data.
### Non Functional Requirements
Auditable configuration; responsive administration UI.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Role register + permission search | UI | Complex | 8 |
| Role and permission editor | UI | Complex | 8 |
| Role, permission, and assignment operations | API | Complex | 8 |
| Role and permission persistence | Database | Complex | 6 |
| Internal authorisation handoff | Integration | Simple | 4 |
| Permission enforcement tests | Testing | Very High | 12 |
| Role administration guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Fine-grained data-scope enforcement is estimated in F01-003.
