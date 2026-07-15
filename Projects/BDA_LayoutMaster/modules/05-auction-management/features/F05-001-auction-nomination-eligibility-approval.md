# F05-001 — Auction Nomination, Eligibility & Approval
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Auction Nomination, Eligibility & Approval |
| **Module** | 05 — Auction Management |
### Description
Nominate only classification-approved eligible sites and obtain approval before marking Approved for Auction.
### Business Objective
Protect auction integrity by consuming only approved sites.
### Actors
Auction Section; department approvers; Auditor.
### User Journey
Officer selects an eligible site, proposes nomination, attaches evidence, submits, and reviews approval outcome.
### Functional Capabilities
Eligible-site lookup, nomination, approval worklist/actions, history, and Approved for Auction status.
### Inputs
Eligible site, nomination details, remarks, embedded documents.
### Outputs
Approved/rejected nomination and auction-ready status.
### Business Rules
Sites without approved Auction/equivalent classification cannot be nominated or scheduled.
### Validations
Eligibility, available site status, authorised action, required remarks.
### Calculations
None.
### Workflow
Propose → configured approval → Approved for Auction/rejected.
### Search Requirements
Site, nomination status, approval stage, date.
### Documents
Embedded nomination/approval documents.
### Reports
Auction nomination register.
### Notifications
Workflow alerts via Module 11.
### Security
RBAC, SoD, audit.
### Integrations
Internal eligibility/workflow consumption (Simple).
### Dependencies
Modules 01–04, F02-006, Module 11.
### Assumptions
Classification approval is completed in Module 04.
### Risks
Eligibility disputes can delay auction scheduling.
### Non Functional Requirements
Auditable decisions and prompt worklist access.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Eligible-site selection | UI | Complex | 8 |
| Nomination/approval worklist | UI | Very High | 16 |
| Eligibility and approval operations | API | Very High | 16 |
| Nomination/approval persistence | Database | Complex | 6 |
| Internal eligibility/workflow consumption | Integration | Simple | 4 |
| Nomination tests | Testing | Very High | 12 |
| Nomination guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
### Estimation Assumptions
Workflow definition remains Module 02.
