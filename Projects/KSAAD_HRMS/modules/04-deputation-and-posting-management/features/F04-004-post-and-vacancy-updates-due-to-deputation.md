# F04-004 — Post and Vacancy Updates due to Deputation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Post and Vacancy Updates due to Deputation |
| **Module** | 04 — Deputation & Posting Management |

### Description
On approved deputation/repatriation, occupied/vacant counts update from mappings. HR confirms the impact screen.

### Business Objective
Vacancy stays consistent with deputation without double-keying Posts.

### Actors
User: System applies mapping changes; HR Establishment Officer confirms the vacancy impact screen. Access Administrator completes F01-003/F01-007 if not auto-applied. Auditor: read-only history.

### User Journey
1. Who creates: System applies mapping changes; HR Establishment Officer confirms the vacancy impact screen. Access Administrator completes F01-003/F01-007 if not auto-applied.
2. How they create: Triggered on F04-002/F04-003 approval: system shows from-Post vacant +1, to-Post occupied +1 (and reverse on repatriation). Officer confirms.
3. How they edit: Officer cannot type occupied counts. They can Return the trigger if the target Post is wrong (sends back to deputation change).
4. How they send for approval: Confirm impact posts the mapping change request to Module 01 (or applies if the same officer holds both Roles).
5. How the approver sees pending items: HR sees Vacancy impact inbox of unconfirmed deputation effects.
6. How the approver decides: Confirm or Return. Mapping approval remains Module 01 checker if required.
7. How the user sees history: Impact events linked to the deputation case.
8. How the supervisor / auditor sees history: Auditor sees vacancy snapshots before/after.

### Functional Capabilities
- Authorised user creates, edits and searches vacancy impact posting records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Vacancy impact posting register | Medium |
| Vacancy impact posting form (create and edit) | Complex |
| Vacancy impact posting history | Medium |
| Vacancy impact confirmation | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create vacancy impact posting | Medium |
| Update vacancy impact posting | Medium |
| Search vacancy impact posting | Medium |
| Read vacancy impact posting history | Easy |
| Apply mapping side-effect | Complex |

### Inputs
Deputation reference, from Post, to Post, effective date.

### Outputs
Persisted vacancy impact posting; searchable register; history.

### Business Rules
- Does not rewrite Post master. Occupied is always derived from mappings after confirm.

### Validations
- Effective date present.
- From and to Post present.

### Calculations
Vacant/occupied as in F03-002 after mapping apply.

### Workflow
Confirm impact posts the mapping change request to Module 01 (or applies if the same officer holds both Roles).

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
None.

### Reports
Vacancy movement due to deputation.

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
| Vacancy impact posting register | UI | Medium | 6 |
| Vacancy impact posting form (create and edit) | UI | Complex | 12 |
| Vacancy impact posting history | UI | Medium | 6 |
| Vacancy impact confirmation | UI | Medium | 6 |
| Create vacancy impact posting | API | Medium | 6 |
| Update vacancy impact posting | API | Medium | 6 |
| Search vacancy impact posting | API | Medium | 6 |
| Read vacancy impact posting history | API | Easy | 4 |
| Apply mapping side-effect | API | Complex | 8 |
| Vacancy impact posting record and history | DB | Medium | 4 |
| Internal identity/document hooks for vacancy impact posting | Integration | Simple | 4 |
| Post and Vacancy Updates due to Deputation feature tests | Testing | Complex | 8 |
| Post and Vacancy Updates due to Deputation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
