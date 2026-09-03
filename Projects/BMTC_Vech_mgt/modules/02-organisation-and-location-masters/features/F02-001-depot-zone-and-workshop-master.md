# F02-001 — Depot, Zone and Workshop Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Depot, Zone and Workshop Master |
| **Module** | 02 — Organisation and Location Masters |

### Description
Administrator maintains BMTC Depots, Zones and Central Workshop as location units used for Post placement, job cards and stock.

### Business Objective
One shared location catalogue.

### Actors
Maker: Master Data Administrator. Checker: Master Data Checker.

### User Journey
1. Who creates: Master Data Administrator.
2. How they create: Location register → New: code, name, type (Depot/Zone/CWS), parent zone if depot, Save draft.
3. How they edit: Draft/Returned editable. Codes not reused.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker location inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Location change history.
8. How the checker / auditor sees history: Same for auditor.

### Functional Capabilities
- Authorised administrator creates and updates the location unit.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Location unit register and search | Medium |
| Location unit create / edit form | Complex |
| Location unit change history | Medium |
| Location unit maker–checker inbox | Medium |
| Location unit approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create location unit | Medium |
| Update location unit | Medium |
| Search location unit register | Medium |
| Read location unit change history | Easy |
| Submit location unit change for checker | Complex |
| Approve or reject location unit change | Complex |

### Inputs
Code, name, type, parent zone, status.

### Outputs
Current location unit record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Code unique.
- Depot requires a zone.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to checker.

### Search Requirements
Search by identifier, name, office, status and effective date.

### Documents
None required unless the administrator attaches a supporting office order.

### Reports
Register export for administrators and auditors.

### Notifications
Checker is notified when a change is submitted. Maker is notified on approve or reject.

### Security
Need-to-know. Only authorised Posts may create, edit or approve. History is read-only for auditors.

### Integrations
Consumed by later modules as the system of record for this master.

### Dependencies
Module 01 access. Downstream modules consume this master; they do not recreate it.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).
- Named screens in the journey are not billed one-for-one; Section 2 uses capability artefacts.

### Risks
Poor unique-identity control on the location unit would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Location unit register and search | UI | Medium | 6 |
| Location unit create / edit form | UI | Complex | 12 |
| Location unit change history | UI | Medium | 6 |
| Location unit maker–checker inbox | UI | Medium | 6 |
| Location unit approval panel | UI | Easy | 4 |
| Create location unit | API | Medium | 6 |
| Update location unit | API | Medium | 6 |
| Search location unit register | API | Medium | 6 |
| Read location unit change history | API | Easy | 4 |
| Submit location unit change for checker | API | Complex | 8 |
| Approve or reject location unit change | API | Complex | 8 |
| Location unit record and change history | DB | Medium | 4 |
| Internal handoff of location unit to consuming modules | Integration | Simple | 4 |
| Depot, Zone and Workshop Master feature tests | Testing | Complex | 8 |
| Depot, Zone and Workshop Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
