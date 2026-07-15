# F06-001 — Allotment Schemes, Eligibility & Pools
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Allotment Schemes, Eligibility & Pools |
| **Module** | 06 — Allotment Management |
### Description
Create BDA allotment schemes, define the eligible site pool, and publish a controlled notification for applications.
### Business Objective
Make only approved, available sites eligible for a defined allotment exercise.
### Actors
Revenue/Allotment Section User; Zonal Officer; configured approvers; Citizen (published notification).
### User Journey
Officer creates a scheme, selects eligible sites from the approved site register, records category and application window, submits it for approval, and publishes the approved notice; the system then opens the pool for applications.
### Functional Capabilities
- Scheme register, create/edit screen, eligible-site selection grid, approval timeline, and published-notice preview.
- Define category, application dates, selection method, eligibility parameters, and available site pool.
### Inputs
Scheme reference, category, eligible-site selection, dates, configured eligibility rules, notice template, and approval remarks.
### Outputs
Approved scheme, locked available-site pool, published notification, and scheme register export.
### Business Rules
Only active sites meeting BDA-configured status/classification rules enter a pool; a site cannot be in concurrent active allotment pools; publication follows approval.
### Validations
Application close date follows open date; selected sites are unique, active, and available; required eligibility and notice fields are present.
### Calculations
Available pool count by site category and scheme.
### Workflow
Draft → submitted → approved/returned/rejected → published → closed; configured maker and approver cannot be the same user where segregation is enabled.
### Search Requirements
Scheme reference, category, zone, status, application window, and site number.
### Documents
Scheme notification, approval note, and supporting Government Order where applicable.
### Reports
Scheme register and pool availability export.
### Notifications
Approval worklist alert; published scheme notice through Module 11.
### Security
Allotment-role and zone scope; approval history and publication audit.
### Integrations
Citizen portal publication feed (Simple).
### Dependencies
Modules 01–04, Module 02 eligibility/workflow/notice masters, Modules 10–11.
### Assumptions
BDA supplies final scheme categories and eligibility parameters.
### Risks
Late rule changes can alter the eligible pool after applications begin.
### Non Functional Requirements
Responsive register, auditable publication, and reliable filtering.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Scheme register and filters | UI | Complex | 8 |
| Scheme setup and eligible-site pool screen | UI | Very High | 16 |
| Scheme approval and publication timeline | UI | Complex | 8 |
| Scheme, pool, eligibility and status processing | API | Very High | 16 |
| Scheme and pool persistence | Database | Complex | 6 |
| Portal publication feed | Integration | Simple | 4 |
| Scheme lifecycle tests | Testing | Very High | 12 |
| Scheme operations guide | Documentation | Medium | 3 |
| **Total** | | | **73** |
### Estimation Assumptions
Eligibility rule configuration is consumed from Module 02; this feature applies it to a scheme and pool.
