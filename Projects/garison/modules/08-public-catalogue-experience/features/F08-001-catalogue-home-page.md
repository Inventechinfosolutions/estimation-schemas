# F08-001 — Catalogue Home Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-001 |
| Feature Name | Catalogue Home Page |
| Module | 08 — Public Catalogue Experience |
| Module Type | Business |
| Release | Go-live |

### Description
Public catalogue landing page: hero with prominent search, category tiles (image, name, product count), featured products carousel, collections strip and introductory content, with admin-managed home settings.

### Business Objective
Give visitors arriving from the Garrison website an immediate way into the catalogue by category, featured profiles or search.

### Actors
- Visitor
- Catalogue Administrator / Content Administrator (home settings)

### User Journey
1. **Who creates:** The Content Administrator or Catalogue Administrator configures home content (hero text and image, intro, featured product order, collections to show).
2. **How they create:** They edit Home content settings and save; featured products are those flagged Featured (F04-001), ordered here.
3. **How they edit:** They edit settings at any time; changes appear after cache refresh (immediate on save).
4. **How they send for approval:** Home settings do not go through review; only Published products and collections appear.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors see the home page; administrators see setting history.
8. **How the approver / auditor sees history:** Auditors see home setting changes in the audit log.

### Functional Capabilities
- Hero with search box and headline
- Category tiles ordered by category order (F02-001)
- Featured products carousel
- Collections strip
- Home content settings for administrators
- Cached rendering with invalidation on publish

### UI Screens
- Catalogue home page
- Category tiles grid
- Featured products carousel
- Home content settings

### Logical API Operations
- Get home page content aggregate
- Get featured products
- Save home content settings

### Inputs
- Hero headline, intro text, hero image, featured order, collections to show

### Outputs
- Public home page

### Business Rules
- Only Published products and Active categories/collections are shown
- Categories with zero Published products are hidden

### Validations
- Hero image max 5 MB, minimum 1920 px wide

### Calculations
- Published product count per category

### Workflow
Not applicable

### Search Requirements
- Search box hands off to F09-002

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Public read-only; settings require content permission

### Integrations
- None

### Dependencies
- F02-001
- F02-002
- F04-001
- F08-005
- F09-004

### Assumptions
- Final layout follows approved visual design

### Risks
- None significant

### Non Functional Requirements
- Largest contentful paint under 2.5 seconds on 4G

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Catalogue home page | Complex | 12 |
| UI | Category tiles grid | Medium | 6 |
| UI | Featured products carousel | Medium | 6 |
| UI | Home content settings | Medium | 6 |
| API | Get home page content aggregate | Medium | 6 |
| API | Get featured products | Easy | 4 |
| API | Save home content settings | Easy | 4 |
| Database | Home content settings | Simple | 1 |
| Testing | Home page responsive layout and content rules | Medium | 6 |
| Testing | Cache invalidation after publish | Easy | 4 |
| Documentation | Home content management guide | Simple | 1 |

**Feature Total: 56 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 14 | 1 | 0 | 10 | 1 | **56** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Standard landing page on shared design system
- No external integration channel in this feature; Integration row omitted.
