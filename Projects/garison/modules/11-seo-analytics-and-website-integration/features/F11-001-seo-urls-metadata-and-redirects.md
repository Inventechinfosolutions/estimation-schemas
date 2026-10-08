# F11-001 — SEO URLs, Metadata & Redirects

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-001 |
| Feature Name | SEO URLs, Metadata & Redirects |
| Module | 11 — SEO, Analytics & Website Integration |
| Module Type | Shared |
| Release | Go-live |

### Description
SEO-friendly URL scheme (for example /mouldings/crown/CM-001, /mouldings/combinations/CB-010), automatic slug generation, editable page titles and meta descriptions with default patterns, canonical URLs, automatic 301 redirects on slug or category change, and a manual redirect manager.

### Business Objective
Make every catalogue page discoverable and keep search rankings intact as the catalogue evolves.

### Actors
- Content Administrator
- Catalogue Administrator

### User Journey
1. **Who creates:** Content Administrators or Catalogue Administrators maintain SEO fields; slugs and redirects are generated automatically.
2. **How they create:** In the SEO panel of products, categories and combinations they review the generated slug, edit title and meta description, and see a search snippet preview; default patterns are set in SEO settings.
3. **How they edit:** They edit SEO fields at any time; slug changes create redirects automatically; manual redirects are managed in the Redirect manager.
4. **How they send for approval:** Product SEO fields are submitted with the product; category and redirect changes apply on save.
5. **How the approver sees pending items:** Reviewers see product SEO fields in the review workspace; no separate SEO approval.
6. **How the approver decides:** Reviewers approve or request changes with the product.
7. **How the maker sees history:** Makers see SEO change history on the record.
8. **How the approver / auditor sees history:** Auditors see SEO and redirect changes in the audit log.

### Functional Capabilities
- URL scheme by entity type
- Slug generation and uniqueness
- Title and meta description with default patterns (for example '{Name} {Code} | {Category} Moulding | Garrison')
- Snippet preview with length guidance
- Canonical URL handling (filters, pagination)
- Automatic 301 redirects on slug/category change, merge and archive
- Manual redirect manager with chain detection
- Server-side meta tag rendering

### UI Screens
- SEO panel with snippet preview
- SEO default patterns settings
- Redirect manager

### Logical API Operations
- Generate unique slug
- Save SEO metadata
- Create automatic redirect on slug or category change
- Resolve URL to entity or redirect
- Maintain manual redirects
- Render meta tags for public pages

### Inputs
- Slug, title, meta description, canonical override, redirect source/target

### Outputs
- Public URLs, meta tags, redirects

### Business Rules
- Slugs unique per entity type and parent
- Redirect chains collapsed to a single hop
- Archived product URLs redirect to their category page

### Validations
- Title 10–65 characters (warning beyond)
- Meta description 50–160 characters (warning beyond)
- Redirect target must exist

### Calculations
- Character counts for snippet guidance

### Workflow
Edited within product workflow (products); direct save (categories, redirects)

### Search Requirements
- Redirect manager by source/target URL

### Documents
- None

### Reports
- Redirect list export

### Notifications
- None

### Security
- Manage SEO permission (Content Administrator, Catalogue Administrator)

### Integrations
- None

### Dependencies
- F02-001
- F04-001
- F04-006
- F05-002
- F08-002
- F08-003

### Assumptions
- URL prefix (/mouldings) confirmed with website integration method

### Risks
- Integration via sub-domain affects URL strategy; decided at discovery

### Non Functional Requirements
- URL resolution under 50 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | SEO panel with snippet preview | Medium | 6 |
| UI | SEO default patterns settings | Medium | 6 |
| UI | Redirect manager | Complex | 12 |
| API | Generate unique slug | Medium | 6 |
| API | Save SEO metadata | Easy | 4 |
| API | Create automatic redirect on slug or category change | Complex | 8 |
| API | Resolve URL to entity or redirect | Complex | 8 |
| API | Maintain manual redirects | Medium | 6 |
| API | Render meta tags for public pages | Medium | 6 |
| Database | SEO metadata | Easy | 2 |
| Database | Redirect map | Easy | 2 |
| Testing | Slug uniqueness and redirect chains | Medium | 6 |
| Testing | Metadata rendering per page type | Medium | 6 |
| Documentation | SEO management guide | Easy | 2 |

**Feature Total: 80 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | 38 | 4 | 0 | 12 | 2 | **80** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Redirect automation and URL resolution drive Complex API rows
- No external integration channel in this feature; Integration row omitted.
