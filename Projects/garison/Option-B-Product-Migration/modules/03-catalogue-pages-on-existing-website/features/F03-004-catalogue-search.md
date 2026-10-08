# F03-004 — Catalogue Search

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-004 |
| Feature Name | Catalogue Search |
| Module | 03 — Catalogue Pages on Existing Website |
| Module Type | Business |
| Release | Go-live |

### Description
Search box with simple suggestions and a results page, matching product code (exact and prefix), category, style and dimension keywords (for example '5 1/2 crown').

### Business Objective
Let visitors who know a code or size jump straight to the right products.

### Actors
- Visitor

### User Journey
1. **Who creates:** Visitors create searches.
2. **How they create:** Visitors type in the search box and see suggestions or the results page.
3. **How they edit:** Visitors refine their query.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison verifies search cases during UAT.

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
- Rate limiting via existing hosting where available

### Integrations
- None

### Dependencies
- F02-001
- F01-003

### Assumptions
- Database or in-page search is sufficient for about 350 products (no separate search engine)

### Risks
- None significant

### Non Functional Requirements
- Results under 500 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Search box with suggestions | Medium | 6 |
| UI | Search results page | Medium | 6 |
| UI | No-results page | Simple | 2 |
| API | Search by code, category, style and dimensions | Complex | 8 |
| Database | Search index | Easy | 2 |
| Testing | Search cases for codes and dimension phrases | Medium | 6 |
| Documentation | Search behaviour notes | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 8 | 2 | 0 | 6 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Simple search without a dedicated search engine
- No external integration channel in this feature; Integration row omitted.
