# F06-004 — Sync & conflict resolution

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-004 |
| Feature Name | Sync & conflict resolution |
| Module | 06 — Mobile Field Application |
| Description | Synchronize queued items when online and resolve conflicts per rules |
| Business Objective | Reliably upload field data when connectivity returns without silent data loss. |
| Actors | Field Personnel; System; Verifier (indirect) |

### User Journey

- Device online → background/foreground sync starts → queue drains → if server version differs, user sees conflict resolution prompt per rule → resolved item completes sync.

### Functional Capabilities

- Batch upload of queued PoD and task updates
- Server-side version comparison for conflicting checklist/task states
- Rule-driven resolution (server wins, client wins, manual merge for notes)
- Sync progress and failure retry with backoff

### Inputs

Local queue; server record versions; conflict policy configuration

### Outputs

Synchronized PoD and tasks visible on web; conflict audit trail

### Business Rules

Conflicts resolved per DIPR-agreed rules without silent overwrite
Failed sync items remain in queue with error reason

### Validations

Auth token valid before sync batch
Media upload integrity checks

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

Support view of sync failures via operational logs (Module 07/10)

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

F06-003; Module 05; F09-004 for integration failure patterns

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Sync progress modal with batch counters | Medium | 6 |
| UI | Background sync status chip on field home | Easy | 4 |
| UI | Conflict resolution choice dialog (server/client/manual) | Medium | 6 |
| UI | Sync failure detail with retry action | Easy | 4 |
| API | Start sync batch with auth gate | Medium | 6 |
| API | Upload queued PoD media chunks | Complex | 8 |
| API | Upload checklist/task delta batch | Complex | 8 |
| API | Server version compare for conflict detection | Complex | 8 |
| API | Apply conflict resolution rule outcome | Very High | 16 |
| Integration | Mobile-to-server delta sync orchestration | Complex | 24 |
| Integration | Exponential backoff retry scheduler | Medium | 16 |
| Database | Sync cursor per device | Easy | 2 |
| Database | Conflict audit and resolution log | Medium | 4 |
| Testing | Server-wins conflict scenario | Complex | 8 |
| Testing | Client-wins with notes merge | Complex | 8 |
| Testing | Auth expiry mid-sync recovery | Medium | 6 |
| Testing | Media integrity failure retry | Medium | 6 |
| Documentation | Sync and conflict DIPR rules matrix | Medium | 3 |
| Documentation | Support troubleshooting guide | Easy | 2 |

**Feature Total: 145 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
