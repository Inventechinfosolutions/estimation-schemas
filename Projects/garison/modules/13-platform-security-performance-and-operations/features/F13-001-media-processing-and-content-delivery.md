# F13-001 — Media Processing & Content Delivery

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-001 |
| Feature Name | Media Processing & Content Delivery |
| Module | 13 — Platform Security, Performance & Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Process uploaded images and drawings into optimised derivatives (thumbnail, card, detail, zoom tiles or large size) in modern formats (WebP/AVIF with JPEG/PNG fallback), rasterise or optimise drawings (SVG sanitise/optimise, PDF first page to image), store in object storage and deliver through CDN with cache headers and purge on change.

### Business Objective
Keep pages fast with large technical drawings and photographs, as the catalogue grows.

### Actors
- System
- Super Administrator (settings)

### User Journey
1. **Who creates:** Derivatives are created automatically by the system whenever media is uploaded or replaced.
2. **How they create:** Uploads queue processing jobs; the Super Administrator configures derivative sizes and quality in Media processing settings.
3. **How they edit:** Changing settings triggers an optional reprocess-all job.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox; the Super Administrator sees processing status and failures on the queue page.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Makers see processing status on each media item.
8. **How the approver / auditor sees history:** Auditors see setting changes and reprocess jobs in the audit log.

### Functional Capabilities
- Derivative generation per media type
- Modern formats with fallback
- SVG sanitisation and optimisation; PDF/scan rasterisation for drawings
- Object storage and CDN delivery with long-lived cache headers and versioned URLs
- CDN purge on replace/delete
- Reprocess-all job
- Processing queue status page

### UI Screens
- Media processing settings
- Media processing queue status

### Logical API Operations
- Generate image derivatives
- Optimise and rasterise drawings
- Apply cache headers and purge CDN on change
- Reprocess all media job

### Inputs
- Uploaded media
- Derivative settings

### Outputs
- Optimised derivatives in storage and CDN URLs

### Business Rules
- Originals retained; derivatives regenerated on demand
- SVGs sanitised to remove scripts before serving

### Validations
- Processing failures flagged on the media item

### Calculations
- Derivative dimensions preserving aspect ratio

### Workflow
Uploaded → Processing → Ready | Failed

### Search Requirements
- Queue status filters

### Documents
- None

### Reports
- Processing failures list

### Notifications
- Alert on repeated processing failures (F13-003)

### Security
- Private originals; public derivatives only for Published content

### Integrations
- Object storage and CDN (aligned with Garrison hosting)

### Dependencies
- F04-004
- F12-002
- F13-002
- F13-003

### Assumptions
- Garrison hosting supports object storage and a CDN, or equivalent is provisioned

### Risks
- Scanned drawings of poor quality; redrawing is population effort

### Non Functional Requirements
- Derivatives ready within 1 minute of upload; product page image weight under 500 KB above the fold

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Media processing settings | Easy | 4 |
| UI | Media processing queue status | Medium | 6 |
| API | Generate image derivatives | Complex | 8 |
| API | Optimise and rasterise drawings | Complex | 8 |
| API | Apply cache headers and purge CDN on change | Medium | 6 |
| API | Reprocess all media job | Complex | 8 |
| Database | Derivative registry | Easy | 2 |
| Integration | Object storage and CDN integration | Medium | 16 |
| Testing | Derivative quality and format fallback | Medium | 6 |
| Testing | Page weight and CDN cache behaviour | Medium | 6 |
| Documentation | Media pipeline runbook | Easy | 2 |

**Feature Total: 72 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 30 | 2 | 16 | 12 | 2 | **72** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Object storage and CDN integration estimated as Medium (auth, mapping, retry)
