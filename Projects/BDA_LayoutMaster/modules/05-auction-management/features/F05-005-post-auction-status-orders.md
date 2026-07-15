# F05-005 — Post-Auction Status & Orders
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F05-005 |
| **Feature Name** | Post-Auction Status & Orders |
| **Module** | 05 — Auction Management |
### Description
Confirm auction outcomes, update site status, and generate/store permitted orders and acknowledgements.
### Business Objective
Complete the controlled handoff from auction outcome to downstream formalities.
### Actors
Auction Section; approvers; Revenue/Allotment consumers; Auditor.
### User Journey
Officer confirms a result, selects approved outcome status, generates an order from template, and exposes handover signal to downstream process.
### Functional Capabilities
Outcome confirmation, site-status update, template order generation, acknowledgements, handover signal, audit.
### Inputs
Confirmed result, selected post-auction status, template, remarks.
### Outputs
Updated site/case status, order/acknowledgement, downstream handover indication.
### Business Rules
Only confirmed outcomes update site status; status history is retained; allotment formalities remain Module 06.
### Validations
Confirmed result, allowed status transition, authorised action.
### Calculations
None.
### Workflow
Result → confirmation → status/order → downstream handover where required.
### Search Requirements
Case, site, post-auction status, order date.
### Documents
Orders/acknowledgements are embedded auction documents.
### Reports
Post-auction status report.
### Notifications
Outcome/order alerts where configured.
### Security
RBAC, SoD, audit.
### Integrations
Internal template/site-status consumption (Simple).
### Dependencies
F02-005, F05-004, Module 04, Module 06.
### Assumptions
Full allotment/possession is not included here.
### Risks
Ownership boundary with Module 06 requires confirmation.
### Non Functional Requirements
Consistent status update and audit history.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Post-auction worklist | UI | Complex | 8 |
| Order/status confirmation UI | UI | Complex | 8 |
| Status/order operations | API | Complex | 8 |
| Status/order persistence | Database | Complex | 6 |
| Internal template/site status consumption | Integration | Simple | 4 |
| Post-auction tests | Testing | Very High | 12 |
| Post-auction guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Payment execution is Module 12.
