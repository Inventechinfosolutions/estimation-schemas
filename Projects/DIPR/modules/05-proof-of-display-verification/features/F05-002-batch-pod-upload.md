# F05-002 — Batch PoD upload

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-002 |
| Feature Name | Batch PoD upload |
| Module | 05 — Proof-of-Display Capture & Verification |
| Description | Upload and associate multiple PoD items to campaigns and sites in batch for agency bulk submissions. |
| Business Objective | Reduce manual effort when vendors submit many site photos after an outdoor flight completes. |
| Actors | Campaign Officer; Vendor User (if permitted); Field Supervisor |

### User Journey

- User opens Batch PoD upload → selects campaign → uploads many files → mapping wizard matches filenames to sites or manual grid assignment → validates rows → submits batch → job status shows per-file success/failure → successful items enter same pipeline as single PoD (F05-001).

### Functional Capabilities

- Multi-file drag-drop with batch size limits
- Grid mapping: file ↔ site/location ↔ optional task line
- Filename pattern helper for auto-mapping (configurable prefix)
- Batch job progress and per-item error report
- Partial success handling with retry for failed rows

### Inputs

- File list, campaign, site mappings, batch notes

### Outputs

- Multiple PoD records; batch job summary

### Business Rules

- Each row must resolve to valid site in campaign plan
- Failed rows do not block successful ones unless atomic batch flag set (default off)
- Vendor batch limited to assigned campaigns

### Validations

- Duplicate file detection in same batch; mapping completeness before submit

### Calculations

- Batch success/fail counts

### Workflow

- Upload → map → validate → process → individual PoD lifecycle

### Search Requirements

- Filter register by batch job ID

### Documents

- Batch error CSV download

### Reports

- Batch summary for Module 07 operational metrics

### Notifications

- Email/in-app when batch completes (Module 08)

### Security

- Batch upload permission may be tighter than single capture

### Integrations

- None

### Dependencies

- F05-001 ingest; F03-007 tasks; F02-003 locations

### Assumptions

- Typical batch ≤ 200 files per job; larger needs ops tuning

### Risks

- Wrong auto-mapping assigns PoD to incorrect site undetected until verification

### Non Functional Requirements

- Background processing for large batches without blocking UI

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Batch PoD upload wizard — file selection step | Medium | 6 |
| UI | Batch wizard — column mapping grid | Complex | 12 |
| UI | Batch wizard — validation preview with errors | Medium | 6 |
| UI | Batch progress and per-row status table | Medium | 6 |
| UI | Download batch error report CSV | Easy | 4 |
| API | Initiate batch PoD ingest job | Complex | 8 |
| API | Map spreadsheet rows to PoD entities | Complex | 8 |
| API | Row-level validation before commit | Medium | 6 |
| API | Commit batch with partial success policy | Complex | 8 |
| API | Export batch error report | Easy | 4 |
| Database | Batch job header and row status | Medium | 4 |
| Database | Batch ingest staging table | Easy | 2 |
| Testing | All-valid rows commit successfully | Medium | 6 |
| Testing | Partial failure and rollback policy | Complex | 8 |
| Testing | Column mapping errors surfaced pre-commit | Medium | 6 |
| Documentation | Batch PoD upload template specification | Easy | 2 |
| Documentation | UAT batch ingest script | Easy | 2 |

**Feature Total: 98 hours**

### Estimation Assumptions

- Virus scan runs per file same as single upload path.
