# F07-002 — Question & Option Jumbling per Candidate

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-002 |
| Feature Name | Question & Option Jumbling per Candidate |
| Module | 07 — Question Paper Generation & Mock Test |
| Module Type | Business |
| Release | Go-live |

### Description
Per-candidate shuffling of question order (optionally within topic blocks) and option order using seeded randomisation, mapping stored to evaluate correctly, ensuring adjacent candidates get different sequences.

### Business Objective
Prevent copying between candidates.

### Actors
- System

### User Journey
1. **Who creates:** The system creates a jumbled paper per candidate at login.
2. **How they create:** The seed and mapping are stored.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Candidates see their own sequence.
8. **How the approver / auditor sees history:** Auditors can reproduce sequence from seed.

### Functional Capabilities
- Seeded question shuffle
- Option shuffle
- Adjacency diversity check
- Mapping for evaluation
- Reproducibility

### UI Screens
- None (no user interface in this feature)

### Logical API Operations
- Generate candidate sequence
- Store and resolve mapping
- Adjacency diversity check

### Inputs
- Session set
- Seat

### Outputs
- Candidate paper

### Business Rules
- Option labels re-lettered after shuffle

### Validations
- Mapping complete

### Calculations
- Seeded permutation

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
- Mapping encrypted

### Integrations
- None

### Dependencies
- F07-001
- F08-005

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Under 100 ms per candidate

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Generate candidate sequence | Complex | 8 |
| API | Store and resolve mapping | Medium | 6 |
| API | Adjacency diversity check | Medium | 6 |
| Database | Candidate paper mapping | Medium | 4 |
| Testing | Jumbling and mapping tests | Medium | 6 |
| Documentation | Jumbling note | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 4 | 0 | 6 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- No UI
- No external integration channel in this feature; Integration row omitted.
