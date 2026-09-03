# F01-003 — Post-to-Person Mapping with Effective Dates

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Post-to-Person Mapping with Effective Dates |
| **Module** | 01 — Person, Post, Role and Access Governance |

### Description
Administrator maps a Person to a Post with effective dates; Checker approves before login under that Post.

### Business Objective
A Person acts only in currently mapped Posts.

### Actors
Applicant: Access Administrator. Approver: Access Checker. Other: mapped Person; Auditor.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Mapping register → New: Person, Post, effective from/to, reason, Save draft.
3. How they edit: Draft/Returned editable. Approved mapping ended by effective-to or new mapping.
4. How they send for approval: Submit. Checker must approve before Person can select that Post at login.
5. How the approver sees pending items: Checker mapping inbox by unit.
6. How the approver decides: Approve or reject.
7. How the applicant sees history: History by Person and by Post.
8. How the approver sees history: Same for checker/auditor.

### Functional Capabilities
- Map Person to Post
- Overlap refusal
- History by Person/Post

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My mapping register | Medium |
| Mapping form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver mapping inbox | Complex |
| Mapping decision panel | Medium |
| My mapping history | Medium |
| Team mapping history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft mapping | Medium |
| Update draft mapping | Medium |
| Submit mapping | Complex |
| Withdraw mapping | Easy |
| Approver inbox query | Medium |
| Approve/reject/return mapping | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Check mapping overlap | Medium |

### Inputs
Person, Post, effective from/to, reason.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Applicant cannot approve own mapping.
- Overlap on same Post refused.

### Validations
- Person and Post mandatory.
- Submit blocked if no supervising Post.

### Calculations
Effective-date overlap check.

### Workflow
Draft → Submitted → Approved/Rejected/Returned.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Optional office order.

### Reports
Current holders by unit.

### Notifications
On submit and decision.

### Security
Only resolved checker Post may decide.

### Integrations
None.

### Dependencies
F01-001, F01-002.

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
| My mapping register | UI | Medium | 6 |
| Mapping form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver mapping inbox | UI | Complex | 12 |
| Mapping decision panel | UI | Medium | 6 |
| My mapping history | UI | Medium | 6 |
| Team mapping history | UI | Medium | 6 |
| Save draft mapping | API | Medium | 6 |
| Update draft mapping | API | Medium | 6 |
| Submit mapping | API | Complex | 8 |
| Withdraw mapping | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve/reject/return mapping | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Check mapping overlap | API | Medium | 6 |
| Mapping record and status history | DB | Medium | 4 |
| Post-to-Person Mapping with Effective Dates feature tests | Testing | Complex | 8 |
| Post-to-Person Mapping with Effective Dates implementation documentation | Documentation | Medium | 3 |

**Feature total: 121 hours**
