# F02-001 — District, Taluk and Administrative Unit Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | District, Taluk and Administrative Unit Master |
| **Module** | 02 — Organisation and Location Masters |

### Description
Master Data Administrator maintains District and Taluk units used for Post placement and district-wise CCC views.

### Business Objective
One shared administrative geography for CCC scope.

### Actors
Maker: Master Data Administrator. Checker: Master Data Checker.

### User Journey
1. Who creates: Master Data Administrator.
2. How they create: Geography register → New: code, name, type (District/Taluk), parent district if taluk, Save draft.
3. How they edit: Draft/Returned editable. Codes not reused.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker geography inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Change history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- District/Taluk masters
- Hierarchy
- Maker–checker

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Geography register | Medium |
| Geography form | Medium |
| Geography history | Medium |
| Geography checker inbox | Medium |
| Geography approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create geography | Medium |
| Update geography | Medium |
| Search geography | Medium |
| Read history | Easy |
| Submit geography | Complex |
| Approve geography | Complex |

### Inputs
Code, name, type, parent, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Taluk requires parent district.

### Validations
- Code unique.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Geography export.

### Notifications
Checker/maker.

### Security
Master admin Posts.

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
| Geography register | UI | Medium | 6 |
| Geography form | UI | Medium | 6 |
| Geography history | UI | Medium | 6 |
| Geography checker inbox | UI | Medium | 6 |
| Geography approval | UI | Easy | 4 |
| Create geography | API | Medium | 6 |
| Update geography | API | Medium | 6 |
| Search geography | API | Medium | 6 |
| Read history | API | Easy | 4 |
| Submit geography | API | Complex | 8 |
| Approve geography | API | Complex | 8 |
| Geography master and history | DB | Medium | 4 |
| District, Taluk and Administrative Unit Master feature tests | Testing | Complex | 8 |
| District, Taluk and Administrative Unit Master implementation documentation | Documentation | Medium | 3 |

**Feature total: 81 hours**
