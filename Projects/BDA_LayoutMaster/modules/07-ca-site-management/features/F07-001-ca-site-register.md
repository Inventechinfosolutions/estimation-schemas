# F07-001 — CA Site Register
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | CA Site Register |
| **Module** | 07 — CA Site Management |
### Description
Create the CA register from sites that have an approved Civic Amenity classification, recording purpose, permitted use, beneficiary type, and availability.
### Business Objective
Ensure CA processing starts only from BDA-approved CA sites and retains a distinct CA operational view.
### Actors
CA Site Section User; Zonal Officer; Auditor.
### User Journey
Officer searches approved CA-classified sites, adds the site to the CA register, records permitted purpose and beneficiary type, confirms availability, and later views occupancy and linked case history.
### Functional Capabilities
- CA register, eligible-site picker, CA profile screen, availability status view, and export.
### Inputs
Approved site, CA purpose, permitted use, beneficiary type, status, and remarks.
### Outputs
CA site record, availability register, and linked site reference.
### Business Rules
Only classification-approved CA sites enter the register; a site has one current CA register profile; classification withdrawal prevents new CA case intake.
### Validations
Approved CA classification, active site, required purpose/use/status, and duplicate CA-site prevention.
### Calculations
Available, occupied, and inactive CA-site counts by zone/purpose.
### Workflow
Eligible CA site → CA registered → available/occupied/inactive status maintained by lifecycle cases.
### Search Requirements
Site/layout, zone, purpose, beneficiary type, availability, and CA status.
### Documents
CA classification approval and purpose reference documents.
### Reports
CA site register and availability summary.
### Notifications
Optional status-change notification via Module 11.
### Security
CA role/zone scope and read-only audit access.
### Integrations
Internal site-master eligibility check (Simple).
### Dependencies
Modules 01–04; F07-005 for ongoing master reflection.
### Assumptions
CA purpose and beneficiary types are configured masters.
### Risks
Incorrect classification status may admit an ineligible site.
### Non Functional Requirements
Auditable status, responsive filters, and export.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| CA register and filters | UI | Complex | 8 |
| CA profile and eligible-site picker | UI | Complex | 8 |
| CA registration validation | API | Complex | 8 |
| CA profile persistence | Database | Medium | 4 |
| Site eligibility check | Integration | Simple | 4 |
| CA register tests | Testing | Complex | 8 |
| CA register guide | Documentation | Medium | 3 |
| **Total** | | | **43** |
