# F04-003 — SEO, Sitemap & Redirects

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-003 |
| Feature Name | SEO, Sitemap & Redirects |
| Module | 04 — Website Integration, SEO & Go-live |
| Module Type | Shared |
| Release | Go-live |

### Description
SEO-friendly catalogue URLs (for example /mouldings/crown/507), page titles and meta descriptions from templates, sitemap entries for all catalogue pages, basic product structured data, and a 301 redirect from the old mouldings page.

### Business Objective
Make the new product pages discoverable and keep existing links working.

### Actors
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer configures URLs, metadata and sitemap generation.
2. **How they create:** Metadata is generated from templates using product data.
3. **How they edit:** Template wording changes are made by a developer.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Garrison reviews sample titles during UAT.

### Functional Capabilities
- Clean URLs
- Template-driven titles and meta descriptions
- Sitemap entries
- Product structured data
- Legacy redirect

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Route SEO-friendly catalogue URLs
- Generate titles and meta descriptions
- Add catalogue pages to sitemap
- Redirect old mouldings page
- Generate product structured data

### Inputs
- Product data, URL pattern

### Outputs
- SEO-ready catalogue pages

### Business Rules
- Unique title per page
- Old mouldings URL returns 301 to the new landing page

### Validations
- Sitemap validates

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
- None specific

### Integrations
- None

### Dependencies
- F02-001
- F03-001
- F03-003

### Assumptions
- Existing site has or can host a sitemap

### Risks
- Duplicate content concerns with source catalogue; Garrison may add its own wording later

### Non Functional Requirements
- No broken links after go-live

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Route SEO-friendly catalogue URLs | Medium | 6 |
| API | Generate titles and meta descriptions | Easy | 4 |
| API | Add catalogue pages to sitemap | Easy | 4 |
| API | Redirect old mouldings page | Simple | 2 |
| API | Generate product structured data | Easy | 4 |
| Testing | SEO checks on URLs, titles, sitemap and redirect | Easy | 4 |
| Documentation | SEO notes | Simple | 1 |

**Feature Total: 25 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 0 | 0 | 4 | 1 | **25** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Standard SEO tasks; no UI effort
- No external integration channel in this feature; Integration row omitted.
