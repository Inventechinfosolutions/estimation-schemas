# F03-003 — Product Detail Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-003 |
| Feature Name | Product Detail Page |
| Module | 03 — Catalogue Pages on Existing Website |
| Module Type | Business |
| Release | Go-live |

### Description
Product page with image (with zoom/lightbox), code, category, style, thickness and width (fraction display), species options, similar products (same category, close dimensions), breadcrumbs and a Request Information button.

### Business Objective
Show each profile's key facts and lead visitors to enquire.

### Actors
- Visitor

### User Journey
1. **Who creates:** Pages are generated from the loaded dataset.
2. **How they create:** Developers build the template; visitors open products from listings or search.
3. **How they edit:** Content changes through dataset reloads only.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves sample pages on staging during UAT.

### Functional Capabilities
- Image with lightbox
- Facts table (code, category, style, thickness, width, species)
- Similar products
- Breadcrumbs
- Request Information button

### UI Screens
- Product detail page
- Image lightbox
- Similar products block
- Breadcrumbs
- Request Information button

### Logical API Operations
- Get product by code
- Get similar products

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
- Public read-only

### Integrations
- None

### Dependencies
- F02-001
- F03-005
- F04-003

### Assumptions
- No descriptions, drawings or PDFs (not in source data)

### Risks
- Thin content may limit SEO value; Garrison can add text later via developer

### Non Functional Requirements
- Page loads in under 2 seconds on 4G

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Product detail page | Complex | 12 |
| UI | Image lightbox | Easy | 4 |
| UI | Similar products block | Medium | 6 |
| UI | Breadcrumbs | Simple | 2 |
| UI | Request Information button | Simple | 2 |
| API | Get product by code | Easy | 4 |
| API | Get similar products | Medium | 6 |
| Testing | Detail page accuracy on a product sample | Medium | 6 |
| Testing | Responsive checks | Easy | 4 |
| Documentation | Product page notes | Simple | 1 |

**Feature Total: 47 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 10 | 0 | 0 | 10 | 1 | **47** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Single-template detail page with a similarity query
- No external integration channel in this feature; Integration row omitted.
