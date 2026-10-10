# F02-003 — Evaluation Rules and Examination Parameters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Evaluation Rules and Examination Parameters |
| **Module** | 02 — Examination Configuration |

### Description
Configure scoring, negative marking, pass criteria, duration, security options and paper parameters.

### Business Objective
Drive automatic evaluation and secure conduct settings.

### Actors
Examination Administrator

### User Journey
1. Examination Administrator initiates the activity through the relevant portal screen.
2. Administrator sets evaluation rules and examination duration and security parameters per exam.
3. Administrator updates parameters before a scheduled session.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Examination Administrator views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Evaluation rule setup
- Examination conduct parameters
- Version and randomisation flags

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Evaluation rules form | Complex |
| Examination parameters form | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save evaluation configuration | Complex |
| Save conduct and security parameters | Complex |

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
| Evaluation rules form | UI | Complex | 12 |
| Examination parameters form | UI | Complex | 12 |
| Save evaluation configuration | API | Complex | 8 |
| Save conduct and security parameters | API | Complex | 8 |
| Examination configuration persistence | DB | Medium | 4 |
| Evaluation Rules and Examination Parameters feature tests | Testing | Complex | 8 |
| Evaluation Rules and Examination Parameters implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
