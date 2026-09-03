# F16-004 — View and Download Issued Audit Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-004 |
| **Feature Name** | View and Download Issued Audit Reports |
| **Module** | 16 — External / Institution Interaction |

### Description
Institution user lists issued reports for their institution, views/downloads per F13 rights; downloads are logged.

### Business Objective
Institution gets the issued report, not drafts.

### Actors
User: Institution user with View report function. Auditor: read-only history.

### User Journey
1. Who creates: Institution user with View report function.
2. How they create: Portal → Reports lists issued items only. Open/view/download.
3. How they edit: Cannot edit the report.
4. How they send for approval: Not applicable.
5. How the approver sees pending items: New issued reports appear as tasks on portal home.
6. How the approver decides: Not applicable.
7. How the user sees history: Institution sees issue date and their download history.
8. How the supervisor / auditor sees history: KSAAD auditor sees who in the institution downloaded (F13-005).

### Functional Capabilities
- Authorised user creates, edits and searches issued report access records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Issued report access register | Medium |
| Issued report access form (create and edit) | Complex |
| Issued report access history | Medium |
| Institution report list | Medium |
| Viewer/download | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create issued report access | Medium |
| Update issued report access | Medium |
| Search issued report access | Medium |
| Read issued report access history | Easy |
| List issued reports for institution | Medium |
| Authorised download | Medium |

### Inputs
Issued report metadata.

### Outputs
Persisted issued report access; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Only issued reports for that institution.

### Calculations
None.

### Workflow
Not applicable.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Issued PDF.

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
| Issued report access register | UI | Medium | 6 |
| Issued report access form (create and edit) | UI | Complex | 12 |
| Issued report access history | UI | Medium | 6 |
| Institution report list | UI | Medium | 6 |
| Viewer/download | UI | Easy | 4 |
| Create issued report access | API | Medium | 6 |
| Update issued report access | API | Medium | 6 |
| Search issued report access | API | Medium | 6 |
| Read issued report access history | API | Easy | 4 |
| List issued reports for institution | API | Medium | 6 |
| Authorised download | API | Medium | 6 |
| Issued report access record and history | DB | Medium | 4 |
| Internal identity/document hooks for issued report access | Integration | Simple | 4 |
| View and Download Issued Audit Reports feature tests | Testing | Complex | 8 |
| View and Download Issued Audit Reports implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **87** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
