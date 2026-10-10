# F06-002 — Authorised Centre Access Enforcement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Authorised Centre Access Enforcement |
| **Module** | 06 — Examination Centre Management and Enforcement |

### Description
Validate candidate, centre, device or network and session before examination access is granted.

### Business Objective
Prevent examination attempt outside allotted authorised centre.

### Actors
Candidate; System

### User Journey
1. Candidate at allotted centre initiates the activity through the relevant portal screen.
2. Candidate attempts examination login; system validates centre, schedule and authorisation rules.
3. Access denied with reason when validation fails.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate at allotted centre views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Pre-exam access validation
- Denial messaging

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination access denied screen | Simple |
| Centre validation status screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Validate authorised centre and session context | Very High |
| Record access denial event | Medium |

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
| Examination access denied screen | UI | Simple | 2 |
| Centre validation status screen | UI | Medium | 6 |
| Validate authorised centre and session context | API | Very High | 16 |
| Record access denial event | API | Medium | 6 |
| Centre access validation log persistence | DB | Medium | 4 |
| Authorised Centre Access Enforcement feature tests | Testing | Very High | 12 |
| Authorised Centre Access Enforcement implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
