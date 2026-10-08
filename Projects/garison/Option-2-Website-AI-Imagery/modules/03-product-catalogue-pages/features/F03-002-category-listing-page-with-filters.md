# F03-002 — Category Listing Page with Filters

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-002 |
| Feature Name | Category Listing Page with Filters |
| Module | 03 — Product Catalogue Pages |
| Module Type | Business |
| Release | Go-live |

### Description
Product grid per category showing image, code and thickness × width, with filters for style, thickness, width and species, sort (code, thickness, width), pagination or load-more, shareable filter URLs and a mobile filter drawer. Filtering runs in the browser against the category's pre-built data file.

### Business Objective
Let visitors narrow a category to the profile size and style they need.

### Actors
- Visitor

### User Journey
1. **Who creates:** Listings are generated from the catalogue dataset at build time.
2. **How they create:** Visitors open a category and apply filters; developers build the templates.
3. **How they edit:** Listing content changes only through a dataset refresh (F04-005).
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the pages on staging during user acceptance testing (F05-005).

### Functional Capabilities
- Product grid with pagination
- Filters: style, thickness, width, species
- Sort
- Mobile filter drawer
- Shareable filter URLs

### UI Screens
- Category listing page
- Filter panel
- Product card
- Mobile filter drawer
- Sort control

### Logical API Operations
- Filter and paginate category products in the browser
- Compute filter values with counts

### Inputs
- Category, filters, sort, page

### Outputs
- Filtered product grid

### Business Rules
- Filter values come only from loaded data
- Empty results show a clear message and a reset option

### Validations
- Unknown filter values in URLs are ignored safely

### Calculations
- Filter counts

### Workflow
Not applicable

### Search Requirements
- Filters combine with category

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Inputs from URLs escaped

### Integrations
- None

### Dependencies
- F02-001
- F04-005

### Assumptions
- Thickness and width filters use the distinct fractional values present

### Risks
- Large categories (about 45 products) need efficient image loading on mobile

### Non Functional Requirements
- Filter updates in under 300 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Category listing page | Complex | 12 |
| UI | Filter panel | Complex | 12 |
| UI | Product card | Easy | 4 |
| UI | Mobile filter drawer | Medium | 6 |
| UI | Sort control | Simple | 2 |
| API | Filter and paginate category products in the browser | Medium | 6 |
| API | Compute filter values with counts | Medium | 6 |
| Testing | Filter combinations and counts | Medium | 6 |
| Testing | Responsive and browser checks | Easy | 4 |
| Documentation | Listing behaviour notes | Simple | 1 |

**Feature Total: 59 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | 12 | 0 | 0 | 10 | 1 | **59** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Filter panel and listing are Complex templates
- No external integration channel in this feature; Integration row omitted.
