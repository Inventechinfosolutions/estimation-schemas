# F04-002 — Site Attributes, Legal & Reservation
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Site Attributes, Legal & Reservation |
| **Module** | 04 — Site Management & Classification |
### Description
Maintain dimensions, area, corner/intermediate, road facing, khata, survey, reservation, legal/litigation, ownership, and possession information.
### Business Objective
Provide complete governed attributes needed for classification and downstream processes.
### Actors
Town Planning; Engineering; Legal; Revenue; Data Entry Operator.
### User Journey
Authorised officer opens a site, records attributes and legal details, attaches references where required, and saves audited updates.
### Functional Capabilities
Attribute maintenance, legal flags/dates/remarks, reservation, ownership/possession status, history.
### Inputs
Dimensions, area, facing, khata, survey, reservation, legal flags/dates, ownership/possession.
### Outputs
Complete site attribute view and audit history.
### Business Rules
Legal information is flags/dates/documents only; full court case management is excluded.
### Validations
Required values, valid master selections, valid dates, non-negative dimensions/area.
### Calculations
Area calculation/display where dimensions are captured.
### Workflow
Direct update or configured controlled change.
### Search Requirements
Survey, reservation, legal flag, possession/ownership status.
### Documents
Legal and supporting files are embedded in F04-003.
### Reports
Site attributes/register export.
### Notifications
Optional legal-status alert.
### Security
Sensitive legal fields restricted by RBAC and audit.
### Integrations
Internal master consumption (Simple).
### Dependencies
F04-001, F02-002, F04-003.
### Assumptions
BDA defines permissible attribute values.
### Risks
Inaccurate legal data can wrongly affect eligibility.
### Non Functional Requirements
Role-based masking; auditability; responsive data entry.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Attribute/legal detail tabs | UI | Very High | 16 |
| Legal/reservation review view | UI | Complex | 8 |
| Attribute validation operations | API | Complex | 8 |
| Attribute persistence | Database | Complex | 6 |
| Internal master consumption | Integration | Simple | 4 |
| Attribute/legal tests | Testing | Very High | 12 |
| Attribute guide | Documentation | Medium | 3 |
| **Total** | | | **57** |
### Estimation Assumptions
No external court-system integration is included.
