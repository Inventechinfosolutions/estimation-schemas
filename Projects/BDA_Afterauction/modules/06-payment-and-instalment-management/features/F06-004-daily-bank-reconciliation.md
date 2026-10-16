# F06-004 — Daily Bank Reconciliation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-004 |
| Feature Name | Daily Bank Reconciliation |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Daily reconciliation of gateway transactions and offline credits with bank settlement / statement files (automatic fetch or upload), auto-matching by reference and amount, manual matching for exceptions, and reports of mismatches, pending credits and unclaimed receipts, with the previous day's reconciliation completed by 11:00 hours.

### Business Objective
Ensure every rupee recorded in the Module matches bank credits and give Finance a daily controlled view.

### Actors
- Payment Reconciler
- Finance Officer
- System

### User Journey
1. **Who creates:** The system imports settlement files; the Payment Reconciler performs reconciliation.
2. **How they create:** Settlement files are fetched or uploaded daily; auto-matching runs and creates matched, unmatched and partially matched lists.
3. **How they edit:** The Payment Reconciler manually matches or marks exceptions with remarks.
4. **How they send for approval:** The Payment Reconciler submits the day's reconciliation for Finance Officer sign-off.
5. **How the approver sees pending items:** The Finance Officer sees daily reconciliation status and exceptions.
6. **How the approver decides:** The Finance Officer signs off or returns.
7. **How the applicant / maker sees history:** The Payment Reconciler sees reconciliation history by date.
8. **How the approver / auditor sees history:** Auditors see files, matches, manual actions and sign-offs.

### Functional Capabilities
- Settlement file import (gateway MIS and bank statement formats)
- Auto-match rules by transaction reference, UTR, amount and date tolerance
- Manual match and split / merge matching
- Exception types: credit without transaction, transaction without credit, amount mismatch, duplicate
- Daily sign-off by Finance Officer
- Scheduled job to complete reconciliation by 11:00 hours

### UI Screens
- Reconciliation dashboard by date
- Settlement file upload and status
- Matching workspace
- Exception list with remarks
- Daily sign-off

### Logical API Operations
- Import settlement file
- Parse bank / gateway formats
- Auto-match
- Manual match / unmatch
- Mark exception
- Sign off day
- Reconciliation status

### Inputs
- Settlement files
- Manual matches
- Remarks

### Outputs
- Reconciled transactions
- Exception reports
- Sign-off

### Business Rules
- Day closed only after Finance sign-off
- Unmatched credits older than 3 days escalate
- Matched lines cannot be unmatched after sign-off without Finance Officer approval

### Validations
- File format and checksum
- No duplicate files

### Calculations
- Totals per day: transactions, credits, differences

### Workflow
Imported → Auto-matched → Manually resolved → Submitted → Signed off

### Search Requirements
- By date, reference, amount, status

### Documents
- Settlement files retained

### Reports
- Daily reconciliation report
- Pending credits
- Mismatch report

### Notifications
- Alert if reconciliation not completed by 11:00

### Security
- Finance roles only

### Integrations
- Bank / gateway settlement files

### Dependencies
- F06-002
- F06-003
- F13-001

### Assumptions
- One bank / gateway format at go-live

### Risks
- Format changes by bank

### Non Functional Requirements
- Reconciliation of 10,000 lines within 5 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Reconciliation dashboard by date | Medium | 6 |
| UI | Settlement file upload and status | Easy | 4 |
| UI | Matching workspace | Complex | 12 |
| UI | Exception list with remarks | Medium | 6 |
| UI | Daily sign-off | Easy | 4 |
| API | Import settlement file | Medium | 6 |
| API | Parse bank / gateway formats | Complex | 8 |
| API | Auto-match | Complex | 8 |
| API | Manual match / unmatch | Medium | 6 |
| API | Mark exception | Easy | 4 |
| API | Sign off day | Easy | 4 |
| API | Reconciliation status | Easy | 4 |
| Database | Settlement lines and match records | Medium | 4 |
| Integration | Gateway settlement / bank statement file intake (SFTP or API) | Medium | 16 |
| Testing | Matching rule tests | Complex | 8 |
| Testing | File parsing tests per format | Medium | 6 |
| Testing | Sign-off and exception tests | Easy | 4 |
| Documentation | Reconciliation procedure | Easy | 2 |

**Feature Total: 112 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 40 | 4 | 16 | 18 | 2 | **112** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Medium integration row for file intake
