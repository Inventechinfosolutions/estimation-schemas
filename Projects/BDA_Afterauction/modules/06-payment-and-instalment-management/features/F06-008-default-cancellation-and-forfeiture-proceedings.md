# F06-008 — Default, Cancellation & Forfeiture Proceedings

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-008 |
| Feature Name | Default, Cancellation & Forfeiture Proceedings |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Rule-based handling of payment defaults: identification of default-eligible sites, show-cause notice generation and dispatch, bidder reply capture, hearing record, cancellation order with DSC, forfeiture computation of EMD / amount paid, refund computation where applicable, and listing of the site for re-auction with status update to the allotment section and CDRMS.

### Business Objective
Apply default rules uniformly with a complete legal record and return defaulted sites to the auction pipeline.

### Actors
- Finance Officer
- Approving Authority
- Auction Admin
- Successful Bidder

### User Journey
1. **Who creates:** The Finance Officer initiates proceedings for default-eligible sites.
2. **How they create:** The Finance Officer selects the site, generates the show-cause notice from the template, and submits it for signature.
3. **How they edit:** The Finance Officer can edit the notice draft before signature.
4. **How they send for approval:** The notice goes for signature to the Approving Authority.
5. **How the approver sees pending items:** The Approving Authority sees notices and later cancellation proposals in My Approvals.
6. **How the approver decides:** The Approving Authority signs the notice; after reply / hearing, approves cancellation or drops proceedings with remarks.
7. **How the applicant / maker sees history:** The bidder sees notices, replies and orders in the portal and can submit a reply with documents.
8. **How the approver / auditor sees history:** Auditors see each step with documents and signatures.

### Functional Capabilities
- Default-eligible list from F06-006
- Show-cause notice generation, signing and dispatch
- Bidder reply submission with documents and deadline
- Hearing date and record
- Decision: drop, extend, cancel
- Cancellation order with DSC
- Forfeiture and refund computation per rules
- Site status update and re-auction listing

### UI Screens
- Default-eligible sites list
- Proceedings case view
- Show-cause notice preparation
- Bidder reply (portal)
- Hearing record
- Cancellation decision and order
- Forfeiture / refund computation

### Logical API Operations
- Initiate proceedings
- Generate and sign notice
- Submit bidder reply
- Record hearing
- Decide proceedings
- Compute forfeiture and refund
- Cancel allotment and list for re-auction
- Proceedings register

### Inputs
- Site
- Notice text
- Reply
- Hearing notes
- Decision

### Outputs
- Signed notices and orders
- Forfeiture / refund amounts
- Re-auction listing

### Business Rules
- Notice only after overdue limit
- Reply period per rules
- Cancellation needs Approving Authority signature
- Cancelled sites close bidder access to payment

### Validations
- Mandatory remarks

### Calculations
- Forfeiture = rule % of amount paid (or EMD)
- Refund = amount paid − forfeiture − dues

### Workflow
Initiated → Notice Issued → Reply / Hearing → Dropped | Extended | Cancelled → Re-auction listed

### Search Requirements
- Proceedings by status, site, DS

### Documents
- Notice, reply, hearing record, cancellation order

### Reports
- Default and cancellation report

### Notifications
- Notice dispatch and decision notices

### Security
- Signed orders; restricted roles

### Integrations
- Status to CDRMS through F09-004 path

### Dependencies
- F06-006
- F02-001
- F02-005
- F13-003
- F09-004

### Assumptions
- Refunds paid outside Module by Finance

### Risks
- Legal challenges; complete record mitigates

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Default-eligible sites list | Easy | 4 |
| UI | Proceedings case view | Medium | 6 |
| UI | Show-cause notice preparation | Medium | 6 |
| UI | Bidder reply (portal) | Easy | 4 |
| UI | Hearing record | Easy | 4 |
| UI | Cancellation decision and order | Medium | 6 |
| UI | Forfeiture / refund computation | Medium | 6 |
| API | Initiate proceedings | Medium | 6 |
| API | Generate and sign notice | Medium | 6 |
| API | Submit bidder reply | Easy | 4 |
| API | Record hearing | Easy | 4 |
| API | Decide proceedings | Medium | 6 |
| API | Compute forfeiture and refund | Complex | 8 |
| API | Cancel allotment and list for re-auction | Complex | 8 |
| API | Proceedings register | Easy | 4 |
| Database | Default proceedings store | Medium | 4 |
| Testing | Proceedings flow tests | Complex | 8 |
| Testing | Forfeiture computation tests | Medium | 6 |
| Documentation | Default proceedings guide | Easy | 2 |

**Feature Total: 102 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | 46 | 4 | 0 | 14 | 2 | **102** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Cancellation cascade rated Complex
- No external integration channel in this feature; Integration row omitted.
