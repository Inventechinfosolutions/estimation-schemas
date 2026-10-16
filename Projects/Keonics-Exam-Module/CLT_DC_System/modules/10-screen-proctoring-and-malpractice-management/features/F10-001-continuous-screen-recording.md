# F10-001 — Continuous Screen Recording

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-001 |
| Feature Name | Continuous Screen Recording |
| Module | 10 — Screen Proctoring & Malpractice Management |
| Module Type | Business |
| Release | Go-live |

### Description
Continuous background screen recording from the exam client at configured resolution and frame rate (for example 720p at 1–2 fps or low-bitrate video), encoded and uploaded in chunks to SDC object storage with checksums, local encrypted buffer for network blips, start / stop tied to the candidate session, and recording health status.

### Business Objective
Provide full screen evidence for every candidate as required by the RFP.

### Actors
- System
- Proctor
- EMU

### User Journey
1. **Who creates:** Recording starts automatically at test start.
2. **How they create:** The client records and uploads chunks.
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Proctor and EMU see recording health per seat.
6. **How the approver decides:** Proctor resolves recording failures (restart, terminal move).
7. **How the applicant / maker sees history:** Not applicable for candidates.
8. **How the approver / auditor sees history:** Auditors see recording metadata and checksums.

### Functional Capabilities
- Configurable resolution / fps / bitrate
- Chunked encrypted upload
- Checksums
- Local buffer and retry
- Recording health heartbeat
- Session-linked start / stop
- Gap detection

### UI Screens
- Recording health panel

### Logical API Operations
- Chunk upload with checksum
- Recording session manifest
- Health heartbeat
- Gap detection job

### Inputs
- Screen frames

### Outputs
- Stored screen recordings

### Business Rules
- Recording mandatory for test start (configurable)
- Gaps flagged

### Validations
- Checksums

### Calculations
- Storage per candidate = bitrate × duration

### Workflow
Recording → Uploaded → Verified

### Search Requirements
- By candidate, session

### Documents
- Recordings

### Reports
- Recording coverage

### Notifications
- Recording failure alerts

### Security
- Encrypted chunks

### Integrations
- SDC object storage

### Dependencies
- F09-007
- F10-006
- F17-002

### Assumptions
- SDC provides object storage and bandwidth

### Risks
- Bandwidth at centres and storage volume

### Non Functional Requirements
- Upload lag under 60 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Recording health panel | Medium | 6 |
| API | Chunk upload with checksum | Complex | 8 |
| API | Recording session manifest | Medium | 6 |
| API | Health heartbeat | Medium | 6 |
| API | Gap detection job | Medium | 6 |
| Database | Recording manifest and chunk index | Medium | 4 |
| Integration | SDC object storage integration | Medium | 16 |
| Testing | Recording reliability tests under load | Complex | 8 |
| Documentation | Recording configuration note | Easy | 2 |

**Feature Total: 62 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 26 | 4 | 16 | 8 | 2 | **62** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Client capture inside F09-007; storage connector here
