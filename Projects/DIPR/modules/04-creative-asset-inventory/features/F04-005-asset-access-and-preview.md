# F04-005 — Asset access & preview

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-005 |
| Feature Name | Asset access & preview |
| Module | 04 — Creative Asset Inventory |
| Description | Role-based preview and download of assets with access logging for audit. |
| Business Objective | Protect DIPR creative materials while enabling verifiers to compare PoD photos against authorized artwork. |
| Actors | All entitled roles; Auditor (access log read) |

### User Journey

- User opens asset from inventory → inline preview (image/video/PDF) → if entitled, downloads copy → system logs user, timestamp, action → unauthorized user sees access denied with optional watermark on preview-only roles.

### Functional Capabilities

- Inline preview player with format-specific rendering
- Download with entitlement check and optional watermark on preview-tier roles
- Access log register per asset and global access audit slice
- Time-limited download link option for external review (disabled by default policy)
- Side-by-side launch point for PoD verification UI (F05-003)

### Inputs

- Asset ID, user session, action (preview/download)

### Outputs

- Rendered preview stream; download file; access log row

### Business Rules

- Vendor roles may preview only assets for assigned campaigns
- Download may be disabled for highly restricted assets flag
- All downloads logged with immutable timestamp

### Validations

- Session and permission check on every preview/download request

### Calculations

- None

### Workflow

- Request → authorize → serve → log

### Search Requirements

- Access log filter by user, asset, date on asset detail

### Documents

- Downloaded creative files

### Reports

- Access log export via Module 07

### Notifications

- None

### Security

- Least privilege; watermarked preview for sensitive outdoor creatives if configured

### Integrations

- None

### Dependencies

- F04-001 storage; F01-002 read permissions

### Assumptions

- DRM beyond watermark not required in baseline

### Risks

- Screen capture cannot be fully prevented; logging deters misuse

### Non Functional Requirements

- Preview starts within acceptable time for large PDFs/videos via streaming

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Asset detail preview page (image/PDF/video) | Medium | 6 |
| UI | Role-based download button visibility | Easy | 4 |
| UI | Watermarked preview for vendor users | Medium | 6 |
| UI | Internal share link expiry dialog | Easy | 4 |
| UI | Access denied explanation panel | Simple | 2 |
| API | Get asset with RBAC permission check | Medium | 6 |
| API | Stream preview rendition | Medium | 6 |
| API | Log asset view and download audit | Easy | 4 |
| API | Generate time-limited internal share token | Medium | 6 |
| Database | Asset access audit log | Easy | 2 |
| Database | Share token store | Simple | 1 |
| Testing | Vendor cannot download without entitlement | Medium | 6 |
| Testing | Watermark applied on vendor preview | Easy | 4 |
| Testing | Expired share link denied | Easy | 4 |
| Documentation | Asset access policy summary | Easy | 2 |

**Feature Total: 63 hours**

### Estimation Assumptions

- CDN/edge delivery follows platform hosting design in Module 10.
