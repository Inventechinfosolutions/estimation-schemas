# F08-003 — Examination Security Activity and Submission

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Examination Security Activity and Submission |
| **Module** | 08 — Computer-Based Examination Conduct |

### Description
Record examination activity, apply security controls and process manual or automatic submission.

### Business Objective
Support audit, monitoring and integrity of conduct.

### Actors
Candidate; Examination Administrator

### User Journey
1. Candidate initiates the activity through the relevant portal screen.
2. Candidate submits examination or system auto-submits.
3. Administrator monitors security events on operational views.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Activity event capture
- Manual submit
- Security event register

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Submit examination confirmation screen | Simple |
| Security event monitor screen | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Record examination activity event | Medium |
| Finalize submission | Complex |

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
| Submit examination confirmation screen | UI | Simple | 2 |
| Security event monitor screen | UI | Complex | 12 |
| Record examination activity event | API | Medium | 6 |
| Finalize submission | API | Complex | 8 |
| Examination activity log persistence | DB | Medium | 4 |
| Examination Security Activity and Submission feature tests | Testing | Complex | 8 |
| Examination Security Activity and Submission implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
