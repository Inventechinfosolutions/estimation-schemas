# F01-004 — Role-to-Post Mapping and Permission Matrix

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Role-to-Post Mapping and Permission Matrix |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Administrator assigns Roles (view/create/approve by module) to Posts; permissions are never granted directly to Persons.

### Business Objective
Menus and actions follow the current Post.

### Actors
Maker: Access Administrator. Checker: Access Checker.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Opens Role–Post matrix for a Post, ticks module actions and data scope (own unit / zone / all), Save draft.
3. How they edit: Approved matrix changes require a new submission.
4. How they send for approval: Submit to Access Checker.
5. How the approver sees pending items: Checker matrix inbox with before/after.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Permission history for the Post.
8. How the checker / auditor sees history: Same for auditor.

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
| Permission matrix grid | Very High |

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
| Resolve effective permissions for current Post | Complex |

### Inputs
Post, Role, module, action, data scope.

### Outputs
Current Role-to-Post mapping record; searchable register; change history.

### Business Rules
- Create and edit are restricted to authorised administrator Posts.
- Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.
- Every change stores actor Person, acting Post, timestamp and before/after values.
- Persons are not granted permissions directly.
- Accounts login (FR-X-09) is a Role on an Accounts Post, not a second directory.

### Validations
- Mandatory identity fields are required.
- Duplicate unique identifiers are refused.

### Calculations
None beyond uniqueness and effective-date overlap checks.

### Workflow
Submit to Access Checker.

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
| Permission matrix grid | UI | Very High | 16 |
| Create Role-to-Post mapping | API | Medium | 6 |
| Update Role-to-Post mapping | API | Medium | 6 |
| Search Role-to-Post mapping register | API | Medium | 6 |
| Read Role-to-Post mapping change history | API | Easy | 4 |
| Submit Role-to-Post mapping change for checker | API | Complex | 8 |
| Approve or reject Role-to-Post mapping change | API | Complex | 8 |
| Resolve effective permissions for current Post | API | Complex | 8 |
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
