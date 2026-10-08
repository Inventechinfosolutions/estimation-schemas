# F02-001 — Product Data Store & Loader

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-001 |
| Feature Name | Product Data Store & Loader |
| Module | 02 — Product Data Store on Existing Website |
| Module Type | Technical |
| Release | Go-live |

### Description
Product storage inside the existing website stack (database tables, content type or structured data files, depending on the platform), an idempotent loader that creates, updates and removes products by key from the frozen dataset, rollback to the previous load, and a data access layer used by catalogue pages.

### Business Objective
Make the approved dataset the single, repeatable source of catalogue content on the website.

### Actors
- Delivery developer
- Future maintenance developer

### User Journey
1. **Who creates:** The delivery developer runs the loader; Garrison does not operate it.
2. **How they create:** They run the loader against staging, verify, then run it on production during deployment.
3. **How they edit:** Later changes are made by editing or refreshing the dataset and re-running the loader; previous loads can be rolled back.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees each load's summary (created, updated, removed).
8. **How the approver / auditor sees history:** The delivery lead keeps load summaries with the deployment record.

### Functional Capabilities
- Product, category and species storage in the existing stack
- Idempotent loader keyed on category + code
- Load summary and rollback to previous load
- Data access layer: list by category with filters, get by code, similar products, search

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Load products idempotently from dataset
- Link product image references
- Provide catalogue data access layer
- Roll back to previous load

### Inputs
- Frozen master dataset
- Image manifest

### Outputs
- Products stored in the website
- Load summary

### Business Rules
- Re-running with an unchanged dataset produces no changes
- Products absent from the dataset are removed or hidden on load
- A backup is taken before every production load

### Validations
- Dataset passes F01-003 validation before load

### Calculations
- Created/updated/removed counts

### Workflow
Dataset → Staging load → Verify → Production load

### Search Requirements
- Data access layer supports search (F03-004)

### Documents
- Update procedure

### Reports
- Load summary

### Notifications
- None

### Security
- Loader runs only with server access; no public endpoint

### Integrations
- None (runs inside the existing website environment)

### Dependencies
- F01-004
- F04-001

### Assumptions
- Existing stack has a database or can store structured data files

### Risks
- Unusual or legacy stack increases effort; confirmed at onboarding

### Non Functional Requirements
- Full load completes in under 5 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Load products idempotently from dataset | Complex | 8 |
| API | Link product image references | Easy | 4 |
| API | Provide catalogue data access layer | Complex | 8 |
| API | Roll back to previous load | Medium | 6 |
| Database | Product, category and species storage | Medium | 4 |
| Database | Filter and search indexes | Easy | 2 |
| Testing | Loader idempotency and re-run | Medium | 6 |
| Testing | Data access performance with full dataset | Easy | 4 |
| Documentation | Product data update procedure | Medium | 3 |

**Feature Total: 45 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 26 | 6 | 0 | 10 | 3 | **45** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Storage approach finalised after code onboarding; estimate assumes a common database-backed stack
- No external integration channel in this feature; Integration row omitted.
