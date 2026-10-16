# F13-004 — Data Retrieval & Query Tool

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-004 |
| Feature Name | Data Retrieval & Query Tool |
| Module | 13 — MIS, Dashboards & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Self-service query tool on curated, scope-filtered views (registrations, bookings, sessions, results, certificates, payments): choose fields, filters, grouping and sorting; save, share and schedule queries; export to Excel / CSV; personal data masked unless permitted.

### Business Objective
Provide the RFP-required software for retrieval of examination data through queries.

### Actors
- KEONICS Administrator
- Center for E-Governance analyst

### User Journey
1. **Who creates:** Authorised users create queries.
2. **How they create:** Users select view, fields, filters and grouping.
3. **How they edit:** Users edit and save.
4. **How they send for approval:** Sharing with others requires administrator approval.
5. **How the approver sees pending items:** Administrator sees share requests.
6. **How the approver decides:** Administrator approves.
7. **How the applicant / maker sees history:** Users see saved queries.
8. **How the approver / auditor sees history:** Auditors see query runs and exports.

### Functional Capabilities
- Curated views
- Field picker and filters
- Grouping and aggregation
- Saved and shared queries
- Export
- Masking

### UI Screens
- Query builder
- Saved queries

### Logical API Operations
- Build and run query safely
- Save / share query
- Export

### Inputs
- Query definitions

### Outputs
- Results

### Business Rules
- Only curated views
- Row limits

### Validations
- Query limits

### Calculations
- Aggregates

### Workflow
Draft → Saved → Shared

### Search Requirements
- Queries

### Documents
- Exports

### Reports
- Ad-hoc

### Notifications
- Scheduled results

### Security
- Masking and scope

### Integrations
- None

### Dependencies
- F01-003

### Assumptions
- None

### Risks
- Heavy queries

### Non Functional Requirements
- Query timeout 30 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Query builder | Complex | 12 |
| UI | Saved queries | Easy | 4 |
| API | Build and run query safely | Complex | 8 |
| API | Save / share query | Easy | 4 |
| API | Export | Easy | 4 |
| Database | Curated views | Medium | 4 |
| Database | Saved queries | Easy | 2 |
| Testing | Query tool tests including scope | Medium | 6 |
| Documentation | Query tool guide | Easy | 2 |

**Feature Total: 46 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 16 | 6 | 0 | 6 | 2 | **46** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
