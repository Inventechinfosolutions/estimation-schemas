# F02-001 — Site Foundation, Layout & Navigation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-001 |
| Feature Name | Site Foundation, Layout & Navigation |
| Module | 02 — Website Build |
| Module Type | Business |
| Release | Go-live |

### Description
Technical foundation of the new website: a modern statically generated site (for example Astro or Next.js static export) with content held in version-controlled files, responsive layout shell, header with main navigation and mobile menu, footer, reusable UI components built from the design system, and 404/error pages. No administration portal is provided; content is changed by a developer.

### Business Objective
Provide a fast, secure, low-maintenance website base that needs no database or admin login.

### Actors
- Delivery developer
- Visitor

### User Journey
1. **Who creates:** The delivery developer builds the foundation; Garrison does not operate it.
2. **How they create:** They set up the project, build the layout and components from the design handoff, and publish to staging.
3. **How they edit:** Later layout or menu changes are made by a developer in the code and content files.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees changes in the version-control history.
8. **How the approver / auditor sees history:** The delivery lead reviews staging builds and the change history.

### Functional Capabilities
- Static site project and build
- Responsive layout shell
- Header with main navigation and mobile menu
- Footer with contact details and links
- Reusable component set from the design system
- 404 and error pages
- Version-controlled content files

### UI Screens
- Responsive page layout shell
- Header with main navigation and mobile menu
- Footer with contact details and links
- Reusable UI component set
- 404 and error pages

### Logical API Operations
- Static site build and routing setup
- Content source structure for pages and site settings

### Inputs
- Approved designs (F01-003)

### Outputs
- Website foundation on staging

### Business Rules
- No admin portal or database
- All content and settings are held in version control

### Validations
- Build fails if content files are malformed

### Calculations
- None

### Workflow
Build → Staging → Review

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- No server-side login surface; static files served over HTTPS

### Integrations
- None

### Dependencies
- F01-003

### Assumptions
- Static generation suits a catalogue that changes rarely
- Garrison accepts developer-made content changes

### Risks
- If Garrison later wants self-service editing, a content management system or Option 3 is needed

### Non Functional Requirements
- Supports current Chrome, Edge, Safari and Firefox
- Core pages pass mobile usability checks

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Responsive page layout shell | Medium | 6 |
| UI | Header with main navigation and mobile menu | Complex | 12 |
| UI | Footer with contact details and links | Easy | 4 |
| UI | Reusable UI component set | Complex | 12 |
| UI | 404 and error pages | Simple | 2 |
| API | Static site build and routing setup | Medium | 6 |
| API | Content source structure for pages and site settings | Easy | 4 |
| Database | Site content file structure | Easy | 2 |
| Testing | Layout responsiveness and browser checks | Medium | 6 |
| Documentation | Developer setup and content update guide | Medium | 3 |

**Feature Total: 57 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | 10 | 2 | 0 | 6 | 3 | **57** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Static architecture removes admin, role and database effort
- No external integration channel in this feature; Integration row omitted.
