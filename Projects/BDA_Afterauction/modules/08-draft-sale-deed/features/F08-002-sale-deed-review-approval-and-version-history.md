# F08-002 — Sale Deed Review, Approval & Version History

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-002 |
| Feature Name | Sale Deed Review, Approval & Version History |
| Module | 08 — Draft Sale Deed |
| Module Type | Business |
| Release | Go-live |

### Description
Review of the draft sale deed by the Deputy Secretary with comments, return for correction, approval and DSC signature, comparison between versions, and complete version history.

### Business Objective
Ensure only reviewed and approved drafts reach the bidder, with a full record of changes.

### Actors
- Deputy Secretary
- Case Worker

### User Journey
1. **Who creates:** The case worker submits; the DS reviews.
2. **How they create:** The DS opens the draft, adds comments on clauses, and approves or returns.
3. **How they edit:** The case worker revises returned drafts and resubmits.
4. **How they send for approval:** Resubmission goes back to the DS queue.
5. **How the approver sees pending items:** The DS sees drafts awaiting review with age.
6. **How the approver decides:** The DS approves and signs with DSC, or returns with comments.
7. **How the applicant / maker sees history:** The case worker sees comments and status.
8. **How the approver / auditor sees history:** Auditors see versions, comments, approvals and signatures.

### Functional Capabilities
- Inline comments
- Version comparison
- Return and resubmit cycle
- Approval with DSC
- Approved draft locked

### UI Screens
- Draft review with comments
- Version comparison
- Approval and signing
- Version history

### Logical API Operations
- Add / resolve comment
- Compare versions
- Return draft
- Approve and sign draft
- Lock approved draft
- Version history

### Inputs
- Comments
- Decision
- Signature

### Outputs
- Approved signed draft

### Business Rules
- Only the case's DS can approve
- Approved draft cannot be edited; changes need re-opening with reason

### Validations
- DSC valid

### Calculations
- None

### Workflow
Submitted → Returned / Approved → Locked

### Search Requirements
- Drafts by status

### Documents
- Approved draft

### Reports
- Draft deed pendency

### Notifications
- Return and approval notices

### Security
- DSC

### Integrations
- Signing via F13-003

### Dependencies
- F08-001
- F13-003

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Draft review with comments | Complex | 12 |
| UI | Version comparison | Medium | 6 |
| UI | Approval and signing | Easy | 4 |
| UI | Version history | Easy | 4 |
| API | Add / resolve comment | Easy | 4 |
| API | Compare versions | Medium | 6 |
| API | Return draft | Easy | 4 |
| API | Approve and sign draft | Medium | 6 |
| API | Lock approved draft | Easy | 4 |
| API | Version history | Easy | 4 |
| Database | Review comments | Easy | 2 |
| Testing | Review cycle and signing tests | Medium | 6 |
| Documentation | Review guide | Simple | 1 |

**Feature Total: 63 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 28 | 2 | 0 | 6 | 1 | **63** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Review screen rated Complex
- No external integration channel in this feature; Integration row omitted.
