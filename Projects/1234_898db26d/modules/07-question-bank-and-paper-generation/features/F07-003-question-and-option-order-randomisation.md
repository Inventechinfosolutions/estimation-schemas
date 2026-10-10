# F07-003 — Question and Option Order Randomisation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Question and Option Order Randomisation |
| **Module** | 07 — Question Bank and Paper Generation |

### Description
Randomise question order and answer option order per candidate paper.

### Business Objective
Further reduce collusion risk during CBT.

### Actors
System

### User Journey
1. System initiates the activity through the relevant portal screen.
2. Randomisation rules apply when paper instance is created for the candidate.
3. Administrators configure whether option shuffling applies per examination.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. System views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Randomisation rule flags
- Shuffled delivery to examination interface

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Randomisation settings screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Apply question order randomisation | Complex |
| Apply option order randomisation | Complex |

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
F07-002

### Assumptions
- KGID, payment and notification channels are available in target environments when referenced.

### Risks
Integration or centre-enforcement mechanism changes may affect delivery effort.

### Non Functional Requirements
Availability during examination windows; responsive conduct under concurrent candidates at centres.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Randomisation settings screen | UI | Medium | 6 |
| Apply question order randomisation | API | Complex | 8 |
| Apply option order randomisation | API | Complex | 8 |
| Randomisation metadata on paper instance | DB | Easy | 2 |
| Question and Option Order Randomisation feature tests | Testing | Complex | 8 |
| Question and Option Order Randomisation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
