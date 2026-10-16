# F07-003 — Deputy Secretary Case File Workspace

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-003 |
| Feature Name | Deputy Secretary Case File Workspace |
| Module | 07 — Case Forwarding & Deputy Secretary Processing |
| Module Type | Business |
| Release | Go-live |

### Description
Complete case file workspace for the Deputy Secretary and case workers: site details with GIS map, auction and bidder details, result approval and proceedings, e-CDR, legal report, allotment section report, all documents and versions, payment ledger, notes, tasks, timeline and stage tracker, with document preview and bundle download.

### Business Objective
Replace the physical file with a complete digital case file and speed up DS processing.

### Actors
- Deputy Secretary
- Case Worker
- Auction Admin (view)
- Finance Officer (view)

### User Journey
1. **Who creates:** The case file is created at intake; DS office users work in it after forwarding.
2. **How they create:** The DS or case worker opens a case from the queue and sees all tabs.
3. **How they edit:** Users add notes and documents through F07-004; core data is read-only.
4. **How they send for approval:** Not applicable (workspace).
5. **How the approver sees pending items:** The DS sees queue counts by stage and timer status.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Users see the full case timeline.
8. **How the approver / auditor sees history:** Auditors see case file access logs.

### Functional Capabilities
- DS queue with filters, counts and RAG timers
- Case summary header with stage and amounts
- Tabs: site, map, auction and bidder, approvals, package, documents, payments, notes, timeline
- Document preview, version view and bundle ZIP / PDF download
- Case timeline of all events
- Watermarked downloads with user and time

### UI Screens
- DS case queue
- Case file summary header
- Case file tabs workspace
- Documents tab with preview and versions
- Case timeline
- Bundle download

### Logical API Operations
- DS queue listing with timers
- Get case file aggregate
- List documents and versions
- Generate document bundle
- Case timeline
- Watermark download
- Log case access

### Inputs
- Case selection

### Outputs
- Case file view
- Bundle

### Business Rules
- DS isolation
- All views logged

### Validations
- Access permission

### Calculations
- Timer status

### Workflow
Not applicable

### Search Requirements
- Cases by number, site, bidder, stage

### Documents
- All case documents

### Reports
- Case file print summary

### Notifications
- None

### Security
- Watermarking; access logging; DS isolation

### Integrations
- GIS via F13-004

### Dependencies
- F03-004
- F06-005
- F13-004
- F01-003

### Assumptions
- None

### Risks
- Performance with many documents; paging and lazy load

### Non Functional Requirements
- Case file loads within 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | DS case queue | Medium | 6 |
| UI | Case file summary header | Medium | 6 |
| UI | Case file tabs workspace | Complex | 12 |
| UI | Documents tab with preview and versions | Medium | 6 |
| UI | Case timeline | Medium | 6 |
| UI | Bundle download | Easy | 4 |
| API | DS queue listing with timers | Medium | 6 |
| API | Get case file aggregate | Complex | 8 |
| API | List documents and versions | Easy | 4 |
| API | Generate document bundle | Medium | 6 |
| API | Case timeline | Medium | 6 |
| API | Watermark download | Medium | 6 |
| API | Log case access | Easy | 4 |
| Database | Case timeline and access log | Easy | 2 |
| Testing | Case file data and isolation tests | Medium | 6 |
| Testing | Bundle and watermark tests | Easy | 4 |
| Documentation | DS case file user guide | Medium | 3 |

**Feature Total: 95 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 40 | 40 | 2 | 0 | 10 | 3 | **95** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Aggregate workspace rated Complex
- No external integration channel in this feature; Integration row omitted.
