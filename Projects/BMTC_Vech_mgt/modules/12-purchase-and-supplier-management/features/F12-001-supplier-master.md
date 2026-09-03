# F12-001 — Supplier Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-001 |
| **Feature Name** | Supplier Master |
| **Module** | 12 — Purchase and Supplier Management |

### Description
Purchase Administrator maintains approved suppliers with contacts, item categories and performance history.

### Business Objective
FR-S-20.

### Actors
Maker: Purchase Administrator. Checker: Purchase Checker / COSP Post.

### User Journey
1. Who creates: Purchase Administrator.
2. How they create: Supplier register → New: name, contacts, categories, Save draft.
3. How they edit: Draft/Returned editable. Performance scores are system-updated, not typed freely.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker supplier inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Supplier history.
8. How the checker / auditor sees history: Auditor.

### Functional Capabilities
- Authorised administrator creates and updates the supplier.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Supplier register and search | Medium |
| Supplier create / edit form | Complex |
| Supplier change history | Medium |
| Supplier maker–checker inbox | Medium |
| Supplier approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create supplier | Medium |
| Update supplier | Medium |
| Search supplier register | Medium |
| Read supplier change history | Easy |
| Submit supplier change for checker | Complex |
| Approve or reject supplier change | Complex |

### Inputs
Name, contacts, categories, status.

### Outputs
Current supplier record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Name unique.

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
Poor unique-identity control on the supplier would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Supplier register and search | UI | Medium | 6 |
| Supplier create / edit form | UI | Complex | 12 |
| Supplier change history | UI | Medium | 6 |
| Supplier maker–checker inbox | UI | Medium | 6 |
| Supplier approval panel | UI | Easy | 4 |
| Create supplier | API | Medium | 6 |
| Update supplier | API | Medium | 6 |
| Search supplier register | API | Medium | 6 |
| Read supplier change history | API | Easy | 4 |
| Submit supplier change for checker | API | Complex | 8 |
| Approve or reject supplier change | API | Complex | 8 |
| Supplier record and change history | DB | Medium | 4 |
| Internal handoff of supplier to consuming modules | Integration | Simple | 4 |
| Supplier Master feature tests | Testing | Complex | 8 |
| Supplier Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
