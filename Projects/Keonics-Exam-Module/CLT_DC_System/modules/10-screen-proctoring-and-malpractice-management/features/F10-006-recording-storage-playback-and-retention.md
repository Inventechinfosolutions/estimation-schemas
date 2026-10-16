# F10-006 — Recording Storage, Playback & Retention

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-006 |
| Feature Name | Recording Storage, Playback & Retention |
| Module | 10 — Screen Proctoring & Malpractice Management |
| Module Type | Business |
| Release | Go-live |

### Description
Indexing of recordings by session, centre and candidate; secure streaming playback of screen and webcam side by side with event timeline markers; access control and watermarking; retention policy (for example 90 days, extended for cases under review); scheduled purge with certificate; storage utilisation dashboard.

### Business Objective
Make recordings usable as evidence while controlling storage.

### Actors
- EMU
- Malpractice Committee
- Super Admin

### User Journey
1. **Who creates:** Recordings are indexed automatically.
2. **How they create:** Authorised users search and play recordings.
3. **How they edit:** Retention settings changed by Super Admin.
4. **How they send for approval:** Retention changes need approval.
5. **How the approver sees pending items:** Approver sees changes.
6. **How the approver decides:** Approver approves.
7. **How the applicant / maker sees history:** Users see recordings within their scope.
8. **How the approver / auditor sees history:** Auditors see playback and purge logs.

### Functional Capabilities
- Recording index
- Side-by-side playback with timeline
- Event markers
- Watermarked playback
- Legal hold for cases
- Retention and purge jobs
- Storage dashboard

### UI Screens
- Recording search
- Playback with event timeline
- Retention settings
- Storage dashboard

### Logical API Operations
- Search recordings
- Secure streaming URLs
- Timeline events
- Legal hold
- Retention purge job

### Inputs
- Recordings

### Outputs
- Playback
- Purge certificates

### Business Rules
- Recordings under legal hold not purged

### Validations
- Access scope

### Calculations
- Storage used

### Workflow
Stored → Held / Purged

### Search Requirements
- By candidate, session

### Documents
- Purge certificates

### Reports
- Storage utilisation

### Notifications
- Storage threshold alerts

### Security
- Streaming tokens; watermark

### Integrations
- SDC object storage

### Dependencies
- F10-001
- F10-002
- F10-005

### Assumptions
- Storage capacity from SDC

### Risks
- Storage growth

### Non Functional Requirements
- Playback start under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Recording search | Medium | 6 |
| UI | Playback with event timeline | Complex | 12 |
| UI | Retention settings | Easy | 4 |
| UI | Storage dashboard | Medium | 6 |
| API | Search recordings | Medium | 6 |
| API | Secure streaming URLs | Medium | 6 |
| API | Timeline events | Medium | 6 |
| API | Legal hold | Easy | 4 |
| API | Retention purge job | Medium | 6 |
| Database | Recording index and retention | Easy | 2 |
| Testing | Playback and retention tests | Medium | 6 |
| Documentation | Recording retention policy note | Easy | 2 |

**Feature Total: 66 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 28 | 2 | 0 | 6 | 2 | **66** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
