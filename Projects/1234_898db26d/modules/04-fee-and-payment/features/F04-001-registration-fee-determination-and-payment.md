# F04-001 — Registration Fee Determination and Payment

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Registration Fee Determination and Payment |
| **Module** | 04 — Fee and Payment |

### Description
Present applicable fee, initiate payment for paid registrations and confirm successful payment before registration completion.

### Business Objective
Collect fees per category and attempt rules.

### Actors
Candidate

### User Journey
1. Candidate initiates the activity through the relevant portal screen.
2. System displays applicable fee after eligibility check; candidate proceeds to payment when due.
3. Payment gateway callback updates registration payment status.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Candidate views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Fee summary
- Payment initiation and return handling

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Registration fee summary screen | Medium |
| Payment status and receipt screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Calculate registration fee | Complex |
| Initiate payment and record outcome | Complex |

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
Payment gateway via Module 11.

### Dependencies
F02-002; F11-002

### Assumptions
- KGID, payment and notification channels are available in target environments when referenced.

### Risks
Integration or centre-enforcement mechanism changes may affect delivery effort.

### Non Functional Requirements
Availability during examination windows; responsive conduct under concurrent candidates at centres.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Registration fee summary screen | UI | Medium | 6 |
| Payment status and receipt screen | UI | Medium | 6 |
| Calculate registration fee | API | Complex | 8 |
| Initiate payment and record outcome | API | Complex | 8 |
| Fee transaction persistence | DB | Medium | 4 |
| Payment gateway integration | Integration | Very High | 40 |
| Registration Fee Determination and Payment feature tests | Testing | Complex | 8 |
| Registration Fee Determination and Payment implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **83** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
