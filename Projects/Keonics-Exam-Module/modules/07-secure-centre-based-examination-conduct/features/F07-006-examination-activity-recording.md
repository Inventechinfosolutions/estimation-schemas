# F07-006 — Examination Activity Recording

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-006 |
| **Feature Name** | Examination Activity Recording |
| **Module** | 07 — Secure Centre-Based Examination Conduct |

### Description
Capture a complete examination-day activity trail for each attempt: login/start/submit times, response change markers, paper version/sequence, centre, device/system and IP/network where available, session events, abnormal events and auto-submit flags, and provide staff search/timeline views and exportable session activity packs for investigation.

### Business Objective
Ensure every critical conduct event is attributable and reconstructable for operational monitoring, disputes and statutory audit.

### Actors
- System (primary recorder of events from F07-001–F07-005)
- Invigilator (views centre-scoped timelines)
- Examination Administrator (cross-centre search and export)
- Auditor (read-only full trail)

### User Journey
1. Who creates: The system creates activity records automatically as gate, login, interface, timer and submit events occur; staff do not manually invent core timing events. Invigilators may flag abnormal observations that are recorded as staff-noted events if approved.
2. How they create: Events are appended when source features fire (access allow/deny, login, start, auto-save markers, resume, auto-submit, lock). Staff open activity timeline/search to review; administrators may export a session activity pack.
3. How they edit: Activity records are append-only; corrections are compensating events, not silent edits. Staff cannot rewrite historical timestamps.
4. How they send for approval: Does not apply — recording is not an approval package.
5. How the approver sees pending items: No approver inbox. Abnormal-event register acts as an operational queue for administrators.
6. How the approver decides: No approval decision on the trail itself; investigation outcomes live outside this feature unless Department adds case handling later.
7. How the applicant / maker sees history: Candidates do not browse the full technical trail; they see only business statuses (started/submitted). Invigilators see centre-scoped timelines.
8. How the approver / auditor sees history: Administrators and auditors search and open full timelines with user/system actor, date/time, activity type, centre and environment metadata.

### Functional Capabilities
- Record login, start and submit timestamps
- Persist response-change / auto-save event markers sufficient for reconstruction (not necessarily every keystroke)
- Capture paper version and question-order sequence identifiers
- Capture centre, device/system, IP/network where available
- Record session events: resume, heartbeat loss, concurrent-session block
- Record abnormal events and auto-submit
- Centre-scoped and administrator search of activity timelines
- Session activity pack export for a candidate attempt
- Append-only integrity posture for critical events
- Link activity rows to registration, schedule, centre and attempt identifiers

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Session activity timeline | Complex |
| Abnormal event register | Medium |
| Environment and device audit detail | Medium |
| Candidate session event history | Easy |
| Activity search and filter | Medium |
| Session activity pack export view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Record login start and submit timestamps | Medium |
| Persist response and navigation event markers | Complex |
| Capture environment IP and device metadata | Complex |
| Record abnormal examination events | Complex |
| Record auto-submit event | Medium |
| Search activity timeline | Medium |
| Load environment audit detail | Easy |
| Export session activity pack | Complex |
| Append staff-noted observation event | Medium |

### Inputs
Event type, attempt/session identifiers, actor (user or system), timestamps, environment metadata, optional staff observation notes, export criteria.

### Outputs
Append-only activity store, searchable timelines, abnormal event list, exported activity pack.

### Business Rules
- Critical conduct actions listed in the SOW appear with actor and timestamp.
- Centre users see only their centre’s activity; administrators see all centres.
- Candidates cannot alter or delete activity history.
- Auto-submit and manual submit are distinctly flagged.
- Environment fields stored only as finally approved (privacy and infrastructure constraints).
- Activity recording failure must not silently succeed a lock without retry/alert to operations (aligned with NFR logging).

### Validations
- Event type and attempt reference mandatory
- Centre scope enforced on invigilator queries
- Export limited to authorised roles

### Calculations
None beyond ordering and duration displays derived from timestamps.

### Workflow
No approval. Source event → append → searchable history → optional export.

### Search Requirements
By candidate/registration, examination, centre, session, date/time, event type, abnormal flag, auto-submit flag.

### Documents
Exported activity pack (approved format) for investigation files.

### Reports
Feeds Module 09 audit and examination reports; this feature owns operational activity UI for Module 07.

### Notifications
Optional admin alert on abnormal bursts via F09-003 if configured.

### Security
Role-scoped read; append-only write path for system events; export audited.

### Integrations
None as external channel; internal event consumption from Module 07 features.

### Dependencies
F07-001–F07-005 as event sources; Module 09 audit may mirror or summarise critical subset (F09-004).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Full packet capture / proctoring video is out of scope unless Department adds it later.
- “Response recording” means answer selections and change markers, not continuous screen recording.

### Risks
High event volume if every auto-save is over-logged — tune marker granularity without losing reconstructability.
Missing environment signals when infrastructure cannot provide IP/device data.

### Non Functional Requirements
Recording path must not materially delay auto-save or submit; retention matches Department audit policy; searches return within interactive time for a single session timeline.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Session activity timeline | UI | Complex | 12 |
| Abnormal event register | UI | Medium | 6 |
| Environment and device audit detail | UI | Medium | 6 |
| Candidate session event history | UI | Easy | 4 |
| Activity search and filter | UI | Medium | 6 |
| Session activity pack export view | UI | Medium | 6 |
| Record login start and submit timestamps | API | Medium | 6 |
| Persist response and navigation event markers | API | Complex | 8 |
| Capture environment IP and device metadata | API | Complex | 8 |
| Record abnormal examination events | API | Complex | 8 |
| Record auto-submit event | API | Medium | 6 |
| Search activity timeline | API | Medium | 6 |
| Load environment audit detail | API | Easy | 4 |
| Export session activity pack | API | Complex | 8 |
| Append staff-noted observation event | API | Medium | 6 |
| Examination activity event store | DB | Complex | 6 |
| Examination activity recording tests | Testing | Complex | 8 |
| Examination activity recording implementation documentation | Documentation | Medium | 3 |

**Feature total: 117 hours**
