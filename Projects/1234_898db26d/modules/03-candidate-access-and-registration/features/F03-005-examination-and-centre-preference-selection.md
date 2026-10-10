# F03-005 — Examination and Centre Preference Selection

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-005 |
| **Feature Name** | Examination and Centre Preference Selection |
| **Module** | 03 — Candidate Access and Registration |

### Description
Select examination and two preferred examination centres during registration.

### Business Objective
Capture preferences for downstream centre allocation.

### Actors
Candidate

### User Journey
1. Candidate initiates the activity through the relevant portal screen.
2. Candidate selects an open examination from the catalogue.
3. Candidate selects centre preference one and two from configured centres.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Open examination picker
- Centre preference selection

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination selection screen | Medium |
| Centre preference selection screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| List open examinations for candidate | Medium |
| Save examination and centre preferences | Medium |

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
F02-001; F04-001

### Assumptions
- KGID, payment and notification channels are available in target environments when referenced.

### Risks
Integration or centre-enforcement mechanism changes may affect delivery effort.

### Non Functional Requirements
Availability during examination windows; responsive conduct under concurrent candidates at centres.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Examination selection screen | UI | Medium | 6 |
| Centre preference selection screen | UI | Medium | 6 |
| List open examinations for candidate | API | Medium | 6 |
| Save examination and centre preferences | API | Medium | 6 |
| Registration examination and preference persistence | DB | Easy | 2 |
| Examination and Centre Preference Selection feature tests | Testing | Complex | 8 |
| Examination and Centre Preference Selection implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
