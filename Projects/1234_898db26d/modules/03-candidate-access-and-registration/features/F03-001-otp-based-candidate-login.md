# F03-001 — OTP-Based Candidate Login

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | OTP-Based Candidate Login |
| **Module** | 03 — Candidate Access and Registration |

### Description
Candidates access the portal using mobile OTP with expiry, retry limits and session timeout.

### Business Objective
Provide secure candidate access without passwords.

### Actors
Candidate

### User Journey
1. Candidate initiates the activity through the relevant portal screen.
2. Candidate enters mobile number and requests OTP.
3. Candidate may request resend within configured limits.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Mobile number entry
- OTP entry and validation
- Failed attempt tracking

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Candidate mobile entry screen | Easy |
| OTP verification screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Send OTP | Medium |
| Verify OTP and establish session | Complex |

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
SMS channel via Module 11 notification service.

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
| Candidate mobile entry screen | UI | Easy | 4 |
| OTP verification screen | UI | Medium | 6 |
| Send OTP | API | Medium | 6 |
| Verify OTP and establish session | API | Complex | 8 |
| OTP attempt and session persistence | DB | Medium | 4 |
| SMS OTP dispatch channel | Integration | Easy | 8 |
| OTP-Based Candidate Login feature tests | Testing | Complex | 8 |
| OTP-Based Candidate Login implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
