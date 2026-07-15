# F06-007 — Mutation, Cancellation & Surrender
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-007 |
| **Feature Name** | Mutation, Cancellation & Surrender |
| **Module** | 06 — Allotment Management |
### Description
Control post-order mutation, cancellation, and voluntary surrender requests with evidence, approval, and resulting site-status changes.
### Business Objective
Preserve the allotment chain of custody while allowing BDA-approved corrections or release of a site.
### Actors
Revenue/Allotment Officer; Applicant/Allottee; configured approvers; Auditor.
### User Journey
Officer registers a mutation, cancellation, or surrender request against the allotment, captures the reason and documents, routes it for approval, then applies the approved outcome and records whether the site is released, retained, or needs further action.
### Functional Capabilities
- Case register, request form, reason/document checklist, approval timeline, and outcome/status view.
- Preserve prior allottee and possession history; prevent new allotment while a change case is pending.
### Inputs
Allotment/order reference, request type, reason, effective date, supporting evidence, and approver remarks.
### Outputs
Approved/rejected change case, revised allotment/site status, and history export.
### Business Rules
Only a current allotment can be changed; cancellation/surrender never deletes history; site availability is restored only after the approved outcome permits release.
### Validations
Valid request type, mandatory reason/evidence, active order reference, and no parallel open change case for the same allotment.
### Calculations
Open-case aging and released-site count.
### Workflow
Draft → submitted → approved/returned/rejected → outcome applied; cancellation after possession retains possession history.
### Search Requirements
Case reference, order/site, allottee, request type, status, effective date.
### Documents
Surrender letter, mutation evidence, cancellation order, and approval notes.
### Reports
Mutation/cancellation/surrender register and released-site summary.
### Notifications
Approval and outcome notification via Module 11.
### Security
Restricted high-impact action; maker-checker; full pre/post status audit.
### Integrations
Internal site availability/status update (Simple).
### Dependencies
F06-005, F06-006, Modules 02, 04, and 11.
### Assumptions
Legal adjudication and court case management remain outside scope.
### Risks
Incorrect release decisions can make a disputed site available prematurely.
### Non Functional Requirements
Immutable history, fine-grained access, reliable outcome audit.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Change-case register and filters | UI | Complex | 8 |
| Mutation/cancellation/surrender request form | UI | Very High | 16 |
| Approval outcome and status history view | UI | Complex | 8 |
| Change validation, approval and status processing | API | Very High | 16 |
| Change case and history persistence | Database | Complex | 6 |
| Site-status reflection | Integration | Simple | 4 |
| High-impact change tests | Testing | Very High | 12 |
| Change-case guide | Documentation | Complex | 4 |
| **Total** | | | **74** |
### Estimation Assumptions
The feature manages administrative case outcomes, not compensation, payment, or court workflows.
