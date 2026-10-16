# F10-005 — Bilingual, Responsive & GIGW-Compliant Portal

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-005 |
| Feature Name | Bilingual, Responsive & GIGW-Compliant Portal |
| Module | 10 — Bidder Tracking Portal |
| Module Type | Business |
| Release | Go-live |

### Description
Kannada–English language toggle across all bidder pages and messages, responsive layout for mobile and tablet, and GIGW 3.0 / WCAG 2.1 AA accessibility (keyboard navigation, screen-reader labels, contrast, text resize), with accessibility testing and statement.

### Business Objective
Meet the RFP's GIGW 3.0 and bilingual requirements and make the portal usable on mobile.

### Actors
- Successful Bidder
- Auction Admin (translations)

### User Journey
1. **Who creates:** The Auction Admin maintains label translations.
2. **How they create:** The Auction Admin edits labels in the translation screen.
3. **How they edit:** Labels can be edited and published.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Bidders switch language at any time.
8. **How the approver / auditor sees history:** Auditors see translation changes.

### Functional Capabilities
- Language toggle with persisted preference
- Translation management for labels
- Responsive layouts
- GIGW 3.0 compliance items (accessibility statement, help, contact, policies)
- Accessibility testing

### UI Screens
- Translation management
- Portal shell with language toggle and accessibility controls
- Accessibility statement and help pages

### Logical API Operations
- Get translations
- Update translations

### Inputs
- Translations

### Outputs
- Bilingual portal

### Business Rules
- All bidder-facing text translatable

### Validations
- No missing keys

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- Labels by key

### Documents
- None

### Reports
- Missing translations

### Notifications
- None

### Security
- Standard

### Integrations
- None

### Dependencies
- Modules 05–10

### Assumptions
- BDA reviews Kannada text

### Risks
- Translation quality

### Non Functional Requirements
- GIGW 3.0
- WCAG 2.1 AA

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Translation management | Easy | 4 |
| UI | Portal shell with language toggle and accessibility controls | Medium | 6 |
| UI | Accessibility statement and help pages | Simple | 2 |
| API | Get translations | Easy | 4 |
| API | Update translations | Easy | 4 |
| Database | Translation store | Easy | 2 |
| Testing | Accessibility audit (WCAG 2.1 AA) | Complex | 8 |
| Testing | Responsive tests across devices | Medium | 6 |
| Testing | Language coverage tests | Easy | 4 |
| Documentation | Accessibility statement and GIGW compliance checklist | Easy | 2 |

**Feature Total: 42 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 8 | 2 | 0 | 18 | 2 | **42** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Accessibility testing rated Complex
- No external integration channel in this feature; Integration row omitted.
