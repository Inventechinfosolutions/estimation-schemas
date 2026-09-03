# F01-001 — Person Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-001 |
| **Feature Name** | Person Master |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Access Administrator maintains each BMTC official as a unique Person. Later job-card, stores and purchase actions are stored against this Person, not a shared login.

### Business Objective
Attribute every privileged action to one named Person.

### Actors
Maker: Access Administrator Post. Checker: Access Checker Post.

### User Journey
1. Who creates: Access Administrator Post.
2. How they create: Administrator opens Person register → New, enters legal name, unique ID, official mobile and email (used for 2FA), saves draft.
3. How they edit: Draft/Returned editable. Unique ID cannot be reused. Deactivation does not delete the Person.
4. How they send for approval: Submit to Access Checker. Person is not usable for Post mapping until approved.
5. How the approver sees pending items: Checker Person approval inbox.
6. How the approver decides: Approve or reject with remarks.
7. How the maker sees history: Administrator opens Person change history.
8. How the checker / auditor sees history: Checker and auditor open the same history.

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

### Inputs
Legal name, unique ID, official mobile, official email, status.

### Outputs
Current Person record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- One Person per official.
- 2FA targets are official mobile/email only.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.
- Unique ID mandatory and unique.
- Official mobile mandatory for 2FA.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to Access Checker. Person is not usable for Post mapping until approved.

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
| Create Person | API | Medium | 6 |
| Update Person | API | Medium | 6 |
| Search Person register | API | Medium | 6 |
| Read Person change history | API | Easy | 4 |
| Submit Person change for checker | API | Complex | 8 |
| Approve or reject Person change | API | Complex | 8 |
| Person record and change history | DB | Medium | 4 |
| Internal handoff of Person to consuming modules | Integration | Simple | 4 |
| Person Master feature tests | Testing | Complex | 8 |
| Person Master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
