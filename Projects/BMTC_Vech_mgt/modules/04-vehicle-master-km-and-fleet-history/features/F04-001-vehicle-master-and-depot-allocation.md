# F04-001 — Vehicle Master and Depot Allocation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Vehicle Master and Depot Allocation |
| **Module** | 04 — Vehicle Master, KM and Fleet History |

### Description
Fleet Administrator maintains vehicle number, type, model, chassis, engine, induction date and depot allocation.

### Business Objective
One vehicle identity for job cards, fuel, tyres and PM.

### Actors
Maker: Fleet Administrator. Checker: Fleet Checker.

### User Journey
1. Who creates: Fleet Administrator.
2. How they create: Vehicle register → New: registration/fleet number, make/model, chassis, engine, induction date, depot, Save draft.
3. How they edit: Draft/Returned editable. Depot change after approval is a transfer event (F04-003), not a silent edit.
4. How they send for approval: Submit to Fleet Checker.
5. How the approver sees pending items: Checker vehicle inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Vehicle master history.
8. How the checker / auditor sees history: Auditor.

### Functional Capabilities
- Authorised administrator creates and updates the vehicle master record.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Vehicle master record register and search | Medium |
| Vehicle master record create / edit form | Complex |
| Vehicle master record change history | Medium |
| Vehicle master record maker–checker inbox | Medium |
| Vehicle master record approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create vehicle master record | Medium |
| Update vehicle master record | Medium |
| Search vehicle master record register | Medium |
| Read vehicle master record change history | Easy |
| Submit vehicle master record change for checker | Complex |
| Approve or reject vehicle master record change | Complex |

### Inputs
Vehicle number, type, model, chassis, engine, induction date, depot.

### Outputs
Current vehicle master record record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Vehicle number unique.
- Depot mandatory.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to Fleet Checker.

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
Poor unique-identity control on the vehicle master record would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Vehicle master record register and search | UI | Medium | 6 |
| Vehicle master record create / edit form | UI | Complex | 12 |
| Vehicle master record change history | UI | Medium | 6 |
| Vehicle master record maker–checker inbox | UI | Medium | 6 |
| Vehicle master record approval panel | UI | Easy | 4 |
| Create vehicle master record | API | Medium | 6 |
| Update vehicle master record | API | Medium | 6 |
| Search vehicle master record register | API | Medium | 6 |
| Read vehicle master record change history | API | Easy | 4 |
| Submit vehicle master record change for checker | API | Complex | 8 |
| Approve or reject vehicle master record change | API | Complex | 8 |
| Vehicle master record record and change history | DB | Medium | 4 |
| Internal handoff of vehicle master record to consuming modules | Integration | Simple | 4 |
| Vehicle Master and Depot Allocation feature tests | Testing | Complex | 8 |
| Vehicle Master and Depot Allocation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
