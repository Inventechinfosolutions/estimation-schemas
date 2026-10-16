# F05-003 — Bilingual Signed Intimation Letter

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-003 |
| Feature Name | Bilingual Signed Intimation Letter |
| Module | 05 — Successful Bidder Notification & Account |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of the result intimation letter to the successful bidder in Kannada and English from the approved template, with site details, bid amount, EMD adjustment, instalment schedule and due dates, payment instructions and portal login details, signed with DSC by the authorised officer.

### Business Objective
Issue the legally required intimation promptly in both languages with an accurate schedule.

### Actors
- Auction Admin
- Approving Authority / authorised signatory

### User Journey
1. **Who creates:** The system generates the letter automatically after approval; the authorised officer signs it.
2. **How they create:** The letter is generated with the instalment schedule from F06-001 and placed in the signing queue.
3. **How they edit:** The Auction Admin can regenerate after correcting source data; manual text edits are not allowed.
4. **How they send for approval:** Generated letters go to the signatory's queue.
5. **How the approver sees pending items:** The signatory sees letters pending signature with preview.
6. **How the approver decides:** The signatory signs individually or in bulk, or returns with remarks.
7. **How the applicant / maker sees history:** The Auction Admin sees letter status and versions per site; the bidder sees the signed letter in the portal.
8. **How the approver / auditor sees history:** Auditors see template version, generation, signing and dispatch.

### Functional Capabilities
- Bilingual letter (Kannada and English sections or two documents)
- Merge of instalment schedule and EMD adjustment
- QR code to verify authenticity
- Single and bulk DSC signing
- Letter number series by year
- Version control on regeneration

### UI Screens
- Letter generation status by auction
- Letter preview (Kannada / English)
- Signing queue with bulk sign
- Letter verification page (QR)

### Logical API Operations
- Generate intimation letter
- Assign letter number
- Sign letter(s)
- Regenerate letter version
- Verify letter by QR
- Get letter for bidder

### Inputs
- Approved result
- Schedule
- Template
- Signature

### Outputs
- Signed bilingual intimation letter
- Letter number

### Business Rules
- Letter cannot be issued unsigned
- Intimation date = signing date and starts the 25% payment clock
- Regeneration after dispatch requires reason and re-dispatch

### Validations
- Schedule present
- Signatory authorised

### Calculations
- Due dates from F06-001

### Workflow
Generated → Signed → Dispatched (F05-004)

### Search Requirements
- Letters by number, auction, bidder

### Documents
- Signed intimation letter PDF

### Reports
- Letters issued by auction

### Notifications
- Signing request to officer

### Security
- DSC; QR verification page shows only minimal data

### Integrations
- Signing through F13-003

### Dependencies
- F02-005
- F06-001
- F13-003
- F04-003

### Assumptions
- Template approved before first auction

### Risks
- Kannada rendering quality

### Non Functional Requirements
- Bulk generation of 500 letters within 10 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Letter generation status by auction | Easy | 4 |
| UI | Letter preview (Kannada / English) | Medium | 6 |
| UI | Signing queue with bulk sign | Medium | 6 |
| UI | Letter verification page (QR) | Easy | 4 |
| API | Generate intimation letter | Medium | 6 |
| API | Assign letter number | Simple | 2 |
| API | Sign letter(s) | Medium | 6 |
| API | Regenerate letter version | Easy | 4 |
| API | Verify letter by QR | Easy | 4 |
| API | Get letter for bidder | Easy | 4 |
| Database | Letter register with versions | Easy | 2 |
| Testing | Letter generation and bilingual rendering tests | Medium | 6 |
| Testing | Signing and verification tests | Medium | 6 |
| Documentation | Intimation process note | Simple | 1 |

**Feature Total: 61 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 26 | 2 | 0 | 12 | 1 | **61** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Rendering via F02-005 engine
- No external integration channel in this feature; Integration row omitted.
