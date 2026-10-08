# F03-001 — Mouldings Landing Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-001 |
| Feature Name | Mouldings Landing Page |
| Module | 03 — Product Catalogue Pages |
| Module Type | Business |
| Release | Go-live |

### Description
Catalogue entry page: introduction, category tiles (image and product count), style shortcuts (Classic, Modern, Transitional, Inspire) and a catalogue search box.

### Business Objective
Give visitors a clear entry point into the moulding range.

### Actors
- Visitor

### User Journey
1. **Who creates:** The page is generated from the catalogue dataset at build time.
2. **How they create:** Developers build the template; tiles appear for each category with products.
3. **How they edit:** Intro text changes are made by a developer.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the pages on staging during user acceptance testing (F05-005).

### Functional Capabilities
- Intro section
- Category tiles with counts
- Style shortcuts
- Search entry

### UI Screens
- Mouldings landing page
- Category tile component
- Style shortcut strip

### Logical API Operations
- Get categories with product counts

### Inputs
- Catalogue dataset

### Outputs
- Landing page

### Business Rules
- Categories with no products are hidden

### Validations
- Every tile links to a valid category page

### Calculations
- Product count per category

### Workflow
Not applicable

### Search Requirements
- Search box hands off to F03-004

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
- F04-005

### Assumptions
- Tile images use a representative product image

### Risks
- None significant

### Non Functional Requirements
- Loads quickly on mobile

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Mouldings landing page | Medium | 6 |
| UI | Category tile component | Easy | 4 |
| UI | Style shortcut strip | Simple | 2 |
| API | Get categories with product counts | Easy | 4 |
| Testing | Landing page layout and responsiveness | Easy | 4 |
| Documentation | Page content notes | Simple | 1 |

**Feature Total: 21 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 4 | 0 | 0 | 4 | 1 | **21** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Simple template generated at build time
- No external integration channel in this feature; Integration row omitted.
