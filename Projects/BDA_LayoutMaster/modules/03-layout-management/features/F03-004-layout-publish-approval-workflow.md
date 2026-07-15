# F03-004 — Layout Publish Approval Workflow
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Layout Publish Approval Workflow |
| **Module** | 03 — Layout Management |
### Description
Execute configured approval for layout creation, major amendment, and publication before activation where required.
### Business Objective
Ensure only authorised, reviewed layouts become active or public.
### Actors
Proposer; Town Planning/Engineering reviewers; approvers; Auditor.
### User Journey
Officer submits layout, reviewers approve/reject/return with remarks, and the system activates/publishes only after successful completion.
### Functional Capabilities
Submit, worklist, approve/reject/return, remarks, history, document context, and effective activation/publish status.
### Inputs
Layout, configured route, action, remarks, supporting attachments.
### Outputs
Approval decision, history, effective layout status.
### Business Rules
Configured approval gates site creation/public display; proposer cannot approve own controlled request.
### Validations
Eligible layout state; authorised approver; required remarks on reject/return.
### Calculations
None.
### Workflow
Draft/amendment → configured levels → active/published or returned/rejected.
### Search Requirements
Layout, status, approver, date, pending stage.
### Documents
Uses embedded layout documents from F03-003.
### Reports
Layout approval history/pendency export.
### Notifications
Workflow alerts via Module 11 where enabled.
### Security
RBAC, SoD enforcement, scoped access, audit.
### Integrations
Internal workflow/notification consumption (Simple).
### Dependencies
F02-006, F01-008, F03-001, Module 11.
### Assumptions
Workflow definition is configured in Module 02.
### Risks
Missing approvers can delay activation.
### Non Functional Requirements
Reliable audit/history and prompt worklist response.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Approval worklist | UI | Very High | 16 |
| Decision and history view | UI | Complex | 8 |
| Runtime approval operations | API | Very High | 16 |
| Approval history persistence | Database | Complex | 6 |
| Internal workflow/notification consumption | Integration | Simple | 4 |
| Approval workflow tests | Testing | Very High | 12 |
| Approval user guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
### Estimation Assumptions
Generic workflow configuration is not duplicated.
