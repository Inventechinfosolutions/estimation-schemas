# F06-007 — Payment Extension Requests

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-007 |
| Feature Name | Payment Extension Requests |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Online request by the bidder for extension of an instalment due date with reason and documents, computation of interest or penalty per rules, multi-level approval, revised schedule, extension order and payment of the extension charge.

### Business Objective
Handle extensions consistently as per BDA rules, with transparent charges and approvals.

### Actors
- Successful Bidder
- Finance Officer
- Approving Authority

### User Journey
1. **Who creates:** The bidder creates the extension request.
2. **How they create:** The bidder selects the instalment, enters requested days and reason, uploads documents, sees the computed charge and submits.
3. **How they edit:** The bidder can edit or withdraw until review starts.
4. **How they send for approval:** The request goes to the Finance Officer and then the Approving Authority as configured.
5. **How the approver sees pending items:** Approvers see pending requests with eligibility check and charge.
6. **How the approver decides:** Approvers approve (with possibly fewer days), reject or return; final approval issues a signed extension order.
7. **How the applicant / maker sees history:** The bidder sees status, order and revised schedule.
8. **How the approver / auditor sees history:** Auditors see requests, computations and decisions.

### Functional Capabilities
- Eligibility checks (max extensions, max days, not in default)
- Charge computation (interest / penalty)
- Multi-level approval with DSC on order
- Extension order generation
- Schedule revision and reminder reset
- Charge added as a demand

### UI Screens
- Extension request form (bidder)
- Request status (bidder)
- Extension review and decision
- Extension order preview
- Extension register

### Logical API Operations
- Check eligibility
- Compute extension charge
- Submit / withdraw request
- Decide request
- Generate and sign order
- Revise schedule and add charge demand
- List requests

### Inputs
- Instalment
- Days
- Reason
- Documents
- Decision

### Outputs
- Extension order
- Revised schedule
- Charge demand

### Business Rules
- Extension limits from rule version
- Request must be before due date + grace (configurable)
- Charge payable as per rule

### Validations
- Days within limit
- Reason mandatory

### Calculations
- Charge = amount × rate × days / 365 or flat penalty

### Workflow
Submitted → Under Review → Approved (order) | Rejected | Returned

### Search Requirements
- By site, status

### Documents
- Supporting documents
- Extension order

### Reports
- Extension register

### Notifications
- Status updates to bidder

### Security
- DSC on order

### Integrations
- Signing via F13-003

### Dependencies
- F02-001
- F06-001
- F13-003

### Assumptions
- Rules defined by BDA

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Extension request form (bidder) | Medium | 6 |
| UI | Request status (bidder) | Easy | 4 |
| UI | Extension review and decision | Medium | 6 |
| UI | Extension order preview | Easy | 4 |
| UI | Extension register | Easy | 4 |
| API | Check eligibility | Medium | 6 |
| API | Compute extension charge | Medium | 6 |
| API | Submit / withdraw request | Easy | 4 |
| API | Decide request | Medium | 6 |
| API | Generate and sign order | Medium | 6 |
| API | Revise schedule and add charge demand | Medium | 6 |
| API | List requests | Easy | 4 |
| Database | Extension request store | Easy | 2 |
| Testing | Eligibility and charge tests | Medium | 6 |
| Testing | Approval and schedule revision tests | Medium | 6 |
| Documentation | Extension process guide | Easy | 2 |

**Feature Total: 78 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | 38 | 2 | 0 | 12 | 2 | **78** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Reuses approval and signing services
- No external integration channel in this feature; Integration row omitted.
