# F15-004 — Payment Gateway Integration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F15-004 |
| Feature Name | Payment Gateway Integration |
| Module | 15 — Integration Hub |
| Module Type | Technical |
| Release | Go-live |

### Description
Integration with the KEONICS-designated payment gateway: order creation, redirect / SDK, callback with signature verification, status inquiry, refund API, and settlement report download.

### Business Objective
Enable online fee collection.

### Actors
- System

### User Journey
1. **Who creates:** Calls triggered by payment flow.
2. **How they create:** Connector creates orders and processes callbacks.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Finance sees failures.
6. **How the approver decides:** Finance resolves via reconciliation.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see gateway logs.

### Functional Capabilities
- Order creation
- Callback verification
- Status inquiry
- Refund API
- Settlement download

### UI Screens
- None (no user interface in this feature)

### Logical API Operations
- Gateway order adapter
- Callback verifier
- Refund adapter
- Settlement fetch

### Inputs
- Orders

### Outputs
- Payment status

### Business Rules
- Verify amount and signature

### Validations
- Signature

### Calculations
- None

### Workflow
Order → Paid / Failed

### Search Requirements
- None

### Documents
- None

### Reports
- Gateway logs

### Notifications
- None

### Security
- PCI scope minimised

### Integrations
- Gateway

### Dependencies
- F15-001

### Assumptions
- KEONICS gateway account

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Gateway order adapter | Medium | 6 |
| API | Callback verifier | Medium | 6 |
| API | Refund adapter | Easy | 4 |
| API | Settlement fetch | Easy | 4 |
| Database | Gateway log | Easy | 2 |
| Integration | Payment gateway API | Complex | 24 |
| Testing | Gateway integration tests | Complex | 8 |
| Documentation | Gateway integration note | Easy | 2 |

**Feature Total: 56 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 2 | 24 | 8 | 2 | **56** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One gateway
