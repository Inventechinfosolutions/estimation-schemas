# F06-005 — Payment Status & Ledger Tracking

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-005 |
| Feature Name | Payment Status & Ledger Tracking |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Site-wise payment ledger showing demands, payments, interest, penalties, adjustments and outstanding balance, with stage status labels (25% / 75% / 100% Payment Completed), statement of account download and history for bidders and officials.

### Business Objective
Provide one authoritative view of each site's financial position used by bidders, DS offices and Finance.

### Actors
- Finance Officer
- Deputy Secretary
- Case Worker
- Successful Bidder

### User Journey
1. **Who creates:** Ledger entries are created by the system from demands, payments and adjustments.
2. **How they create:** Each confirmed event posts a ledger entry; status labels update automatically.
3. **How they edit:** Manual adjustments (e.g., refund of excess) are raised by the Finance Officer with reason.
4. **How they send for approval:** Manual adjustments go for approval by a senior Finance officer / Approving Authority.
5. **How the approver sees pending items:** The approver sees pending adjustments.
6. **How the approver decides:** The approver approves or rejects.
7. **How the applicant / maker sees history:** Bidders and officials see the ledger and statement of account.
8. **How the approver / auditor sees history:** Auditors see every ledger entry with source.

### Functional Capabilities
- Double-entry style ledger per site
- Status labels and milestone dates
- Interest and penalty postings from F06-007 / F06-008
- Manual adjustment with approval
- Statement of account PDF (bilingual)
- Trigger events on 25%, 75% and 100% completion to other modules

### UI Screens
- Site ledger view
- Statement of account
- Manual adjustment request
- Adjustment approval

### Logical API Operations
- Post ledger entry
- Compute balance and status
- Raise milestone events
- Manual adjustment with approval
- Generate statement
- Get ledger

### Inputs
- Demands, payments, adjustments

### Outputs
- Ledger
- Status
- Milestone events

### Business Rules
- Ledger entries are immutable; corrections by reversal
- Status computed from confirmed credits only

### Validations
- Adjustment reason mandatory

### Calculations
- Outstanding = demands + interest + penalty − payments − adjustments
- Paid % = confirmed payments / bid amount

### Workflow
Posted → (reversal) Reversed

### Search Requirements
- Ledgers by site, bidder, status

### Documents
- Statement of account

### Reports
- Outstanding by site

### Notifications
- Milestone notifications via F12-002

### Security
- Bidders see own ledger only; DS isolation for DS roles

### Integrations
- None

### Dependencies
- F06-001
- F06-002
- F06-003
- F07-001

### Assumptions
- None

### Risks
- Incorrect milestone events cascade; covered by tests

### Non Functional Requirements
- Ledger view under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Site ledger view | Medium | 6 |
| UI | Statement of account | Easy | 4 |
| UI | Manual adjustment request | Easy | 4 |
| UI | Adjustment approval | Easy | 4 |
| API | Post ledger entry | Medium | 6 |
| API | Compute balance and status | Medium | 6 |
| API | Raise milestone events | Complex | 8 |
| API | Manual adjustment with approval | Medium | 6 |
| API | Generate statement | Medium | 6 |
| API | Get ledger | Easy | 4 |
| Database | Site ledger | Medium | 4 |
| Testing | Ledger posting and balance tests | Complex | 8 |
| Testing | Milestone event tests | Medium | 6 |
| Documentation | Ledger reference | Easy | 2 |

**Feature Total: 74 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 36 | 4 | 0 | 14 | 2 | **74** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Milestone event publishing rated Complex
- No external integration channel in this feature; Integration row omitted.
