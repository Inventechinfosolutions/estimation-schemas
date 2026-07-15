# F03-003 — Layout Documents & Photographs
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Layout Documents & Photographs |
| **Module** | 03 — Layout Management |
### Description
Attach, view, replace/version, and retrieve plans, photographs, GOs, acquisition papers, survey sketches, and GIS references within a layout record.
### Business Objective
Keep layout evidence with its business record.
### Actors
Town Planning Officer; Engineering Section; authorised approver; Auditor.
### User Journey
User selects a layout, uploads a typed file/photo, adds remarks, views permitted attachments, and replaces a file with retained history where allowed.
### Functional Capabilities
Typed upload, list/view/download, replacement history, role-based access, and audit.
### Inputs
Layout reference, document type, file/photo, remarks.
### Outputs
Embedded attachment, retrieval view, attachment history.
### Business Rules
Attachments remain linked to the layout; document access follows role/scope; no separate DMS feature.
### Validations
Valid layout/type; configured file constraints; mandatory documents where configured.
### Calculations
None.
### Workflow
Documents travel with layout creation/amendment/publish workflow where relevant.
### Search Requirements
Layout, document type, upload date, uploader.
### Documents
Approved plans, photos, GOs, acquisition papers, survey sketches, GIS references.
### Reports
Layout document register.
### Notifications
Optional workflow/document replacement alert.
### Security
Document ACL, upload audit, controlled download.
### Integrations
Internal document storage service (Simple).
### Dependencies
F02-003 document types; F03-001; F03-004 as applicable.
### Assumptions
Physical scanning is BDA responsibility.
### Risks
Large or poor-quality files may affect upload and storage.
### Non Functional Requirements
Secure upload/download; responsive retrieval; audit trail.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Attachment list and retrieval | UI | Complex | 8 |
| Upload/replace dialog | UI | Complex | 8 |
| Attachment lifecycle operations | API | Complex | 8 |
| Attachment metadata persistence | Database | Complex | 6 |
| Internal document storage handoff | Integration | Simple | 4 |
| Attachment and access tests | Testing | Very High | 12 |
| Document handling guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Document-type configuration is F02-003; no standalone DMS is included.
