# F01-003 — Visual Design System & Page Designs

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-003 |
| Feature Name | Visual Design System & Page Designs |
| Module | 01 — Discovery & Website Design |
| Module Type | Business |
| Release | Go-live |

### Description
Brand-aligned visual design for the new website: style guide (colour, typography, spacing, iconography, imagery treatment), a UI component library (buttons, cards, product tiles, filters, forms, navigation), and high-fidelity desktop and mobile designs for each template, with a clickable prototype for Garrison review.

### Business Objective
Give Garrison a modern, consistent website design that presents its products professionally.

### Actors
- Delivery designer
- Garrison business owner

### User Journey
1. **Who creates:** The delivery designer creates the style guide, component library and page designs.
2. **How they create:** They design in the design tool from the approved wireframes and publish a clickable prototype.
3. **How they edit:** Designs are revised after Garrison's feedback (up to two rounds).
4. **How they send for approval:** The prototype link is sent to Garrison for approval.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's approval email freezes the designs for build.
7. **How the maker sees history:** Garrison sees design versions in the design tool.
8. **How the approver / auditor sees history:** The delivery lead keeps the approved design version, approval email and handoff specification.

### Functional Capabilities
- Style guide
- Component library
- High-fidelity designs for every template (desktop and mobile)
- Clickable prototype
- Design handoff specification for developers
- Two design review rounds

### UI Screens
- Style guide (colour, typography, spacing, iconography)
- UI component library design
- Home page visual design (desktop and mobile)
- Content page visual design
- Catalogue landing and category listing visual design
- Product detail and search visual design
- Contact and enquiry visual design
- Clickable prototype

### Logical API Operations
- None (no application operations in this feature)

### Inputs
- Approved wireframes (F01-002)
- Brand assets (F01-001)

### Outputs
- Approved visual designs
- Component library
- Handoff specification

### Business Rules
- Designs reuse Garrison's existing logo and brand colours unless Garrison requests a refresh
- Colour contrast meets accessibility guidance

### Validations
- Every template has an approved desktop and mobile design

### Calculations
- None

### Workflow
Style guide → Components → Page designs → Prototype → Approved

### Search Requirements
- None

### Documents
- Design files and handoff specification

### Reports
- None

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F01-002

### Assumptions
- Garrison keeps its current logo; new logo or brand identity work is not included
- Two review rounds

### Risks
- Subjective design feedback extending beyond two rounds

### Non Functional Requirements
- Designs at 360 px, 768 px and 1440 px widths

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Style guide (colour, typography, spacing, iconography) | Complex | 12 |
| UI | UI component library design | Complex | 12 |
| UI | Home page visual design (desktop and mobile) | Complex | 12 |
| UI | Content page visual design | Medium | 6 |
| UI | Catalogue landing and category listing visual design | Complex | 12 |
| UI | Product detail and search visual design | Medium | 6 |
| UI | Contact and enquiry visual design | Easy | 4 |
| UI | Clickable prototype | Medium | 6 |
| Testing | Design review rounds with Garrison | Medium | 6 |
| Documentation | Design handoff specification | Medium | 3 |

**Feature Total: 79 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 70 | 0 | 0 | 0 | 6 | 3 | **79** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Design artefacts are sized on the UI scale of the Estimation Master
- No external integration channel in this feature; Integration row omitted.
