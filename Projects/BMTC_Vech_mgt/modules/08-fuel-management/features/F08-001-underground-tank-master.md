# F08-001 — Underground Tank Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Underground Tank Master |
| **Module** | 08 — Fuel Management |

### Description
Depot fuel administrator maintains UGT details and capacity per depot.

### Business Objective
FR-M-33.

### Actors
Maker: Fuel Administrator at depot. Checker: Depot Manager / Fuel Checker.

### User Journey
1. Who creates: Fuel Administrator at depot.
2. How they create: UGT register → New: depot, tank ID, capacity, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker UGT inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: UGT history.
8. How the checker / auditor sees history: Auditor.

### Functional Capabilities
- Authorised administrator creates and updates the UGT master.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Ugt master register and search | Medium |
| Ugt master create / edit form | Complex |
| Ugt master change history | Medium |
| Ugt master maker–checker inbox | Medium |
| Ugt master approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create UGT master | Medium |
| Update UGT master | Medium |
| Search UGT master register | Medium |
| Read UGT master change history | Easy |
| Submit UGT master change for checker | Complex |
| Approve or reject UGT master change | Complex |

### Inputs
Depot, tank ID, capacity, status.

### Outputs
Current UGT master record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Capacity > 0.
- Tank ID unique per depot.

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
Poor unique-identity control on the UGT master would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Ugt master register and search | UI | Medium | 6 |
| Ugt master create / edit form | UI | Complex | 12 |
| Ugt master change history | UI | Medium | 6 |
| Ugt master maker–checker inbox | UI | Medium | 6 |
| Ugt master approval panel | UI | Easy | 4 |
| Create UGT master | API | Medium | 6 |
| Update UGT master | API | Medium | 6 |
| Search UGT master register | API | Medium | 6 |
| Read UGT master change history | API | Easy | 4 |
| Submit UGT master change for checker | API | Complex | 8 |
| Approve or reject UGT master change | API | Complex | 8 |
| Ugt master record and change history | DB | Medium | 4 |
| Internal handoff of UGT master to consuming modules | Integration | Simple | 4 |
| Underground Tank Master feature tests | Testing | Complex | 8 |
| Underground Tank Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
