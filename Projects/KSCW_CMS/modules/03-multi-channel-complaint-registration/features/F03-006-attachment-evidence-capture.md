# F03-006 — Attachment / Evidence Capture

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-006 |
| Feature Name | Attachment / Evidence Capture |
| Module | 03 — Multi-Channel Complaint Registration |
| Description | Upload and link supporting documents/media to a complaint as configured. |
| Business Objective | Preserve evidence with the complaint record. |
| Actors | Complainant; Operator |

### User Journey

- User selects files during/after intake → uploads within size/type limits → files linked to complaint.

### Functional Capabilities

- File upload UI on intake channels
- Link/list/remove (pre-submit) attachments
- Enforce type/size limits from parameters

### Inputs

- Files
- Complaint ID
- File metadata

### Outputs

- Stored attachments linked to complaint

### Business Rules

- Limits from Module 02 parameters
- Malware/type checks per FRS

### Validations

- Allowed MIME/types
- Max size/count

### Calculations

- None

### Workflow

- Select → validate → store → link

### Search Requirements

- List attachments on complaint detail

### Documents

- Complaint evidence files

### Reports

- None

### Notifications

- None

### Security

- Authorized access only; storage isolation

### Integrations

- Object/file storage as platform provides

### Dependencies

- F02-005
- F03-001–F03-004

### Assumptions

- Infrastructure storage available from KSCW

### Risks

- Large media volumes drive storage cost (ops, not feature hours)

### Non Functional Requirements

- Reliable upload with progress/error handling

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Attachment upload and evidence list controls | Medium | 6 |
| API | Upload, link, list, delete (pre-submit) attachments | Complex | 8 |
| Database | Attachment metadata and complaint link | Medium | 4 |
| Testing | Size/type limit and multi-file cases | Complex | 8 |
| Documentation | Attachment capture notes | Easy | 2 |

**Feature Total: 28 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
