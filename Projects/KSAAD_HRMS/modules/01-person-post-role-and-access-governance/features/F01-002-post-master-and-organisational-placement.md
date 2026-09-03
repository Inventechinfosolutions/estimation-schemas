# F01-002 — Post Master and Organisational Placement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-002 |
| **Feature Name** | Post Master and Organisational Placement |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Administrator maintains the Post catalogue: office, designation and supervising Post used for approval routing.

### Business Objective
Provide the organisational Post that Roles and Persons are mapped to.

### Actors
Maker: Access Administrator. Checker: Access Checker.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Administrator opens Post register → New Post, enters post code, designation, office (HO/RO/LAC), and supervising Post, then saves.
3. How they edit: Administrator updates office placement or supervising Post with effective dates. Past mappings remain in history.
4. How they send for approval: Create/update of a Post is submitted to the Access Checker before the Post can be used in mapping.
5. How the approver sees pending items: Checker opens Post approval inbox.
6. How the approver decides: Checker approves or rejects. Reject returns the Post to draft.
7. How the maker sees history: Administrator opens Post history (placement and supervising-Post changes).
8. How the checker / auditor sees history: Checker and auditor open the same history.

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
| Supervising Post lookup | Easy |

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
Post code, designation, office, supervising Post, effective from/to, status.

### Outputs
Current Post record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- A Post cannot supervise itself.
- Approval routing in later modules uses the current supervising Post.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Post code unique.
- Office mandatory.
- Supervising Post, when entered, must be an existing Post.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Create/update of a Post is submitted to the Access Checker before the Post can be used in mapping.

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
| Supervising Post lookup | UI | Easy | 4 |
| Create Post | API | Medium | 6 |
| Update Post | API | Medium | 6 |
| Search Post register | API | Medium | 6 |
| Read Post change history | API | Easy | 4 |
| Submit Post change for checker | API | Complex | 8 |
| Approve or reject Post change | API | Complex | 8 |
| Post record and change history | DB | Medium | 4 |
| Internal handoff of Post to consuming modules | Integration | Simple | 4 |
| Post Master and Organisational Placement feature tests | Testing | Complex | 8 |
| Post Master and Organisational Placement implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **95** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
