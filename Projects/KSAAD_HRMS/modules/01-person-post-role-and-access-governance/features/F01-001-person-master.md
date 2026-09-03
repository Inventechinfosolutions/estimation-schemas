# F01-001 — Person Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Person Master |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
An Administrator maintains each official as a unique Person. Later privileged actions are stored against this Person, not a shared login.

### Business Objective
Ensure every official action is attributable to one named Person.

### Actors
Maker: Access Administrator (Post with Person-administration Role). Checker: Access Checker Post (maker–checker on Person create/update).

### User Journey
1. Who creates: Access Administrator (Post with Person-administration Role).
2. How they create: Administrator opens Person register → New Person, enters legal name, unique ID, official email and mobile, and saves. Duplicate unique ID is refused.
3. How they edit: Administrator searches the Person, opens the record, edits particulars. Unique ID cannot be reused on another Person. Deactivation does not delete the Person.
4. How they send for approval: Create/update is submitted to the Access Checker. The Person is not usable for login mapping until approved.
5. How the approver sees pending items: Access Checker opens Person approval inbox listing pending creates/updates.
6. How the approver decides: Checker opens the Person, sees before/after values, Approves or Rejects with remarks. Reject returns to the Administrator for correction.
7. How the maker sees history: Administrator opens the Person and views change history (who changed what, when).
8. How the checker / auditor sees history: Checker and auditor open the same Person history. Login and mapping events are in F01-008.

### Functional Capabilities
- Authorised administrator creates and updates the Person.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Person register and search | Medium |
| Person create / edit form | Complex |
| Person change history | Medium |
| Person maker–checker inbox | Medium |
| Person approval panel | Easy |
| Person uniqueness conflict dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Person | Medium |
| Update Person | Medium |
| Search Person register | Medium |
| Read Person change history | Easy |
| Submit Person change for checker | Complex |
| Approve or reject Person change | Complex |
| Refuse duplicate Person | Easy |

### Inputs
Legal name, unique ID, official email, official mobile, status (Active / Inactive), remarks.

### Outputs
Current Person record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- One Person per official. A second Person for the same unique ID is refused.
- Person is the identity consumed by Post-to-Person mapping (F01-003).

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Unique ID is mandatory and unique.
- Official email, when entered, must be unique.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Create/update is submitted to the Access Checker. The Person is not usable for login mapping until approved.

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
Poor unique-identity control on the Person would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Person register and search | UI | Medium | 6 |
| Person create / edit form | UI | Complex | 12 |
| Person change history | UI | Medium | 6 |
| Person maker–checker inbox | UI | Medium | 6 |
| Person approval panel | UI | Easy | 4 |
| Person uniqueness conflict dialog | UI | Simple | 2 |
| Create Person | API | Medium | 6 |
| Update Person | API | Medium | 6 |
| Search Person register | API | Medium | 6 |
| Read Person change history | API | Easy | 4 |
| Submit Person change for checker | API | Complex | 8 |
| Approve or reject Person change | API | Complex | 8 |
| Refuse duplicate Person | API | Easy | 4 |
| Person record and change history | DB | Medium | 4 |
| Internal handoff of Person to consuming modules | Integration | Simple | 4 |
| Person Master feature tests | Testing | Complex | 8 |
| Person Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **97** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
