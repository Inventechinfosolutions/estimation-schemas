# F04-005 — Catalogue Data Build & Publishing

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-005 |
| Feature Name | Catalogue Data Build & Publishing |
| Module | 04 — One-time Product Data Migration |
| Module Type | Technical |
| Release | Go-live |

### Description
Turn the frozen dataset into the website's catalogue data files (per category, per product and search index), link product images, generate page routes, and stop the build if any product fails validation. A documented refresh procedure lets a developer apply later product changes by editing the dataset and rebuilding.

### Business Objective
Make the approved dataset the single, repeatable source of every catalogue page, with no admin portal.

### Actors
- Delivery developer
- Future maintenance developer

### User Journey
1. **Who creates:** The delivery developer runs the catalogue build; Garrison does not operate it.
2. **How they create:** The build generates data files and pages on staging; the developer verifies and releases to production.
3. **How they edit:** Later changes: edit the dataset (or re-run extraction), rebuild on staging, verify, release.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees build summaries (products published, excluded, failed).
8. **How the approver / auditor sees history:** The delivery lead keeps build summaries with the release record.

### Functional Capabilities
- Catalogue data files per category and product
- Search index generation
- Image linking and route generation
- Build-time validation gate
- Documented refresh procedure

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Generate catalogue data files from frozen dataset
- Link images and generate page routes
- Build-time data validation gate
- Product refresh procedure script

### Inputs
- Frozen master dataset
- Image manifest

### Outputs
- Catalogue data files and pages
- Build summary

### Business Rules
- Only Included products are published
- A failed validation stops the release
- Every release can be rolled back to the previous build

### Validations
- Dataset passes F04-003 validation

### Calculations
- Published, excluded and failed counts

### Workflow
Frozen dataset → Staging build → Verify → Production release

### Search Requirements
- None

### Documents
- Refresh procedure

### Reports
- Build summary

### Notifications
- None

### Security
- No public write endpoint; changes only through version control

### Integrations
- None

### Dependencies
- F04-004
- F02-001

### Assumptions
- Catalogue changes are rare (as advised by Garrison) and handled by a developer

### Risks
- Frequent changes would make developer-led updates costly; Option 3 provides self-service

### Non Functional Requirements
- Full catalogue build completes in under 5 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Generate catalogue data files from frozen dataset | Medium | 6 |
| API | Link images and generate page routes | Medium | 6 |
| API | Build-time data validation gate | Easy | 4 |
| API | Product refresh procedure script | Easy | 4 |
| Database | Catalogue data file schema | Easy | 2 |
| Testing | Build output verification for all products | Medium | 6 |
| Documentation | Product data refresh procedure | Medium | 3 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 2 | 0 | 6 | 3 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Static data build replaces a database loader
- No external integration channel in this feature; Integration row omitted.
