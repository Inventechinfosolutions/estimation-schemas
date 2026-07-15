# F01-003 — Department, Zone & Data Scoping
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Department, Zone & Data Scoping |
| **Module** | 01 — User & Role Management |
### Description
Define and apply department, zone, and assigned-record visibility for officer users.
### Business Objective
Ensure officers see and act only on records within their authorised organisational scope.
### Actors
Super Administrator; departmental administrator; Auditor.
### User Journey
Administrator selects a user or role, assigns permitted departments and zones, reviews effective scope, and saves the controlled assignment.
### Functional Capabilities
- Configure department and zone assignments.
- Support scoped visibility for layouts, sites, and process records.
- Review effective scope and audit changes.
### Inputs
User/role, department, zone, and scope selections.
### Outputs
Effective access scope and assignment audit.
### Business Rules
Data access requires both role permission and applicable scope; inactive scopes are not newly assignable.
### Validations
Valid active user, department, and zone; no duplicate assignment.
### Calculations
None.
### Workflow
Direct administration with audit.
### Search Requirements
User, role, department, zone, and scope status.
### Documents
None.
### Reports
User scope assignment export.
### Notifications
Optional scope-change notification.
### Security
Restricted to authorised administrators; scope changes are privileged actions.
### Integrations
Internal authorisation service (Simple).
### Dependencies
F01-001, F01-002, and Module 02 organisation masters.
### Assumptions
Layout-specific exceptions use the same configured scope model.
### Risks
Unclear zone ownership can cause access conflicts between sections.
### Non Functional Requirements
Consistent scope enforcement; auditability; responsive UI.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Scope assignment register | UI | Complex | 8 |
| Department/zone scope editor | UI | Complex | 8 |
| Scope evaluation and assignment operations | API | Complex | 8 |
| Scope assignment persistence | Database | Complex | 6 |
| Internal authorisation handoff | Integration | Simple | 4 |
| Scope enforcement tests | Testing | Very High | 12 |
| Scope configuration guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
External identity-provider claims are excluded.
