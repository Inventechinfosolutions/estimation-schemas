# F03-004 — Catalogue Search

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-004 |
| Feature Name | Catalogue Search |
| Module | 03 — Product Catalogue Pages |
| Module Type | Business |
| Release | Go-live |

### Description
Search box with suggestions and a results page, matching product code (exact and prefix), category, style and dimension phrases (for example '5 1/2 crown'), using a pre-built search index loaded in the browser.

### Business Objective
Let visitors who know a code or size go straight to the right products.

### Actors
- Visitor

### User Journey
1. **Who creates:** Visitors create searches.
2. **How they create:** Visitors type in the search box and see suggestions or the results page.
3. **How they edit:** Visitors refine their query.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison verifies agreed search cases during user acceptance testing.

### Functional Capabilities
- Search box with suggestions
- Results page
- No-results page
- Code-first ranking
- Fraction-aware dimension matching

### UI Screens
- Search box with suggestions
- Search results page
- No-results page

### Logical API Operations
- Search by code, category, style and dimensions

### Inputs
- Query text

### Outputs
- Ranked results

### Business Rules
- Exact code match ranks first

### Validations
- Query length limited and escaped

### Calculations
- Dimension tolerance ±1/8 inch

### Workflow
Not applicable

### Search Requirements
- This feature is the search capability

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
- F04-005

### Assumptions
- Browser-side index is sufficient for about 350 products (no search server)

### Risks
- None significant

### Non Functional Requirements
- Results in under 300 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Search box with suggestions | Medium | 6 |
| UI | Search results page | Medium | 6 |
| UI | No-results page | Simple | 2 |
| API | Search by code, category, style and dimensions | Complex | 8 |
| Database | Pre-built search index | Easy | 2 |
| Testing | Search cases for codes and dimension phrases | Medium | 6 |
| Documentation | Search behaviour notes | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 8 | 2 | 0 | 6 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Client-side search; no search engine hosting
- No external integration channel in this feature; Integration row omitted.
