# F04-002 — Reference Image Capture (Internal Use Only)

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-002 |
| Feature Name | Reference Image Capture (Internal Use Only) |
| Module | 04 — One-time Product Data Migration |
| Module Type | Technical |
| Release | Go-live |

### Description
Download the source product images solely as internal references for profile silhouette preparation (F06-002). The images are stored privately, linked to each product record and never published on the Garrison website.

### Business Objective
Give the imagery team an accurate visual reference for each profile without publishing Brenlo's photographs.

### Actors
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer captures reference images after extraction.
2. **How they create:** The script downloads images to private storage and links them to product records.
3. **How they edit:** Missing references are re-fetched or flagged for Garrison to supply a sample or drawing.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees the reference capture log.
8. **How the approver / auditor sees history:** The delivery lead checks that no reference image is placed in the website build.

### Functional Capabilities
- Private reference download with checksum
- Link reference to product record
- Missing-reference report
- Build check that blocks reference images from publication

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Download reference images to private storage
- Link references and report gaps

### Inputs
- Raw dataset image references

### Outputs
- Private reference set
- Gap report

### Business Rules
- Reference images are never published or shipped in the website build
- Reference set deleted at project close unless Garrison instructs otherwise

### Validations
- Every product has a reference or a flagged gap

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Reference gap report

### Notifications
- None

### Security
- Reference storage restricted to the delivery team

### Integrations
- None beyond F04-001 source access

### Dependencies
- F04-001

### Assumptions
- One reference image per product

### Risks
- Using references to redraw profiles still relies on Brenlo material; see legal notes

### Non Functional Requirements
- None specific

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Download reference images to private storage | Medium | 6 |
| API | Link references and report gaps | Easy | 4 |
| Database | Reference image manifest | Simple | 1 |
| Testing | Publication block check for reference images | Simple | 2 |
| Documentation | Reference handling rules | Simple | 1 |

**Feature Total: 14 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10 | 1 | 0 | 2 | 1 | **14** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Smaller than the publish variant: no web derivatives
- No external integration channel in this feature; Integration row omitted.
