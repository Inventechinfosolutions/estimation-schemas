# F03-004 — CDRMS Site Package Retrieval & Case File Creation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-004 |
| Feature Name | CDRMS Site Package Retrieval & Case File Creation |
| Module | 03 — KPPP Result Intake & Site Package |
| Module Type | Business |
| Release | Go-live |

### Description
Read-only retrieval from CDRMS of the site package for each matched site — site master data, e-CDR (encumbrance / corner data), legal report, allotment section report, site sketch and photographs — and creation of the case file that travels with the site through all later stages.

### Business Objective
Give verifiers, Deputy Secretaries and case workers the complete site information in one place without re-entry, and preserve the version used for decisions.

### Actors
- System
- Auction Admin
- All case-handling roles (view)

### User Journey
1. **Who creates:** The system creates the case file automatically when a result is matched.
2. **How they create:** The connector requests the site package from CDRMS, stores the data and documents with hashes and links them to the case.
3. **How they edit:** Users cannot edit CDRMS data; the Auction Admin can trigger a refresh, which creates a new package version.
4. **How they send for approval:** The case file becomes available to verification automatically.
5. **How the approver sees pending items:** Users see the case file from any queue; missing package items are shown as warnings.
6. **How the approver decides:** No approval; the Auction Admin decides whether to refresh or proceed with warnings.
7. **How the applicant / maker sees history:** Users see package versions and retrieval dates in the case file.
8. **How the approver / auditor sees history:** Auditors see retrieval requests, responses and hashes.

### Functional Capabilities
- CDRMS read API client for site master and documents
- Case file creation with unique case number
- Package versioning on refresh with differences highlighted
- Completeness check for mandatory items
- Document storage with hash and preview
- Retry and error handling through the integration error queue

### UI Screens
- Case file: site package tab
- Package version comparison
- Package completeness warnings
- Document preview

### Logical API Operations
- Request site package from CDRMS
- Store package data and documents with hash
- Create case file and case number
- Refresh package version
- Completeness check
- Get case file package
- Compare package versions

### Inputs
- Matched site ID
- Refresh request

### Outputs
- Case file with site package
- Package versions
- Completeness warnings

### Business Rules
- CDRMS data is read-only in the Module
- Each decision records the package version in use
- Refresh does not overwrite earlier versions

### Validations
- Site ID exists in CDRMS
- Documents of allowed types

### Calculations
- Case number = BPA/{year}/{auction}/{site}

### Workflow
Requested → Retrieved → Linked; Retrieval failed → Error queue → Retried

### Search Requirements
- Case files by case number, site, layout, auction

### Documents
- e-CDR, legal report, allotment section report, sketch, photographs

### Reports
- Package completeness report

### Notifications
- Alert on retrieval failure

### Security
- Read-only service account for CDRMS

### Integrations
- CDRMS

### Dependencies
- F13-001
- F13-002
- F03-003

### Assumptions
- CDRMS exposes read APIs for site package

### Risks
- Incomplete packages in CDRMS delay verification

### Non Functional Requirements
- Package retrieval within 30 seconds per site

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Case file: site package tab | Medium | 6 |
| UI | Package version comparison | Medium | 6 |
| UI | Package completeness warnings | Easy | 4 |
| UI | Document preview | Easy | 4 |
| API | Request site package from CDRMS | Complex | 8 |
| API | Store package data and documents with hash | Medium | 6 |
| API | Create case file and case number | Medium | 6 |
| API | Refresh package version | Medium | 6 |
| API | Completeness check | Easy | 4 |
| API | Get case file package | Easy | 4 |
| API | Compare package versions | Medium | 6 |
| Database | Case file and site package versions | Complex | 6 |
| Database | Document store metadata | Medium | 4 |
| Integration | CDRMS site package read API | Complex | 24 |
| Testing | CDRMS contract and data mapping tests | Complex | 8 |
| Testing | Versioning and completeness tests | Medium | 6 |
| Documentation | CDRMS interface specification (read) | Medium | 3 |

**Feature Total: 111 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 40 | 10 | 24 | 14 | 3 | **111** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Complex integration row for CDRMS read
