# F01-008 — Segregation of Duties Enforcement
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F01-008 |
| **Feature Name** | Segregation of Duties Enforcement |
| **Module** | 01 — User & Role Management |
### Description
Prevent the same user from proposing and approving controlled classification, auction, allotment, and CA actions.
### Business Objective
Enforce maker–checker accountability across governed processes.
### Actors
Super Administrator; proposer; approver; Auditor.
### User Journey
User submits a controlled transaction; the system identifies the originating user and excludes them from approval actions, showing an actionable restriction where necessary.
### Functional Capabilities
Configure governed action pairs, detect conflicts at action time, block conflicts, and retain decision audit evidence.
### Inputs
User identity, role, transaction originator, workflow action.
### Outputs
Allowed action, conflict block message, and SoD audit entry.
### Business Rules
An originator cannot approve their own controlled transaction; configured exception authority is auditable.
### Validations
Valid governed process/action; transaction originator present; authorised approver.
### Calculations
None.
### Workflow
Propose → route to eligible non-originator approver → approve/reject/return.
### Search Requirements
Process, transaction reference, originator, approver, conflict outcome.
### Documents
None.
### Reports
SoD conflict and exception report.
### Notifications
Workflow notification remains in the owning business process.
### Security
Server-side enforcement, RBAC, audit, and restricted exception configuration.
### Integrations
Internal workflow/authorisation service (Simple).
### Dependencies
F01-002, F01-003, Module 02 workflow configuration, and consuming business modules.
### Assumptions
Controlled processes are those named by the SOW; workflow runtime remains embedded in business features.
### Risks
Incomplete workflow configuration could leave an approval route without an eligible approver.
### Non Functional Requirements
Reliable transaction-time enforcement and auditability.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| SoD rule and exception review | UI | Complex | 8 |
| Conflict message/detail view | UI | Medium | 6 |
| SoD evaluation operations | API | Complex | 8 |
| SoD policy and event persistence | Database | Medium | 4 |
| Internal workflow/authorisation handoff | Integration | Simple | 4 |
| Maker–checker enforcement tests | Testing | Very High | 12 |
| SoD configuration guide | Documentation | Medium | 3 |
| **Total** | | | **45** |
### Estimation Assumptions
Workflow definition is not duplicated here; it is Module 02 scope.
