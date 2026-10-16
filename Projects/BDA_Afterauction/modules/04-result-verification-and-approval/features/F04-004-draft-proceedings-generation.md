# F04-004 — Draft Proceedings Generation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-004 |
| Feature Name | Draft Proceedings Generation |
| Module | 04 — Result Verification & Approval |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of draft proceedings for the approval of auction results from the approved template, listing sites, bidders, amounts and decisions per auction, with editing by the Auction Admin, approval and DSC signature, and issue of the signed proceedings PDF.

### Business Objective
Produce the formal record of result approval quickly and consistently.

### Actors
- Auction Admin
- Approving Authority

### User Journey
1. **Who creates:** The Auction Admin generates the proceedings for an auction once decisions are complete.
2. **How they create:** The Auction Admin selects the auction, chooses Generate Proceedings, and the system fills the template with all decided sites.
3. **How they edit:** The Auction Admin edits permitted text blocks and regenerates; each regeneration is a new draft version.
4. **How they send for approval:** The Auction Admin submits the draft for signature.
5. **How the approver sees pending items:** The Approving Authority sees the draft in My Approvals with preview.
6. **How the approver decides:** The Approving Authority signs with DSC or returns with remarks.
7. **How the applicant / maker sees history:** The Auction Admin sees versions and the signed final.
8. **How the approver / auditor sees history:** Auditors see versions, template version used and signature details.

### Functional Capabilities
- Template-based generation with site tables
- Editable narrative sections; data tables locked
- Version history
- DSC signature and issue number
- Signed PDF with QR code for verification

### UI Screens
- Proceedings generation and editor
- Proceedings preview
- Signature / return screen
- Proceedings register

### Logical API Operations
- Generate proceedings draft
- Save edited draft
- Submit for signature
- Sign and issue proceedings
- List proceedings
- Verify proceedings by QR

### Inputs
- Auction ID
- Edited text
- Signature

### Outputs
- Signed proceedings PDF
- Issue number

### Business Rules
- Generated only when every site in the auction has a final decision or is explicitly excluded
- Signed proceedings cannot be changed; corrections need a new proceedings with reference

### Validations
- Approved template exists

### Calculations
- Totals of sites, upset value, bid value

### Workflow
Draft → Submitted → Signed / Returned

### Search Requirements
- Proceedings by auction and date

### Documents
- Draft and signed proceedings PDF

### Reports
- Proceedings register

### Notifications
- Signature request and outcome

### Security
- DSC signature

### Integrations
- F13-003 signing

### Dependencies
- F02-005
- F04-003
- F13-003

### Assumptions
- One proceedings per auction

### Risks
- None significant

### Non Functional Requirements
- Generation within 10 seconds for 500 sites

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Proceedings generation and editor | Medium | 6 |
| UI | Proceedings preview | Easy | 4 |
| UI | Signature / return screen | Easy | 4 |
| UI | Proceedings register | Easy | 4 |
| API | Generate proceedings draft | Medium | 6 |
| API | Save edited draft | Easy | 4 |
| API | Submit for signature | Easy | 4 |
| API | Sign and issue proceedings | Medium | 6 |
| API | List proceedings | Easy | 4 |
| API | Verify proceedings by QR | Easy | 4 |
| Database | Proceedings register with versions | Easy | 2 |
| Testing | Generation and signing tests | Medium | 6 |
| Documentation | Proceedings procedure | Simple | 1 |

**Feature Total: 55 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 28 | 2 | 0 | 6 | 1 | **55** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Uses common template renderer
- No external integration channel in this feature; Integration row omitted.
