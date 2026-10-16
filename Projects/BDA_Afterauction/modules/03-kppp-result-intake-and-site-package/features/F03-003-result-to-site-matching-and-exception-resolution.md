# F03-003 — Result-to-Site Matching & Exception Resolution

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-003 |
| Feature Name | Result-to-Site Matching & Exception Resolution |
| Module | 03 — KPPP Result Intake & Site Package |
| Module Type | Business |
| Release | Go-live |

### Description
Matching of each received result to the BDA site master (from CDRMS) using site number, layout and aliases, and an exception queue for unmatched sites, duplicate results, withdrawn sites, data mismatches (area, dimensions, upset price) and bidder data gaps, resolved by the Auction Admin before verification.

### Business Objective
Ensure every result entering verification is linked to the correct BDA site and that data problems are resolved before decisions are made.

### Actors
- System
- Auction Admin

### User Journey
1. **Who creates:** The system matches records automatically; the Auction Admin resolves exceptions.
2. **How they create:** After intake, the matcher compares each result with the site master and creates exceptions with type and suggested matches.
3. **How they edit:** The Auction Admin opens the Exception Queue, reviews an exception, chooses a suggested site, maps a layout alias, marks the result withdrawn or requests correction, and records remarks.
4. **How they send for approval:** Resolved records are released to verification; withdrawn records are closed with reason.
5. **How the approver sees pending items:** The Auction Admin sees open exceptions by type and age; Result Verifiers see the count blocking their queue.
6. **How the approver decides:** The Auction Admin decides each exception; major changes (manual site mapping) can require Result Verifier confirmation (configurable).
7. **How the applicant / maker sees history:** The Auction Admin sees resolution history per record.
8. **How the approver / auditor sees history:** Auditors see the original data, resolution, user and time.

### Functional Capabilities
- Automatic matching on site number + layout with alias table
- Fuzzy suggestions for near matches
- Exception types: unmatched site, duplicate result, site already sold / withdrawn, area mismatch, upset price mismatch, missing bidder contact
- Resolution actions: map to site, add alias, mark withdrawn, hold, send for re-import
- Optional confirmation of manual mapping
- Exception ageing and alerts

### UI Screens
- Exception queue with filters
- Exception resolution workspace with suggestions
- Layout alias maintenance
- Matching summary per batch

### Logical API Operations
- Run matching for batch
- Generate suggestions
- Resolve exception
- Maintain aliases
- Confirm manual mapping
- Exception ageing job
- Release records to verification

### Inputs
- Received records
- Site master data
- Resolution choices and remarks

### Outputs
- Matched records released to verification
- Exception list
- Aliases

### Business Rules
- No record enters verification with an open exception
- Sites already completed or under another active case cannot be matched
- Mismatched upset price is flagged, not auto-corrected

### Validations
- Selected site exists and is in auction status in CDRMS

### Calculations
- Similarity score for suggestions

### Workflow
Matched → Released | Exception → Resolved → Released / Withdrawn

### Search Requirements
- Exceptions by type, auction, site, age

### Documents
- Supporting note for manual mapping

### Reports
- Exception summary by auction

### Notifications
- Alert to Auction Admin on new exceptions and ageing

### Security
- Auction Admin only

### Integrations
- Uses CDRMS site data retrieved in F03-004

### Dependencies
- F03-001
- F03-002
- F03-004
- F02-006

### Assumptions
- CDRMS site numbers are consistent with KPPP site IDs in most cases

### Risks
- High exception volume if CDRMS and KPPP use different site identifiers

### Non Functional Requirements
- Matching 1,000 records within 1 minute

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Exception queue with filters | Medium | 6 |
| UI | Exception resolution workspace with suggestions | Complex | 12 |
| UI | Layout alias maintenance | Easy | 4 |
| UI | Matching summary per batch | Easy | 4 |
| API | Run matching for batch | Complex | 8 |
| API | Generate suggestions | Medium | 6 |
| API | Resolve exception | Medium | 6 |
| API | Maintain aliases | Easy | 4 |
| API | Confirm manual mapping | Easy | 4 |
| API | Exception ageing job | Easy | 4 |
| API | Release records to verification | Medium | 6 |
| Database | Exception register and alias table | Medium | 4 |
| Testing | Matching accuracy tests with sample data | Complex | 8 |
| Testing | Exception resolution flow tests | Medium | 6 |
| Documentation | Exception handling guide | Easy | 2 |

**Feature Total: 84 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 38 | 4 | 0 | 14 | 2 | **84** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Matching engine with suggestions is Complex
- No external integration channel in this feature; Integration row omitted.
