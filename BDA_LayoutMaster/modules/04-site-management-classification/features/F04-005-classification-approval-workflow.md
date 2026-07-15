# F04-005 — Classification Approval Workflow
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Classification Approval Workflow |
| **Module** | 04 — Site Management & Classification |
### Description
Execute department-wise multi-level verification and approval for special site classifications.
### Business Objective
Prevent unapproved classifications from driving Auction, CA, Land Loser, Commercial, Utility, or Reserved processes.
### Actors
Proposer; department verifiers; approvers; Auditor.
### User Journey
Proposer submits classification, reviewers examine site/document context and act with remarks, and approval makes the category effective.
### Functional Capabilities
Worklist, verify/approve/reject/return, remarks, history, evidence context, effective-status update.
### Inputs
Classification proposal, configured route, decision, remarks, attachments.
### Outputs
Approval result, complete history, updated eligibility status.
### Business Rules
Only successful approval makes special classification effective; proposer cannot self-approve.
### Validations
Valid pending proposal; authorised stage actor; reasons required for reject/return.
### Calculations
None.
### Workflow
Propose → department verification → multi-level decision → effective/rejected/returned.
### Search Requirements
Site, category, status, stage, approver, date.
### Documents
Classification approval documents use F04-003.
### Reports
Approval pendency/history report.
### Notifications
Workflow alerts via Module 11 where enabled.
### Security
RBAC, SoD, scope controls, audit.
### Integrations
Internal workflow/notification consumption (Simple).
### Dependencies
F01-008, F02-006, F04-004, Module 11.
### Assumptions
Workflow definitions are maintained in Module 02.
### Risks
Variable departmental routes can increase configuration complexity.
### Non Functional Requirements
Reliable audit and worklist performance.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Classification approval worklist | UI | Very High | 16 |
| Decision/history/evidence view | UI | Complex | 8 |
| Runtime approval operations | API | Very High | 16 |
| Approval history persistence | Database | Complex | 6 |
| Internal workflow/notification consumption | Integration | Simple | 4 |
| Workflow tests | Testing | Very High | 12 |
| Approval guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
### Estimation Assumptions
No standalone workflow engine is estimated.
