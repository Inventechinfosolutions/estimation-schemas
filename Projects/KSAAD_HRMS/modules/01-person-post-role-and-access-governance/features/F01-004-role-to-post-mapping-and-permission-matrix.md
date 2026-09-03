# F01-004 — Role-to-Post Mapping and Permission Matrix

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Role-to-Post Mapping and Permission Matrix |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Administrator assigns Roles to Posts and maintains the permission matrix (module, action, data scope).

### Business Objective
Permissions attach to the Post, not to the Person. The Person inherits them through mapping.

### Actors
Maker: Access Administrator. Checker: Access Checker.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Administrator opens Role–Post matrix, selects a Post, ticks Roles / permissions (view, create, approve, download) per module, Save draft.
3. How they edit: Draft matrix edits are allowed. Approved matrix changes require a new submission. Removing Approve from a Post immediately stops that Post appearing as approver after checker approval.
4. How they send for approval: Submit sends the matrix change to the Access Checker.
5. How the approver sees pending items: Checker opens Role-matrix inbox with before/after permission summary.
6. How the approver decides: Checker approves or rejects. On approve, Persons currently mapped to the Post get the new menus on next session refresh.
7. How the maker sees history: Administrator opens permission change history for a Post.
8. How the checker / auditor sees history: Checker and auditor open the same history.

### Functional Capabilities
- Authorised administrator creates and updates the Role-to-Post mapping.
- Searchable register and replayable change history.
- Checker approval where maker–checker is required.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Role-to-post mapping register and search | Medium |
| Role-to-post mapping create / edit form | Very High |
| Role-to-post mapping change history | Medium |
| Role-to-post mapping maker–checker inbox | Medium |
| Role-to-post mapping approval panel | Easy |
| Permission matrix grid for a Post | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Role-to-Post mapping | Medium |
| Update Role-to-Post mapping | Medium |
| Search Role-to-Post mapping register | Medium |
| Read Role-to-Post mapping change history | Easy |
| Submit Role-to-Post mapping change for checker | Complex |
| Approve or reject Role-to-Post mapping change | Complex |
| Resolve effective permissions for a Person's current Post | Complex |

### Inputs
Post, Role, module, action (view/create/edit/submit/approve/download), data scope (own office / subordinate offices / all).

### Outputs
Current Role-to-Post mapping record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- Persons are not granted permissions directly.
- Institution users (F01-006) are not given staff Post Roles.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit sends the matrix change to the Access Checker.

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
Poor unique-identity control on the Role-to-Post mapping would split later transactions across duplicate records.

### Non Functional Requirements
Register search remains responsive. History is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Role-to-post mapping register and search | UI | Medium | 6 |
| Role-to-post mapping create / edit form | UI | Very High | 16 |
| Role-to-post mapping change history | UI | Medium | 6 |
| Role-to-post mapping maker–checker inbox | UI | Medium | 6 |
| Role-to-post mapping approval panel | UI | Easy | 4 |
| Permission matrix grid for a Post | UI | Very High | 16 |
| Create Role-to-Post mapping | API | Medium | 6 |
| Update Role-to-Post mapping | API | Medium | 6 |
| Search Role-to-Post mapping register | API | Medium | 6 |
| Read Role-to-Post mapping change history | API | Easy | 4 |
| Submit Role-to-Post mapping change for checker | API | Complex | 8 |
| Approve or reject Role-to-Post mapping change | API | Complex | 8 |
| Resolve effective permissions for a Person's current Post | API | Complex | 8 |
| Role-to-post mapping record and change history | DB | Medium | 4 |
| Internal handoff of Role-to-Post mapping to consuming modules | Integration | Simple | 4 |
| Role-to-Post Mapping and Permission Matrix feature tests | Testing | Complex | 8 |
| Role-to-Post Mapping and Permission Matrix implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
