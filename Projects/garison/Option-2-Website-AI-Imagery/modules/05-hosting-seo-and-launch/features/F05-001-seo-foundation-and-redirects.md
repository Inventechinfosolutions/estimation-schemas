# F05-001 — SEO Foundation & Redirects

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-001 |
| Feature Name | SEO Foundation & Redirects |
| Module | 05 — Hosting, SEO & Launch |
| Module Type | Shared |
| Release | Go-live |

### Description
SEO-friendly URLs (for example /mouldings/crown/507), template-driven titles and meta descriptions, XML sitemap and robots file, product and organisation structured data, Open Graph tags, and 301 redirects from every current URL in the discovery inventory to its new page.

### Business Objective
Make the new pages discoverable and keep existing search rankings and links working after the redesign.

### Actors
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer configures URLs, metadata, sitemap and redirects.
2. **How they create:** Metadata is generated from templates and data; redirects are generated from the current URL list (F01-001).
3. **How they edit:** Template wording and redirect changes are made by a developer.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees SEO check results per build.
8. **How the approver / auditor sees history:** Garrison reviews sample titles during user acceptance testing.

### Functional Capabilities
- Clean URLs
- Template-driven titles and meta descriptions
- XML sitemap and robots
- Structured data (Product, Organization, LocalBusiness)
- Open Graph tags
- 301 redirects from current URLs

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Route SEO-friendly URLs
- Generate titles and meta descriptions
- Generate sitemap and robots file
- Generate structured data
- Generate 301 redirects from current URL map

### Inputs
- Catalogue dataset
- Current URL list

### Outputs
- SEO-ready pages
- Redirect rules

### Business Rules
- Unique title per page
- Every current URL redirects to the closest new page

### Validations
- Sitemap validates
- No redirect chains or loops

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
- F01-001
- F03-003
- F05-002

### Assumptions
- Search console access is created or transferred by Garrison

### Risks
- Product data duplicated from the source catalogue gives limited SEO value; Garrison wording helps

### Non Functional Requirements
- No broken links after go-live

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Route SEO-friendly URLs | Medium | 6 |
| API | Generate titles and meta descriptions | Easy | 4 |
| API | Generate sitemap and robots file | Easy | 4 |
| API | Generate structured data | Easy | 4 |
| API | Generate 301 redirects from current URL map | Medium | 6 |
| Testing | SEO checks on URLs, titles, sitemap and redirects | Easy | 4 |
| Documentation | SEO notes | Simple | 1 |

**Feature Total: 29 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 24 | 0 | 0 | 4 | 1 | **29** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Standard SEO tasks; no UI effort
- No external integration channel in this feature; Integration row omitted.
