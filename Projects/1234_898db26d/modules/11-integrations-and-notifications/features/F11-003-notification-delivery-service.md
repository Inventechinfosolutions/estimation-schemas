# F11-003 — Notification Delivery Service

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-003 |
| **Feature Name** | Notification Delivery Service |
| **Module** | 11 — Integrations and Notifications |

### Description
Send SMS, email and portal notifications for registration, payment, schedule, hall ticket, credentials, results and certificates.

### Business Objective
Keep candidates informed across the examination lifecycle.

### Actors
System; Candidate

### User Journey
1. System initiates the activity through the relevant portal screen.
2. Business events enqueue notification templates.
3. Candidate receives messages on configured channels.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. System views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Template configuration consumption
- Channel dispatch
- Delivery status logging

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Notification template and channel configuration screen | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Send notification on business event | Complex |
| Query notification delivery status | Medium |

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
SMS and email providers as configured by the department.

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
| Notification template and channel configuration screen | UI | Complex | 12 |
| Send notification on business event | API | Complex | 8 |
| Query notification delivery status | API | Medium | 6 |
| Notification queue and log persistence | DB | Medium | 4 |
| SMS provider | Integration | Easy | 8 |
| Email provider | Integration | Easy | 8 |
| Notification Delivery Service feature tests | Testing | Complex | 8 |
| Notification Delivery Service implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
