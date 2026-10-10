# F10-002 — Examination Centre Dashboard

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-002 |
| **Feature Name** | Examination Centre Dashboard |
| **Module** | 10 — Dashboards Reports and Audit |

### Description
Centre-specific view of today's examinations, attendance and session status.

### Business Objective
Support invigilator and centre management.

### Actors
Centre or Invigilator user

### User Journey
1. Centre user initiates the activity through the relevant portal screen.
2. Centre user opens dashboard scoped to their centre only.
3. Metrics refresh for active sessions.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Centre user views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Centre-scoped metrics
- Attendance and completion counts

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination centre dashboard screen | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Load centre dashboard metrics | Complex |

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
| Examination centre dashboard screen | UI | Very High | 16 |
| Load centre dashboard metrics | API | Complex | 8 |
| Centre-scoped aggregates | DB | Medium | 4 |
| Examination Centre Dashboard feature tests | Testing | Complex | 8 |
| Examination Centre Dashboard implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
