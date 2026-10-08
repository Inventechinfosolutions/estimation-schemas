# F03-006 — Combinations Pages

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-006 |
| Feature Name | Combinations Pages |
| Module | 03 — Catalogue Pages on Existing Website |
| Module Type | Business |
| Release | Optional |

### Description
Optional listing and detail pages for moulding combinations from the source catalogue, showing the combination image and component profiles linked to their product pages.

### Business Objective
Show coordinated trim assemblies if Garrison wishes to include them.

### Actors
- Visitor
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer extracts and loads combinations.
2. **How they create:** Combination records are captured with their component codes and reviewed in the workbook.
3. **How they edit:** Corrections follow the review rounds.
4. **How they send for approval:** Approval follows the review workbook sign-off.
5. **How the approver sees pending items:** No in-system inbox.
6. **How the approver decides:** Garrison's sign-off email is the decision.
7. **How the maker sees history:** Garrison sees the change log.
8. **How the approver / auditor sees history:** The delivery lead keeps the review records.

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
- Component codes exist in dataset

### Calculations
- None

### Workflow
Same as mouldings

### Search Requirements
- Included in search

### Documents
- None

### Reports
- Included in reconciliation

### Notifications
- None

### Security
- Public read-only

### Integrations
- Source catalogue (via F01-001)

### Dependencies
- F01-001
- F02-001
- F03-003

### Assumptions
- Optional; combination count confirmed on first extraction

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
| Database | Combination and component storage | Easy | 2 |
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
