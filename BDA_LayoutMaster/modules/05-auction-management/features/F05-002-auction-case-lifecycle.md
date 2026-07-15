# F05-002 — Auction Case Lifecycle
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Auction Case Lifecycle |
| **Module** | 05 — Auction Management |
### Description
Create and manage auction cases/batches, schedules, terms, mode, EMD conditions, linked sites, and lifecycle states.
### Business Objective
Provide a controlled operational record for each BDA auction.
### Actors
Auction Section; approvers; Auditor.
### User Journey
Officer creates case, selects approved sites, records schedule/terms, progresses or cancels/postpones it with auditable reasons.
### Functional Capabilities
Case/batch CRUD, multi-site linkage, schedule, mode/terms, EMD conditions, cancellation/postponement/unsuccessful handling, history.
### Inputs
Reference, approved sites, schedule, location/mode, terms, EMD conditions, status.
### Outputs
Auction case and lifecycle history.
### Business Rules
Only Approved for Auction sites may be included; unavailable sites cannot be duplicated in conflicting active cases.
### Validations
Unique reference; eligible sites; valid schedule and status transition.
### Calculations
None.
### Workflow
Draft → scheduled/published → concluded/cancelled/postponed/unsuccessful.
### Search Requirements
Reference, date, status, site, mode.
### Documents
Embedded documents use F05-006.
### Reports
Auction case register.
### Notifications
Configured schedule/status alerts.
### Security
RBAC, scope, audit.
### Integrations
Internal eligibility/notification consumption (Simple).
### Dependencies
F05-001, F05-003–006, Module 11.
### Assumptions
Detailed e-auction mechanics are subject to BDA workshops.
### Risks
Auction-mode ambiguity can expand this scope.
### Non Functional Requirements
Auditable lifecycle; responsive case retrieval.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Case register/search | UI | Complex | 8 |
| Case/batch editor | UI | Very High | 16 |
| Lifecycle operations | API | Very High | 16 |
| Case persistence | Database | Complex | 6 |
| Internal eligibility/notification consumption | Integration | Simple | 4 |
| Lifecycle tests | Testing | Very High | 12 |
| Case guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
### Estimation Assumptions
Public portal UX is Module 10.
