# F03-006 — Layout Archive
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F03-006 |
| **Feature Name** | Layout Archive |
| **Module** | 03 — Layout Management |
### Description
Archive applicable layouts without losing history or linked site references.
### Business Objective
Control lifecycle closure while preserving the authoritative record.
### Actors
Town Planning Officer; authorised approver; Auditor.
### User Journey
Officer selects an eligible layout, records reason, submits if approval is configured, and views its retained archived record.
### Functional Capabilities
Archive request, reason capture, impact warning, status transition, historical retrieval, audit.
### Inputs
Layout, archive reason, remarks, configured approval action.
### Outputs
Archived status and retained historical record.
### Business Rules
Archived layouts retain linked-site references and are not available for new site creation.
### Validations
Eligible state; mandatory reason; authorised action.
### Calculations
Linked-site impact summary.
### Workflow
Request → configured approval when required → archive.
### Search Requirements
Layout identity, archive status, date, actor.
### Documents
Existing layout documents remain linked.
### Reports
Archived layout register.
### Notifications
Optional workflow alert.
### Security
RBAC, scope, audit.
### Integrations
Internal site/workflow consumption (Simple).
### Dependencies
F03-001, F03-004, Module 04.
### Assumptions
Archive does not erase GIS or documents.
### Risks
Archiving a layout with active sites requires controlled business decision.
### Non Functional Requirements
Historical retrieval; auditable state change.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Archive confirmation/impact view | UI | Medium | 6 |
| Archived layout search | UI | Easy | 4 |
| Archive lifecycle operations | API | Complex | 8 |
| Archive status/audit persistence | Database | Medium | 4 |
| Internal site/workflow consumption | Integration | Simple | 4 |
| Archive integrity tests | Testing | Complex | 8 |
| Archive guide | Documentation | Easy | 2 |
| **Total** | | | **36** |
### Estimation Assumptions
No physical record deletion is included.
