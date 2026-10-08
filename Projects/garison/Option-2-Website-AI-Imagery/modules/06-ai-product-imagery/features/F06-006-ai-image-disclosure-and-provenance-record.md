# F06-006 — AI Image Disclosure & Provenance Record

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-006 |
| Feature Name | AI Image Disclosure & Provenance Record |
| Module | 06 — AI Product Imagery |
| Module Type | Technical |
| Release | Go-live |

### Description
Show an 'illustrative image' note on product pages, embed provenance metadata (AI-assisted, model, date) in published image files, and keep a provenance register (product, prompt, model, base render, approver, date) that Garrison receives at handover.

### Business Objective
Be transparent with visitors and keep an evidence trail if image rights or accuracy are ever questioned.

### Actors
- Delivery developer
- Garrison business owner
- Visitor

### User Journey
1. **Who creates:** The delivery developer sets up the disclosure and register.
2. **How they create:** The build adds the note to product pages and metadata to images; the register is exported from the generation log.
3. **How they edit:** Register entries update automatically when images are regenerated.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees the register per build.
8. **How the approver / auditor sees history:** Garrison receives the register at handover.

### Functional Capabilities
- Illustrative image notice
- Provenance metadata in image files
- Provenance register export
- AI content usage note for Garrison

### UI Screens
- Illustrative image notice on product pages

### Logical API Operations
- Embed provenance metadata in image files
- Export provenance register

### Inputs
- Generation log
- Review decisions

### Outputs
- Disclosure on pages
- Provenance register

### Business Rules
- Every AI-assisted image is disclosed and registered

### Validations
- Register entry exists for every published AI image

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- Provenance register

### Reports
- Provenance register

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F06-003
- F06-004

### Assumptions
- Garrison's counsel confirms the disclosure wording

### Risks
- None significant

### Non Functional Requirements
- Metadata does not noticeably increase file size

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Illustrative image notice on product pages | Simple | 2 |
| API | Embed provenance metadata in image files | Easy | 4 |
| API | Export provenance register | Easy | 4 |
| Database | Provenance register | Simple | 1 |
| Testing | Disclosure and metadata checks | Simple | 2 |
| Documentation | AI content usage note for Garrison | Easy | 2 |

**Feature Total: 15 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 1 | 0 | 2 | 2 | **15** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Small compliance feature
- No external integration channel in this feature; Integration row omitted.
