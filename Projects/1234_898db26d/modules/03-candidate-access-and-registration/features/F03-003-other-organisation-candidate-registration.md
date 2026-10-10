# F03-003 — Other Organisation Candidate Registration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Other Organisation Candidate Registration |
| **Module** | 03 — Candidate Access and Registration |

### Description
Manual capture of candidate and employment details for PSU, Board, Corporation, Society and other eligible organisations.

### Business Objective
Support non-government candidate registration with configurable fields.

### Actors
Candidate

### User Journey
1. Non-government candidate initiates the activity through the relevant portal screen.
2. Candidate selects organisation category and completes profile and employment details.
3. Candidate may edit draft registration before submission.
4. Submission for verification or approval applies only where the source SOW requires administrator review; otherwise the candidate completes self-service steps without an approver inbox.
5. Where registration verification applies, the Examination Administrator reviews pending registrations from an administrator worklist; otherwise this step does not apply.
6. The approver accepts or returns the registration with remarks when verification is in scope; pure self-service steps have no approver decision.
7. Non-government candidate views status, history and downloadable outputs from their login.
8. Administrators and auditors review the same history through role-scoped registers and audit views.

### Functional Capabilities
- Category selection
- Candidate and employment detail form

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Organisation category selection screen | Easy |
| Other organisation detail form | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save other organisation registration draft | Complex |
| Submit registration for verification | Complex |

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
| Organisation category selection screen | UI | Easy | 4 |
| Other organisation detail form | UI | Complex | 12 |
| Save other organisation registration draft | API | Complex | 8 |
| Submit registration for verification | API | Complex | 8 |
| Other organisation candidate persistence | DB | Medium | 4 |
| Other Organisation Candidate Registration feature tests | Testing | Complex | 8 |
| Other Organisation Candidate Registration implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
