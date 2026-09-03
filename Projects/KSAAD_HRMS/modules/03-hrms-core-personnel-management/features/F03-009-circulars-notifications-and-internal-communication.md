# F03-009 — Circulars, Notifications and Internal Communication

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-009 |
| **Feature Name** | Circulars, Notifications and Internal Communication |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
An authorised officer drafts a circular, submits for release approval, publishes to selected Posts/offices; staff acknowledge if required; history of publish and acknowledgement is kept.

### Business Objective
Controlled internal communication with audience and acknowledgement.

### Actors
User: Communications / Establishment Officer drafts. Competent Post approves release. Staff in audience read and acknowledge. Auditor: read-only history.

### User Journey
1. Who creates: Communications / Establishment Officer drafts. Competent Post approves release. Staff in audience read and acknowledge.
2. How they create: Officer opens Circulars → New, enters title, body or attachment, audience (office, Role, Post), acknowledgement required yes/no, Save draft.
3. How they edit: Draft/Returned editable. After Publish, content is frozen; only expire/withdraw with reason.
4. How they send for approval: Submit for release approval. On approve, system publishes to audience.
5. How the approver sees pending items: Release-approver inbox. Staff see My Circulars inbox of unpublished-to-them items (published circulars).
6. How the approver decides: Approver Approves release or Rejects. Staff click Acknowledge when required.
7. How the user sees history: Author sees versions, publish time, acknowledgement counts.
8. How the supervisor / auditor sees history: Approver sees release decisions. Author/auditor see who acknowledged and when.

### Functional Capabilities
- Authorised user creates, edits and searches circular records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Circular register | Medium |
| Circular form (create and edit) | Complex |
| Circular history | Medium |
| Circular draft form | Complex |
| Release approver inbox | Medium |
| My Circulars (staff) | Medium |
| Acknowledgement register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create circular | Medium |
| Update circular | Medium |
| Search circular | Medium |
| Read circular history | Easy |
| Submit circular for release | Complex |
| Publish to audience | Complex |
| Record acknowledgement | Easy |

### Inputs
Title, body/attachment, audience, acknowledgement required, effective from/to.

### Outputs
Persisted circular; searchable register; history.

### Business Rules
- Withdrawn circulars remain in history.
- Audience is Post/office based, not ad-hoc email lists only.

### Validations
- Title mandatory.
- Audience not empty.

### Calculations
Acknowledgement % = acknowledged / audience size.

### Workflow
Submit for release approval. On approve, system publishes to audience.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Circular PDF/attachment via DMS.

### Reports
Unacknowledged circulars by office.

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
| Circular register | UI | Medium | 6 |
| Circular form (create and edit) | UI | Complex | 12 |
| Circular history | UI | Medium | 6 |
| Circular draft form | UI | Complex | 12 |
| Release approver inbox | UI | Medium | 6 |
| My Circulars (staff) | UI | Medium | 6 |
| Acknowledgement register | UI | Medium | 6 |
| Create circular | API | Medium | 6 |
| Update circular | API | Medium | 6 |
| Search circular | API | Medium | 6 |
| Read circular history | API | Easy | 4 |
| Submit circular for release | API | Complex | 8 |
| Publish to audience | API | Complex | 8 |
| Record acknowledgement | API | Easy | 4 |
| Circular record and history | DB | Medium | 4 |
| Internal identity/document hooks for circular | Integration | Simple | 4 |
| Circulars, Notifications and Internal Communication feature tests | Testing | Very High | 12 |
| Circulars, Notifications and Internal Communication implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
