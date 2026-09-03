# F01-004 — Role-to-Post Mapping and Permission Matrix

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-004 |
| **Feature Name** | Role-to-Post Mapping and Permission Matrix |
| **Module** | 01 — Person, Post, Role and Access Governance |

### Description
Administrator assigns Roles (view/create/approve by CCC module) to Posts; permissions are never granted directly to Persons.

### Business Objective
Menus and actions follow the current Post.

### Actors
Maker: Access Administrator. Checker: Access Checker.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Opens Role–Post matrix for a Post, ticks module actions and data scope (own unit / district / state), Save draft.
3. How they edit: Approved matrix changes require a new submission.
4. How they send for approval: Submit to Access Checker.
5. How the approver sees pending items: Checker matrix inbox with before/after.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Permission history for the Post.
8. How the checker/auditor sees history: Same for auditor.

### Functional Capabilities
- Role–Post matrix
- Unit/district/state data scope
- Maker–checker

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Role–Post register | Medium |
| Permission matrix grid | Very High |
| Matrix change history | Medium |
| Matrix maker–checker inbox | Medium |
| Matrix approval panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create Role–Post mapping | Medium |
| Update matrix | Medium |
| Search matrix | Medium |
| Read matrix history | Easy |
| Submit matrix change | Complex |
| Approve or reject matrix | Complex |
| Resolve effective permissions for current Post | Complex |

### Inputs
Post, Role, module, action, data scope.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Persons are not granted permissions directly.

### Validations
- Post and Role mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → Approved/Rejected.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Permission export.

### Notifications
Checker/maker.

### Security
Administrator Posts only.

### Integrations
None.

### Dependencies
F01-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Role–Post register | UI | Medium | 6 |
| Permission matrix grid | UI | Very High | 16 |
| Matrix change history | UI | Medium | 6 |
| Matrix maker–checker inbox | UI | Medium | 6 |
| Matrix approval panel | UI | Easy | 4 |
| Create Role–Post mapping | API | Medium | 6 |
| Update matrix | API | Medium | 6 |
| Search matrix | API | Medium | 6 |
| Read matrix history | API | Easy | 4 |
| Submit matrix change | API | Complex | 8 |
| Approve or reject matrix | API | Complex | 8 |
| Resolve effective permissions for current Post | API | Complex | 8 |
| Role–Post matrix and history | DB | Complex | 6 |
| Role-to-Post Mapping and Permission Matrix feature tests | Testing | Very High | 12 |
| Role-to-Post Mapping and Permission Matrix implementation documentation | Documentation | Complex | 4 |

**Feature total: 106 hours**
