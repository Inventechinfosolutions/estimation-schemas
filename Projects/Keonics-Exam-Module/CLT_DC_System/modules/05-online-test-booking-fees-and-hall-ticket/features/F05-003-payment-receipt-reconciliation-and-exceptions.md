# F05-003 — Payment Receipt, Reconciliation & Exceptions

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-003 |
| Feature Name | Payment Receipt, Reconciliation & Exceptions |
| Module | 05 — Online Test Booking, Fees & Hall Ticket |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of bilingual payment receipts, daily reconciliation of payments with gateway settlement files, exception queue for unmatched, pending and double payments, refund recording for duplicates and finance reports.

### Business Objective
Ensure every rupee collected is matched and receipted.

### Actors
- Finance Officer
- Candidate

### User Journey
1. **Who creates:** Receipts are generated on payment success; settlement files are uploaded or fetched daily.
2. **How they create:** The Finance Officer runs reconciliation.
3. **How they edit:** The officer resolves exceptions with remarks.
4. **How they send for approval:** Refunds for duplicates need approval.
5. **How the approver sees pending items:** The approver sees refund requests.
6. **How the approver decides:** The approver approves; refund is processed through the gateway.
7. **How the applicant / maker sees history:** Candidates download receipts.
8. **How the approver / auditor sees history:** Auditors see reconciliation runs and decisions.

### Functional Capabilities
- Bilingual PDF receipt with number
- Settlement file import
- Auto-matching by transaction reference
- Exception queue
- Refund request and approval
- Daily collection report

### UI Screens
- Reconciliation run
- Exception queue
- Refund approval
- Receipt view

### Logical API Operations
- Generate receipt
- Import settlement file
- Auto-match
- Resolve exception
- Refund request and approval

### Inputs
- Settlement files

### Outputs
- Matched records
- Receipts

### Business Rules
- Unmatched items must be resolved within 3 days

### Validations
- File format

### Calculations
- Collections vs settlement differences

### Workflow
Unmatched → Matched / Refund

### Search Requirements
- By transaction ID

### Documents
- Receipt

### Reports
- Daily collections
- Reconciliation

### Notifications
- Refund notice

### Security
- Finance only

### Integrations
- Gateway settlement API / files

### Dependencies
- F05-002
- F15-004

### Assumptions
- One gateway format

### Risks
- Format changes

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Reconciliation run | Medium | 6 |
| UI | Exception queue | Medium | 6 |
| UI | Refund approval | Easy | 4 |
| UI | Receipt view | Easy | 4 |
| API | Generate receipt | Easy | 4 |
| API | Import settlement file | Medium | 6 |
| API | Auto-match | Complex | 8 |
| API | Resolve exception | Medium | 6 |
| API | Refund request and approval | Medium | 6 |
| Database | Settlement, reconciliation and refund records | Medium | 4 |
| Testing | Reconciliation tests | Complex | 8 |
| Documentation | Finance reconciliation guide | Easy | 2 |

**Feature Total: 64 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 30 | 4 | 0 | 8 | 2 | **64** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Matching rated Complex
- No external integration channel in this feature; Integration row omitted.
