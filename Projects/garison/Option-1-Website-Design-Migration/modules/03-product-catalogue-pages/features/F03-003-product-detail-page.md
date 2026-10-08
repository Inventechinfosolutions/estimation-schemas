# F03-003 — Product Detail Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-003 |
| Feature Name | Product Detail Page |
| Module | 03 — Product Catalogue Pages |
| Module Type | Business |
| Release | Go-live |

### Description
Product page with image and lightbox, code, category, style, thickness and width (fraction display), available species, similar products (same category, close dimensions), breadcrumbs and a Request Information button.

### Business Objective
Show each profile's key facts and lead visitors to enquire.

### Actors
- Visitor

### User Journey
1. **Who creates:** One page per product is generated from the catalogue dataset at build time.
2. **How they create:** Developers build the template; visitors open products from listings or search.
3. **How they edit:** Content changes only through a dataset refresh.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the pages on staging during user acceptance testing (F05-005).

### Functional Capabilities
- Image with lightbox
- Facts table (code, category, style, thickness, width)
- Species options
- Similar products
- Breadcrumbs
- Request Information button

### UI Screens
- Product detail page
- Image lightbox
- Species options block
- Similar products block
- Breadcrumbs

### Logical API Operations
- Get product by category and code
- Compute similar products at build time

### Inputs
- Product URL

### Outputs
- Product page

### Business Rules
- Similar products: same category, thickness within 1/8 inch and width within 1/2 inch, up to 6

### Validations
- Unknown product URLs return a helpful 404 with search

### Calculations
- Dimension similarity window

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
- F03-005
- F04-005
- F05-001

### Assumptions
- No descriptions, drawings or PDFs (not present in the source data)

### Risks
- Thin content limits SEO value; Garrison can supply text later

### Non Functional Requirements
- Page loads in under 2 seconds on 4G

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Product detail page | Complex | 12 |
| UI | Image lightbox | Easy | 4 |
| UI | Species options block | Easy | 4 |
| UI | Similar products block | Medium | 6 |
| UI | Breadcrumbs | Simple | 2 |
| API | Get product by category and code | Easy | 4 |
| API | Compute similar products at build time | Medium | 6 |
| Testing | Detail page accuracy on a product sample | Medium | 6 |
| Testing | Responsive checks | Easy | 4 |
| Documentation | Product page notes | Simple | 1 |

**Feature Total: 49 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 10 | 0 | 0 | 10 | 1 | **49** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Single template generating about 350 pages
- No external integration channel in this feature; Integration row omitted.
