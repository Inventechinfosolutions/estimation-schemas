# F09-002 — Global Keyword, Code & Dimension Search

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-002 |
| Feature Name | Global Keyword, Code & Dimension Search |
| Module | 09 — Search & Filtering |
| Module Type | Business |
| Release | Go-live |

### Description
Global search across code, name, category, style, material, finish, dimension and keywords, with ranking that prioritises exact and prefix code matches, query parsing for dimension phrases (for example '5 inch crown', '3/4 x 5', '2051'), synonym support (for example 'crown' = 'cornice'), and search term logging.

### Business Objective
Support specification-oriented search so contractors and architects find the right profile in one query.

### Actors
- Visitor
- Catalogue Administrator (synonyms)

### User Journey
1. **Who creates:** Visitors create searches; the Catalogue Administrator creates synonym entries.
2. **How they create:** Visitors type in the header search and submit; administrators add synonym groups in the Synonym manager.
3. **How they edit:** Administrators edit or remove synonyms at any time; changes apply after index refresh.
4. **How they send for approval:** No approval applies to searches or synonyms.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors see recent searches in their browser (local only); administrators see synonym history.
8. **How the approver / auditor sees history:** Auditors see synonym changes in the audit log; search terms and zero-result terms are reported in F11-004.

### Functional Capabilities
- Header search box on all catalogue pages
- Ranking: exact code, code prefix, name, category/style, attributes, description
- Dimension phrase parsing using the shared parser (F03-004) with tolerance matching
- Category inference from query terms (for example 'crown')
- Synonym groups
- Search term and zero-result logging

### UI Screens
- Header search box
- Search results page
- Synonym manager

### Logical API Operations
- Execute ranked catalogue search
- Parse query for dimensions, units and categories
- Maintain synonym groups
- Log search terms and zero results

### Inputs
- Query text
- Synonym groups
- Dimension tolerance (default ±1/8 inch for search)

### Outputs
- Ranked results (products and combinations)
- Search logs

### Business Rules
- Exact code match always ranks first
- Dimension phrases match products whose relevant dimension is within tolerance
- Only Published content returned

### Validations
- Query length 1–100 characters; special characters escaped

### Calculations
- Tolerance window around parsed dimension values

### Workflow
Not applicable

### Search Requirements
- This feature is the search capability

### Documents
- None

### Reports
- Top and zero-result searches (F11-004)

### Notifications
- None

### Security
- Rate limited (F13-002); no personal data logged with search terms

### Integrations
- Search engine (via F09-001)

### Dependencies
- F09-001
- F03-004
- F09-004
- F11-004

### Assumptions
- Exact search behaviour (ranking weights, tolerance) refined during UX design

### Risks
- Ambiguous dimension phrases (which dimension is '5 inch'); resolved by category-specific primary dimension setting

### Non Functional Requirements
- Search response under 500 ms at 10,000 products

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Header search box | Easy | 4 |
| UI | Search results page | Complex | 12 |
| UI | Synonym manager | Medium | 6 |
| API | Execute ranked catalogue search | Very High | 16 |
| API | Parse query for dimensions, units and categories | Complex | 8 |
| API | Maintain synonym groups | Easy | 4 |
| API | Log search terms and zero results | Easy | 4 |
| Database | Synonym groups | Simple | 1 |
| Database | Search term log | Easy | 2 |
| Testing | Ranking and code search cases | Complex | 8 |
| Testing | Dimension phrase parsing cases | Complex | 8 |
| Testing | Synonym effectiveness | Easy | 4 |
| Documentation | Search behaviour reference | Easy | 2 |

**Feature Total: 79 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 32 | 3 | 0 | 20 | 2 | **79** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Ranked search with query parsing is a Very High API
- No external integration channel in this feature; Integration row omitted.
