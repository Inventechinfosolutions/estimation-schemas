# F08-004 — Combination Detail Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-004 |
| Feature Name | Combination Detail Page |
| Module | 08 — Public Catalogue Experience |
| Module Type | Business |
| Release | Go-live |

### Description
Public combination page showing the assembly image and drawing, overall dimensions, description, component list with thumbnails, roles and links to each component's product page, interactive highlight of components on the assembly image, documents and Request Information action.

### Business Objective
Show coordinated trim assemblies and make every component easy to find and enquire about.

### Actors
- Visitor

### User Journey
1. **Who creates:** Combination pages are generated automatically when combinations are Published; content is created in Module 05.
2. **How they create:** Administrators maintain content through the combination workspace.
3. **How they edit:** Edits go live after republication.
4. **How they send for approval:** The page has no approval; content is approved before publication.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors view the page; no visitor history.
8. **How the approver / auditor sees history:** Auditors see combination publication history.

### Functional Capabilities
- Assembly image and drawing viewer
- Overall dimensions and description
- Component list with role, thumbnail, code, name and link
- Interactive highlight: hovering or tapping a component highlights its list entry and assembly position label
- Documents and Request Information action

### UI Screens
- Combination detail page
- Component list with links and thumbnails
- Interactive component highlight

### Logical API Operations
- Get published combination aggregate
- Get component product summaries

### Inputs
- Combination slug/code

### Outputs
- Public combination page

### Business Rules
- Only Published combinations shown
- Component links go to Published product pages only

### Validations
- Unknown codes redirect per F11-001

### Calculations
- Dimension display formatting

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- Combination PDFs

### Reports
- Views tracked (F11-004)

### Notifications
- None

### Security
- Public read-only

### Integrations
- None

### Dependencies
- F05-002
- F05-003
- F08-005
- F10-001

### Assumptions
- Component positions are labelled using order and role, not pixel-mapped hotspots

### Risks
- Pixel-accurate hotspot mapping would require extra admin tooling (not included)

### Non Functional Requirements
- Same performance targets as product pages

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Combination detail page | Complex | 12 |
| UI | Component list with links and thumbnails | Medium | 6 |
| UI | Interactive component highlight | Complex | 12 |
| API | Get published combination aggregate | Complex | 8 |
| API | Get component product summaries | Easy | 4 |
| Database | Combination read model | Easy | 2 |
| Testing | Component links and unpublished component handling | Medium | 6 |
| Testing | Responsive assembly display | Easy | 4 |
| Documentation | Combination page notes | Simple | 1 |

**Feature Total: 55 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 12 | 2 | 0 | 10 | 1 | **55** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Interactive highlight is the main Complex driver
- No external integration channel in this feature; Integration row omitted.
