# F09-002 — Certificate Generation with QR Code

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Certificate Generation with QR Code |
| **Module** | 09 — Results Certificates and Verification |

### Description
Generate downloadable certificates for eligible candidates embedding unique QR verification reference.

### Business Objective
Provide tamper-evident credential to successful candidates.

### Actors
Candidate; Examination Administrator

### User Journey
1. Candidate initiates the activity through the relevant portal screen.
2. Certificate becomes available after pass criteria met; candidate downloads PDF.
3. Administrator may revoke or cancel certificate when policy requires.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Certificate template rendering
- QR embedding

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Certificate download screen | Medium |
| Certificate administration register | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Generate certificate with QR reference | Complex |
| Download certificate | Medium |

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
| Certificate download screen | UI | Medium | 6 |
| Certificate administration register | UI | Complex | 12 |
| Generate certificate with QR reference | API | Complex | 8 |
| Download certificate | API | Medium | 6 |
| Certificate issuance persistence | DB | Medium | 4 |
| Certificate Generation with QR Code feature tests | Testing | Complex | 8 |
| Certificate Generation with QR Code implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
