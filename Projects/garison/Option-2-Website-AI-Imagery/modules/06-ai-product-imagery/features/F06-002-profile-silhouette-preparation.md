# F06-002 — Profile Silhouette Preparation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-002 |
| Feature Name | Profile Silhouette Preparation |
| Module | 06 — AI Product Imagery |
| Module Type | Technical |
| Release | Go-live |

### Description
Create a clean vector cross-section silhouette for each product, scaled to its published thickness × width. A script extracts edges from the reference (F04-002) or from a Garrison-supplied drawing or sample photo; an operator corrects the outline in an internal workspace and exports SVG. The silhouette controls geometry so generated images show the correct profile.

### Business Objective
Make sure each AI image shows the real profile shape and proportions.

### Actors
- Delivery imagery specialist
- Delivery developer

### User Journey
1. **Who creates:** The delivery imagery specialist prepares silhouettes; Garrison does not operate this.
2. **How they create:** The script proposes an outline per product; the operator corrects it and exports SVG scaled to dimensions.
3. **How they edit:** Silhouettes are corrected if pilot or review shows a mismatch.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The operator sees the silhouette manifest with status per product.
8. **How the approver / auditor sees history:** The delivery lead samples silhouettes for dimension accuracy.

### Functional Capabilities
- Edge-detection outline proposal
- Scaling to thickness × width
- Operator correction workspace
- SVG export
- Silhouette manifest

### UI Screens
- Silhouette correction workspace (internal)

### Logical API Operations
- Edge-detection silhouette extraction from reference
- Scale silhouette to published thickness × width
- Silhouette clean-up and SVG export

### Inputs
- Reference images or Garrison drawings
- Product dimensions

### Outputs
- SVG silhouette per product
- Manifest

### Business Rules
- Aspect ratio matches thickness:width within 3%
- Silhouettes are internal working files

### Validations
- Closed outline; no self-intersections

### Calculations
- Scale factor from published dimensions

### Workflow
Proposed → Corrected → Approved

### Search Requirements
- None

### Documents
- None

### Reports
- Silhouette manifest

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F04-002
- F04-003

### Assumptions
- Per-product operator time is the separate volume line (0.3 h per product)

### Risks
- Low-resolution references make fine details uncertain; Garrison drawings preferred where available
- Redrawing profiles from Brenlo photographs remains a derivative use; see legal notes

### Non Functional Requirements
- Batch outline proposal runs in minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Silhouette correction workspace (internal) | Medium | 6 |
| API | Edge-detection silhouette extraction from reference | Complex | 8 |
| API | Scale silhouette to published thickness × width | Medium | 6 |
| API | Silhouette clean-up and SVG export | Medium | 6 |
| Database | Silhouette asset manifest | Simple | 1 |
| Testing | Silhouette dimension accuracy checks | Medium | 6 |
| Documentation | Silhouette preparation guide | Easy | 2 |

**Feature Total: 35 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 20 | 1 | 0 | 6 | 2 | **35** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Tooling only; per-product operator time is a volume line
- No external integration channel in this feature; Integration row omitted.
