# F06-005 — Allotment Approval & Order
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Allotment Approval & Order |
| **Module** | 06 — Allotment Management |
### Description
Route recommended allotments through configured approvals, issue the allotment order, and record acceptance or refusal within the BDA timeline.
### Business Objective
Create a legally traceable allotment decision and stop double allotment of the same active site.
### Actors
Revenue/Allotment Officer; configured approvers; Applicant; Auditor.
### User Journey
Officer submits a recommendation; each approver reviews the applicant, site, selection evidence, and remarks; after final approval the system produces the order, notifies the applicant, and records acceptance/refusal by the due date.
### Functional Capabilities
- Approval worklist and decision screen, approved allotment register, order preview/download, and acceptance tracker.
- Generate template-based allotment order; lock site allocation while approval/acceptance is active.
### Inputs
Approved recommendation, order template, approver remarks, acceptance/refusal response, and dates.
### Outputs
Approval history, issued order, acceptance outcome, and site allotment status.
### Business Rules
Only approved recommendations produce orders; the same active site cannot have a second approved/current allotment; refusal or expiry releases the site only through the prescribed status action.
### Validations
Required approval sequence, active order template, acceptance date within configured timeline, and unique active site allocation.
### Calculations
Acceptance due date and pending-acceptance aging.
### Workflow
Recommended → multi-level approval → order issued → accepted/refused/expired → possession eligible.
### Search Requirements
Order reference, scheme, site, applicant, approval stage, issue date, acceptance status.
### Documents
Selection evidence, approval note, allotment order, acceptance/refusal communication.
### Reports
Allotment order register and acceptance-pendency report.
### Notifications
Approval tasks, order issue, acceptance reminder, and expiry alert via Module 11.
### Security
Maker-checker, role/zone scope, immutable approval history, applicant-owned order access only.
### Integrations
Citizen order publication/status notification (Simple).
### Dependencies
F06-004, Module 02 workflow/order templates, Modules 10–11, Module 04 site register.
### Assumptions
Order wording and acceptance period are maintained by BDA templates/configuration.
### Risks
Incorrect site lock/release status could cause conflicting allocations.
### Non Functional Requirements
Generated orders must be reproducible, access controlled, and audit timestamped.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Approval worklist and decision timeline | UI | Very High | 16 |
| Order register, preview and acceptance tracker | UI | Complex | 8 |
| Approval, allocation lock and acceptance processing | API | Very High | 16 |
| Allotment order and approval persistence | Database | Complex | 6 |
| Citizen order/status handoff | Integration | Simple | 4 |
| Approval and double-allotment tests | Testing | Very High | 12 |
| Order and approval guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
### Estimation Assumptions
Template configuration is in Module 02; payment collection is excluded unless enabled in Module 12.
