# F09-003 — Configurable Faceted Filters

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-003 |
| Feature Name | Configurable Faceted Filters |
| Module | 09 — Search & Filtering |
| Module Type | Business |
| Release | Go-live |

### Description
Faceted filtering driven by template configuration: list facets (category, style, collection, material, finish, application) with counts, and numeric range facets for dimensions (thickness, width, height, projection, diameter) with fraction-friendly buckets or sliders; applied filter chips; shareable filter URLs; admin facet configuration.

### Business Objective
Let visitors narrow results by specification, and let Garrison turn a new attribute into a filter without development.

### Actors
- Visitor
- Catalogue Administrator (facet configuration)

### User Journey
1. **Who creates:** Visitors apply filters; the Catalogue Administrator configures facets.
2. **How they create:** Visitors tick list values or adjust dimension ranges; administrators mark attributes filterable in templates (F03-002) and set order, display type and range buckets in Facet configuration.
3. **How they edit:** Administrators edit facet configuration at any time; changes apply on save.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors share or bookmark filtered URLs; administrators see configuration history.
8. **How the approver / auditor sees history:** Auditors see facet configuration changes in the audit log.

### Functional Capabilities
- List facets with live counts
- Range facets with predefined fractional buckets (for example 1/2", 3/4", 7/8") or slider
- Facets scoped to category (only that category's filterable attributes)
- Applied filter chips and clear-all
- Shareable, SEO-safe filter URLs (filtered pages noindex)
- Facet configuration: order, display type, bucket definitions, collapse default

### UI Screens
- Filter panel with list and range facets
- Applied filter chips and clear-all
- Facet configuration screen

### Logical API Operations
- Compute facets with counts for current query
- Apply filter combinations to results
- Get facet configuration from templates
- Save facet configuration
- Encode and decode filter URL state

### Inputs
- Selected facet values and ranges
- Facet configuration

### Outputs
- Filtered results with facet counts

### Business Rules
- Only attributes flagged filterable in the template appear
- Facet values with zero results hidden (configurable)
- Filtered URLs are noindex with canonical to the unfiltered listing

### Validations
- Range min ≤ max

### Calculations
- Facet counts; range bucket boundaries on canonical values

### Workflow
Not applicable

### Search Requirements
- Combined with keyword search (F09-002)

### Documents
- None

### Reports
- Filter usage (F11-004)

### Notifications
- None

### Security
- Public read-only; configuration requires template permission

### Integrations
- Search engine (via F09-001)

### Dependencies
- F03-002
- F09-001
- F08-002
- F11-001

### Assumptions
- Up to about 12 facets per category

### Risks
- Too many facets on mobile; mobile drawer collapses by default

### Non Functional Requirements
- Facet computation under 500 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Filter panel with list and range facets | Very High | 16 |
| UI | Applied filter chips and clear-all | Easy | 4 |
| UI | Facet configuration screen | Complex | 12 |
| API | Compute facets with counts for current query | Very High | 16 |
| API | Apply filter combinations to results | Complex | 8 |
| API | Get facet configuration from templates | Medium | 6 |
| API | Save facet configuration | Easy | 4 |
| API | Encode and decode filter URL state | Medium | 6 |
| Database | Facet configuration | Easy | 2 |
| Testing | Facet count accuracy and combinations | Complex | 8 |
| Testing | Range filters with fractional values | Medium | 6 |
| Testing | New filterable attribute appears without deployment | Medium | 6 |
| Documentation | Filter configuration guide | Easy | 2 |

**Feature Total: 96 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 40 | 2 | 0 | 20 | 2 | **96** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Facet computation and filter panel are Very High items
- No external integration channel in this feature; Integration row omitted.
