# F01-002 — Product Image Acquisition & Optimisation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-002 |
| Feature Name | Product Image Acquisition & Optimisation |
| Module | 01 — Catalogue Data Extraction & Preparation |
| Module Type | Technical |
| Release | Go-live |

### Description
Download every product image referenced in the raw dataset, verify it, rename it to a Garrison convention (category-code), and generate web derivatives (thumbnail, listing and detail sizes in WebP with JPEG fallback), with an image QA report.

### Business Objective
Provide fast-loading, consistently named product images for the website.

### Actors
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer runs image acquisition after extraction.
2. **How they create:** The script downloads images from the raw dataset, checks file integrity and generates derivatives.
3. **How they edit:** Failed or low-quality images are re-downloaded or flagged for manual sourcing.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees the image QA report.
8. **How the approver / auditor sees history:** The delivery lead and Garrison see image thumbnails in the review workbook (F01-004).

### Functional Capabilities
- Bulk download with checksum and retry
- Renaming to Garrison convention
- Derivatives: thumbnail, listing, detail; WebP plus JPEG fallback
- Image QA report: missing, broken, low resolution

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Download product images with checksum
- Rename images to Garrison convention
- Generate web image derivatives
- Produce image QA report

### Inputs
- Raw dataset image URLs

### Outputs
- Original and optimised images
- Image manifest
- QA report

### Business Rules
- Original files retained unchanged
- Every product has at least a listing and detail derivative

### Validations
- File is a valid image; minimum resolution met

### Calculations
- Derivative sizes preserving aspect ratio

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Image QA report

### Notifications
- None

### Security
- None specific

### Integrations
- None beyond F01-001 source access

### Dependencies
- F01-001

### Assumptions
- One isometric image per product, as observed on the source

### Risks
- Source images are about 541×402 px; no high-resolution zoom is possible

### Non Functional Requirements
- Listing image under 40 KB; detail image under 120 KB

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Download product images with checksum | Medium | 6 |
| API | Rename images to Garrison convention | Easy | 4 |
| API | Generate web image derivatives | Complex | 8 |
| API | Produce image QA report | Easy | 4 |
| Database | Image manifest | Simple | 1 |
| Testing | Image completeness and quality checks | Easy | 4 |
| Documentation | Image naming and size conventions | Simple | 1 |

**Feature Total: 28 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 22 | 1 | 0 | 4 | 1 | **28** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Straightforward batch processing
- No external integration channel in this feature; Integration row omitted.
