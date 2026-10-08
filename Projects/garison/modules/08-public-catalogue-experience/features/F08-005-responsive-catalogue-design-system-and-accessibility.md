# F08-005 — Responsive Catalogue Design System & Accessibility

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-005 |
| Feature Name | Responsive Catalogue Design System & Accessibility |
| Module | 08 — Public Catalogue Experience |
| Module Type | Business |
| Release | Go-live |

### Description
Brand-aligned responsive design system for the public catalogue: design tokens (Garrison colours, typography, spacing), reusable components (buttons, cards, chips, forms, modals, tabs, breadcrumbs, carousels), catalogue sub-navigation, error pages (404, 500, archived product), consent banner, and an accessibility baseline built with reference to WCAG 2.1 AA.

### Business Objective
Deliver a consistent, accessible experience across desktop, tablet and mobile that matches the Garrison website identity.

### Actors
- Visitor
- Garrison design approver

### User Journey
1. **Who creates:** The design system is created by the delivery team from the Garrison-approved visual design; no administrator creates content here.
2. **How they create:** Not applicable to administrators; components are built once and reused across public pages.
3. **How they edit:** Changes to tokens or components are made through releases, not through administration.
4. **How they send for approval:** Garrison approves the visual design at the design checkpoint before build (project-level approval, not in-system).
5. **How the approver sees pending items:** No in-system approver inbox.
6. **How the approver decides:** No in-system decision.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Not applicable; accessibility audit results are recorded in test reports.

### Functional Capabilities
- Design tokens and theme aligned to Garrison branding
- Responsive component library with documented states
- Catalogue sub-navigation (categories mega-menu on desktop, drawer on mobile)
- Error and archived-product pages
- Cookie/consent banner for analytics
- Keyboard navigation, focus states, contrast, alt text, ARIA landmarks
- Print stylesheet for product pages

### UI Screens
- Design tokens and Garrison theme
- Responsive component library
- Catalogue sub-navigation and mobile drawer
- Error and archived-product pages
- Cookie and consent banner
- Product page print stylesheet

### Logical API Operations
- Get catalogue navigation menu

### Inputs
- Approved visual design, brand guidelines and assets

### Outputs
- Reusable component library used by all public pages

### Business Rules
- All public pages use the design system
- Colour contrast meets 4.5:1 for body text

### Validations
- Automated accessibility checks pass with no critical issues

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- Style guide

### Reports
- Accessibility audit report

### Notifications
- None

### Security
- No sensitive data; consent respected before analytics loads

### Integrations
- None

### Dependencies
- Garrison brand assets
- F08-001 to F08-004
- F11-003
- F11-004

### Assumptions
- Garrison provides brand guidelines and assets
- Design follows the approved UX/UI phase

### Risks
- Late branding changes cause rework across pages

### Non Functional Requirements
- Supports current Chrome, Edge, Safari, Firefox; responsive from 360 px to 1920 px

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Design tokens and Garrison theme | Complex | 12 |
| UI | Responsive component library | Very High | 16 |
| UI | Catalogue sub-navigation and mobile drawer | Medium | 6 |
| UI | Error and archived-product pages | Easy | 4 |
| UI | Cookie and consent banner | Easy | 4 |
| UI | Product page print stylesheet | Easy | 4 |
| API | Get catalogue navigation menu | Easy | 4 |
| Testing | Cross-browser and device matrix | Complex | 8 |
| Testing | WCAG 2.1 AA audit and remediation | Complex | 8 |
| Documentation | Design system and style guide | Medium | 3 |

**Feature Total: 69 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 46 | 4 | 0 | 0 | 16 | 3 | **69** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Component library is a Very High UI item
- No database effort
- No external integration channel in this feature; Integration row omitted.
