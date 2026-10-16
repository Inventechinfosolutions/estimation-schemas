# F10-003 — Bidder Payment History & Receipts

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-003 |
| Feature Name | Bidder Payment History & Receipts |
| Module | 10 — Bidder Tracking Portal |
| Module Type | Business |
| Release | Go-live |

### Description
Bidder view of instalment schedule, dues, payments made (online and offline), receipts download, extension and dispute status, and statement of account, with links to pay, request extension and raise dispute.

### Business Objective
Self-service payment information for bidders.

### Actors
- Successful Bidder

### User Journey
1. **Who creates:** Records come from Module 06.
2. **How they create:** The bidder opens Payments for a site.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The bidder sees full payment history.
8. **How the approver / auditor sees history:** Auditors see access logs.

### Functional Capabilities
- Schedule and dues
- Payment history
- Receipts and statement download
- Links to pay, extension, dispute

### UI Screens
- Payments overview
- Payment history and receipts
- Statement of account download

### Logical API Operations
- Get bidder schedule and dues
- Get payment history
- Download receipt / statement

### Inputs
- Site

### Outputs
- Payment views

### Business Rules
- Own sites only

### Validations
- Ownership

### Calculations
- Outstanding

### Workflow
Not applicable

### Search Requirements
- By date

### Documents
- Receipts

### Reports
- None

### Notifications
- None

### Security
- Bidder isolation

### Integrations
- None

### Dependencies
- F06-001
- F06-002
- F06-005

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Payments overview | Medium | 6 |
| UI | Payment history and receipts | Easy | 4 |
| UI | Statement of account download | Simple | 2 |
| API | Get bidder schedule and dues | Easy | 4 |
| API | Get payment history | Easy | 4 |
| API | Download receipt / statement | Easy | 4 |
| Testing | Bidder payment view tests | Easy | 4 |
| Documentation | Bidder help: payments | Simple | 1 |

**Feature Total: 29 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 12 | 0 | 0 | 4 | 1 | **29** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Reuses Module 06 services
- No external integration channel in this feature; Integration row omitted.
