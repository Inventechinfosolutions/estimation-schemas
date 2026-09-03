# F06-001 — e-Office and Department Upload

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | e-Office and Department Upload |
| **Module** | 06 — e-Office Upload, Backup and Progress MIS |

### Description
Record the pre-scale e-Office compatibility test, then upload (or record manual upload of) each QC-passed, metadated PDF/A into e-Office and/or the Department system, with status and retry.

### Business Objective
Digitised files are available where DMG actually works.

### Actors
Maker: Supervisor / designated operator. Approver: none.

### User Journey
1. Who creates: Supervisor records sample compatibility pass, then uploads production files.
2. How they create: Compatibility gate (once) → Upload queue of complete files → Submit upload or record manual e-Office user upload → see status.
3. How they edit: Retry failed uploads.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox. Department Officer sees uploaded vs pending.
6. How the approver decides: No decision.
7. How the maker sees history: Upload attempts on the file.
8. How the auditor sees history: Same.

### Functional Capabilities
- Compatibility-test record before full scan
- Upload queue
- Status and retry
- Manual-upload recording if no system API

### UI Screens
| Screen | Complexity |
|---|---|
| Upload queue | Medium |
| Upload status detail | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Submit upload | Complex |
| Read upload status | Medium |
| Retry upload | Medium |

### Inputs
Unique ID, target (e-Office / Department), package.

### Outputs
Upload status per file.

### Business Rules
- Full-scale scanning should not proceed without recorded compatibility pass (gate).
- Only QC-passed files with metadata.
- Department internet used for upload.

### Validations
- QC pass and metadata complete.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
Pending / failed / uploaded.

### Documents
PDF/A payload.

### Reports
Uploaded count on MIS.

### Notifications
None.

### Security
Supervisor-led upload.

### Integrations
e-Office and/or Department system (real channel).

### Dependencies
F04-001, F05-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Integration hours assume a documented upload channel; if only manual e-Office UI exists, the same screens record checklist completion without a system feed.

### Risks
Undocumented e-Office interface delays the job.

### Non Functional Requirements
Retry safe; no duplicate confuse Department.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Upload queue | UI | Medium | 6 |
| Upload status detail | UI | Easy | 4 |
| Submit upload | API | Complex | 8 |
| Read upload status | API | Medium | 6 |
| Retry upload | API | Medium | 6 |
| e-Office / department upload channel | Integration | Medium | 16 |
| Upload records | DB | Easy | 2 |
| e-Office and department upload tests | Testing | Complex | 8 |
| e-Office and department upload implementation documentation | Documentation | Medium | 3 |

**Feature total: 59 hours**
