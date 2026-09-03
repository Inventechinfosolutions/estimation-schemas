# F02-002 — Stores Location and Section Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Stores Location and Section Master |
| **Module** | 02 — Organisation and Location Masters |

### Description
Administrator maintains Central Stores, Depot Stores, Scrap Store and mechanical sections (Engine, Transmission, Electrical, Tyre, Body).

### Business Objective
Stock and job-card section codes are shared, not typed free-text.

### Actors
Maker: Master Data Administrator. Checker: Master Data Checker.

### User Journey
1. Who creates: Master Data Administrator.
2. How they create: Stores location register → New linked to a Depot/CWS/Central; Section register → New section code.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Change history.
8. How the checker / auditor sees history: Auditor history.

### Functional Capabilities
- Authorised administrator creates and updates the stores location.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Stores location register and search | Medium |
| Stores location create / edit form | Complex |
| Stores location change history | Medium |
| Stores location maker–checker inbox | Medium |
| Stores location approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create stores location | Medium |
| Update stores location | Medium |
| Search stores location register | Medium |
| Read stores location change history | Easy |
| Submit stores location change for checker | Complex |
| Approve or reject stores location change | Complex |

### Inputs
Location code, parent unit, store type; section code and name.

### Outputs
Current stores location record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.

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
Poor unique-identity control on the stores location would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Stores location register and search | UI | Medium | 6 |
| Stores location create / edit form | UI | Complex | 12 |
| Stores location change history | UI | Medium | 6 |
| Stores location maker–checker inbox | UI | Medium | 6 |
| Stores location approval panel | UI | Easy | 4 |
| Create stores location | API | Medium | 6 |
| Update stores location | API | Medium | 6 |
| Search stores location register | API | Medium | 6 |
| Read stores location change history | API | Easy | 4 |
| Submit stores location change for checker | API | Complex | 8 |
| Approve or reject stores location change | API | Complex | 8 |
| Stores location record and change history | DB | Medium | 4 |
| Internal handoff of stores location to consuming modules | Integration | Simple | 4 |
| Stores Location and Section Master feature tests | Testing | Complex | 8 |
| Stores Location and Section Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
