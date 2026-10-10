# F01-001 — Internal User Lifecycle

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Internal User Lifecycle |
| **Module** | 01 — User and Role Management |

### Description
Create and maintain staff and centre user accounts used by administration and centre operations.

### Business Objective
Ensure only authorised personnel operate examination administration and centre functions.

### Actors
Examination Administrator; IT support (as configured)

### User Journey
1. Examination Administrator initiates the activity through the relevant portal screen.
2. Administrator opens the user register and creates a user with role assignment.
3. Administrator updates user details, activation status and role mapping until deactivation.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Examination Administrator views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- User register with search
- Create and edit user profile
- Activate and deactivate users

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| User register and search screen | Complex |
| User create and edit form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search and list users | Medium |
| Create and update user | Complex |
| Activate and deactivate user | Easy |

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
| User register and search screen | UI | Complex | 12 |
| User create and edit form | UI | Medium | 6 |
| Search and list users | API | Medium | 6 |
| Create and update user | API | Complex | 8 |
| Activate and deactivate user | API | Easy | 4 |
| User identity and role linkage persistence | DB | Medium | 4 |
| Internal User Lifecycle feature tests | Testing | Complex | 8 |
| Internal User Lifecycle implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
