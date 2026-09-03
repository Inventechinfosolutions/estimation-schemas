# F01-001 — Person Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Person Master |
| **Module** | 01 — Person, Post, Role and Access Governance |

### Description
Access Administrator maintains each FCS official as a unique Person. CCC actions are attributed to this Person, not a shared login.

### Business Objective
Attribute every privileged CCC action to one named Person.

### Actors
Maker: Access Administrator. Checker: Access Checker. Auditor: read history.

### User Journey
1. Who creates: Access Administrator Post.
2. How they create: Person register → New: legal name, unique ID, official mobile/email, Save draft.
3. How they edit: Draft/Returned editable. Unique ID not reused. Deactivation does not delete.
4. How they send for approval: Submit to Access Checker. Person not usable for Post mapping until approved.
5. How the approver sees pending items: Checker Person approval inbox.
6. How the approver decides: Approve or reject with remarks.
7. How the applicant sees history: Person change history.
8. How the approver/auditor sees history: Same history for checker and auditor.

### Functional Capabilities
- Create/update Person
- Maker–checker on Person
- Searchable register and history

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Person register and search | Medium |
| Person create/edit form | Complex |
| Person change history | Medium |
| Person maker–checker inbox | Medium |
| Person approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Person | Medium |
| Update Person | Medium |
| Search Person register | Medium |
| Read Person change history | Easy |
| Submit Person for checker | Complex |
| Approve or reject Person | Complex |

### Inputs
Legal name, unique ID, official mobile, official email, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- One Person per official.
- 2FA targets official mobile/email only.

### Validations
- Unique ID mandatory and unique.
- Official mobile mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → Approved/Rejected.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Person register export.

### Notifications
Checker on submit; maker on decision.

### Security
Need-to-know administrator Posts only.

### Integrations
None external.

### Dependencies
None.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Person register and search | UI | Medium | 6 |
| Person create/edit form | UI | Complex | 12 |
| Person change history | UI | Medium | 6 |
| Person maker–checker inbox | UI | Medium | 6 |
| Person approval panel | UI | Easy | 4 |
| Create Person | API | Medium | 6 |
| Update Person | API | Medium | 6 |
| Search Person register | API | Medium | 6 |
| Read Person change history | API | Easy | 4 |
| Submit Person for checker | API | Complex | 8 |
| Approve or reject Person | API | Complex | 8 |
| Person record and change history | DB | Medium | 4 |
| Person Master feature tests | Testing | Complex | 8 |
| Person Master implementation documentation | Documentation | Medium | 3 |

**Feature total: 87 hours**
