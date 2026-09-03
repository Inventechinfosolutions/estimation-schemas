# F16-001 — Institution Portal Workspace

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-001 |
| **Feature Name** | Institution Portal Workspace |
| **Module** | 16 — External / Institution Interaction |

### Description
Institution user (F01-006) signs in to a constrained workspace listing their tasks (AFS, replies, reports, fee). No staff menus.

### Business Objective
One landing place for institution work.

### Actors
User: Activated institution user. KSAAD staff do not work here; they see submissions in staff modules. Auditor: read-only history.

### User Journey
1. Who creates: Activated institution user. KSAAD staff do not work here; they see submissions in staff modules.
2. How they create: User logs in (institution identity). System shows institution-scoped task tiles. No create of staff Persons/Posts.
3. How they edit: Profile (contact) edit submitted to Institution Administrator / KSAAD checker as in F01-006.
4. How they send for approval: Not a business document. Tasks open F16-002..005.
5. How the approver sees pending items: Portal home = inbox of pending institution tasks (AFS due, para reply due).
6. How the approver decides: Not applicable at workspace level.
7. How the user sees history: User sees own task history tiles.
8. How the supervisor / auditor sees history: KSAAD officer sees institution activity in staff modules, not this UI.

### Functional Capabilities
- Authorised user creates, edits and searches institution portal session records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Institution portal session register | Medium |
| Institution portal session form (create and edit) | Very High |
| Institution portal session history | Medium |
| Institution home / task inbox | Very High |
| Institution profile | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create institution portal session | Medium |
| Update institution portal session | Medium |
| Search institution portal session | Medium |
| Read institution portal session history | Easy |
| List institution tasks | Complex |

### Inputs
Institution context (system), task list.

### Outputs
Persisted institution portal session; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- User must be Active institution user for that institution.

### Calculations
Counts of pending tasks.

### Workflow
Not a business document. Tasks open F16-002..005.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
N/A.

### Notifications
On-screen confirmation. Optional notice to the user on save failure.

### Security
Need-to-know by Post. Actions attributed to Person acting in a Post.

### Integrations
Module 01 identity. Document store if attachments are used.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).

### Risks
Unscoped access would expose records outside the user's office.

### Non Functional Requirements
Register and history remain searchable during office hours.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Institution portal session register | UI | Medium | 6 |
| Institution portal session form (create and edit) | UI | Very High | 16 |
| Institution portal session history | UI | Medium | 6 |
| Institution home / task inbox | UI | Very High | 16 |
| Institution profile | UI | Easy | 4 |
| Create institution portal session | API | Medium | 6 |
| Update institution portal session | API | Medium | 6 |
| Search institution portal session | API | Medium | 6 |
| Read institution portal session history | API | Easy | 4 |
| List institution tasks | API | Complex | 8 |
| Institution portal session record and history | DB | Medium | 4 |
| Internal identity/document hooks for institution portal session | Integration | Simple | 4 |
| Institution Portal Workspace feature tests | Testing | Very High | 12 |
| Institution Portal Workspace implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **101** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
