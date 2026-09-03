# F02-002 — Wholesale Godown and FPS Location Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Wholesale Godown and FPS Location Master |
| **Module** | 02 — Organisation and Location Masters |

### Description
Administrator maintains Wholesale Godown and Fair Price Shop locations with coordinates used for geo-fence, RFID/ANPR sites and GIS.

### Business Objective
Authoritative locations for route ends, geo-fences and surveillance sites.

### Actors
Maker: Master Data Administrator. Checker: Master Data Checker.

### User Journey
1. Who creates: Master Data Administrator.
2. How they create: Location register → New: type (Godown/FPS), code, name, district/taluk, coordinates, Save draft.
3. How they edit: Draft/Returned editable. Coordinate change after approval is a new version.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker location inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Location change history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- Godown/FPS catalogue
- Coordinates for GIS/geo-fence
- Maker–checker

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Location register | Medium |
| Location form with map pin | Very High |
| Location history | Medium |
| Location checker inbox | Medium |
| Location approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create location | Medium |
| Update location | Medium |
| Search location | Medium |
| Read history | Easy |
| Submit location | Complex |
| Approve location | Complex |

### Inputs
Type, code, name, district/taluk, lat/long, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Coordinates mandatory for geo-fence use.

### Validations
- Code unique per type.
- District mandatory.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Location register.

### Notifications
Checker/maker.

### Security
Master admin Posts.

### Integrations
None.

### Dependencies
F02-001.

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
| Location register | UI | Medium | 6 |
| Location form with map pin | UI | Very High | 16 |
| Location history | UI | Medium | 6 |
| Location checker inbox | UI | Medium | 6 |
| Location approval | UI | Easy | 4 |
| Create location | API | Medium | 6 |
| Update location | API | Medium | 6 |
| Search location | API | Medium | 6 |
| Read history | API | Easy | 4 |
| Submit location | API | Complex | 8 |
| Approve location | API | Complex | 8 |
| Location master and history | DB | Complex | 6 |
| Wholesale Godown and FPS Location Master feature tests | Testing | Very High | 12 |
| Wholesale Godown and FPS Location Master implementation documentation | Documentation | Medium | 3 |

**Feature total: 97 hours**
