# F03-002 — Schedule Hierarchy, ABC and Substitute Items

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Schedule Hierarchy, ABC and Substitute Items |
| **Module** | 03 — Item Master and Catalogue |

### Description
Administrator classifies items under Main/Sub schedule and ABC, captures warranty/batch/expiry where applicable, and links substitutes.

### Business Objective
Classification and substitutes without a second item ID.

### Actors
Maker: Stores Master Administrator. Checker: Stores Checker.

### User Journey
1. Who creates: Stores Master Administrator.
2. How they create: Opens an approved item → Classification tab: schedule, ABC, warranty flags, substitute item IDs, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit classification change to checker.
5. How the approver sees pending items: Checker classification inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Classification history on the item.
8. How the checker / auditor sees history: Auditor.

### Functional Capabilities
- Authorised administrator creates and updates the item classification.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Item classification register and search | Medium |
| Item classification create / edit form | Complex |
| Item classification change history | Medium |
| Item classification maker–checker inbox | Medium |
| Item classification approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create item classification | Medium |
| Update item classification | Medium |
| Search item classification register | Medium |
| Read item classification change history | Easy |
| Submit item classification change for checker | Complex |
| Approve or reject item classification change | Complex |

### Inputs
Main/sub schedule, ABC, warranty, batch/expiry flags, substitute Item IDs.

### Outputs
Current item classification record; searchable register; change history.

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
Submit classification change to checker.

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
Poor unique-identity control on the item classification would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Item classification register and search | UI | Medium | 6 |
| Item classification create / edit form | UI | Complex | 12 |
| Item classification change history | UI | Medium | 6 |
| Item classification maker–checker inbox | UI | Medium | 6 |
| Item classification approval panel | UI | Easy | 4 |
| Create item classification | API | Medium | 6 |
| Update item classification | API | Medium | 6 |
| Search item classification register | API | Medium | 6 |
| Read item classification change history | API | Easy | 4 |
| Submit item classification change for checker | API | Complex | 8 |
| Approve or reject item classification change | API | Complex | 8 |
| Item classification record and change history | DB | Medium | 4 |
| Internal handoff of item classification to consuming modules | Integration | Simple | 4 |
| Schedule Hierarchy, ABC and Substitute Items feature tests | Testing | Complex | 8 |
| Schedule Hierarchy, ABC and Substitute Items implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
