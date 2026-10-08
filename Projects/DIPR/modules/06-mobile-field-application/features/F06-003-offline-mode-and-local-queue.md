# F06-003 — Offline mode & local queue

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-003 |
| Feature Name | Offline mode & local queue |
| Module | 06 — Mobile Field Application |
| Description | Queue PoD and task updates while offline |
| Business Objective | Allow uninterrupted field work in low-connectivity areas without losing captures or checklist updates. |
| Actors | Field Personnel; System |

### User Journey

- Connectivity lost → app switches to offline mode → user continues PoD/checklist work → items appear in local queue → user sees pending sync count.

### Functional Capabilities

- Detect online/offline state and surface offline banner
- Persist PoD media and task/checklist updates in encrypted local queue
- Retry-safe queue ordering for upload
- Storage limits and cleanup warnings

### Inputs

Queued PoD payloads; checklist deltas; timestamps

### Outputs

Durable local queue ready for F06-004 sync

### Business Rules

Designated functions only operate offline per SoW
Queue items retain campaign/task linkage

### Validations

Prevent duplicate queue keys for same task action where applicable
Disk quota handling with user messaging

### Calculations

- None

### Workflow

Capture/update offline → enqueue → await connectivity

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

F06-001; F06-002

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

Queue must survive app restart; sensitive data encrypted at rest on device

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Global offline banner and connectivity badge | Easy | 4 |
| UI | Queued items list with type and retry status | Medium | 6 |
| UI | Queue item detail with error reason dialog | Easy | 4 |
| UI | Storage quota warning dialog | Simple | 2 |
| API | Connectivity state observer hook | Simple | 2 |
| API | Enqueue PoD media and checklist delta operations | Very High | 16 |
| API | Dequeue and mark-in-flight queue operations | Complex | 8 |
| API | Queue deduplication key validation | Medium | 6 |
| API | Encrypted local persistence read/write layer | Complex | 8 |
| Database | On-device queue entity store | Complex | 6 |
| Database | Staged media blob index | Medium | 4 |
| Testing | App restart queue survival | Complex | 8 |
| Testing | Duplicate enqueue prevention | Medium | 6 |
| Testing | Disk quota handling | Medium | 6 |
| Testing | Offline PoD then online drain smoke | Very High | 12 |
| Documentation | Offline operations field runbook | Medium | 3 |
| Documentation | Queue encryption and retention notes | Easy | 2 |

**Feature Total: 103 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
