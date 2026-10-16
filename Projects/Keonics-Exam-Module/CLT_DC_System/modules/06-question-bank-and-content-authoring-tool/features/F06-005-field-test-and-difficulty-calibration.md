# F06-005 — Field Test & Difficulty Calibration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-005 |
| Feature Name | Field Test & Difficulty Calibration |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Conditional |

### Description
Optional field testing of new items in non-scoring slots or pilot sessions, collection of response statistics, computation of difficulty (p-value) and discrimination indices, and recommendation to adjust difficulty or retire items, with committee confirmation.

### Business Objective
Calibrate item difficulty where KEONICS requires it.

### Actors
- Question Bank Administrator
- Technical Committee Member

### User Journey
1. **Who creates:** The administrator creates a field test plan.
2. **How they create:** The administrator selects items and pilot sessions.
3. **How they edit:** The plan is editable until start.
4. **How they send for approval:** The plan goes to the committee.
5. **How the approver sees pending items:** Committee sees plan.
6. **How the approver decides:** Committee approves; after the pilot, it confirms calibration results.
7. **How the applicant / maker sees history:** The administrator sees statistics per item.
8. **How the approver / auditor sees history:** Auditors see changes in difficulty.

### Functional Capabilities
- Field test plans
- Non-scoring item slots
- Item statistics (p-value, discrimination, distractor analysis)
- Calibration recommendations
- Committee confirmation

### UI Screens
- Field test plan
- Item statistics
- Calibration confirmation

### Logical API Operations
- Create plan
- Compute item statistics
- Apply calibration

### Inputs
- Items, sessions

### Outputs
- Calibrated difficulty

### Business Rules
- Non-scoring items do not affect scores

### Validations
- Minimum responses

### Calculations
- p-value, point-biserial

### Workflow
Planned → Running → Calibrated

### Search Requirements
- Items

### Documents
- None

### Reports
- Item analysis

### Notifications
- None

### Security
- Question bank roles

### Integrations
- None

### Dependencies
- F06-003
- F07-001

### Assumptions
- Taken up only if KEONICS requires field testing

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Field test plan | Medium | 6 |
| UI | Item statistics | Complex | 12 |
| UI | Calibration confirmation | Easy | 4 |
| API | Create plan | Easy | 4 |
| API | Compute item statistics | Complex | 8 |
| API | Apply calibration | Medium | 6 |
| Database | Field test and statistics | Easy | 2 |
| Testing | Statistics tests | Medium | 6 |
| Documentation | Calibration method note | Easy | 2 |

**Feature Total: 50 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 18 | 2 | 0 | 6 | 2 | **50** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Conditional (RFP: if required)
- No external integration channel in this feature; Integration row omitted.
