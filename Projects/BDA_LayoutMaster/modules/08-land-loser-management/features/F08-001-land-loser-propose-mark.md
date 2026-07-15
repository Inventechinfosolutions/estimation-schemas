# F08-001 — Land Loser Propose & Mark
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Land Loser Propose & Mark |
| **Module** | 08 — Land Loser Management |
### Description
Create a proposed Land Loser case for a site, capturing BDA acquisition and beneficiary references before verification.
### Business Objective
Replace informal Land Loser markings with a documented, non-effective proposal.
### Actors
Land Acquisition Section User; Data Entry Operator; Legal User; Auditor.
### User Journey
Officer searches the site, selects Land Loser proposal, records acquisition reference, beneficiary linkage and remarks, attaches acquisition papers/GO/entitlement evidence, and submits the case for verification.
### Functional Capabilities
Proposal register, site selector, acquisition/beneficiary form, document checklist, and submission history.
### Inputs
Site, acquisition reference, beneficiary fields defined by BDA, remarks, and mandatory evidence.
### Outputs
Land Loser proposal reference and verification-ready case.
### Business Rules
A proposed marking is not effective on the site master; a site cannot have duplicate active Land Loser proposals.
### Validations
Active site, mandatory BDA-configured reference fields, document checklist, and duplicate proposal check.
### Calculations
Proposal count and pending age by zone/section.
### Workflow
Draft → submitted → department verification in F08-002.
### Search Requirements
Proposal, site/layout, acquisition reference, beneficiary, proposer, status.
### Documents
Acquisition paper, Government Order, entitlement/identity proof, and remarks evidence.
### Reports
Land Loser proposal register.
### Notifications
Verification assignment alert via Module 11.
### Security
Land Acquisition scope; beneficiary evidence restricted; audit.
### Integrations
Internal site lookup (Simple).
### Dependencies
Modules 01–04, Module 02 document/workflow configuration, F08-002.
### Assumptions
BDA defines beneficiary linkage fields and required evidence.
### Risks
Inconsistent acquisition references can create duplicate or false claims.
### Non Functional Requirements
Secure document access, timestamped proposal history, responsive search.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Proposal register and filters | UI | Complex | 8 |
| Land Loser proposal/evidence form | UI | Complex | 8 |
| Proposal validation and submission | API | Complex | 8 |
| Proposal/reference persistence | Database | Complex | 6 |
| Site lookup | Integration | Simple | 4 |
| Proposal tests | Testing | Complex | 8 |
| Proposal guide | Documentation | Medium | 3 |
| **Total** | | | **45** |
