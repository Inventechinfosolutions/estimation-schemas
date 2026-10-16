# F06-008 — Typing Test Passage Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-008 |
| Feature Name | Typing Test Passage Management |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Authoring and approval of typing passages for English and Kannada (Unicode, with configured keyboard layout such as Nudi / KGP or InScript), with length, difficulty, and separate pools for mock and main tests.

### Business Objective
Provide the content for the Part 2 typing tests.

### Actors
- SME Author
- Reviewer

### User Journey
1. **Who creates:** Authors create passages.
2. **How they create:** Authors enter text, language, layout and difficulty.
3. **How they edit:** Authors edit drafts.
4. **How they send for approval:** Passages go to review.
5. **How the approver sees pending items:** Reviewers see passages.
6. **How the approver decides:** Reviewers approve or return.
7. **How the applicant / maker sees history:** Authors see status.
8. **How the approver / auditor sees history:** Auditors see versions.

### Functional Capabilities
- Passage editor
- Language and layout tagging
- Word and character counts
- Mock / main pools
- Review

### UI Screens
- Passage editor
- Passage review

### Logical API Operations
- Save passage
- Review passage
- Select passage pool

### Inputs
- Passage text

### Outputs
- Approved passages

### Business Rules
- Kannada passages in Unicode

### Validations
- Length range

### Calculations
- Word count

### Workflow
Draft → Approved

### Search Requirements
- Passages

### Documents
- None

### Reports
- Passage pool

### Notifications
- None

### Security
- Encrypted

### Integrations
- None

### Dependencies
- F09-004

### Assumptions
- Kannada keyboard layout confirmed in FRS

### Risks
- Layout choice

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Passage editor | Medium | 6 |
| UI | Passage review | Easy | 4 |
| API | Save passage | Easy | 4 |
| API | Review passage | Easy | 4 |
| API | Select passage pool | Easy | 4 |
| Database | Passages | Easy | 2 |
| Testing | Passage tests | Easy | 4 |
| Documentation | Passage guidelines | Simple | 1 |

**Feature Total: 29 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 12 | 2 | 0 | 4 | 1 | **29** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
