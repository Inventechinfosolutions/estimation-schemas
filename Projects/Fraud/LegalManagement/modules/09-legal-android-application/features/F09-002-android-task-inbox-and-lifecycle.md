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
1. Who creates: Advocate
2. How they create: User opens Android Task Inbox.
3. How they edit: Creates or is assigned a task; accepts or rejects; reassigns; marks completed; views overdue and outbox. Draft or returned records can be edited; decided records are not silently overwritten.
4. How they send for approval: Status matches the web task on the same matter. Inbox → action → sync → web parity.
5. How the approver sees pending items: Legal Cell opens the pending inbox for this feature and opens a row.
6. How the approver decides: Legal Cell approves, rejects or returns with remarks.
7. How the applicant sees history: Advocate opens history on the record (actor Person, Post, time, status, remarks).
8. How the approver / auditor sees history: Legal Cell and auditor open the same history for items in their scope.

### Functional Capabilities
- Android Task Inbox / Outbox / Overdue
- Accept / Reject / Reassign / Complete screens
- Create task on device
- Parity with web F05-001–F05-003 status
- Completion attachment as on web

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My android task inbox and lifecycle register | Medium |
| Accept / Reject / Reassign / Complete screens | Complex |
| Submit confirmation | Simple |
| Approver android task inbox and lifecycle inbox | Complex |
| Android task inbox and lifecycle decision panel (approve / reject / return) | Medium |
| My android task inbox and lifecycle history | Medium |
| Team android task inbox and lifecycle history (approver) | Medium |
| Android Task Inbox / Outbox / Overdue | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft android task inbox and lifecycle | Medium |
| Update draft android task inbox and lifecycle | Medium |
| Task lifecycle operations | Complex |
| Withdraw android task inbox and lifecycle | Easy |
| Approver inbox query | Medium |
| Approve, reject or return android task inbox and lifecycle | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Task fields; actions; matter; completion report where required.

### Outputs
Updated task status on web and Android.

### Business Rules
- Status matches the web task on the same matter.
- Same Person; no Android-only assignees.
- Reprimand may be web-supervisor; device supports the listed inbox actions.

### Validations
- Session valid; matter visible; complete rules as web.

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
- Push notifications use approved channel; not a public FCM marketing app.

### Risks
Split-brain status if sync delayed — last-write policy must match web.

### Non Functional Requirements
Inbox usable on court day; sync retry.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My android task inbox and lifecycle register | UI | Medium | 6 |
| Accept / Reject / Reassign / Complete screens | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver android task inbox and lifecycle inbox | UI | Complex | 12 |
| Android task inbox and lifecycle decision panel (approve / reject / return) | UI | Medium | 6 |
| My android task inbox and lifecycle history | UI | Medium | 6 |
| Team android task inbox and lifecycle history (approver) | UI | Medium | 6 |
| Android Task Inbox / Outbox / Overdue | UI | Very High | 16 |
| Save draft android task inbox and lifecycle | API | Medium | 6 |
| Update draft android task inbox and lifecycle | API | Medium | 6 |
| Task lifecycle operations | API | Complex | 8 |
| Withdraw android task inbox and lifecycle | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return android task inbox and lifecycle | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Android task inbox and lifecycle record and status history | DB | Medium | 4 |
| Web task backend | Integration | Medium | 16 |
| Android task inbox and lifecycle feature tests | Testing | Very High | 12 |
| Android task inbox and lifecycle implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **152** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
