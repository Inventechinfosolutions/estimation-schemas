# F16-003 — Migrated Case Activation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-003 |
| Feature Name | Migrated Case Activation |
| Module | 16 — Legacy Case Migration |
| Module Type | Technical |
| Release | Go-live |

### Description
Activation of signed-off cases into live tables at the correct stage (awaiting payment, DS processing, draft deed, registration), creation of bidder accounts, schedules, ledgers and timers, and notification to bidders where configured.

### Business Objective
Make migrated cases fully workable in the live system.

### Actors
- Migration team
- Auction Admin

### User Journey
1. **Who creates:** The migration team activates batches.
2. **How they create:** Activation creates live records and accounts.
3. **How they edit:** Not editable; rollback by batch if needed before go-live.
4. **How they send for approval:** Activation requires Auction Admin approval.
5. **How the approver sees pending items:** Auction Admin sees batches ready.
6. **How the approver decides:** Auction Admin approves activation.
7. **How the applicant / maker sees history:** Bidders see migrated sites.
8. **How the approver / auditor sees history:** Activation logged.

### Functional Capabilities
- Stage placement
- Account, schedule and ledger creation
- Timer initialisation
- Batch rollback
- Bidder notification

### UI Screens
- Activation batches

### Logical API Operations
- Activate batch to live
- Rollback batch
- Notify bidders

### Inputs
- Signed-off data

### Outputs
- Live cases

### Business Rules
- Migrated records flagged as migrated

### Validations
- Stage consistency

### Calculations
- None

### Workflow
Ready → Activated

### Search Requirements
- Batches

### Documents
- None

### Reports
- Activation report

### Notifications
- Bidder notices

### Security
- Restricted

### Integrations
- None

### Dependencies
- F16-002
- F05-001
- F06-001

### Assumptions
- None

### Risks
- Stage mismatches

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Activation batches | Easy | 4 |
| API | Activate batch to live | Complex | 8 |
| API | Rollback batch | Medium | 6 |
| API | Notify bidders | Easy | 4 |
| Testing | Activation and stage placement tests | Medium | 6 |
| Documentation | Activation runbook | Easy | 2 |

**Feature Total: 30 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 18 | 0 | 0 | 6 | 2 | **30** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Activation rated Complex
- No external integration channel in this feature; Integration row omitted.
