# F02-003 — Company & Service Content Pages

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-003 |
| Feature Name | Company & Service Content Pages |
| Module | 02 — Website Build |
| Module Type | Business |
| Release | Go-live |

### Description
Templates for Garrison's company pages: About, Products & Services overview (covering lines beyond mouldings), Projects/Gallery with lightbox, generic content page (for example FAQ, delivery information, privacy and terms) and a location and opening hours block with map.

### Business Objective
Present Garrison's business and services clearly in the new design.

### Actors
- Visitor

### User Journey
1. **Who creates:** Pages are built from content files; no Garrison user edits them in-system.
2. **How they create:** Developers build templates and populate them with the migrated content (F02-005).
3. **How they edit:** Text changes are made by a developer.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the pages on staging during user acceptance testing (F05-005).

### Functional Capabilities
- About page
- Products & Services overview
- Projects/Gallery with lightbox
- Generic content page template
- Location, hours and map

### UI Screens
- About page template
- Products and services overview template
- Projects / gallery page with lightbox
- Generic content page template (FAQ, policies)
- Location and opening hours block with map

### Logical API Operations
- Render content pages from content files

### Inputs
- Captured and new content

### Outputs
- Company and service pages

### Business Rules
- Privacy and terms text supplied or approved by Garrison

### Validations
- All internal links resolve

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F02-001
- F02-005

### Assumptions
- About 15 pages in total share these templates

### Risks
- Missing legal page text delays go-live

### Non Functional Requirements
- Gallery images lazy-loaded

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | About page template | Medium | 6 |
| UI | Products and services overview template | Medium | 6 |
| UI | Projects / gallery page with lightbox | Medium | 6 |
| UI | Generic content page template (FAQ, policies) | Easy | 4 |
| UI | Location and opening hours block with map | Easy | 4 |
| API | Render content pages from content files | Easy | 4 |
| Testing | Content page checks | Easy | 4 |
| Documentation | Content page notes | Simple | 1 |

**Feature Total: 35 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 4 | 0 | 0 | 4 | 1 | **35** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Templates are reused across pages; per-page population is the volume line in F02-005
- No external integration channel in this feature; Integration row omitted.
