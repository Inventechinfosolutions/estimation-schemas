# F08-003 — Candidate Identity Validation & Photo Capture

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-003 |
| Feature Name | Candidate Identity Validation & Photo Capture |
| Module | 08 — Test Centre Operations & Candidate Validation |
| Module Type | Business |
| Release | Go-live |

### Description
Entry validation console: proctor scans hall ticket barcode, system shows registration photo, HRMS / eKYC details and booking; proctor checks employee ID card or certified photograph, captures a live photo, and marks verified, rejected (with reason) or impersonation suspected.

### Business Objective
Ensure the right candidate takes the test.

### Actors
- Proctor
- Candidate

### User Journey
1. **Who creates:** The proctor starts validation as candidates arrive.
2. **How they create:** The proctor scans the barcode, compares details and captures a live photo.
3. **How they edit:** The proctor can correct a mistaken decision before session start with reason.
4. **How they send for approval:** Rejections are reported to EMU.
5. **How the approver sees pending items:** EMU sees rejections.
6. **How the approver decides:** EMU confirms or overrides.
7. **How the applicant / maker sees history:** Candidates see status on the terminal login.
8. **How the approver / auditor sees history:** Auditors see validation records with photos.

### Functional Capabilities
- Barcode scan and token verification
- Side-by-side registration vs live photo
- Document check checklist
- Live photo capture
- Reject / impersonation flags
- Late entry block after cut-off

### UI Screens
- Candidate validation console
- Live photo capture
- Validation summary

### Logical API Operations
- Verify hall ticket token
- Fetch candidate validation profile
- Store live photo
- Record validation decision
- Optional face match score

### Inputs
- Barcode
- Live photo

### Outputs
- Verified candidates

### Business Rules
- Unverified candidates cannot log in
- Entry closes at configured time; no compensation for late entry

### Validations
- Valid token for this session and centre

### Calculations
- Face match score (advisory)

### Workflow
Pending → Verified / Rejected

### Search Requirements
- By hall ticket

### Documents
- Live photo

### Reports
- Validation report

### Notifications
- Rejection alert to EMU

### Security
- Photos encrypted

### Integrations
- None

### Dependencies
- F05-004
- F08-005

### Assumptions
- Barcode scanners or webcams available

### Risks
- Queue delays

### Non Functional Requirements
- Validation under 30 seconds per candidate

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Candidate validation console | Complex | 12 |
| UI | Live photo capture | Medium | 6 |
| UI | Validation summary | Easy | 4 |
| API | Verify hall ticket token | Medium | 6 |
| API | Fetch candidate validation profile | Medium | 6 |
| API | Store live photo | Easy | 4 |
| API | Record validation decision | Medium | 6 |
| API | Optional face match score | Complex | 8 |
| Database | Validation records and photos | Medium | 4 |
| Testing | Validation tests | Medium | 6 |
| Documentation | Validation SOP | Easy | 2 |

**Feature Total: 64 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 30 | 4 | 0 | 6 | 2 | **64** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Face match advisory only
- No external integration channel in this feature; Integration row omitted.
