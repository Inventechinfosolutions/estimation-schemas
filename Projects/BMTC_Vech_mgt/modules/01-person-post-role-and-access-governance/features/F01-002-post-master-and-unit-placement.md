# F01-002 — Post Master and Unit Placement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Post Master and Unit Placement |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Administrator maintains Posts placed on Depot, Zone, Central Workshop, Central Stores, Depot Stores or Central Office, with a supervising Post for approvals.

### Business Objective
Place Roles and Persons on organisational Posts scoped by BMTC unit.

### Actors
Maker: Access Administrator. Checker: Access Checker.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Opens Post register → New: post code, designation, unit type and unit, supervising Post, Save draft.
3. How they edit: Placement and supervising Post change with effective dates; history retained.
4. How they send for approval: Submit to Access Checker before the Post can be mapped.
5. How the approver sees pending items: Checker Post inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Post placement history.
8. How the checker / auditor sees history: Same for checker/auditor.

### Functional Capabilities
- Authorised administrator creates and updates the Post.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Post register and search | Medium |
| Post create / edit form | Complex |
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
| Read Post change history | Easy |
| Submit Post change for checker | Complex |
| Approve or reject Post change | Complex |

### Inputs
Post code, designation, unit type, unit, supervising Post, effective from/to.

### Outputs
Current Post record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- A Post cannot supervise itself.
- Data scope follows the Post's unit unless a Central Office Role allows wider view.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Unit mandatory.
- Post code unique.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to Access Checker before the Post can be mapped.

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
Poor unique-identity control on the Post would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Post register and search | UI | Medium | 6 |
| Post create / edit form | UI | Complex | 12 |
| Post change history | UI | Medium | 6 |
| Post maker–checker inbox | UI | Medium | 6 |
| Post approval panel | UI | Easy | 4 |
| Create Post | API | Medium | 6 |
| Update Post | API | Medium | 6 |
| Search Post register | API | Medium | 6 |
| Read Post change history | API | Easy | 4 |
| Submit Post change for checker | API | Complex | 8 |
| Approve or reject Post change | API | Complex | 8 |
| Post record and change history | DB | Medium | 4 |
| Internal handoff of Post to consuming modules | Integration | Simple | 4 |
| Post Master and Unit Placement feature tests | Testing | Complex | 8 |
| Post Master and Unit Placement implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
