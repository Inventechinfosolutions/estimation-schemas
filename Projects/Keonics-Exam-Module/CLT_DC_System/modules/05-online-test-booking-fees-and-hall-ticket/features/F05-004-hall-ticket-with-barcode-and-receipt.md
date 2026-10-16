# F05-004 — Hall Ticket with Barcode & Receipt

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-004 |
| Feature Name | Hall Ticket with Barcode & Receipt |
| Module | 05 — Online Test Booking, Fees & Hall Ticket |
| Module Type | Business |
| Release | Go-live |

### Description
Generation of bilingual hall ticket PDF with barcode / QR encoding a signed token, candidate name, registration and hall ticket number, session, centre address, reporting time, payment receipt details and instructions, without photograph, dispatched by e-mail and SMS link and downloadable anytime; regenerated on rescheduling.

### Business Objective
Give candidates a verifiable admission document as required by the RFP.

### Actors
- Candidate
- Proctor (scan)

### User Journey
1. **Who creates:** The system generates the hall ticket on booking confirmation.
2. **How they create:** The PDF is created from the approved template and sent by e-mail and SMS.
3. **How they edit:** Rescheduling regenerates the hall ticket and voids the old barcode.
4. **How they send for approval:** No approval.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate downloads the hall ticket from portal or app.
8. **How the approver / auditor sees history:** Proctors scan the barcode at the centre (F08-003).

### Functional Capabilities
- Signed barcode / QR token
- Template-based PDF
- No photograph per RFP
- Receipt details printed
- E-mail and SMS dispatch
- Void on reschedule
- Bulk regeneration

### UI Screens
- Hall ticket download
- Hall ticket admin search and resend

### Logical API Operations
- Generate hall ticket PDF
- Create signed barcode token
- Dispatch hall ticket
- Void and regenerate
- Verify barcode token

### Inputs
- Booking

### Outputs
- Hall ticket

### Business Rules
- Only latest hall ticket valid

### Validations
- Barcode signature

### Calculations
- None

### Workflow
Issued → Void → Reissued

### Search Requirements
- By hall ticket number

### Documents
- Hall ticket PDF

### Reports
- Hall tickets issued

### Notifications
- Hall ticket e-mail / SMS

### Security
- Signed token prevents forgery

### Integrations
- E-mail / SMS via F14-002

### Dependencies
- F02-005
- F05-001
- F14-002

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Generation under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Hall ticket download | Easy | 4 |
| UI | Hall ticket admin search and resend | Easy | 4 |
| API | Generate hall ticket PDF | Medium | 6 |
| API | Create signed barcode token | Medium | 6 |
| API | Dispatch hall ticket | Easy | 4 |
| API | Void and regenerate | Easy | 4 |
| API | Verify barcode token | Medium | 6 |
| Database | Hall ticket records | Easy | 2 |
| Testing | Hall ticket generation and barcode tests | Medium | 6 |
| Documentation | Hall ticket format note | Simple | 1 |

**Feature Total: 43 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 26 | 2 | 0 | 6 | 1 | **43** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Uses template renderer
- No external integration channel in this feature; Integration row omitted.
