# F03-004 — Competent Authority Document Handling

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Competent Authority Document Handling |
| **Module** | 03 — Candidate Access and Registration |

### Description
Download prescribed competent authority format, upload digitally signed confirmation and associate with registration.

### Business Objective
Evidence employment status for non-government candidates.

### Actors
Candidate; Examination Administrator

### User Journey
1. Non-government candidate initiates the activity through the relevant portal screen.
2. Candidate downloads the prescribed template and uploads the digitally signed document.
3. Administrator may verify or return the document from a verification worklist when required.
4. Submission for verification or approval applies only where the source SOW requires administrator review; otherwise the candidate completes self-service steps without an approver inbox.
5. Where registration verification applies, the Examination Administrator reviews pending registrations from an administrator worklist; otherwise this step does not apply.
6. The approver accepts or returns the registration with remarks when verification is in scope; pure self-service steps have no approver decision.
7. Non-government candidate views status, history and downloadable outputs from their login.
8. Administrators and auditors review the same history through role-scoped registers and audit views.

### Functional Capabilities
- Template download
- Document upload with format and size validation

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Competent authority template download screen | Simple |
| Document upload screen | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Download template | Easy |
| Upload and attach competent authority document | Complex |

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
| Competent authority template download screen | UI | Simple | 2 |
| Document upload screen | UI | Medium | 6 |
| Download template | API | Easy | 4 |
| Upload and attach competent authority document | API | Complex | 8 |
| Registration document metadata persistence | DB | Easy | 2 |
| Competent Authority Document Handling feature tests | Testing | Complex | 8 |
| Competent Authority Document Handling implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **33** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
