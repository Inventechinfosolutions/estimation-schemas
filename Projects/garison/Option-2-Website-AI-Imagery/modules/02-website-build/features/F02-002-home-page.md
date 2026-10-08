# F02-002 — Home Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-002 |
| Feature Name | Home Page |
| Module | 02 — Website Build |
| Module Type | Business |
| Release | Go-live |

### Description
New home page: hero banner, product range highlights linking into the catalogue, company introduction and value proposition, featured moulding categories and a call-to-action strip for enquiries.

### Business Objective
Make a strong first impression and route visitors quickly to products or enquiries.

### Actors
- Visitor

### User Journey
1. **Who creates:** The page is built from content files and the catalogue dataset; no Garrison user edits it in-system.
2. **How they create:** Developers build the sections; visitors land on the page from search or direct visits.
3. **How they edit:** Copy and featured items are changed by a developer.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the pages on staging during user acceptance testing (F05-005).

### Functional Capabilities
- Hero banner
- Product range highlights
- Company introduction
- Featured moulding categories
- Enquiry call-to-action

### UI Screens
- Hero banner section
- Product range highlight section
- Company introduction and value proposition section
- Featured mouldings section
- Call-to-action and contact strip

### Logical API Operations
- Get featured categories and products for home page

### Inputs
- Home page copy and images
- Featured category list

### Outputs
- Home page

### Business Rules
- Featured categories link only to categories with products

### Validations
- Images have alt text

### Calculations
- None

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
- F04-005

### Assumptions
- Garrison supplies or approves home page copy; hero imagery from Garrison photos or licensed stock

### Risks
- Lack of quality photography weakens the design

### Non Functional Requirements
- Largest content element renders within 2.5 seconds on mobile

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Hero banner section | Medium | 6 |
| UI | Product range highlight section | Medium | 6 |
| UI | Company introduction and value proposition section | Easy | 4 |
| UI | Featured mouldings section | Easy | 4 |
| UI | Call-to-action and contact strip | Simple | 2 |
| API | Get featured categories and products for home page | Easy | 4 |
| Testing | Home page layout and content checks | Easy | 4 |
| Documentation | Home page content notes | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 4 | 0 | 0 | 4 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Section-level UI rows
- No external integration channel in this feature; Integration row omitted.
