# F07-002 — Random Paper Generation and Versions

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Random Paper Generation and Versions |
| **Module** | 07 — Question Bank and Paper Generation |

### Description
Generate examination papers with random question selection and multiple versions such as A/B/C/D.

### Business Objective
Reduce predictability and support parallel sessions.

### Actors
Examination Administrator; System

### User Journey
1. Examination Administrator initiates the activity through the relevant portal screen.
2. Administrator configures paper blueprint linked to examination.
3. System generates candidate-specific paper at session start.
4. No separate approval workflow applies; the action completes on successful validation.
5. There is no approver inbox for this feature.
6. There is no approver decision step.
7. Examination Administrator views outcomes and history from their login.
8. Administrators and auditors review activity through audit and operational registers.

### Functional Capabilities
- Paper blueprint configuration
- Runtime paper generation

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Paper blueprint configuration screen | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save paper blueprint | Complex |
| Generate candidate paper instance | Very High |

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
| Paper blueprint configuration screen | UI | Complex | 12 |
| Save paper blueprint | API | Complex | 8 |
| Generate candidate paper instance | API | Very High | 16 |
| Paper blueprint and instance persistence | DB | Complex | 6 |
| Random Paper Generation and Versions feature tests | Testing | Very High | 12 |
| Random Paper Generation and Versions implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
