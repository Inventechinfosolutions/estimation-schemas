# F11-001 — Automatic MCQ & Typing Evaluation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-001 |
| Feature Name | Automatic MCQ & Typing Evaluation |
| Module | 11 — Evaluation, Results & Digital Certification |
| Module Type | Business |
| Release | Go-live |

### Description
Evaluation engine computing MCQ marks from jumbled-paper mappings and the answer key, optional negative marking per pattern, typing marks from typing metrics, totals, qualifying status at the configured percentage, re-computation after answer key changes, and evaluation logs.

### Business Objective
Produce accurate scores automatically.

### Actors
- System
- Result Officer

### User Journey
1. **Who creates:** Evaluation runs at submission and again at finalisation.
2. **How they create:** Scores computed and stored.
3. **How they edit:** Re-computation after key change by Result Officer.
4. **How they send for approval:** Re-computation results need approval.
5. **How the approver sees pending items:** Approver sees changes.
6. **How the approver decides:** Approver approves.
7. **How the applicant / maker sees history:** Candidates see scores.
8. **How the approver / auditor sees history:** Auditors see evaluation logs.

### Functional Capabilities
- Mapping-aware evaluation
- Negative marking
- Typing marks
- Qualifying status
- Batch re-evaluation after key change
- Evaluation logs

### UI Screens
- Evaluation run status
- Re-computation comparison

### Logical API Operations
- Evaluate candidate
- Batch evaluation
- Re-compute after key change
- Evaluation log

### Inputs
- Responses
- Answer key
- Pattern snapshot

### Outputs
- Scores

### Business Rules
- Pattern snapshot of the session applies

### Validations
- Key completeness

### Calculations
- Score = Σ correct × marks − Σ wrong × negative + typing

### Workflow
Provisional → Final

### Search Requirements
- None

### Documents
- None

### Reports
- Score distribution

### Notifications
- None

### Security
- Key decrypted only in engine

### Integrations
- None

### Dependencies
- F07-002
- F09-004
- F02-001

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- 2,000 candidates evaluated under 1 minute

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Evaluation run status | Easy | 4 |
| UI | Re-computation comparison | Medium | 6 |
| API | Evaluate candidate | Medium | 6 |
| API | Batch evaluation | Complex | 8 |
| API | Re-compute after key change | Complex | 8 |
| API | Evaluation log | Easy | 4 |
| Database | Scores and evaluation logs | Medium | 4 |
| Testing | Evaluation accuracy tests | Complex | 8 |
| Documentation | Evaluation rules note | Easy | 2 |

**Feature Total: 50 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 26 | 4 | 0 | 8 | 2 | **50** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Core engine
- No external integration channel in this feature; Integration row omitted.
