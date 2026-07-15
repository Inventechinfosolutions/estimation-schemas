# F07-003 — CA Approval, Order & Agreement
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | CA Approval, Order & Agreement |
| **Module** | 07 — CA Site Management |
### Description
Route a recommended CA proposal for approval and issue the BDA allotment, assignment, or lease order/agreement with approved terms.
### Business Objective
Make CA occupancy effective only after configured authority approval and traceable documentation.
### Actors
CA Officer; configured approvers; institutional representative; Auditor.
### User Journey
Approvers review the proposal, site, terms, and documents; final approval generates the selected order/agreement; officer records execution and the site becomes occupied.
### Functional Capabilities
Approval worklist, term-review screen, order/agreement preview, execution tracker, and approved CA register.
### Inputs
Recommendation, period, conditions, fees/deposits if applicable, approver remarks, template, execution date.
### Outputs
Approval history, order/agreement, executed status, occupied CA site.
### Business Rules
Only recommended available CA cases may be approved; no order before final approval; occupancy starts only after approved/executed outcome as configured.
### Validations
Required approval path, valid period/conditions, active template, and no competing active CA allocation.
### Calculations
Agreement end date from effective date and approved period.
### Workflow
Recommended → approved/returned/rejected → order issued → agreement executed → occupied.
### Search Requirements
Case/order, CA site, institution, approval stage, term end date, execution status.
### Documents
Recommendation, approval note, order/agreement, execution certificate.
### Reports
CA approved-order and unexecuted-agreement registers.
### Notifications
Approval tasks, order issue, and execution reminder via Module 11.
### Security
Maker-checker, CA role scope, immutable approval record.
### Integrations
Internal CA/site status update (Simple).
### Dependencies
F07-002, Module 02 templates/workflow, F07-005, Module 11.
### Assumptions
Fee collection is recorded only if enabled elsewhere; no financial ledger.
### Risks
Unapproved template/term changes can create invalid orders.
### Non Functional Requirements
Reproducible order documents, protected institutional records, complete audit.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| CA approval worklist and timeline | UI | Very High | 16 |
| Terms, order and execution screens | UI | Very High | 16 |
| Approval/order/term processing | API | Very High | 16 |
| Agreement and approval persistence | Database | Complex | 6 |
| CA master status update | Integration | Simple | 4 |
| CA approval tests | Testing | Very High | 12 |
| CA order guide | Documentation | Complex | 4 |
| **Total** | | | **74** |
