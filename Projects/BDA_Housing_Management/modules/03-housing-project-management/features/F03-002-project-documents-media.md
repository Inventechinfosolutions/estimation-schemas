# F03-002 — Project Documents & Media

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Project Documents & Media |
| **Module** | 03 — Housing Project Management |

### Description
Embed project photographs, brochures, layout plans, and supporting files in the project record.

### Business Objective
Make approved project information retrievable for officers and publication processes.

### Actors
Engineering Section; Housing officers; Approvers; Auditor.

### User Journey
Officer opens a project, uploads or replaces a classified document/media item, adds description/version context, and retrieves it from the project record.

### Functional Capabilities
Upload, list, preview/download where supported, replace/version, classify and remove per permission; project document history.

### Inputs
Project reference, file, document/media type, title, description, version/replacement reason.

### Outputs
Project document set and retrieval links.

### Business Rules
Files are tied to the project; only authorised users change them; published content must follow approval/publish control.

### Validations
Supported type/size; required classification; project must exist; duplicate filename warning.

### Calculations
None.

### Workflow
Upload/replace → record history → available to authorised project views and publication process.

### Search Requirements
Project, document type, title, uploader, date, current/superseded status.

### Documents
Photographs, brochures, layout plans, supporting project documents.

### Reports
Project Document Register export.

### Notifications
Optional notice on document replacement when approval is pending.

### Security
Role-based document access; audit uploads/downloads; secure storage expectation.

### Integrations
Internal document storage handoff (Simple).

### Dependencies
F03-001; F03-003; document type masters.

### Assumptions
Physical scanning and a standalone DMS product are excluded.

### Risks
Large/poorly classified files may delay review.

### Non Functional Requirements
Reliable upload/retrieval; file-size controls; auditability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Project document list and filters | UI | Medium | 6 |
| Project upload/replace panel | UI | Complex | 8 |
| Project document operations | API | Complex | 8 |
| Project document metadata persistence | Database | Medium | 4 |
| Document storage handoff | Integration | Simple | 4 |
| Project document tests | Testing | Complex | 8 |
| Project document guide | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
