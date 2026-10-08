# F11-002 — Sitemap, Structured Data & Social Metadata

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-002 |
| Feature Name | Sitemap, Structured Data & Social Metadata |
| Module | 11 — SEO, Analytics & Website Integration |
| Module Type | Shared |
| Release | Go-live |

### Description
Automatically generated XML sitemap (index plus segmented sitemaps for categories, products, combinations, collections) regenerated on publication events; Product and BreadcrumbList structured data (JSON-LD); Open Graph and Twitter card metadata using the primary image or drawing.

### Business Objective
Help search engines crawl and understand the catalogue and make shared product links look professional.

### Actors
- System
- Content Administrator (monitoring)

### User Journey
1. **Who creates:** Sitemaps and structured data are generated automatically by the system from Published content.
2. **How they create:** Publication events trigger sitemap regeneration; structured data and social tags are rendered on each public page.
3. **How they edit:** Content changes are reflected after republication.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox; the Content Administrator sees last generation time on the Sitemap status page.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see sitemap generation log entries.

### Functional Capabilities
- Sitemap index and segmented sitemaps with lastmod
- Regeneration on publish, unpublish, archive and slug change
- Product structured data (name, sku/code, image, description, brand, category)
- Breadcrumb structured data
- Open Graph and Twitter card tags
- Sitemap status page

### UI Screens
- Sitemap status page

### Logical API Operations
- Generate XML sitemap index and segments
- Regenerate sitemap on publication events
- Generate product structured data
- Generate breadcrumb structured data
- Generate social sharing metadata

### Inputs
- Published content, primary images

### Outputs
- sitemap.xml files, JSON-LD blocks, social meta tags

### Business Rules
- Only Published, indexable pages in the sitemap
- No price or availability offers in structured data (catalogue only)

### Validations
- Structured data passes rich results test without errors

### Calculations
- lastmod from publication date

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Sitemap status

### Notifications
- None

### Security
- Public read-only

### Integrations
- None (sitemap submitted through Garrison's search engine webmaster accounts)

### Dependencies
- F06-004
- F11-001
- F08-003
- F08-004

### Assumptions
- Garrison owns search engine webmaster accounts

### Risks
- None significant

### Non Functional Requirements
- Sitemap generation under 2 minutes at 10,000 items

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Sitemap status page | Simple | 2 |
| API | Generate XML sitemap index and segments | Complex | 8 |
| API | Regenerate sitemap on publication events | Medium | 6 |
| API | Generate product structured data | Medium | 6 |
| API | Generate breadcrumb structured data | Easy | 4 |
| API | Generate social sharing metadata | Easy | 4 |
| Database | Sitemap generation log | Simple | 1 |
| Testing | Sitemap validity and structured data validation | Medium | 6 |
| Testing | Social preview checks | Easy | 4 |
| Documentation | SEO technical checklist | Easy | 2 |

**Feature Total: 43 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 28 | 1 | 0 | 10 | 2 | **43** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Segmented sitemap generation is Complex
- No external integration channel in this feature; Integration row omitted.
