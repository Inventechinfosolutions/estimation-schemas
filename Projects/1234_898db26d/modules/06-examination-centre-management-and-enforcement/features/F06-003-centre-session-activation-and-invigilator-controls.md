# F06-003 — Centre Session Activation and Invigilator Controls

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Centre Session Activation and Invigilator Controls |
| **Module** | 06 — Examination Centre Management and Enforcement |

### Description
Centre or invigilator user verifies candidate, activates examination session and monitors status.

### Business Objective
Operational control at the examination centre.

### Actors
Centre or Invigilator user; Candidate

### User Journey
1. Centre or Invigilator user initiates the activity through the relevant portal screen.
2. Invigilator verifies candidate identity against hall ticket and activates session.
3. Invigilator monitors active and submitted candidates on centre workspace.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Centre or Invigilator user views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Candidate verification
- Session activation
- Live session monitor

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Centre candidate verification screen | Complex |
| Session activation screen | Medium |
| Active session monitor screen | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Verify candidate at centre | Complex |
| Activate examination session | Complex |
| List active sessions for centre | Medium |

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
F06-001; F06-002

### Assumptions
- KGID, payment and notification channels are available in target environments when referenced.

### Risks
Integration or centre-enforcement mechanism changes may affect delivery effort.

### Non Functional Requirements
Availability during examination windows; responsive conduct under concurrent candidates at centres.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Centre candidate verification screen | UI | Complex | 12 |
| Session activation screen | UI | Medium | 6 |
| Active session monitor screen | UI | Complex | 12 |
| Verify candidate at centre | API | Complex | 8 |
| Activate examination session | API | Complex | 8 |
| List active sessions for centre | API | Medium | 6 |
| Centre session state persistence | DB | Medium | 4 |
| Centre Session Activation and Invigilator Controls feature tests | Testing | Complex | 8 |
| Centre Session Activation and Invigilator Controls implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
