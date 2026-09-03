# F13-002 — Document Version Control

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-002 |
| **Feature Name** | Document Version Control |
| **Module** | 13 — Document Management System (DMS) |

### Description
User uploads a replacement; previous bytes remain as version N; user and auditor see version history; cannot edit old versions.

### Business Objective
Never lose prior evidence.

### Actors
User: Same Posts that can attach on the parent. Auditor: read-only history.

### User Journey
1. Who creates: Same Posts that can attach on the parent.
2. How they create: On an attachment → New version, upload file, comment, Save.
3. How they edit: Cannot patch version N. Supersede only.
4. How they send for approval: Save publishes new current version.
5. How the approver sees pending items: None unless parent is in approval — approver sees current version.
6. How the approver decides: Not a document-level approve.
7. How the user sees history: Version list: N, who, when, comment, download prior.
8. How the supervisor / auditor sees history: Same on the parent.

### Functional Capabilities
- Authorised user creates, edits and searches document version records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Document version register | Medium |
| Document version form (create and edit) | Complex |
| Document version history | Medium |
| Version history panel | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create document version | Medium |
| Update document version | Medium |
| Search document version | Medium |
| Read document version history | Easy |
| Add version | Medium |
| Get version bytes | Easy |

### Inputs
Attachment, file, comment.

### Outputs
Persisted document version; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Parent attachment exists.

### Calculations
Next version number = max+1.

### Workflow
Save publishes new current version.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
All versions retained.

### Reports
None beyond history.

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
| Document version register | UI | Medium | 6 |
| Document version form (create and edit) | UI | Complex | 12 |
| Document version history | UI | Medium | 6 |
| Version history panel | UI | Medium | 6 |
| Create document version | API | Medium | 6 |
| Update document version | API | Medium | 6 |
| Search document version | API | Medium | 6 |
| Read document version history | API | Easy | 4 |
| Add version | API | Medium | 6 |
| Get version bytes | API | Easy | 4 |
| Document version record and history | DB | Medium | 4 |
| Internal identity/document hooks for document version | Integration | Simple | 4 |
| Document Version Control feature tests | Testing | Complex | 8 |
| Document Version Control implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **81** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
