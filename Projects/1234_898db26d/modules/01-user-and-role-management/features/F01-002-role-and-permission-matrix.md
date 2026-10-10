# F01-002 — Role and Permission Matrix

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Role and Permission Matrix |
| **Module** | 01 — User and Role Management |

### Description
Define roles for Examination Administrator, Centre or Invigilator user and map functional permissions.

### Business Objective
Enforce segregation between candidate, centre and administrator capabilities.

### Actors
Examination Administrator

### User Journey
1. Examination Administrator initiates the activity through the relevant portal screen.
2. Administrator opens the role matrix and defines permissions per examination function.
3. Administrator adjusts permissions when policy changes.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Examination Administrator views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Role catalogue
- Permission matrix by function
- Assign roles to users

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Role permission matrix screen | Complex |
| Role assignment screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| List roles and permissions | Medium |
| Update role permissions | Complex |
| Resolve effective permissions for session | Medium |

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
| Role permission matrix screen | UI | Complex | 12 |
| Role assignment screen | UI | Medium | 6 |
| List roles and permissions | API | Medium | 6 |
| Update role permissions | API | Complex | 8 |
| Resolve effective permissions for session | API | Medium | 6 |
| Role and permission persistence | DB | Easy | 2 |
| Role and Permission Matrix feature tests | Testing | Complex | 8 |
| Role and Permission Matrix implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
