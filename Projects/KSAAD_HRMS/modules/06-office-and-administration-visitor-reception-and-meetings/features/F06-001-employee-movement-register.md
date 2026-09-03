# F06-001 — Employee Movement Register

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Employee Movement Register |
| **Module** | 06 — Office & Administration (Visitor, Reception and Meetings) |

### Description
Staff or reception records in/out movement; supervisor may confirm exceptions; history is the register itself.

### Business Objective
Digitise the movement register with attribution.

### Actors
User: The Person records own movement, or reception/office clerk records on their behalf with reason. Auditor: read-only history.

### User Journey
1. Who creates: The Person records own movement, or reception/office clerk records on their behalf with reason.
2. How they create: Opens Movement register → New, Person (default self), out time, expected in, purpose, Save. Or check-in to close an open out.
3. How they edit: Open entries can be edited until check-in. Closed entries need a correction request to the supervising Post.
4. How they send for approval: Save is enough for normal entries. Correction of a closed entry is submitted to supervisor.
5. How the approver sees pending items: Supervisor sees pending movement corrections, not every check-in.
6. How the approver decides: Supervisor approves correction or rejects.
7. How the user sees history: My movement history by date.
8. How the supervisor / auditor sees history: Office movement register and correction log.

### Functional Capabilities
- Authorised user creates, edits and searches movement entry records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Movement entry register | Medium |
| Movement entry form (create and edit) | Complex |
| Movement entry history | Medium |
| Movement register (day grid) | Medium |
| My movement history | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create movement entry | Medium |
| Update movement entry | Medium |
| Search movement entry | Medium |
| Read movement entry history | Easy |

### Inputs
Person, out time, in time, purpose, place.

### Outputs
Persisted movement entry; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Out time mandatory.
- In time ≥ out time when closed.

### Calculations
Duration = in − out.

### Workflow
Save is enough for normal entries. Correction of a closed entry is submitted to supervisor.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Daily movement by office.

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
| Movement entry register | UI | Medium | 6 |
| Movement entry form (create and edit) | UI | Complex | 12 |
| Movement entry history | UI | Medium | 6 |
| Movement register (day grid) | UI | Medium | 6 |
| My movement history | UI | Easy | 4 |
| Create movement entry | API | Medium | 6 |
| Update movement entry | API | Medium | 6 |
| Search movement entry | API | Medium | 6 |
| Read movement entry history | API | Easy | 4 |
| Movement entry record and history | DB | Medium | 4 |
| Internal identity/document hooks for movement entry | Integration | Simple | 4 |
| Employee Movement Register feature tests | Testing | Complex | 8 |
| Employee Movement Register implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **75** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
