# F03-001 — Vehicle and Transporter Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Vehicle and Transporter Master |
| **Module** | 03 — Vehicle and GPS Device Onboarding |

### Description
Fleet Administrator maintains transport vehicles and contractor/transporter details including load capacity, permit and fitness validity.

### Business Objective
Authenticated vehicle records for commodity transportation.

### Actors
Maker: Fleet Administrator. Checker: Fleet Checker.

### User Journey
1. Who creates: Fleet Administrator.
2. How they create: Vehicle register → New: registration number, transporter, capacity, permit/fitness dates, Save draft.
3. How they edit: Draft/Returned editable. Duplicate registration refused.
4. How they send for approval: Submit to Fleet Checker.
5. How the approver sees pending items: Checker vehicle inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Vehicle change history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- Vehicle master
- Transporter details
- Permit/fitness tracking
- Duplicate validation

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Vehicle register | Medium |
| Vehicle/transporter form | Complex |
| Vehicle history | Medium |
| Vehicle checker inbox | Medium |
| Vehicle approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create vehicle | Medium |
| Update vehicle | Medium |
| Search vehicle | Medium |
| Read history | Easy |
| Submit vehicle | Complex |
| Approve vehicle | Complex |
| Validate duplicate registration | Medium |

### Inputs
Registration, transporter, capacity, permit, fitness, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Duplicate vehicle refused.
- Expired permit flagged.

### Validations
- Registration unique.
- Transporter mandatory.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Optional RC/permit scan (embedded).

### Reports
Vehicle-wise monitoring list.

### Notifications
Checker/maker.

### Security
Fleet Posts.

### Integrations
None.

### Dependencies
Module 01.

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
| Vehicle register | UI | Medium | 6 |
| Vehicle/transporter form | UI | Complex | 12 |
| Vehicle history | UI | Medium | 6 |
| Vehicle checker inbox | UI | Medium | 6 |
| Vehicle approval | UI | Easy | 4 |
| Create vehicle | API | Medium | 6 |
| Update vehicle | API | Medium | 6 |
| Search vehicle | API | Medium | 6 |
| Read history | API | Easy | 4 |
| Submit vehicle | API | Complex | 8 |
| Approve vehicle | API | Complex | 8 |
| Validate duplicate registration | API | Medium | 6 |
| Vehicle and transporter records | DB | Complex | 6 |
| Vehicle and Transporter Master feature tests | Testing | Complex | 8 |
| Vehicle and Transporter Master implementation documentation | Documentation | Medium | 3 |

**Feature total: 95 hours**
