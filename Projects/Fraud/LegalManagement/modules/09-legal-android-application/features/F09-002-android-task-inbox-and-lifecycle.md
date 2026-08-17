# F09-002 — Android task inbox and lifecycle

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Android task inbox and lifecycle |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user opens Task inbox, creates or is assigned a task, accepts or rejects, reassigns, marks completed, views overdue and outbox. Status matches the web task on the same matter.

### Business Objective
Run the Annexure-I task lifecycle on Android in lockstep with the web task on the same matter.

### Actors
Advocate; Legal Cell.

### User Journey
1. User opens Android Task Inbox.
2. Creates or is assigned a task; accepts or rejects; reassigns; marks completed; views overdue and outbox.
3. Status matches the web task on the same matter.

### Functional Capabilities
- Android Task Inbox / Outbox / Overdue
- Accept / Reject / Reassign / Complete screens
- Create task on device
- Parity with web F05-001–F05-003 status
- Completion attachment as on web

### Inputs
Task fields; actions; matter; completion report where required.

### Outputs
Updated task status on web and Android.

### Business Rules
- Status matches the web task on the same matter.
- Same Person; no Android-only assignees.
- Reprimand may be web-supervisor; device supports the listed inbox actions.

### Validations
Session valid; matter visible; complete rules as web.

### Calculations
Overdue as web.

### Workflow
Inbox → action → sync → web parity.

### Search Requirements
Inbox/outbox/overdue lists.

### Documents
Completion report on device upload.

### Reports
None on device (web schedule is F05-003).

### Notifications
Push/in-app for new assignment if configured.

### Security
Need-to-know; task body not in a public notification preview if sensitive.

### Integrations
Web task backend (Medium).

### Dependencies
F05-001–F05-003; F01-004.

### Assumptions
Push notifications use approved channel; not a public FCM marketing app.

### Risks
Split-brain status if sync delayed — last-write policy must match web.

### Non Functional Requirements
Inbox usable on court day; sync retry.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Task Inbox / Outbox / Overdue | UI | Very High | 16 |
| Accept / Reject / Reassign / Complete screens | UI | Complex | 12 |
| Task lifecycle operations | API | Complex | 8 |
| Device task cache | Database | Medium | 4 |
| Web task backend | Integration | Medium | 16 |
| Android task tests | Testing | Very High | 12 |
| Android task inbox guide | Documentation | Complex | 4 |
| **Total** | | | **72** |

### Estimation Assumptions
- Web lifecycle hours remain Module 05; this is Android + sync.
