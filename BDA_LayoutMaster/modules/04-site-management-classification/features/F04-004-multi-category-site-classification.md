# F04-004 — Multi-Category Site Classification
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Multi-Category Site Classification |
| **Module** | 04 — Site Management & Classification |
### Description
Propose and maintain one or more categories and effective status for a site.
### Business Objective
Make approved site classifications available to eligible BDA processes.
### Actors
Town Planning; Engineering; Legal; Revenue; Auction/CA/Land Acquisition sections.
### User Journey
Officer opens a site, proposes categories and effective details, submits special categories for approval, and reviews the resulting status.
### Functional Capabilities
Multi-category assignment, effective dates/status, proposal history, eligibility indicators, and controlled updates.
### Inputs
Site, category, effective dates, status, remarks, supporting documents.
### Outputs
Classification proposal and effective classification/eligibility status.
### Business Rules
Special/process-driving categories are not effective until F04-005 approval; rejected/returned proposals do not enable consumption.
### Validations
Valid site/category; no duplicate active category; required effective details.
### Calculations
Effective eligibility status from approved category state.
### Workflow
Propose → approval for special categories → effective or rejected/returned.
### Search Requirements
Site, category, effective status, approval status.
### Documents
Uses F04-003 embedded attachments.
### Reports
Classification register.
### Notifications
Workflow alerts where enabled.
### Security
RBAC, data scope, audit, SoD.
### Integrations
Internal workflow/eligibility consumption (Simple).
### Dependencies
F02-002, F02-004, F04-001, F04-005, Modules 05–08.
### Assumptions
BDA confirms process-driving category rules.
### Risks
Misclassification can expose a site to an incorrect process.
### Non Functional Requirements
Auditable effective dates/status; reliable process gating.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Classification register | UI | Complex | 8 |
| Multi-category proposal editor | UI | Very High | 16 |
| Classification/eligibility operations | API | Very High | 16 |
| Classification persistence | Database | Complex | 6 |
| Internal workflow/eligibility consumption | Integration | Simple | 4 |
| Classification tests | Testing | Very High | 12 |
| Classification guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
### Estimation Assumptions
Approval runtime is F04-005.
