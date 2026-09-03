# F13-004 — Document Search and Retrieval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-004 |
| **Feature Name** | Document Search and Retrieval |
| **Module** | 13 — Document Management System (DMS) |

### Description
Authorised user searches metadata they are allowed to see, opens/downloads current version; search itself is logged.

### Business Objective
Find evidence without bypassing ACL.

### Actors
User: Any Person with view on some documents. Auditor: read-only history.

### User Journey
1. Who creates: Any Person with view on some documents.
2. How they create: Opens DMS search: type, parent, date, text, Search. Results respect F13-003.
3. How they edit: Not a record-create. Saved filters optional Save as my filter.
4. How they send for approval: Not approval.
5. How the approver sees pending items: None.
6. How the approver decides: Not applicable.
7. How the user sees history: User sees recent searches if enabled; auditor sees search log.
8. How the supervisor / auditor sees history: Auditor search log.

### Functional Capabilities
- Authorised user creates, edits and searches document search records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Document search register | Medium |
| Document search form (create and edit) | Complex |
| Document search history | Medium |
| Search form and results | Complex |
| Saved filters | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create document search | Medium |
| Update document search | Medium |
| Search document search | Medium |
| Read document search history | Easy |
| Search metadata | Complex |
| Retrieve current file | Easy |

### Inputs
Filters: type, module, date, name.

### Outputs
Persisted document search; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- At least one filter if required by policy.

### Calculations
None.

### Workflow
Not approval.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Retrieved files.

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
| Document search register | UI | Medium | 6 |
| Document search form (create and edit) | UI | Complex | 12 |
| Document search history | UI | Medium | 6 |
| Search form and results | UI | Complex | 12 |
| Saved filters | UI | Easy | 4 |
| Create document search | API | Medium | 6 |
| Update document search | API | Medium | 6 |
| Search document search | API | Medium | 6 |
| Read document search history | API | Easy | 4 |
| Search metadata | API | Complex | 8 |
| Retrieve current file | API | Easy | 4 |
| Document search record and history | DB | Medium | 4 |
| Internal identity/document hooks for document search | Integration | Simple | 4 |
| Document Search and Retrieval feature tests | Testing | Complex | 8 |
| Document Search and Retrieval implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **93** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
