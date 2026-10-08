# F04-002 — Navigation & Theme Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-002 |
| Feature Name | Navigation & Theme Integration |
| Module | 04 — Website Integration, SEO & Go-live |
| Module Type | Shared |
| Release | Go-live |

### Description
Add the catalogue to the main navigation (replacing the current mouldings link), reuse the existing header and footer, and style all catalogue templates to match the current theme responsively.

### Business Objective
Make the catalogue look like part of the current Garrison website.

### Actors
- Visitor
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer implements navigation and styling.
2. **How they create:** Templates are built using the existing theme assets and layout.
3. **How they edit:** Style adjustments are made after Garrison feedback on staging.
4. **How they send for approval:** Garrison approves the look on staging during UAT.
5. **How the approver sees pending items:** No in-system inbox.
6. **How the approver decides:** Garrison's UAT sign-off is the decision.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** The delivery lead keeps UAT feedback records.

### Functional Capabilities
- Mouldings menu entry
- Header/footer reuse
- Responsive catalogue styles in existing theme

### UI Screens
- Main navigation Mouldings menu update
- Catalogue styles aligned to existing theme
- Header and footer reuse in catalogue templates

### Logical API Operations
- None (no application operations in this feature)

### Inputs
- Existing theme assets

### Outputs
- Consistent catalogue styling

### Business Rules
- No redesign of existing pages

### Validations
- Existing pages unchanged visually

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
- None specific

### Integrations
- None

### Dependencies
- F04-001

### Assumptions
- Existing theme is responsive or can be made responsive for catalogue templates only

### Risks
- Very old theme may need extra CSS work

### Non Functional Requirements
- Supports current Chrome, Edge, Safari, Firefox

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Main navigation Mouldings menu update | Easy | 4 |
| UI | Catalogue styles aligned to existing theme | Complex | 12 |
| UI | Header and footer reuse in catalogue templates | Easy | 4 |
| Testing | Cross-browser and device checks | Medium | 6 |
| Documentation | Theme integration notes | Simple | 1 |

**Feature Total: 27 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 0 | 0 | 0 | 6 | 1 | **27** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Styling effort concentrated in one Complex row
- No external integration channel in this feature; Integration row omitted.
