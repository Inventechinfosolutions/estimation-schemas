# F02-001 — Organisation Hierarchy and Office Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Organisation Hierarchy and Office Master |
| **Module** | 02 — Master Data & System Configuration |

### Description
Administrator maintains HO, RO and LAC offices and their parent hierarchy.

### Business Objective
Give every Post and transaction an office scope.

### Actors
Maker: Master Data Administrator. Checker: Master Data Checker.

### User Journey
1. Who creates: Master Data Administrator.
2. How they create: Opens Office register → New office, enters code, name, type (HO/RO/LAC), parent office, then Save.
3. How they edit: Draft edits allowed. Approved offices can be renamed or re-parented via a checked change. Offices in use cannot be deleted.
4. How they send for approval: Submit to checker before the office can be selected on Posts.
5. How the approver sees pending items: Checker office-change inbox.
6. How the approver decides: Approve or reject with remarks.
7. How the maker sees history: Office change history on the record.
8. How the checker / auditor sees history: Same history for checker/auditor.

### Functional Capabilities
- Authorised administrator creates and updates the office.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Office register and search | Medium |
| Office create / edit form | Complex |
| Office change history | Medium |
| Office maker–checker inbox | Medium |
| Office approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create office | Medium |
| Update office | Medium |
| Search office register | Medium |
| Read office change history | Easy |
| Submit office change for checker | Complex |
| Approve or reject office change | Complex |

### Inputs
Office code, name, type, parent office, status.

### Outputs
Current office record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Code unique.
- LAC must have a parent RO unless type is HO.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to checker before the office can be selected on Posts.

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
Poor unique-identity control on the office would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Office register and search | UI | Medium | 6 |
| Office create / edit form | UI | Complex | 12 |
| Office change history | UI | Medium | 6 |
| Office maker–checker inbox | UI | Medium | 6 |
| Office approval panel | UI | Easy | 4 |
| Create office | API | Medium | 6 |
| Update office | API | Medium | 6 |
| Search office register | API | Medium | 6 |
| Read office change history | API | Easy | 4 |
| Submit office change for checker | API | Complex | 8 |
| Approve or reject office change | API | Complex | 8 |
| Office record and change history | DB | Medium | 4 |
| Internal handoff of office to consuming modules | Integration | Simple | 4 |
| Organisation Hierarchy and Office Master feature tests | Testing | Complex | 8 |
| Organisation Hierarchy and Office Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
