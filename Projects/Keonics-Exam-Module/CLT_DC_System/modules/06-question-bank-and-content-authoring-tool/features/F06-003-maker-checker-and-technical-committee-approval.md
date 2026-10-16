# F06-003 — Maker-Checker & Technical Committee Approval

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-003 |
| Feature Name | Maker-Checker & Technical Committee Approval |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Two-stage review: Reviewer checks accuracy, language parity, difficulty and metadata and approves or returns with comments; Technical Committee reviews approved items in batches and accepts into the bank or rejects; segregation hides answer key or other components as configured (F06-004).

### Business Objective
Ensure only vetted questions are used.

### Actors
- Reviewer
- Technical Committee Member
- SME Author

### User Journey
1. **Who creates:** Items arrive from authors.
2. **How they create:** The Reviewer opens an item with review checklist.
3. **How they edit:** The Reviewer can suggest edits (as comments; content edits go back to author).
4. **How they send for approval:** Approved items move to the committee batch.
5. **How the approver sees pending items:** Committee members see batches.
6. **How the approver decides:** Members accept or reject items; decisions recorded with batch minutes.
7. **How the applicant / maker sees history:** Authors see outcomes and comments.
8. **How the approver / auditor sees history:** Auditors see the full review trail.

### Functional Capabilities
- Review queue with checklist
- Inline comments
- Return to author
- Committee batches
- Accept / reject with reasons
- Reviewer cannot review own items
- Turnaround metrics

### UI Screens
- Review queue
- Item review with checklist
- Committee batch review
- Decision history

### Logical API Operations
- Review queue by subject
- Record review decision
- Create committee batch
- Committee decision
- Turnaround metrics

### Inputs
- Items

### Outputs
- Approved bank items

### Business Rules
- Author ≠ Reviewer
- Only committee-accepted items usable

### Validations
- Checklist complete

### Calculations
- Turnaround days

### Workflow
Submitted → Reviewed → Committee → Approved / Rejected

### Search Requirements
- By status, topic

### Documents
- Batch minutes

### Reports
- Review statistics

### Notifications
- Queue notifications

### Security
- Segregated views

### Integrations
- None

### Dependencies
- F06-002
- F06-004

### Assumptions
- Committee meets periodically

### Risks
- Backlog

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Review queue | Medium | 6 |
| UI | Item review with checklist | Complex | 12 |
| UI | Committee batch review | Complex | 12 |
| UI | Decision history | Easy | 4 |
| API | Review queue by subject | Medium | 6 |
| API | Record review decision | Medium | 6 |
| API | Create committee batch | Medium | 6 |
| API | Committee decision | Medium | 6 |
| API | Turnaround metrics | Easy | 4 |
| Database | Review and committee decisions | Medium | 4 |
| Testing | Maker-checker tests | Complex | 8 |
| Documentation | Review guide | Easy | 2 |

**Feature Total: 76 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 28 | 4 | 0 | 8 | 2 | **76** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Two-stage workflow
- No external integration channel in this feature; Integration row omitted.
