# F10-004 — Audit Trail Inquiry

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-004 |
| **Feature Name** | Audit Trail Inquiry |
| **Module** | 10 — Dashboards Reports and Audit |

### Description
Capture and inquire audit logs for critical activities listed in the SOW.

### Business Objective
Support compliance and forensic review.

### Actors
Examination Administrator; Auditor

### User Journey
1. Auditor initiates the activity through the relevant portal screen.
2. Auditor searches audit log by user, activity and date range.
3. Auditor exports audit extract when permitted.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Auditor views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Audit log search register
- Audit detail view

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Audit trail search register screen | Complex |
| Audit event detail screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search audit events | Medium |
| Fetch audit event detail | Easy |

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
| Audit trail search register screen | UI | Complex | 12 |
| Audit event detail screen | UI | Medium | 6 |
| Search audit events | API | Medium | 6 |
| Fetch audit event detail | API | Easy | 4 |
| Audit log persistence | DB | Medium | 4 |
| Audit Trail Inquiry feature tests | Testing | Complex | 8 |
| Audit Trail Inquiry implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
