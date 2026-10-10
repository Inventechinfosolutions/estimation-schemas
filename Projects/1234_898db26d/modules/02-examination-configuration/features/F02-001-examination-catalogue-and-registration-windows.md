# F02-001 — Examination Catalogue and Registration Windows

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Examination Catalogue and Registration Windows |
| **Module** | 02 — Examination Configuration |

### Description
Maintain examinations open for registration with schedules and descriptive details.

### Business Objective
Control which examinations candidates may register for.

### Actors
Examination Administrator

### User Journey
1. Examination Administrator initiates the activity through the relevant portal screen.
2. Administrator creates an examination record and sets registration open and close dates.
3. Administrator updates examination details or closes registration.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Examination Administrator views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Examination register
- Examination definition form
- Registration window control

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination register screen | Complex |
| Examination definition form | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search examinations | Medium |
| Save examination definition | Complex |
| Publish registration window | Medium |

### Inputs
Values captured on the named screens and through integrated channels per the SOW.

### Outputs
Persisted records, status updates, downloadable artefacts and notifications as applicable.

### Business Rules
- Behaviour must align with the Examination Module business rules in the source SOW.

### Validations
- Mandatory fields, eligibility checks and role-scoped access enforced before commit.

### Calculations
As per configured fee, scoring or allocation rules where applicable; otherwise none.

### Workflow
Draft or in-progress → validated → completed (and verified where required).

### Search Requirements
List and filter on registers where a search register is named in UI screens.

### Documents
Upload and download of prescribed templates and evidence where the SOW requires.

### Reports
Operational extracts only where this feature owns a report named in the SOW.

### Notifications
Triggered through Module 11 when the business event requires candidate or staff notification.

### Security
Role-based access, session controls and audit logging for critical actions.

### Integrations
None unless stated in feature integrations row.

### Dependencies
Prior modules as applicable.

### Assumptions
- KGID, payment and notification channels are available in target environments when referenced.

### Risks
Integration or centre-enforcement mechanism changes may affect delivery effort.

### Non Functional Requirements
Availability during examination windows; responsive conduct under concurrent candidates at centres.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Examination register screen | UI | Complex | 12 |
| Examination definition form | UI | Complex | 12 |
| Search examinations | API | Medium | 6 |
| Save examination definition | API | Complex | 8 |
| Publish registration window | API | Medium | 6 |
| Examination master persistence | DB | Medium | 4 |
| Examination Catalogue and Registration Windows feature tests | Testing | Complex | 8 |
| Examination Catalogue and Registration Windows implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **59** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
