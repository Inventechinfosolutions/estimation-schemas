# F09-002 — Rich MCQ Delivery & Navigation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-002 |
| Feature Name | Rich MCQ Delivery & Navigation |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Candidate test interface: question panel rendering rich content in Kannada / English (text, images with zoom, formulae, tables, simulation items with hotspot and drag-and-drop), option selection and clearing, mark for review, question palette with status colours, topic sections, any-order navigation, revisit and modify, font size control and accessibility support.

### Business Objective
Deliver a clear, robust test experience that supports all item types.

### Actors
- Candidate

### User Journey
1. **Who creates:** The candidate answers after instructions.
2. **How they create:** The candidate navigates, selects answers and marks for review.
3. **How they edit:** The candidate changes answers anytime before submission.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees answered, unanswered and marked counts.
8. **How the approver / auditor sees history:** Auditors see answer change events (F09-005).

### Functional Capabilities
- Rich content renderer
- Simulation item player
- Question palette with status colours
- Mark for review
- Clear response
- Section navigation
- Language toggle per question
- Font size and contrast controls
- Keyboard navigation

### UI Screens
- Test interface shell
- Question renderer (text, image, formula)
- Simulation item player
- Question palette
- Section summary

### Logical API Operations
- Fetch candidate paper (encrypted payload)
- Fetch media securely
- Language switch content

### Inputs
- Paper

### Outputs
- Responses

### Business Rules
- Answer in any order; revisit and modify allowed

### Validations
- One option per MCQ

### Calculations
- Status counts

### Workflow
Not Visited → Not Answered → Answered / Marked

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Content encrypted in transit and memory

### Integrations
- None

### Dependencies
- F07-002
- F09-005

### Assumptions
- Same interface used by mock test

### Risks
- Simulation item compatibility across browsers

### Non Functional Requirements
- Question switch under 300 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Test interface shell | Very High | 16 |
| UI | Question renderer (text, image, formula) | Complex | 12 |
| UI | Simulation item player | Very High | 16 |
| UI | Question palette | Medium | 6 |
| UI | Section summary | Easy | 4 |
| API | Fetch candidate paper (encrypted payload) | Complex | 8 |
| API | Fetch media securely | Medium | 6 |
| API | Language switch content | Easy | 4 |
| Database | Candidate paper cache state | Easy | 2 |
| Testing | Interface tests across item types and devices | Complex | 8 |
| Testing | Usability tests | Medium | 6 |
| Documentation | Interface user guide | Easy | 2 |

**Feature Total: 90 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 54 | 18 | 2 | 0 | 14 | 2 | **90** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Shell and simulation player rated Very High
- No external integration channel in this feature; Integration row omitted.
