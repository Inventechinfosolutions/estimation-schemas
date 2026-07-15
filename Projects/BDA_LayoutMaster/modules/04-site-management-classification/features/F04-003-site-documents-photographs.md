# F04-003 — Site Documents & Photographs
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Site Documents & Photographs |
| **Module** | 04 — Site Management & Classification |
### Description
Embed typed site photographs and supporting documents, including legal and survey evidence.
### Business Objective
Keep site evidence retrievable with the authoritative record.
### Actors
Operational officers; Legal; authorised approvers; Auditor.
### User Journey
User selects site, uploads a typed file/photo, views/downloads permitted material, and replaces files with history where allowed.
### Functional Capabilities
Upload, view, download, replace/version, typed attachment, access control, audit.
### Inputs
Site, document type, file/photo, remarks.
### Outputs
Embedded site attachments and history.
### Business Rules
Files remain with the site; no standalone DMS; document access follows role/scope.
### Validations
Valid site/type; configured file restrictions; mandatory types when configured.
### Calculations
None.
### Workflow
Attachments accompany site and classification actions.
### Search Requirements
Site, type, date, uploader.
### Documents
Khata, survey sketches, court orders, photos, certificates, supporting files.
### Reports
Site document register.
### Notifications
Optional attachment/change alert.
### Security
Document ACL, audit, controlled download.
### Integrations
Internal document storage (Simple).
### Dependencies
F02-003; F04-001; F04-005.
### Assumptions
Scanning physical files is BDA responsibility.
### Risks
File quality/volume can affect storage.
### Non Functional Requirements
Secure attachment handling; responsive retrieval.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Attachment list/retrieval | UI | Complex | 8 |
| Upload/replace interface | UI | Complex | 8 |
| Attachment lifecycle operations | API | Complex | 8 |
| Attachment metadata persistence | Database | Complex | 6 |
| Internal document storage | Integration | Simple | 4 |
| Document/access tests | Testing | Very High | 12 |
| Document guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Document type configuration is F02-003.
