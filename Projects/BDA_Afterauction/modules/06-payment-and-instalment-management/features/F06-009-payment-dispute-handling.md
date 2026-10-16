# F06-009 — Payment Dispute Handling

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-009 |
| Feature Name | Payment Dispute Handling |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Registration of payment disputes by bidders or staff (amount debited but not credited, wrong amount, duplicate payment, receipt error), with acknowledgement number, assignment, investigation with gateway / bank references, resolution timelines, escalation and closure with resolution note.

### Business Objective
Resolve payment problems quickly and transparently, protecting bidders from wrongful default.

### Actors
- Successful Bidder
- Payment Reconciler
- Finance Officer

### User Journey
1. **Who creates:** The bidder (or staff on behalf) raises the dispute.
2. **How they create:** The bidder selects the transaction, chooses dispute type, enters details and uploads bank proof; an acknowledgement number is issued.
3. **How they edit:** The bidder can add information while the dispute is open.
4. **How they send for approval:** The dispute is assigned to the Payment Reconciler automatically.
5. **How the approver sees pending items:** The Payment Reconciler sees assigned disputes with SLA.
6. **How the approver decides:** The Payment Reconciler resolves (credit applied, refund initiated, rejected) or escalates to the Finance Officer.
7. **How the applicant / maker sees history:** The bidder sees status and resolution.
8. **How the approver / auditor sees history:** Auditors see dispute timeline.

### Functional Capabilities
- Dispute types and SLA per type
- Acknowledgement number and notifications
- Gateway status re-query from the dispute
- Hold on default proceedings while dispute open
- Escalation on SLA breach
- Resolution with ledger action

### UI Screens
- Raise dispute (bidder)
- Dispute status (bidder)
- Dispute queue
- Dispute investigation and resolution

### Logical API Operations
- Register dispute
- Assign and escalate
- Re-query gateway
- Resolve dispute with ledger action
- Hold default proceedings
- List disputes

### Inputs
- Transaction
- Type
- Details
- Proof

### Outputs
- Acknowledgement
- Resolution

### Business Rules
- Open dispute pauses default escalation for that instalment
- SLA per type

### Validations
- Transaction belongs to bidder

### Calculations
- SLA due date

### Workflow
Registered → Under Investigation → Resolved | Escalated → Resolved → Closed

### Search Requirements
- By acknowledgement number, site, status

### Documents
- Bank proof

### Reports
- Dispute ageing report

### Notifications
- Acknowledgement, updates, resolution

### Security
- Finance roles

### Integrations
- Gateway verify via F06-002 connector

### Dependencies
- F06-002
- F06-004
- F06-008

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Raise dispute (bidder) | Easy | 4 |
| UI | Dispute status (bidder) | Easy | 4 |
| UI | Dispute queue | Medium | 6 |
| UI | Dispute investigation and resolution | Medium | 6 |
| API | Register dispute | Easy | 4 |
| API | Assign and escalate | Medium | 6 |
| API | Re-query gateway | Easy | 4 |
| API | Resolve dispute with ledger action | Medium | 6 |
| API | Hold default proceedings | Easy | 4 |
| API | List disputes | Easy | 4 |
| Database | Dispute register | Easy | 2 |
| Testing | Dispute lifecycle tests | Medium | 6 |
| Documentation | Dispute handling guide | Easy | 2 |

**Feature Total: 58 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 28 | 2 | 0 | 6 | 2 | **58** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Reuses gateway verification
- No external integration channel in this feature; Integration row omitted.
