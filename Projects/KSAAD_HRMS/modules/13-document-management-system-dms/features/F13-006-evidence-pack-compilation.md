# F13-006 — Evidence Pack Compilation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-006 |
| **Feature Name** | Evidence Pack Compilation |
| **Module** | 13 — Document Management System (DMS) |

### Description
Officer selects documents on a parent (audit, recovery, claim), compiles a pack, submits if the parent workflow requires a frozen pack; history of pack versions.

### Business Objective
One frozen pack for review.

### Actors
User: Officer on the parent record. Approver of the parent sees the frozen pack. Auditor: read-only history.

### User Journey
1. Who creates: Officer on the parent record. Approver of the parent sees the frozen pack.
2. How they create: Parent → Compile pack, tick documents/versions, title, Save draft pack.
3. How they edit: Draft pack editable. After freeze (on parent Submit), new pack version required.
4. How they send for approval: Freeze pack when parent is submitted.
5. How the approver sees pending items: No separate pack inbox; parent approver opens the pack.
6. How the approver decides: Not decided here; parent workflow decides.
7. How the user sees history: Pack versions on the parent.
8. How the supervisor / auditor sees history: Approver sees frozen pack at decision time.

### Functional Capabilities
- Authorised user creates, edits and searches evidence pack records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Evidence pack register | Medium |
| Evidence pack form (create and edit) | Complex |
| Evidence pack history | Medium |
| Pack builder | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create evidence pack | Medium |
| Update evidence pack | Medium |
| Search evidence pack | Medium |
| Read evidence pack history | Easy |
| Compile pack snapshot | Complex |

### Inputs
Parent, selected documents, pack title.

### Outputs
Persisted evidence pack; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- At least one document.

### Calculations
None.

### Workflow
Freeze pack when parent is submitted.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Snapshot list of document versions.

### Reports
None.

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
| Evidence pack register | UI | Medium | 6 |
| Evidence pack form (create and edit) | UI | Complex | 12 |
| Evidence pack history | UI | Medium | 6 |
| Pack builder | UI | Complex | 12 |
| Create evidence pack | API | Medium | 6 |
| Update evidence pack | API | Medium | 6 |
| Search evidence pack | API | Medium | 6 |
| Read evidence pack history | API | Easy | 4 |
| Compile pack snapshot | API | Complex | 8 |
| Evidence pack record and history | DB | Medium | 4 |
| Internal identity/document hooks for evidence pack | Integration | Simple | 4 |
| Evidence Pack Compilation feature tests | Testing | Complex | 8 |
| Evidence Pack Compilation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **85** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
