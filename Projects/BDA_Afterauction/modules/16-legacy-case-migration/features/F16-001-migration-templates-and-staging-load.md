# F16-001 — Migration Templates & Staging Load

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F16-001 |
| Feature Name | Migration Templates & Staging Load |
| Module | 16 — Legacy Case Migration |
| Module Type | Technical |
| Release | Go-live |

### Description
Excel templates for pending legacy cases (site, auction, bidder, bid, approvals, schedule, payments, DS status, documents index) and loading into staging tables with format validation and load reports.

### Business Objective
Bring pending cases from earlier auctions into the Module in a controlled way.

### Actors
- Migration team
- Auction Admin

### User Journey
1. **Who creates:** BDA fills templates; the migration team loads them.
2. **How they create:** Templates are uploaded and loaded into staging.
3. **How they edit:** Rejected rows are corrected and reloaded.
4. **How they send for approval:** Not applicable at staging.
5. **How the approver sees pending items:** Auction Admin sees load reports.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Load logs retained.

### Functional Capabilities
- Templates
- Staging load
- Format validation
- Load reports
- Document bulk upload with index

### UI Screens
- Migration upload
- Load report

### Logical API Operations
- Load templates to staging
- Format validation
- Bulk document upload with index

### Inputs
- Templates
- Documents

### Outputs
- Staged data

### Business Rules
- Template version enforced

### Validations
- Formats

### Calculations
- Counts

### Workflow
Uploaded → Staged | Rejected

### Search Requirements
- None

### Documents
- Legacy documents

### Reports
- Load report

### Notifications
- None

### Security
- Restricted

### Integrations
- None

### Dependencies
- Modules 03–09 data model

### Assumptions
- BDA provides data

### Risks
- Data quality

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Migration upload | Easy | 4 |
| UI | Load report | Easy | 4 |
| API | Load templates to staging | Medium | 6 |
| API | Format validation | Medium | 6 |
| API | Bulk document upload with index | Medium | 6 |
| Database | Staging tables | Medium | 4 |
| Testing | Load tests with sample data | Medium | 6 |
| Documentation | Migration templates and guide | Medium | 3 |

**Feature Total: 39 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 18 | 4 | 0 | 6 | 3 | **39** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
