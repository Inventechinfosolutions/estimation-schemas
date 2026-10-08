# F03-002 — Category Listing Page with Filters

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-002 |
| Feature Name | Category Listing Page with Filters |
| Module | 03 — Catalogue Pages on Existing Website |
| Module Type | Business |
| Release | Go-live |

### Description
Product grid per category showing image, code and thickness × width, with filters for style, thickness, width and species, sort (code, thickness, width) and pagination, plus a mobile filter drawer.

### Business Objective
Let visitors narrow a category to the profile size and style they need.

### Actors
- Visitor

### User Journey
1. **Who creates:** Listings are generated from the loaded dataset.
2. **How they create:** Visitors open a category and apply filters; developers build the templates.
3. **How they edit:** Listing content changes only through dataset reloads.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves listings on staging during UAT.

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
- Get products by category with filters and pagination
- Get filter values with counts

### Inputs
- Category, filters, sort, page

### Outputs
- Filtered product grid

### Business Rules
- Filter values come from loaded data
- Empty results show a clear message and reset option

### Validations
- Unknown filter values ignored safely

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
- Inputs validated and escaped

### Integrations
- None

### Dependencies
- F02-001
- F04-002

### Assumptions
- Thickness and width filters use the distinct fractional values present

### Risks
- Large categories (about 45 products) need pagination on mobile

### Non Functional Requirements
- Listing response under 1 second

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Category listing page | Complex | 12 |
| UI | Filter panel | Complex | 12 |
| UI | Product card | Easy | 4 |
| UI | Mobile filter drawer | Medium | 6 |
| UI | Sort control | Simple | 2 |
| API | Get products by category with filters and pagination | Medium | 6 |
| API | Get filter values with counts | Medium | 6 |
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
