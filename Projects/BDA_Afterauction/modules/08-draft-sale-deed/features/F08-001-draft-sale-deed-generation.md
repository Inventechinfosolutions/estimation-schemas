# F08-001 — Draft Sale Deed Generation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-001 |
| Feature Name | Draft Sale Deed Generation |
| Module | 08 — Draft Sale Deed |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of the draft sale deed from the approved bilingual template with case data: parties, site schedule and boundaries, measurements, sale consideration, payments received, conditions of sale and annexures (sketch), with editing of permitted clauses by the case worker.

### Business Objective
Produce an accurate draft deed quickly from verified data with consistent legal wording.

### Actors
- Case Worker
- Deputy Secretary

### User Journey
1. **Who creates:** The case worker creates the draft after DS orders.
2. **How they create:** The case worker clicks Generate Draft Deed; the system fills the template and shows it in the editor.
3. **How they edit:** The case worker edits permitted clauses; each save creates a version.
4. **How they send for approval:** The case worker submits the draft for review (F08-002).
5. **How the approver sees pending items:** The DS sees the draft in the review queue.
6. **How the approver decides:** The DS reviews in F08-002.
7. **How the applicant / maker sees history:** The case worker sees versions and status.
8. **How the approver / auditor sees history:** Auditors see template version and edits.

### Functional Capabilities
- Template-based generation with merge of site schedule and boundaries
- Annexure insertion (sketch, payment summary)
- Editable clauses with locked data fields
- Version on each save
- Kannada and English output

### UI Screens
- Draft deed generation
- Draft deed editor
- Draft deed preview

### Logical API Operations
- Generate draft deed
- Save draft version
- Insert annexures
- Preview PDF
- Submit for review

### Inputs
- Case data
- Template
- Edits

### Outputs
- Draft deed versions

### Business Rules
- Data fields cannot be edited in the editor
- Only DS-office users of the case can generate

### Validations
- Payments at 75% or more
- Template active

### Calculations
- Amounts in words

### Workflow
Generated → Draft → Submitted for Review

### Search Requirements
- Drafts by case and status

### Documents
- Draft deed

### Reports
- None

### Notifications
- Review request to DS

### Security
- DS isolation

### Integrations
- None

### Dependencies
- F02-005
- F07-004

### Assumptions
- Template provided by BDA legal

### Risks
- Template complexity

### Non Functional Requirements
- Generation within 10 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Draft deed generation | Easy | 4 |
| UI | Draft deed editor | Complex | 12 |
| UI | Draft deed preview | Medium | 6 |
| API | Generate draft deed | Medium | 6 |
| API | Save draft version | Medium | 6 |
| API | Insert annexures | Medium | 6 |
| API | Preview PDF | Easy | 4 |
| API | Submit for review | Easy | 4 |
| Database | Sale deed draft and version store | Medium | 4 |
| Testing | Generation, merge and rendering tests | Medium | 6 |
| Testing | Locked field and version tests | Easy | 4 |
| Documentation | Draft deed preparation guide | Easy | 2 |

**Feature Total: 64 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 26 | 4 | 0 | 10 | 2 | **64** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Editor with locked fields rated Complex
- No external integration channel in this feature; Integration row omitted.
