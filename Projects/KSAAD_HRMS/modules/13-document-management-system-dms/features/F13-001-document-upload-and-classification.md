# F13-001 — Document Upload and Classification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-001 |
| **Feature Name** | Document Upload and Classification |
| **Module** | 13 — Document Management System (DMS) |

### Description
User in a business transaction or DMS Role uploads a file, classifies type and links parent record; virus/size checks; history of uploads.

### Business Objective
Classified, linked documents.

### Actors
User: Any Person whose Post may attach on that parent (leave, audit, bill, etc.). Auditor: read-only history.

### User Journey
1. Who creates: Any Person whose Post may attach on that parent (leave, audit, bill, etc.).
2. How they create: From parent record → Attach, or DMS Upload: select file, type, parent type/id, Save.
3. How they edit: Replace file creates a new version (F13-002). Metadata edit if still draft.
4. How they send for approval: Save attaches. No separate approver unless parent workflow requires it.
5. How the approver sees pending items: None for upload itself. Failed uploads shown to the user.
6. How the approver decides: Not applicable.
7. How the user sees history: Attachments list on the parent with who/when.
8. How the supervisor / auditor sees history: Auditor sees upload log.

### Functional Capabilities
- Authorised user creates, edits and searches document upload records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Document upload register | Medium |
| Document upload form (create and edit) | Complex |
| Document upload history | Medium |
| Upload dialog | Medium |
| Attachments list on parent | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create document upload | Medium |
| Update document upload | Medium |
| Search document upload | Medium |
| Read document upload history | Easy |
| Store file and metadata | Complex |
| Link to parent | Medium |

### Inputs
File, document type, parent record, remarks.

### Outputs
Persisted document upload; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Type from catalogue.
- Size/type allowed.
- Parent exists.

### Calculations
None.

### Workflow
Save attaches. No separate approver unless parent workflow requires it.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
The file itself.

### Reports
Uploads by type/module.

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
| Document upload register | UI | Medium | 6 |
| Document upload form (create and edit) | UI | Complex | 12 |
| Document upload history | UI | Medium | 6 |
| Upload dialog | UI | Medium | 6 |
| Attachments list on parent | UI | Easy | 4 |
| Create document upload | API | Medium | 6 |
| Update document upload | API | Medium | 6 |
| Search document upload | API | Medium | 6 |
| Read document upload history | API | Easy | 4 |
| Store file and metadata | API | Complex | 8 |
| Link to parent | API | Medium | 6 |
| Document upload record and history | DB | Medium | 4 |
| Internal identity/document hooks for document upload | Integration | Simple | 4 |
| Document Upload and Classification feature tests | Testing | Complex | 8 |
| Document Upload and Classification implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **89** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
