# F01-001 — Officer User Management
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Officer User Management |
| **Module** | 01 — User & Role Management |
### Description
Maintain BDA officer accounts, their status, department, zone, and assigned access roles.
### Business Objective
Provide controlled officer access to LMS operations.
### Actors
Super Administrator; departmental administrator; Auditor (read-only).
### User Journey
Administrator searches users, creates or updates an officer account, assigns organisational context and roles, then activates or deactivates access.
### Functional Capabilities
- Create, update, view, activate, and deactivate officer accounts.
- Assign departments, zones, and one or more roles; retain activity history.
- Search and export the officer user register.
### Inputs
Officer identity, contact details, employee reference, department, zone, roles, and status.
### Outputs
Officer user record and searchable/exportable user register.
### Business Rules
Only authorised administrators manage users; deactivation blocks future access while retaining history.
### Validations
Required identity and organisation fields; unique login identifier; active role and department selections.
### Calculations
None.
### Workflow
Direct administration with audit; optional maker-checker is governed by configured policy.
### Search Requirements
Name, login ID, department, zone, role, and active status.
### Documents
None.
### Reports
Officer User Register export.
### Notifications
Optional account activation notification.
### Security
RBAC, least privilege, privileged-action audit, and restricted administrator access.
### Integrations
Internal authorisation service (Simple).
### Dependencies
Module 02 organisation masters and F01-002 roles.
### Assumptions
External IdP/SSO federation is excluded.
### Risks
Incorrect organisational assignment can expose records outside the intended scope.
### Non Functional Requirements
Responsive administration UI; auditable changes; agreed page response targets.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Officer user register + search | UI | Complex | 8 |
| Officer create/edit and role assignment | UI | Complex | 8 |
| User lifecycle and register operations | API | Complex | 8 |
| User and organisational assignment persistence | Database | Complex | 6 |
| Internal authorisation handoff | Integration | Simple | 4 |
| User administration tests | Testing | Very High | 12 |
| User administration guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Role and data-scope rule definition is estimated separately in F01-002 and F01-003.
