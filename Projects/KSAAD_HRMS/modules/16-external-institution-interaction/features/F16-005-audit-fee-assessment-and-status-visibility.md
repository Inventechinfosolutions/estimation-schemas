# F16-005 — Audit Fee Assessment and Status Visibility

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-005 |
| **Feature Name** | Audit Fee Assessment and Status Visibility |
| **Module** | 16 — External / Institution Interaction |

### Description
Institution user sees approved assessments, dispatched bills and outstanding/paid status; cannot edit.

### Business Objective
Transparency of fee status.

### Actors
User: Institution user with View fee function. Auditor: read-only history.

### User Journey
1. Who creates: Institution user with View fee function.
2. How they create: Portal → Fees shows approved/dispatched items from Module 10.
3. How they edit: Cannot edit. Questions are not a payment screen unless later ordered.
4. How they send for approval: Not applicable.
5. How the approver sees pending items: New bill dispatch can appear as a portal task.
6. How the approver decides: Not applicable.
7. How the user sees history: Status timeline as published (assessed, billed, dispatched, paid, outstanding).
8. How the supervisor / auditor sees history: Staff see the ledger in Module 10.

### Functional Capabilities
- Authorised user creates, edits and searches institution fee view records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Institution fee view register | Medium |
| Institution fee view form (create and edit) | Complex |
| Institution fee view history | Medium |
| Institution fee status | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create institution fee view | Medium |
| Update institution fee view | Medium |
| Search institution fee view | Medium |
| Read institution fee view history | Easy |
| Read fee status for institution | Medium |

### Inputs
Read-only assessment, bill, outstanding.

### Outputs
Persisted institution fee view; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Only that institution's records.

### Calculations
Outstanding as in F10-004.

### Workflow
Not applicable.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Bill PDF download if dispatched.

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
| Institution fee view register | UI | Medium | 6 |
| Institution fee view form (create and edit) | UI | Complex | 12 |
| Institution fee view history | UI | Medium | 6 |
| Institution fee status | UI | Medium | 6 |
| Create institution fee view | API | Medium | 6 |
| Update institution fee view | API | Medium | 6 |
| Search institution fee view | API | Medium | 6 |
| Read institution fee view history | API | Easy | 4 |
| Read fee status for institution | API | Medium | 6 |
| Institution fee view record and history | DB | Medium | 4 |
| Internal identity/document hooks for institution fee view | Integration | Simple | 4 |
| Audit Fee Assessment and Status Visibility feature tests | Testing | Complex | 8 |
| Audit Fee Assessment and Status Visibility implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **77** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
