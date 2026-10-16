# F03-002 — Controlled KPPP Result Report Upload

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-002 |
| Feature Name | Controlled KPPP Result Report Upload |
| Module | 03 — KPPP Result Intake & Site Package |
| Module Type | Business |
| Release | Go-live |

### Description
Upload of KPPP auction result reports (Excel and PDF as downloaded from KPPP) by the Auction Admin when the API is not available, with template detection, row-level validation, maker-checker confirmation and integrity locking of the uploaded files.

### Business Objective
Ensure the post-auction process is not blocked if the KPPP API is unavailable, while keeping evidence-grade control over the uploaded data.

### Actors
- Auction Admin (maker)
- Result Verifier (checker)

### User Journey
1. **Who creates:** The Auction Admin uploads the result report for a closed auction.
2. **How they create:** The Auction Admin selects Upload Result, enters auction ID and closure date, attaches the KPPP Excel report and the signed PDF report, and the system parses and validates every row.
3. **How they edit:** The Auction Admin can correct mapping of columns or discard and re-upload before submission; parsed values themselves cannot be edited.
4. **How they send for approval:** The Auction Admin submits the upload for checker confirmation.
5. **How the approver sees pending items:** The Result Verifier sees pending uploads with parsed rows side by side with the PDF.
6. **How the approver decides:** The Result Verifier confirms (records created and files locked with hash) or rejects with reason.
7. **How the applicant / maker sees history:** The Auction Admin sees upload history and status.
8. **How the approver / auditor sees history:** Auditors see file hashes, maker, checker and timestamps.

### Functional Capabilities
- Upload of KPPP Excel and PDF result reports
- Template detection and column mapping profiles for known KPPP report formats
- Row-level validation with error report download
- Cross-check of Excel totals with PDF summary (site count, total bid value) where text-extractable
- Maker-checker confirmation
- File hash and lock on confirmation
- Same record creation path as the API (idempotent)

### UI Screens
- Result upload form
- Parsing and validation result with errors
- Column mapping profile editor
- Checker review: parsed rows and PDF side by side
- Upload history

### Logical API Operations
- Upload and store result files
- Parse Excel result report
- Extract PDF summary totals
- Validate rows
- Submit / confirm / reject upload
- Create records from confirmed upload
- Maintain mapping profiles

### Inputs
- Auction ID
- Excel report
- PDF report
- Mapping profile

### Outputs
- Validated rows
- Awarded site records on confirmation
- Locked files with hash

### Business Rules
- Upload allowed only for auctions without API results, or with Super Admin override
- Checker must be a different user from the maker
- Parsed values cannot be edited; corrections need a new upload
- Totals mismatch between Excel and PDF blocks submission

### Validations
- File type and size (Excel ≤ 10 MB, PDF ≤ 20 MB)
- Mandatory columns present
- Numeric amounts
- No duplicate site rows

### Calculations
- Totals of site count and bid values compared between files

### Workflow
Uploaded → Validated → Submitted → Confirmed (records created) | Rejected

### Search Requirements
- Uploads by auction ID, date, status

### Documents
- KPPP Excel and PDF reports stored and locked

### Reports
- Upload log

### Notifications
- Checker alert on submission
- Maker alert on decision

### Security
- Malware scan on upload
- Hash lock

### Integrations
- None (manual route)

### Dependencies
- F03-003
- F03-005
- F14-001

### Assumptions
- KPPP report format is stable per auction type

### Risks
- Report format changes; mitigated by mapping profiles

### Non Functional Requirements
- Parse 1,000 rows within 30 seconds
- Same-day import

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Result upload form | Medium | 6 |
| UI | Parsing and validation result with errors | Medium | 6 |
| UI | Column mapping profile editor | Medium | 6 |
| UI | Checker review: parsed rows and PDF side by side | Complex | 12 |
| UI | Upload history | Easy | 4 |
| API | Upload and store result files | Medium | 6 |
| API | Parse Excel result report | Complex | 8 |
| API | Extract PDF summary totals | Medium | 6 |
| API | Validate rows | Medium | 6 |
| API | Submit / confirm / reject upload | Medium | 6 |
| API | Create records from confirmed upload | Medium | 6 |
| API | Maintain mapping profiles | Easy | 4 |
| Database | Upload batch, files and mapping profiles | Medium | 4 |
| Testing | Parsing tests across report variants | Complex | 8 |
| Testing | Maker-checker and locking tests | Medium | 6 |
| Documentation | Result upload procedure | Easy | 2 |

**Feature Total: 96 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 34 | 42 | 4 | 0 | 14 | 2 | **96** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Parsing is Complex due to report variants; no external integration row
- No external integration channel in this feature; Integration row omitted.
