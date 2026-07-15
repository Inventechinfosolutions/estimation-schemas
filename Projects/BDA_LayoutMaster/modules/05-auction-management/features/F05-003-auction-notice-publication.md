# F05-003 — Auction Notice Publication
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Auction Notice Publication |
| **Module** | 05 — Auction Management |
### Description
Prepare, approve, publish, withdraw, and retain auction notices for permitted citizen visibility.
### Business Objective
Publish accurate, approved auction information from operational cases.
### Actors
Auction Section; approvers; citizen (view via Module 10).
### User Journey
Officer selects case/template, prepares notice, obtains configured approval, publishes or withdraws it, and retains history.
### Functional Capabilities
Template-based notice preparation, approval, publish/unpublish, portal publication status, audit.
### Inputs
Auction case, template, published fields, dates, approval action.
### Outputs
Published notice, portal availability status, history.
### Business Rules
Only approved content is published; Module 10 owns public presentation; sensitive fields are excluded.
### Validations
Valid case/template/dates; authorised publication; required approval.
### Calculations
None.
### Workflow
Prepare → approval → publish → withdraw/expire.
### Search Requirements
Case, notice status, publish date, template.
### Documents
Notice is embedded with auction documents.
### Reports
Published notice register.
### Notifications
Publication alert via Module 11 where enabled.
### Security
RBAC, approval audit, disclosure controls.
### Integrations
Internal template/portal/notification consumption (Simple).
### Dependencies
F02-005, F02-006, F05-002, Module 10, Module 11.
### Assumptions
Citizen portal displays only BDA-permitted content.
### Risks
Incorrect publication can expose non-public information.
### Non Functional Requirements
Auditable publish state; timely public availability.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Notice register | UI | Complex | 8 |
| Notice preparation/publication UI | UI | Complex | 8 |
| Notice lifecycle operations | API | Complex | 8 |
| Notice persistence | Database | Complex | 6 |
| Internal template/portal consumption | Integration | Simple | 4 |
| Publication tests | Testing | Very High | 12 |
| Notice guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Portal shell is not included.
