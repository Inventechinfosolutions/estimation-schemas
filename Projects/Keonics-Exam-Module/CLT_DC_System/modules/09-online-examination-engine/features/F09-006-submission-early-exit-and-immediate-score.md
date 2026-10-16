# F09-006 — Submission, Early Exit & Immediate Score

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-006 |
| Feature Name | Submission, Early Exit & Immediate Score |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Submission flow with summary of answered and unanswered items, confirmation, early exit allowed, auto-submit at time end, immediate computation and display of MCQ, typing and total score with provisional qualifying status, and score slip download / print; locking of responses after submission.

### Business Objective
Meet the RFP requirement that the score is displayed immediately.

### Actors
- Candidate
- Proctor

### User Journey
1. **Who creates:** The candidate submits or time ends.
2. **How they create:** Summary shown; candidate confirms.
3. **How they edit:** No edits after submission.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Proctor sees submission status.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Candidate sees score immediately and later in account.
8. **How the approver / auditor sees history:** Auditors see submission records.

### Functional Capabilities
- Submission summary
- Early exit
- Auto-submit
- Immediate scoring
- Score slip
- Response locking

### UI Screens
- Submission summary
- Score display

### Logical API Operations
- Submit test
- Compute immediate score
- Generate score slip

### Inputs
- Responses

### Outputs
- Provisional score

### Business Rules
- Score provisional until result finalisation
- Re-evaluation not permitted

### Validations
- All sections closed

### Calculations
- Total = MCQ marks − negative marks + typing marks

### Workflow
In Test → Submitted → Scored

### Search Requirements
- None

### Documents
- Score slip

### Reports
- Submissions

### Notifications
- Score SMS (optional)

### Security
- Responses locked

### Integrations
- None

### Dependencies
- F11-001

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Score shown within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Submission summary | Easy | 4 |
| UI | Score display | Medium | 6 |
| API | Submit test | Medium | 6 |
| API | Compute immediate score | Medium | 6 |
| API | Generate score slip | Easy | 4 |
| Database | Submission and provisional score | Easy | 2 |
| Testing | Submission and scoring tests | Medium | 6 |
| Documentation | Score display note | Simple | 1 |

**Feature Total: 35 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 16 | 2 | 0 | 6 | 1 | **35** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Uses evaluation engine
- No external integration channel in this feature; Integration row omitted.
