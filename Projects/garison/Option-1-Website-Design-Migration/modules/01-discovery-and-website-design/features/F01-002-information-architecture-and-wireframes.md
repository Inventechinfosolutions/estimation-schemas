# F01-002 — Information Architecture & Wireframes

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-002 |
| Feature Name | Information Architecture & Wireframes |
| Module | 01 — Discovery & Website Design |
| Module Type | Business |
| Release | Go-live |

### Description
New sitemap and navigation model covering the company pages and the product catalogue. Low-fidelity wireframes are produced for every page template (home, content page, catalogue landing, category listing with filters, product detail, search results, contact), including mobile navigation and the mobile filter drawer.

### Business Objective
Agree the structure and page layouts before visual design, so design and build are not reworked.

### Actors
- Delivery designer
- Garrison business owner

### User Journey
1. **Who creates:** The delivery designer creates the sitemap and wireframes.
2. **How they create:** They draft the sitemap and template wireframes in the design tool and walk Garrison through them.
3. **How they edit:** Wireframes are revised after Garrison's feedback (up to two rounds).
4. **How they send for approval:** The wireframe set is shared by link for Garrison's approval.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's approval email freezes the information architecture.
7. **How the maker sees history:** Garrison sees the version history in the design tool.
8. **How the approver / auditor sees history:** The delivery lead keeps the approved wireframe version and approval email.

### Functional Capabilities
- Sitemap and navigation model
- Wireframes for each page template
- Mobile navigation and filter patterns
- Catalogue hierarchy: mouldings → category → product
- Two feedback rounds

### UI Screens
- Sitemap and navigation model
- Home page wireframe
- Content page wireframe
- Catalogue landing and category listing wireframes
- Product detail and search results wireframes
- Contact page wireframe
- Mobile navigation and filter drawer wireframes

### Logical API Operations
- None (no application operations in this feature)

### Inputs
- Confirmed page list (F01-001)
- Product catalogue structure (F04-003)

### Outputs
- Approved sitemap
- Approved wireframes

### Business Rules
- Every confirmed page maps to a template
- Product catalogue reachable within two clicks of the home page

### Validations
- All templates needed by the build are covered by a wireframe

### Calculations
- None

### Workflow
Draft → Walkthrough → Revise → Approved

### Search Requirements
- None

### Documents
- Wireframe set

### Reports
- None

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F01-001

### Assumptions
- Two feedback rounds
- Design tool link shared with Garrison (for example Figma)

### Risks
- Late navigation changes after approval affect design and build

### Non Functional Requirements
- Wireframes cover desktop and mobile breakpoints

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Sitemap and navigation model | Easy | 4 |
| UI | Home page wireframe | Medium | 6 |
| UI | Content page wireframe | Easy | 4 |
| UI | Catalogue landing and category listing wireframes | Medium | 6 |
| UI | Product detail and search results wireframes | Easy | 4 |
| UI | Contact page wireframe | Simple | 2 |
| UI | Mobile navigation and filter drawer wireframes | Easy | 4 |
| Testing | Wireframe walkthrough with Garrison | Easy | 4 |
| Documentation | Information architecture and wireframe notes | Easy | 2 |

**Feature Total: 36 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 0 | 0 | 0 | 4 | 2 | **36** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Design artefacts are sized on the UI scale of the Estimation Master
- No external integration channel in this feature; Integration row omitted.
