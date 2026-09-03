# F03-001 — BMTC Item ID and OEM Linkage

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | BMTC Item ID and OEM Linkage |
| **Module** | 03 — Item Master and Catalogue |

### Description
Stores Administrator creates a unique BMTC Item ID and links OEM part numbers. The item is shared across all locations with no duplicate IDs.

### Business Objective
One item identity for stock, job card and purchase.

### Actors
Maker: Stores Master Administrator. Checker: Stores Checker.

### User Journey
1. Who creates: Stores Master Administrator.
2. How they create: Item register → New: nomenclature, BMTC Item ID, OEM numbers, UOM, Save draft.
3. How they edit: Draft/Returned editable. Approved ID is not recycled.
4. How they send for approval: Submit to Stores Checker.
5. How the approver sees pending items: Checker item inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Item change history.
8. How the checker / auditor sees history: Auditor history.

### Functional Capabilities
- Authorised administrator creates and updates the item master record.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Item master record register and search | Medium |
| Item master record create / edit form | Complex |
| Item master record change history | Medium |
| Item master record maker–checker inbox | Medium |
| Item master record approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create item master record | Medium |
| Update item master record | Medium |
| Search item master record register | Medium |
| Read item master record change history | Easy |
| Submit item master record change for checker | Complex |
| Approve or reject item master record change | Complex |

### Inputs
BMTC Item ID, nomenclature, OEM part numbers, UOM, status.

### Outputs
Current item master record record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- BMTC Item ID unique.
- Nomenclature mandatory.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to Stores Checker.

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
Poor unique-identity control on the item master record would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Item master record register and search | UI | Medium | 6 |
| Item master record create / edit form | UI | Complex | 12 |
| Item master record change history | UI | Medium | 6 |
| Item master record maker–checker inbox | UI | Medium | 6 |
| Item master record approval panel | UI | Easy | 4 |
| Create item master record | API | Medium | 6 |
| Update item master record | API | Medium | 6 |
| Search item master record register | API | Medium | 6 |
| Read item master record change history | API | Easy | 4 |
| Submit item master record change for checker | API | Complex | 8 |
| Approve or reject item master record change | API | Complex | 8 |
| Item master record record and change history | DB | Medium | 4 |
| Internal handoff of item master record to consuming modules | Integration | Simple | 4 |
| BMTC Item ID and OEM Linkage feature tests | Testing | Complex | 8 |
| BMTC Item ID and OEM Linkage implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
