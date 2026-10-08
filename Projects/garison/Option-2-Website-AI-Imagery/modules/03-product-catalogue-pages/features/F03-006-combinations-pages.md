# F03-006 — Combinations Pages

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-006 |
| Feature Name | Combinations Pages |
| Module | 03 — Product Catalogue Pages |
| Module Type | Business |
| Release | Optional |

### Description
Optional listing and detail pages for moulding combinations from the source catalogue, showing the combination image and component profiles linked to their product pages.

### Business Objective
Show coordinated trim assemblies if Garrison wishes.

### Actors
- Visitor
- Delivery developer

### User Journey
1. **Who creates:** Combinations are extracted and loaded once by the delivery developer.
2. **How they create:** Combination records are captured with component codes and reviewed in the workbook (F04-004).
3. **How they edit:** Changes only through a dataset refresh.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison approves the pages on staging during user acceptance testing (F05-005).

### Functional Capabilities
- Combination extraction
- Combination listing
- Combination detail with component links

### UI Screens
- Combinations listing page
- Combination detail page

### Logical API Operations
- Extract combinations and component codes
- Get combinations with components

### Inputs
- Source combinations section

### Outputs
- Combination pages

### Business Rules
- Components link only to loaded products

### Validations
- Component codes exist in the dataset

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- Included in search

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- Source catalogue (via F04-001)

### Dependencies
- F04-001
- F04-005
- F03-003

### Assumptions
- Combination count confirmed on first extraction

### Risks
- Source combination data may lack structured component lists

### Non Functional Requirements
- Same as product pages

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Combinations listing page | Medium | 6 |
| UI | Combination detail page | Medium | 6 |
| API | Extract combinations and component codes | Medium | 6 |
| API | Get combinations with components | Easy | 4 |
| Database | Combination data file | Easy | 2 |
| Testing | Combination display and component links | Easy | 4 |
| Documentation | Combinations notes | Simple | 1 |

**Feature Total: 29 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 10 | 2 | 0 | 4 | 1 | **29** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Two templates and a small extraction adapter
- No external integration channel in this feature; Integration row omitted.
