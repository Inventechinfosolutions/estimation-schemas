# F04-004 — Product Media & Drawing Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-004 |
| Feature Name | Product Media & Drawing Management |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Typed media management per product: primary image, profile drawing, cross-section/dimension drawing, installed/application images and gallery images; upload with progress, alt text, caption, ordering, primary selection, focal point/crop and third-party rights flag.

### Business Objective
Present both technical drawings and design inspiration, as the existing Garrison catalogue does, with accessible, well-ordered media.

### Actors
- Catalogue Administrator
- Content Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator or Content Administrator adds media to a product.
2. **How they create:** In the Media tab they drag files into typed slots (primary image, profile drawing, dimension drawing, installed, gallery), see upload progress and processing status, and enter alt text and captions.
3. **How they edit:** They reorder, set primary, crop/set focal point, replace or remove media while the product is editable.
4. **How they send for approval:** Media is submitted with the product through Submit for review; a profile drawing (where available) and alt text are checked by completeness rules.
5. **How the approver sees pending items:** Reviewers see the media in the review workspace.
6. **How the approver decides:** Reviewers approve or request changes.
7. **How the maker sees history:** The maker sees media changes in the product history.
8. **How the approver / auditor sees history:** Auditors see media add/replace/remove events in the audit log.

### Functional Capabilities
- Typed media slots with per-type rules (single primary, single profile drawing, many gallery)
- Multi-file drag-and-drop upload with progress and processing status
- Alt text (mandatory for public images), caption, credit
- Reorder and set primary
- Crop / focal point for card thumbnails
- Third-party media flag used by the rights gate (F07-003)
- Replace file while preserving references

### UI Screens
- Media manager with typed slots
- Media upload dialog with progress
- Media detail editor (alt text, caption, rights flag)
- Media reorder and primary selection
- Crop and focal point tool

### Logical API Operations
- Upload media file with validation
- Update media metadata
- Reorder media and set primary
- Replace or delete media with reference check
- Get product media list
- Save crop and focal point

### Inputs
- Image files (JPG, PNG, WebP), drawings (SVG, PNG, PDF), media type, alt text, caption, credit, rights flag, order, focal point

### Outputs
- Media records with derivatives (via F13-001) linked to the product

### Business Rules
- Exactly one primary image per product
- At most one profile drawing per product
- Alt text mandatory for any media shown publicly
- Third-party flagged media blocked from publication unless rights confirmed (F07-003)

### Validations
- Image max 20 MB; drawing max 30 MB
- Minimum image width 1200 px for primary
- Allowed file types only (content-sniffed)

### Calculations
- None (derivatives in F13-001)

### Workflow
Edited within product workflow

### Search Requirements
- None

### Documents
- Technical PDFs handled separately in F04-005

### Reports
- None

### Notifications
- None

### Security
- Manage media permission
- Upload scanning (F13-002)

### Integrations
- Object storage / CDN (shared connector in F13-001)

### Dependencies
- F04-001
- F13-001
- F13-002
- F07-003
- F06-001

### Assumptions
- Garrison supplies drawings in usable digital quality or they are prepared in the population workstream

### Risks
- Low-quality scans from the print catalogue may need redrawing (population cost, not platform)

### Non Functional Requirements
- Uploads up to 30 MB complete reliably on office broadband

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Media manager with typed slots | Very High | 16 |
| UI | Media upload dialog with progress | Medium | 6 |
| UI | Media detail editor (alt text, caption, rights flag) | Medium | 6 |
| UI | Media reorder and primary selection | Easy | 4 |
| UI | Crop and focal point tool | Complex | 12 |
| API | Upload media file with validation | Complex | 8 |
| API | Update media metadata | Easy | 4 |
| API | Reorder media and set primary | Easy | 4 |
| API | Replace or delete media with reference check | Medium | 6 |
| API | Get product media list | Simple | 2 |
| API | Save crop and focal point | Easy | 4 |
| Database | Media asset and product-media link with type and order | Medium | 4 |
| Integration | Media storage service usage through shared storage connector | Simple | 4 |
| Testing | Upload type, size, ordering and primary rules | Medium | 6 |
| Testing | Alt text and accessibility of media | Easy | 4 |
| Testing | Large drawing file handling | Medium | 6 |
| Documentation | Media standards guide (naming, sizes, drawing formats) | Easy | 2 |

**Feature Total: 98 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 44 | 28 | 4 | 4 | 16 | 2 | **98** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Typed slot media manager is a Very High UI
