# F04-006 — Site Cancellation & Deactivation
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-006 |
| **Feature Name** | Site Cancellation & Deactivation |
| **Module** | 04 — Site Management & Classification |
### Description
Cancel or deactivate applicable site records with reason, controlled approval, and retained history.
### Business Objective
Prevent invalid sites from future process use without deleting evidence.
### Actors
Town Planning; authorised approver; Auditor.
### User Journey
Officer requests cancellation, records reason and impact, completes configured approval, and views archived status.
### Functional Capabilities
Cancellation request, reason, impact warning, approval, status update, audit/history.
### Inputs
Site, reason, remarks, approval action.
### Outputs
Cancelled/deactivated status and audit outcome.
### Business Rules
Cancelled sites are unavailable to new processes; history/documents/classifications are retained.
### Validations
Eligible site state; mandatory reason; authorised actor.
### Calculations
Open-process impact summary.
### Workflow
Request → configured approval → cancelled/deactivated.
### Search Requirements
Site, status, cancellation date/reason.
### Documents
Supporting evidence uses F04-003.
### Reports
Cancellation register.
### Notifications
Workflow alerts where enabled.
### Security
RBAC, SoD, audit.
### Integrations
Internal workflow/process-status consumption (Simple).
### Dependencies
F02-006, F04-001, F04-003, downstream process modules.
### Assumptions
BDA defines permitted cancellation states.
### Risks
Cancellation with active case dependencies needs business resolution.
### Non Functional Requirements
Auditable state transition and historical access.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Cancellation request/impact | UI | Complex | 8 |
| Cancellation history search | UI | Easy | 4 |
| Cancellation lifecycle operations | API | Complex | 8 |
| Status/audit persistence | Database | Medium | 4 |
| Internal workflow/process consumption | Integration | Simple | 4 |
| Cancellation tests | Testing | Complex | 8 |
| Cancellation guide | Documentation | Easy | 2 |
| **Total** | | | **38** |
### Estimation Assumptions
Workflow configuration is Module 02 scope.
