# F02-002 — Department, Post and Designation Masters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Department, Post and Designation Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Administrator maintains departments and designations used when creating Posts. This does not replace the Post master in Module 01.

### Business Objective
Keep designation and department lists consistent for Post creation.

### Actors
Maker: Master Data Administrator. Checker: Master Data Checker.

### User Journey
1. Who creates: Master Data Administrator.
2. How they create: Opens Designation / Department register → New, enters code and name.
3. How they edit: Edit draft or submit a change to rename. Items in use on Posts cannot be deleted.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker inbox for catalogue changes.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Catalogue item history.
8. How the checker / auditor sees history: Same for checker.

### Functional Capabilities
- Authorised administrator creates and updates the designation catalogue item.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Designation catalogue item register and search | Medium |
| Designation catalogue item create / edit form | Complex |
| Designation catalogue item change history | Medium |
| Designation catalogue item maker–checker inbox | Medium |
| Designation catalogue item approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create designation catalogue item | Medium |
| Update designation catalogue item | Medium |
| Search designation catalogue item register | Medium |
| Read designation catalogue item change history | Easy |
| Submit designation catalogue item change for checker | Complex |
| Approve or reject designation catalogue item change | Complex |

### Inputs
Code, name, department (for designation), status.

### Outputs
Current designation catalogue item record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- Post master (F01-002) selects from this catalogue; it does not free-type designation.

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
Poor unique-identity control on the designation catalogue item would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Designation catalogue item register and search | UI | Medium | 6 |
| Designation catalogue item create / edit form | UI | Complex | 12 |
| Designation catalogue item change history | UI | Medium | 6 |
| Designation catalogue item maker–checker inbox | UI | Medium | 6 |
| Designation catalogue item approval panel | UI | Easy | 4 |
| Create designation catalogue item | API | Medium | 6 |
| Update designation catalogue item | API | Medium | 6 |
| Search designation catalogue item register | API | Medium | 6 |
| Read designation catalogue item change history | API | Easy | 4 |
| Submit designation catalogue item change for checker | API | Complex | 8 |
| Approve or reject designation catalogue item change | API | Complex | 8 |
| Designation catalogue item record and change history | DB | Medium | 4 |
| Internal handoff of designation catalogue item to consuming modules | Integration | Simple | 4 |
| Department, Post and Designation Masters feature tests | Testing | Complex | 8 |
| Department, Post and Designation Masters implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
