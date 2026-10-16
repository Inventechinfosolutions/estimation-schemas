# F04-005 — Rejected & Unsold Site Intimation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-005 |
| Feature Name | Rejected & Unsold Site Intimation |
| Module | 04 — Result Verification & Approval |
| Module Type | Business |
| Release | Go-live |

### Description
Listing of sites rejected or ordered for re-auction and sites unsold in KPPP (no bids), generation of the intimation to the allotment section with reasons, and status update so those sites can be taken up for re-auction.

### Business Objective
Close the loop on sites that will not proceed and hand them back to the allotment section promptly.

### Actors
- Auction Admin
- Allotment Section (recipient)
- Approving Authority (signature)

### User Journey
1. **Who creates:** The system lists the sites automatically after final decisions; the Auction Admin prepares the intimation.
2. **How they create:** The Auction Admin opens Rejected / Unsold Sites, selects sites, and generates the intimation letter from the template.
3. **How they edit:** The Auction Admin can edit the covering text before submission.
4. **How they send for approval:** The Auction Admin submits the intimation for signature.
5. **How the approver sees pending items:** The Approving Authority sees it in My Approvals.
6. **How the approver decides:** The Approving Authority signs or returns.
7. **How the applicant / maker sees history:** The Auction Admin sees intimation history and acknowledgement status.
8. **How the approver / auditor sees history:** Auditors see lists, letters and signatures.

### Functional Capabilities
- Lists of rejected, re-auction and unsold sites by auction
- Intimation letter generation and DSC signature
- Dispatch to allotment section by e-mail and in-system acknowledgement
- Status update of the site to Returned for Re-auction
- No bidder intimation for these sites

### UI Screens
- Rejected / unsold sites list
- Intimation preparation
- Acknowledgement tracking

### Logical API Operations
- List rejected / unsold sites
- Generate intimation
- Sign and dispatch intimation
- Record acknowledgement
- Update site status

### Inputs
- Selected sites
- Covering text

### Outputs
- Signed intimation
- Updated site status

### Business Rules
- Each site appears in one intimation
- Re-auction sites keep their full history

### Validations
- Sites in final rejected / re-auction / unsold status

### Calculations
- None

### Workflow
Listed → Intimation signed → Acknowledged

### Search Requirements
- By auction, reason

### Documents
- Signed intimation letter

### Reports
- Rejected and unsold sites report

### Notifications
- E-mail to allotment section

### Security
- Auction Admin and Approving Authority only

### Integrations
- E-mail through F12-003; status through F09-004 path where CDRMS is updated

### Dependencies
- F04-003
- F02-005
- F09-004

### Assumptions
- Allotment section has an official e-mail

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Rejected / unsold sites list | Easy | 4 |
| UI | Intimation preparation | Medium | 6 |
| UI | Acknowledgement tracking | Easy | 4 |
| API | List rejected / unsold sites | Easy | 4 |
| API | Generate intimation | Medium | 6 |
| API | Sign and dispatch intimation | Medium | 6 |
| API | Record acknowledgement | Easy | 4 |
| API | Update site status | Easy | 4 |
| Database | Intimation register | Easy | 2 |
| Testing | Listing, intimation and status tests | Medium | 6 |
| Documentation | Procedure note | Simple | 1 |

**Feature Total: 47 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 24 | 2 | 0 | 6 | 1 | **47** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small workflow reusing templates and signing
- No external integration channel in this feature; Integration row omitted.
