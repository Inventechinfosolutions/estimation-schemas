# F01-002 — Post Master and Organisational Placement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Post Master and Organisational Placement |
| **Module** | 01 — Person, Post, Role and Access Governance |

### Description
Administrator maintains Posts placed on State CCC, District, Taluk or Godown units with a supervising Post for approvals.

### Business Objective
Place Roles and Persons on organisational Posts scoped by FCS unit.

### Actors
Maker: Access Administrator. Checker: Access Checker.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Post register → New: post code, designation, unit type/unit, supervising Post, Save draft.
3. How they edit: Placement and supervising Post change with effective dates; history retained.
4. How they send for approval: Submit to Access Checker.
5. How the approver sees pending items: Checker Post inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Post placement history.
8. How the checker/auditor sees history: Same history.

### Functional Capabilities
- Post catalogue with unit placement
- Supervising Post for routing
- Maker–checker

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Post register and search | Medium |
| Post create/edit form | Complex |
| Post change history | Medium |
| Post maker–checker inbox | Medium |
| Post approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Post | Medium |
| Update Post | Medium |
| Search Post register | Medium |
| Read Post history | Easy |
| Submit Post change | Complex |
| Approve or reject Post | Complex |

### Inputs
Post code, designation, unit type, unit, supervising Post, effective from/to.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- A Post cannot supervise itself.
- Data scope follows Post unit unless State CCC Role allows wider view.

### Validations
- Unit mandatory.
- Post code unique.

### Calculations
None.

### Workflow
Draft → Submitted → Approved/Rejected.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Posts by unit.

### Notifications
Checker/maker notifications.

### Security
Administrator Posts only.

### Integrations
None.

### Dependencies
F01-001.

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
| Post register and search | UI | Medium | 6 |
| Post create/edit form | UI | Complex | 12 |
| Post change history | UI | Medium | 6 |
| Post maker–checker inbox | UI | Medium | 6 |
| Post approval panel | UI | Easy | 4 |
| Create Post | API | Medium | 6 |
| Update Post | API | Medium | 6 |
| Search Post register | API | Medium | 6 |
| Read Post history | API | Easy | 4 |
| Submit Post change | API | Complex | 8 |
| Approve or reject Post | API | Complex | 8 |
| Post record and placement history | DB | Medium | 4 |
| Post Master and Organisational Placement feature tests | Testing | Complex | 8 |
| Post Master and Organisational Placement implementation documentation | Documentation | Medium | 3 |

**Feature total: 87 hours**
