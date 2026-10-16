# F04-003 — Multi-Level Result Approval Workflow

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-003 |
| Feature Name | Multi-Level Result Approval Workflow |
| Module | 04 — Result Verification & Approval |
| Module Type | Business |
| Release | Go-live |

### Description
Configurable, multi-level approval of site results following the chain resolved from F02-003, with DSC-signed decisions (confirm, reject, order re-auction, return for clarification, refer to Government), site-wise and bulk decisions, delegation, SLA tracking and full decision history.

### Business Objective
Implement BDA's approval process digitally with signed, auditable decisions and reduce the time from auction closure to bidder intimation.

### Actors
- Approving Authority (each level)
- Result Verifier
- Auction Admin

### User Journey
1. **Who creates:** The Result Verifier creates approval requests by submitting sites (F04-001).
2. **How they create:** Submission creates an approval task at the first level of the resolved chain with the verification note and flags.
3. **How they edit:** The verifier edits only when a site is returned; returned sites go back to the workbench.
4. **How they send for approval:** Each level forwards automatically to the next on approval until the final level.
5. **How the approver sees pending items:** Each approver sees pending sites in My Approvals with flags, premium, ageing against SLA and the case file.
6. **How the approver decides:** The approver chooses confirm, reject, re-auction, return or refer to Government, enters remarks and signs with DSC (single or bulk).
7. **How the applicant / maker sees history:** The verifier and Auction Admin see the decision trail and current level for each site.
8. **How the approver / auditor sees history:** Auditors see each decision with signer, certificate, signed hash and time.

### Functional Capabilities
- Approval inbox per approver with filters and SLA ageing
- Decision options: confirm, reject, re-auction, return for clarification, refer to Government
- Mandatory remarks for reject, re-auction and return
- DSC signing of each decision (single and bulk signing of a selected list)
- Referral to Government with upload of Government order on receipt
- Delegation-aware routing
- Decision history with all levels
- Final outcome: Approved (to intimation), Rejected / Re-auction (to F04-005)

### UI Screens
- My Approvals inbox
- Approval decision screen with case summary
- Bulk approval and signing
- Government referral and order upload
- Decision history timeline
- Approval status tracker by auction

### Logical API Operations
- Create approval task
- List approval inbox
- Record decision with remarks
- Sign decision with DSC
- Bulk decide and sign
- Route to next level
- Refer to Government and record order
- Get decision history
- SLA ageing computation

### Inputs
- Decision
- Remarks
- DSC signature
- Government order file

### Outputs
- Signed decisions
- Final result status
- Trigger to intimation or rejection listing

### Business Rules
- An approver can decide only at their level and within their signing authority (F01-004)
- The same user cannot act at two levels for one site
- Bulk approval only for sites with identical decision and no flags requiring individual remarks
- Return sends the site back to the verifier, resetting later levels

### Validations
- DSC valid and authorised
- Remarks where mandatory

### Calculations
- SLA days elapsed at each level

### Workflow
Submitted → Level 1 … Level n → Approved | Rejected | Re-auction | Returned | Referred → Government order → Approved / Rejected

### Search Requirements
- Approvals by auction, site, level, status, age

### Documents
- Signed decision record
- Government order

### Reports
- Approval pendency by level
- Decisions by auction

### Notifications
- New task alert to approver
- Escalation on SLA breach
- Outcome to verifier and Auction Admin

### Security
- DSC mandatory for decisions
- Signed hash stored with decision

### Integrations
- Signing through F13-003

### Dependencies
- F02-003
- F01-004
- F13-003
- F04-001

### Assumptions
- Approvers have DSC tokens

### Risks
- Approver unavailability; delegation mitigates

### Non Functional Requirements
- Bulk signing of 100 sites within 2 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | My Approvals inbox | Medium | 6 |
| UI | Approval decision screen with case summary | Complex | 12 |
| UI | Bulk approval and signing | Complex | 12 |
| UI | Government referral and order upload | Medium | 6 |
| UI | Decision history timeline | Easy | 4 |
| UI | Approval status tracker by auction | Medium | 6 |
| API | Create approval task | Medium | 6 |
| API | List approval inbox | Medium | 6 |
| API | Record decision with remarks | Medium | 6 |
| API | Sign decision with DSC | Complex | 8 |
| API | Bulk decide and sign | Complex | 8 |
| API | Route to next level | Medium | 6 |
| API | Refer to Government and record order | Medium | 6 |
| API | Get decision history | Easy | 4 |
| API | SLA ageing computation | Easy | 4 |
| Database | Approval task and decision store | Medium | 4 |
| Testing | Multi-level routing tests across rules | Complex | 8 |
| Testing | Signing and bulk signing tests | Complex | 8 |
| Testing | Return and referral flow tests | Medium | 6 |
| Documentation | Approver user guide | Medium | 3 |

**Feature Total: 129 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 46 | 54 | 4 | 0 | 22 | 3 | **129** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Signing is via shared service; workflow routing rated Complex
- No external integration channel in this feature; Integration row omitted.
