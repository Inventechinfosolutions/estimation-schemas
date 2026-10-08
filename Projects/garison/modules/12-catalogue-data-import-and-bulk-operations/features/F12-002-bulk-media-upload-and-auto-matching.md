# F12-002 — Bulk Media Upload & Auto-matching

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F12-002 |
| Feature Name | Bulk Media Upload & Auto-matching |
| Module | 12 — Catalogue Data Import & Bulk Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Upload images and drawings in bulk (ZIP or multi-file), auto-match files to products and media types using a naming convention (for example CM-101_profile.svg, CM-101_installed_01.jpg), review matched, unmatched and conflicting files, manually assign, and commit to products.

### Business Objective
Attach hundreds of drawings and images to imported products without one-by-one uploads.

### Actors
- Catalogue Administrator
- Data population team

### User Journey
1. **Who creates:** The Catalogue Administrator or population team creates media upload batches.
2. **How they create:** They upload a ZIP or select multiple files; the system extracts, scans and matches files by code and type suffix.
3. **How they edit:** They manually assign unmatched files or resolve conflicts (for example two primary images), then commit.
4. **How they send for approval:** Media commit does not publish; media becomes part of the Draft products and follows the product review workflow.
5. **How the approver sees pending items:** There is no approver inbox for media batches.
6. **How the approver decides:** No decision applies on the batch.
7. **How the maker sees history:** Importers see batch history with matched/unmatched counts.
8. **How the approver / auditor sees history:** Auditors see media batch commits in the audit log.

### Functional Capabilities
- ZIP and multi-file upload with progress
- Configurable naming convention (code + type + sequence)
- Auto-match to products (including staged products) and media types
- Match review: matched, unmatched, conflicts, replacements
- Manual assignment
- Commit with derivative generation (F13-001)

### UI Screens
- Bulk media upload with progress
- Match results review with manual assignment

### Logical API Operations
- Upload and extract media archive
- Match files to products by naming convention
- Manually assign unmatched media
- Commit matched media to products

### Inputs
- ZIP/multi-file upload, naming convention settings, manual assignments

### Outputs
- Media attached to products
- Match report

### Business Rules
- Files not matching allowed types are rejected
- Conflicts must be resolved before commit
- Existing media replaced only when 'replace' is explicitly chosen

### Validations
- ZIP max 1 GB; per-file limits as F04-004
- Malware scan passed

### Calculations
- Match statistics

### Workflow
Uploaded → Matched → Reviewed → Committed

### Search Requirements
- Match review filters: matched/unmatched/conflict

### Documents
- None

### Reports
- Match report

### Notifications
- None

### Security
- Import permission; scanning (F13-002)

### Integrations
- Object storage (shared connector)

### Dependencies
- F04-004
- F12-001
- F13-001
- F13-002

### Assumptions
- Population team renames files to the convention during preparation

### Risks
- Inconsistent file naming increases manual assignment

### Non Functional Requirements
- 1 GB archive processed within 30 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Bulk media upload with progress | Complex | 12 |
| UI | Match results review with manual assignment | Complex | 12 |
| API | Upload and extract media archive | Complex | 8 |
| API | Match files to products by naming convention | Complex | 8 |
| API | Manually assign unmatched media | Easy | 4 |
| API | Commit matched media to products | Complex | 8 |
| Database | Media staging and match log | Easy | 2 |
| Testing | Naming convention match cases | Medium | 6 |
| Testing | Large archive handling | Medium | 6 |
| Documentation | Media naming convention guide | Easy | 2 |

**Feature Total: 68 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | 28 | 2 | 0 | 12 | 2 | **68** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Matching and commit are Complex APIs
- No external integration channel in this feature; Integration row omitted.
