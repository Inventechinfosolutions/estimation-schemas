# F04-001 — Asset upload & metadata

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-001 |
| Feature Name | Asset upload & metadata |
| Module | 04 — Creative Asset Inventory |
| Description | Upload creatives and capture channel, format, language, validity, and ownership metadata linked to campaigns. |
| Business Objective | Build the authoritative creative repository DIPR uses to compare approved artwork against field PoD evidence. |
| Actors | Asset Manager; Campaign Officer |

### User Journey

- User opens Asset upload wizard → selects campaign → drops image/video/document → enters metadata (channel, format, language, valid-from/to, owner) → upload completes with scan status → asset appears in inventory pending versioning designation (F04-002).

### Functional Capabilities

- Multi-file upload with progress and size/type validation
- Metadata form aligned to print/digital/outdoor channel needs
- Campaign linkage mandatory for advertisement creatives
- Ownership and department fields for DIPR accountability
- Upload status including platform virus-scan result display

### Inputs

- Files, campaign reference, channel, format, language, validity dates, ownership, description tags

### Outputs

- Stored creative blob with metadata record

### Business Rules

- Allowed MIME types configured per channel
- Expired validity flagged on search but not auto-deleted
- Vendor-uploaded assets limited to assigned campaigns (F03-005)

### Validations

- Mandatory campaign, channel, and title; validity end after start

### Calculations

- None

### Workflow

- Upload → metadata saved → available for versioning (F04-002)

### Search Requirements

- Immediate find by campaign and title post-upload

### Documents

- Creative files as primary artefacts

### Reports

- None

### Notifications

- Optional notify campaign officer on new asset (Module 08)

### Security

- Upload permission distinct from preview/download (F04-005)

### Integrations

- Internal storage service embedded in module

### Dependencies

- F03-001, F02-001 lookups, F01 permissions

### Assumptions

- Maximum file sizes defined with DIPR in Phase 1

### Risks

- Large video creatives impact storage and upload UX on slow links

### Non Functional Requirements

- Resumable or chunked upload for large outdoor video assets

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Creative asset upload drop zone with progress | Medium | 6 |
| UI | Asset metadata form (campaign, channel, language) | Medium | 6 |
| UI | File type and size validation messages | Simple | 2 |
| UI | Bulk upload queue panel | Medium | 6 |
| UI | Upload failure retry list | Easy | 4 |
| UI | Asset thumbnail preview strip | Easy | 4 |
| API | Initiate multipart creative upload | Medium | 6 |
| API | Complete upload and persist metadata | Complex | 8 |
| API | List upload job status | Easy | 4 |
| API | Validate MIME type and size limits | Medium | 6 |
| API | Link uploaded asset to campaign | Easy | 4 |
| Database | Asset binary storage pointer | Easy | 2 |
| Database | Asset metadata entity | Medium | 4 |
| Database | Upload job queue record | Easy | 2 |
| Testing | Happy path for image/PDF/video types | Medium | 6 |
| Testing | Oversize and invalid MIME rejected | Medium | 6 |
| Testing | Bulk partial failure recovery | Easy | 4 |
| Documentation | Creative asset upload operator guide | Easy | 2 |

**Feature Total: 82 hours**

### Estimation Assumptions

- Full enterprise DAM taxonomy not in scope; metadata set matches SOW.
