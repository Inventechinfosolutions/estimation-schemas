# F11-003 — Garrison Website Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-003 |
| Feature Name | Garrison Website Integration |
| Module | 11 — SEO, Analytics & Website Integration |
| Module Type | Shared |
| Release | Go-live |

### Description
Integrate the catalogue into the existing Garrison website: shared header and footer (or matching replica), Mouldings navigation entry and category menu, consistent branding, routing via sub-path, sub-domain or embedded module (confirmed in discovery), and 301 redirects from the existing mouldings page and legacy URLs.

### Business Objective
Make the catalogue feel like part of the Garrison website and preserve existing traffic to the mouldings page.

### Actors
- Delivery team
- Garrison web administrator
- Visitor

### User Journey
1. **Who creates:** Integration is created by the delivery team with Garrison's web administrator; no in-portal user creates it.
2. **How they create:** The team implements the shared header/footer, navigation entry and routing on staging, then production.
3. **How they edit:** Changes to the main site navigation are made by Garrison's web administrator; the catalogue category menu updates automatically from the navigation feed.
4. **How they send for approval:** Garrison approves the integration on staging (project checkpoint), not in-system.
5. **How the approver sees pending items:** No in-system approver inbox.
6. **How the approver decides:** No in-system decision.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Redirect mappings are visible in the redirect manager (F11-001); changes are audited.

### Functional Capabilities
- Shared header/footer integration or faithful replica
- Mouldings navigation entry with category menu fed from the catalogue
- Routing for sub-path (/mouldings) or sub-domain, including reverse proxy/CDN rules
- Legacy mouldings page and URL redirect mapping
- Shared analytics and consent across the site

### UI Screens
- Shared header and footer integration
- Mouldings navigation entry and category menu
- Legacy URL redirect mapping

### Logical API Operations
- Provide navigation categories feed for main site
- Resolve legacy URLs to catalogue pages

### Inputs
- Garrison website access, theme assets, legacy URL list, chosen integration method

### Outputs
- Integrated catalogue within the Garrison site
- Redirects from legacy pages

### Business Rules
- Legacy mouldings URLs return 301 to catalogue equivalents
- Header/footer must stay consistent when Garrison updates the main site (shared include or documented update procedure)

### Validations
- All legacy URLs mapped or redirected to catalogue home

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- Integration document

### Reports
- None

### Notifications
- None

### Security
- HTTPS across both sites; no shared admin credentials

### Integrations
- Garrison website platform (CMS) and hosting/CDN

### Dependencies
- Garrison website and hosting access
- F08-005
- F11-001
- F11-004

### Assumptions
- Integration via sub-path or sub-domain; embedding inside the CMS as a plugin would require re-estimation
- Garrison's web administrator is available for routing changes

### Risks
- Unknown website platform constraints; mitigated by early technical discovery

### Non Functional Requirements
- No measurable slowdown of the main website

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Shared header and footer integration | Complex | 12 |
| UI | Mouldings navigation entry and category menu | Medium | 6 |
| UI | Legacy URL redirect mapping | Easy | 4 |
| API | Provide navigation categories feed for main site | Easy | 4 |
| API | Resolve legacy URLs to catalogue pages | Easy | 4 |
| Integration | Garrison website platform integration (routing, shared assets, proxy rules) | Complex | 24 |
| Testing | Cross-site navigation, branding and redirects | Medium | 6 |
| Testing | Integration verification on staging with Garrison site | Medium | 6 |
| Documentation | Website integration document | Medium | 3 |

**Feature Total: 69 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 8 | 0 | 24 | 12 | 3 | **69** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Website platform integration estimated as Complex (multi-system routing and shared assets)
- No database effort
