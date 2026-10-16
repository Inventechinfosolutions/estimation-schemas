# F02-002 — Deputy Secretary Area Allocation Rules

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-002 |
| Feature Name | Deputy Secretary Area Allocation Rules |
| Module | 02 — Auction Rules & Configuration |
| Module Type | Business |
| Release | Go-live |

### Description
Configuration of the mapping between layouts, blocks, sectors or wards and Deputy Secretary offices (DS1, DS2, DS3 and any added later), with effective dates, used for automatic case forwarding and DS-wise data isolation.

### Business Objective
Route every case to the correct DS office automatically and allow BDA to change jurisdictions without code changes.

### Actors
- Auction Admin
- Approving Authority (approval)
- Deputy Secretary (view)

### User Journey
1. **Who creates:** The Auction Admin creates DS offices and area mappings.
2. **How they create:** The Auction Admin opens Area Allocation, selects a DS office and adds layouts / blocks / sectors from the masters (F02-006) or by Excel upload, sets the effective date and saves as draft.
3. **How they edit:** The Auction Admin edits the draft; overlap and gap checks highlight areas mapped to none or to more than one DS.
4. **How they send for approval:** The Auction Admin submits the draft for approval.
5. **How the approver sees pending items:** The Approving Authority sees pending allocation changes with added / removed areas per DS.
6. **How the approver decides:** The Approving Authority approves or returns; on approval the mapping becomes active from the effective date.
7. **How the applicant / maker sees history:** Deputy Secretaries see their area list; the Auction Admin sees version history.
8. **How the approver / auditor sees history:** Auditors see all versions and the rule used for each forwarded case.

### Functional Capabilities
- DS office master (code, name, head officer, address)
- Area mapping at layout, block, sector or ward level with most-specific match
- Excel upload of mappings with validation
- Overlap and unmapped-area detection
- Effective-dated versions with approval
- Rule test: enter a site number to see which DS it would go to
- Option to re-map open cases on approval or apply to new forwards only

### UI Screens
- DS office master
- Area mapping editor
- Excel upload and validation result
- Overlap / gap report
- Rule test by site
- Approval and version history

### Logical API Operations
- Maintain DS offices
- Save area mapping draft
- Upload mappings
- Detect overlaps and gaps
- Approve / return mapping version
- Resolve DS office for a site
- Re-map open cases on approval

### Inputs
- DS office details
- Area selections or upload file
- Effective date
- Re-map option

### Outputs
- Active mapping
- DS resolution for sites
- Overlap / gap list

### Business Rules
- Each area maps to exactly one DS office on a date
- Most specific mapping wins (ward > sector > block > layout)
- Open cases are re-mapped only if chosen at approval; re-mapping is audited per case

### Validations
- Areas exist in masters
- No overlapping mappings on the effective date

### Calculations
- None

### Workflow
Draft → Submitted → Active → Superseded

### Search Requirements
- Mappings by DS office, layout, area

### Documents
- Office order reference for jurisdiction change

### Reports
- Area allocation by DS office
- Unmapped areas

### Notifications
- Approval request and outcome
- Notice to affected DS offices on change

### Security
- Only Auction Admin edits

### Integrations
- None

### Dependencies
- F02-006
- F07-001
- F01-003

### Assumptions
- BDA provides the current jurisdiction list

### Risks
- Unmapped areas block forwarding; caught by gap check and an exception queue in F07-001

### Non Functional Requirements
- Resolution under 100 ms per site

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | DS office master | Easy | 4 |
| UI | Area mapping editor | Medium | 6 |
| UI | Excel upload and validation result | Medium | 6 |
| UI | Overlap / gap report | Easy | 4 |
| UI | Rule test by site | Easy | 4 |
| UI | Approval and version history | Easy | 4 |
| API | Maintain DS offices | Easy | 4 |
| API | Save area mapping draft | Medium | 6 |
| API | Upload mappings | Medium | 6 |
| API | Detect overlaps and gaps | Medium | 6 |
| API | Approve / return mapping version | Easy | 4 |
| API | Resolve DS office for a site | Complex | 8 |
| API | Re-map open cases on approval | Complex | 8 |
| Database | DS office and area mapping versions | Medium | 4 |
| Testing | Mapping resolution tests at all levels | Medium | 6 |
| Testing | Overlap, upload and re-map tests | Medium | 6 |
| Documentation | Area allocation guide | Easy | 2 |

**Feature Total: 88 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 42 | 4 | 0 | 12 | 2 | **88** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Re-mapping of open cases is Complex because queues, isolation and history must move together
- No external integration channel in this feature; Integration row omitted.
