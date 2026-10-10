# F08-001 — Examination Credential Issuance and Exam Login

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Examination Credential Issuance and Exam Login |
| **Module** | 08 — Computer-Based Examination Conduct |

### Description
Generate system examination credentials and authenticate candidate for the assigned session.

### Business Objective
Separate portal login from secure examination login.

### Actors
Candidate; System

### User Journey
1. Candidate initiates the activity through the relevant portal screen.
2. Credentials are issued after scheduling; candidate uses them at centre for examination login.
3. Credential invalid after submission or expiry.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Credential generation
- Examination login screen

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination credential display for candidate | Easy |
| Examination login screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Generate examination credentials | Complex |
| Authenticate examination login | Complex |

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
F06-003; F05-003

### Assumptions
- KGID, payment and notification channels are available in target environments when referenced.

### Risks
Integration or centre-enforcement mechanism changes may affect delivery effort.

### Non Functional Requirements
Availability during examination windows; responsive conduct under concurrent candidates at centres.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Examination credential display for candidate | UI | Easy | 4 |
| Examination login screen | UI | Medium | 6 |
| Generate examination credentials | API | Complex | 8 |
| Authenticate examination login | API | Complex | 8 |
| Examination credential persistence | DB | Medium | 4 |
| Examination Credential Issuance and Exam Login feature tests | Testing | Complex | 8 |
| Examination Credential Issuance and Exam Login implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
