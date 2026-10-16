# F11-003 — Result Finalisation & Signed Submission

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-003 |
| Feature Name | Result Finalisation & Signed Submission |
| Module | 11 — Evaluation, Results & Digital Certification |
| Module Type | Business |
| Release | Go-live |

### Description
After challenge closure and malpractice decisions, Result Officer finalises session results, generates rank list or pass / fail list, digitally signs the final score file (Service Provider DSC), submits to KEONICS for approval, and publishes results to candidates.

### Business Objective
Deliver signed, approved results as required by the RFP.

### Actors
- Result Officer
- KEONICS Approver
- Candidate

### User Journey
1. **Who creates:** The Result Officer prepares the session result.
2. **How they create:** The officer checks pending cases and challenges, generates lists and signs.
3. **How they edit:** Corrections allowed before approval.
4. **How they send for approval:** The result goes to the KEONICS Approver.
5. **How the approver sees pending items:** The approver sees result summaries.
6. **How the approver decides:** The approver approves; results publish.
7. **How the applicant / maker sees history:** Candidates see final result.
8. **How the approver / auditor sees history:** Auditors see signed files and approvals.

### Functional Capabilities
- Pre-finalisation checks
- Rank / pass-fail lists
- Signed result file
- Approval
- Publication
- Withheld results for open cases

### UI Screens
- Result finalisation
- Result approval
- Published result view

### Logical API Operations
- Pre-finalisation checks
- Generate result lists
- Sign result file
- Approve and publish

### Inputs
- Scores

### Outputs
- Signed final results

### Business Rules
- Finalise only after challenge window and case decisions

### Validations
- No pending items

### Calculations
- Ranks

### Workflow
Draft → Signed → Approved → Published

### Search Requirements
- Results by session

### Documents
- Signed result file

### Reports
- Result lists

### Notifications
- Result SMS / e-mail

### Security
- DSC signing

### Integrations
- DSC via F15-006

### Dependencies
- F11-001
- F11-002
- F10-005
- F15-006

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Result finalisation | Medium | 6 |
| UI | Result approval | Medium | 6 |
| UI | Published result view | Easy | 4 |
| API | Pre-finalisation checks | Medium | 6 |
| API | Generate result lists | Medium | 6 |
| API | Sign result file | Medium | 6 |
| API | Approve and publish | Medium | 6 |
| Database | Final results | Easy | 2 |
| Testing | Finalisation tests | Medium | 6 |
| Documentation | Result process note | Easy | 2 |

**Feature Total: 50 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 24 | 2 | 0 | 6 | 2 | **50** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
