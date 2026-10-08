# F08-002 — Category, Style & Collection Listing Pages

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-002 |
| Feature Name | Category, Style & Collection Listing Pages |
| Module | 08 — Public Catalogue Experience |
| Module Type | Business |
| Release | Go-live |

### Description
Public listing pages for categories, sub-categories, styles and collections: introductory SEO text, sub-category chips, product cards (profile drawing, code, name, key dimensions), sort, pagination/load-more, breadcrumbs, faceted filter slot (F09-003) and mobile filter drawer.

### Business Objective
Support discovery-oriented browsing and give each category a strong, SEO-friendly landing page.

### Actors
- Visitor

### User Journey
1. **Who creates:** Listing pages are generated automatically from taxonomy and Published products; administrators create content through F02-001/F02-002.
2. **How they create:** Administrators maintain listing intro text in category, style and collection forms.
3. **How they edit:** Changes to taxonomy or products update listings on publish.
4. **How they send for approval:** Listing pages have no approval; only Published content appears.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors browse listings; there is no visitor history.
8. **How the approver / auditor sees history:** Auditors see underlying taxonomy and publication changes in the audit log.

### Functional Capabilities
- Category and sub-category listing with intro text and chips
- Style and collection listings (collection uses curated order)
- Product card showing drawing, code, name and key dimensions flagged 'show on card' in template
- Sort (featured, code, name, width, height) and pagination or load-more
- Breadcrumbs
- Mobile filter drawer and sort sheet
- Lazy-loaded images

### UI Screens
- Category listing page
- Style listing page
- Collection listing page
- Product card component
- Breadcrumb and pagination components
- Mobile filter drawer and sort sheet

### Logical API Operations
- Get category listing with facets and pagination
- Get style listing
- Get collection listing
- Get breadcrumb trail

### Inputs
- Category/style/collection slug, sort, page, filters

### Outputs
- Listing pages with product cards

### Business Rules
- Only Published products listed
- Card dimensions come from template 'show on card' attributes
- Empty listings show guidance and links to related categories

### Validations
- Unknown slugs return 404 or redirect (F11-001)

### Calculations
- Result counts

### Workflow
Not applicable

### Search Requirements
- Filters via F09-003

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Public read-only

### Integrations
- None

### Dependencies
- F02-001
- F02-002
- F03-002
- F08-005
- F09-003
- F11-001

### Assumptions
- Server-rendered or pre-rendered pages for SEO

### Risks
- Card density with long codes on mobile; resolved in visual design

### Non Functional Requirements
- Listing response under 1 second; images lazy-loaded

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Category listing page | Very High | 16 |
| UI | Style listing page | Complex | 12 |
| UI | Collection listing page | Medium | 6 |
| UI | Product card component | Medium | 6 |
| UI | Breadcrumb and pagination components | Easy | 4 |
| UI | Mobile filter drawer and sort sheet | Complex | 12 |
| API | Get category listing with facets and pagination | Complex | 8 |
| API | Get style listing | Medium | 6 |
| API | Get collection listing | Medium | 6 |
| API | Get breadcrumb trail | Simple | 2 |
| Database | Listing read model and indexes | Easy | 2 |
| Testing | Listing correctness (published only, sort, pagination) | Medium | 6 |
| Testing | Responsive and lazy-load behaviour | Medium | 6 |
| Testing | Listing performance at 10,000 products | Medium | 6 |
| Documentation | Public listing behaviour notes | Simple | 1 |

**Feature Total: 99 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 56 | 22 | 2 | 0 | 18 | 1 | **99** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Category listing integrates facets and is a Very High UI
- No external integration channel in this feature; Integration row omitted.
