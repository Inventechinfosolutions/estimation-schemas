# F03-001 — Mouldings Landing Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-001 |
| Feature Name | Mouldings Landing Page |
| Module | 03 — Catalogue Pages on Existing Website |
| Module Type | Business |
| Release | Go-live |

### Description
Replacement for the current mouldings page: introduction, category tiles (image and product count), style shortcuts and a catalogue search box, built in the existing theme.

### Business Objective
Give visitors a clear entry point into the moulding range from the main navigation.

### Actors
- Visitor

### User Journey
1. **Who creates:** The page is generated from the loaded dataset; no Garrison user creates content in-system.
2. **How they create:** Developers build the template; tiles appear for each category with products.
3. **How they edit:** Intro text changes are made by a developer.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the page on staging during UAT.

### Functional Capabilities
- Intro section
- Category tiles with counts
- Style shortcuts
- Search entry

### UI Screens
- Mouldings landing page
- Category tile component

### Logical API Operations
- Get categories with product counts

### Inputs
- Loaded categories

### Outputs
- Landing page

### Business Rules
- Categories with no products are hidden

### Validations
- None

### Calculations
- Product counts per category

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
- Public read-only

### Integrations
- None

### Dependencies
- F02-001
- F04-002

### Assumptions
- Category tile images use a representative product image

### Risks
- None significant

### Non Functional Requirements
- Loads quickly on mobile

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Mouldings landing page | Medium | 6 |
| UI | Category tile component | Easy | 4 |
| API | Get categories with product counts | Easy | 4 |
| Testing | Landing page layout and responsiveness | Easy | 4 |
| Documentation | Page content notes | Simple | 1 |

**Feature Total: 19 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 4 | 0 | 0 | 4 | 1 | **19** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Simple template within the existing theme
- No external integration channel in this feature; Integration row omitted.
