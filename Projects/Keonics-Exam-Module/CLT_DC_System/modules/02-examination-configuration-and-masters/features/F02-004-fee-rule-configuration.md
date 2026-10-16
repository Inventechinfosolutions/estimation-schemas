# F02-004 — Fee Rule Configuration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-004 |
| Feature Name | Fee Rule Configuration |
| Module | 02 — Examination Configuration & Masters |
| Module Type | Business |
| Release | Go-live |

### Description
Configuration of test fees by candidate category (government employee, board / corporation staff, prospective candidate) and attempt number, with free first attempt for government employees, GST treatment, effective dates and approval.

### Business Objective
Charge correct fees as decided by the competent authority without code changes.

### Actors
- KEONICS Administrator
- Finance Officer
- Approving Authority

### User Journey
1. **Who creates:** The KEONICS Administrator creates a fee version.
2. **How they create:** The administrator enters fee amounts by category and attempt band and the effective date.
3. **How they edit:** The administrator edits drafts; a calculator previews fees.
4. **How they send for approval:** The draft goes to the Finance Officer and Approving Authority.
5. **How the approver sees pending items:** Approvers see the version with comparison.
6. **How the approver decides:** Approvers approve or return.
7. **How the applicant / maker sees history:** Candidates see the applicable fee during booking.
8. **How the approver / auditor sees history:** Auditors see versions and fee applied per booking.

### Functional Capabilities
- Fee matrix by category × attempt
- Free first attempt rule
- GST and convenience charge handling
- Effective-dated versions
- Fee preview calculator

### UI Screens
- Fee versions
- Fee matrix editor
- Fee calculator preview
- Approval

### Logical API Operations
- Save fee draft
- Approve fee version
- Resolve fee for candidate
- Preview fee

### Inputs
- Fee amounts

### Outputs
- Approved fee version

### Business Rules
- Fee version stamped on each booking
- Attempts counted from all past CLT records including ported data

### Validations
- Amounts ≥ 0

### Calculations
- Fee = matrix(category, attempt) + charges

### Workflow
Draft → Approved → Active

### Search Requirements
- Versions

### Documents
- Order reference

### Reports
- Fee history

### Notifications
- Approval requests

### Security
- Finance approval

### Integrations
- None

### Dependencies
- F05-002
- F18-001

### Assumptions
- Fees decided by competent authority

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Fee versions | Easy | 4 |
| UI | Fee matrix editor | Medium | 6 |
| UI | Fee calculator preview | Easy | 4 |
| UI | Approval | Easy | 4 |
| API | Save fee draft | Easy | 4 |
| API | Approve fee version | Easy | 4 |
| API | Resolve fee for candidate | Medium | 6 |
| API | Preview fee | Easy | 4 |
| Database | Fee rules | Easy | 2 |
| Testing | Fee resolution tests | Medium | 6 |
| Documentation | Fee configuration note | Simple | 1 |

**Feature Total: 45 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 18 | 2 | 0 | 6 | 1 | **45** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
