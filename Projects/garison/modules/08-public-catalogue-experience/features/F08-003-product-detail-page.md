# F08-003 — Product Detail Page

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-003 |
| Feature Name | Product Detail Page |
| Module | 08 — Public Catalogue Experience |
| Module Type | Business |
| Release | Go-live |

### Description
Public product page combining technical and inspirational content: name, code, category and style; technical drawing viewer with zoom/pan/full-screen; template-driven dimensions table; description; materials and finishes with swatches; available lengths and availability; applications; installed-image gallery; technical document downloads; related products; 'Used in combinations'; and a Request Information action.

### Business Objective
Give customers everything needed to identify and specify a profile on one page, and convert interest into enquiries.

### Actors
- Visitor

### User Journey
1. **Who creates:** Product pages are generated automatically when products are Published (F06-004); content is created by administrators in Module 04.
2. **How they create:** Administrators maintain content through the product workspace.
3. **How they edit:** Edits go live only after republication.
4. **How they send for approval:** The page itself has no approval; content is approved before publication.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Visitors view the page; there is no visitor history.
8. **How the approver / auditor sees history:** Auditors see the publication history of the product in the audit log.

### Functional Capabilities
- Header block: name, code, category, style tags
- Technical drawing viewer (zoom, pan, full-screen, touch gestures, download PNG/PDF where permitted)
- Dimensions table driven by template order and display settings (fraction and optional metric)
- Materials and finishes chips with swatches
- Available lengths, minimum quantity and special-order indicator
- Applications and installed-image gallery with lightbox
- Technical document downloads with tracking
- Related products carousel grouped by type
- Used-in-combinations block
- Sticky Request Information action opening F10-001
- Third-party media suppression where the rights gate requires

### UI Screens
- Product detail page layout
- Technical drawing viewer
- Dimensions table component
- Materials and finishes chips
- Available lengths and availability block
- Application image gallery with lightbox
- Documents download block
- Related products carousel
- Used-in-combinations block
- Request Information sticky action

### Logical API Operations
- Get published product detail aggregate
- Get published related products
- Get combinations using product
- Track document download

### Inputs
- Product slug/code

### Outputs
- Public product page with structured data (F11-002)

### Business Rules
- Only Published snapshot content is shown
- Attributes hidden on detail by template are not shown
- Unpublished related products and combinations are omitted

### Validations
- Unknown or archived product codes redirect per F11-001

### Calculations
- Dimension display formatting (F03-004)

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- Technical PDFs downloadable

### Reports
- Views and downloads tracked (F11-004)

### Notifications
- None

### Security
- Public read-only; internal documents never exposed

### Integrations
- None

### Dependencies
- F04-001 to F04-005
- F05-001
- F05-003
- F07-003
- F08-005
- F10-001
- F11-002

### Assumptions
- Visual design approved before build

### Risks
- Very large drawings; mitigated by derivatives and progressive loading (F13-001)

### Non Functional Requirements
- Page interactive under 3 seconds on 4G; drawing viewer smooth on mobile

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Product detail page layout | Very High | 16 |
| UI | Technical drawing viewer | Complex | 12 |
| UI | Dimensions table component | Medium | 6 |
| UI | Materials and finishes chips | Easy | 4 |
| UI | Available lengths and availability block | Easy | 4 |
| UI | Application image gallery with lightbox | Medium | 6 |
| UI | Documents download block | Easy | 4 |
| UI | Related products carousel | Medium | 6 |
| UI | Used-in-combinations block | Easy | 4 |
| UI | Request Information sticky action | Easy | 4 |
| API | Get published product detail aggregate | Complex | 8 |
| API | Get published related products | Easy | 4 |
| API | Get combinations using product | Easy | 4 |
| API | Track document download | Simple | 2 |
| Database | Published product read model | Medium | 4 |
| Testing | Template-driven display across categories | Complex | 8 |
| Testing | Drawing viewer cross-browser and touch | Medium | 6 |
| Testing | Accessibility of product page | Medium | 6 |
| Documentation | Product page content guide | Easy | 2 |

**Feature Total: 110 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 66 | 18 | 4 | 0 | 20 | 2 | **110** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Rich multi-block page is Very High; drawing viewer is Complex
- No external integration channel in this feature; Integration row omitted.
