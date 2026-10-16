# F04-001 — Site-wise Result Review Workbench

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-001 |
| Feature Name | Site-wise Result Review Workbench |
| Module | 04 — Result Verification & Approval |
| Module Type | Business |
| Release | Go-live |

### Description
Workbench for the Result Verifier to review each awarded site with upset price, highest bid, premium, number of bidders and bids, bidder details, flags, CDRMS site package and map, record a verification note and checklist, and submit sites (individually or in bulk) for approval.

### Business Objective
Give verifiers all the information needed to verify a result in one screen and produce a consistent verification record.

### Actors
- Result Verifier
- Auction Admin (view)

### User Journey
1. **Who creates:** Results arrive automatically after matching; the Result Verifier creates the verification record.
2. **How they create:** The Result Verifier opens the Verification Queue, selects an auction or site, reviews indicators and the case file, completes the verification checklist and writes a note.
3. **How they edit:** The Result Verifier can edit the note and checklist until submission; a site can be put on hold with reason.
4. **How they send for approval:** The Result Verifier submits the site (or a selected group) for approval; the approval chain is resolved from F02-003.
5. **How the approver sees pending items:** Approvers see submitted sites in their approval inbox (F04-003).
6. **How the approver decides:** Approvers decide in F04-003; returned sites come back to the workbench with remarks.
7. **How the applicant / maker sees history:** The Result Verifier sees all sites they verified with status and decisions.
8. **How the approver / auditor sees history:** Auditors see checklist answers, notes, holds and submissions with timestamps.

### Functional Capabilities
- Queue by auction, layout, flag and status with counts
- Site result card: upset price, highest bid, premium amount and %, bidder count, bid count, closure time
- Bidder panel: name, KPPP bidder ID, contact, EMD paid, previous awards and defaults in BDA
- Flags panel from F04-002
- Case file tabs: site package, documents, GIS map (F13-004)
- Configurable verification checklist
- Verification note, hold with reason, return handling
- Bulk submit for clean (unflagged) sites
- Auction-level summary: total sites, total upset value, total bid value, average premium

### UI Screens
- Verification queue with filters and counts
- Site result review workbench
- Bidder details and history panel
- Verification checklist and note
- Auction-level summary
- Bulk submit dialog
- Hold / release dialog

### Logical API Operations
- List verification queue
- Get site result with indicators
- Get bidder history in BDA
- Save checklist and note
- Hold / release site
- Submit site(s) for approval with chain resolution
- Auction summary computation
- Maintain checklist items

### Inputs
- Checklist answers
- Verification note
- Hold reason
- Selection for bulk submit

### Outputs
- Verification record
- Sites submitted for approval

### Business Rules
- Flagged sites cannot be bulk submitted; each needs an individual note
- Sites with open intake exceptions are not shown
- Result data is read-only (locked)
- Verifier cannot approve the same site

### Validations
- All mandatory checklist items answered
- Note mandatory for flagged sites

### Calculations
- Premium and premium %
- Auction totals and averages

### Workflow
Pending Verification → (Hold) On Hold → Verified & Submitted → (Return) Pending Verification

### Search Requirements
- By auction, site number, layout, bidder name, flag

### Documents
- Site package documents (view)

### Reports
- Verification status by auction

### Notifications
- New results alert to verifiers
- Return alert

### Security
- Result Verifier role; DS isolation not applicable at this stage (central function)

### Integrations
- GIS map view through F13-004

### Dependencies
- F03-003
- F03-004
- F04-002
- F02-003

### Assumptions
- Verification checklist provided by BDA

### Risks
- Large auctions create peaks; bulk submission mitigates

### Non Functional Requirements
- Workbench loads within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Verification queue with filters and counts | Medium | 6 |
| UI | Site result review workbench | Complex | 12 |
| UI | Bidder details and history panel | Medium | 6 |
| UI | Verification checklist and note | Medium | 6 |
| UI | Auction-level summary | Medium | 6 |
| UI | Bulk submit dialog | Easy | 4 |
| UI | Hold / release dialog | Simple | 2 |
| API | List verification queue | Medium | 6 |
| API | Get site result with indicators | Medium | 6 |
| API | Get bidder history in BDA | Medium | 6 |
| API | Save checklist and note | Easy | 4 |
| API | Hold / release site | Easy | 4 |
| API | Submit site(s) for approval with chain resolution | Complex | 8 |
| API | Auction summary computation | Medium | 6 |
| API | Maintain checklist items | Easy | 4 |
| Database | Verification record and checklist answers | Medium | 4 |
| Testing | Workbench data and indicator tests | Medium | 6 |
| Testing | Submission and chain resolution tests | Medium | 6 |
| Testing | Bulk submission tests | Easy | 4 |
| Documentation | Result verification user guide | Medium | 3 |

**Feature Total: 109 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 42 | 44 | 4 | 0 | 16 | 3 | **109** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Workbench screen rated Complex because of combined panels
- No external integration channel in this feature; Integration row omitted.
