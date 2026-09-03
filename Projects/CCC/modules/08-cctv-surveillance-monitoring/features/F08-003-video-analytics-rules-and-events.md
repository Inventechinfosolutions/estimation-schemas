# F08-003 — Video Analytics Rules and Events

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Video Analytics Rules and Events |
| **Module** | 08 — CCTV Surveillance Monitoring |

### Description
Surveillance Administrator configures godown camera analytics (tripwire, intrusion, intelligent motion detection and similar events named in the tender). The CCC receives analytics events from the integrated CCTV/VMS channel, lets operators review clips/metadata, and escalates confirmed exceptions to Module 09 incidents. Analytics engine capability on cameras/NVR is assumed from the field CCTV ecosystem; this feature is the CCC configuration, event intake, review and escalation software.

### Business Objective
Detect and act on warehouse surveillance exceptions beyond passive live viewing (tender: video analytics and surveillance management).

### Actors
Maker: Surveillance Administrator (rules). Checker: Surveillance Checker. User: CCC Operator / Vigilance Officer (event review). System: ingests analytics events. Other: Module 09 assignee when escalated.

### User Journey
1. Who creates: Surveillance Administrator creates analytics rules; system creates events from camera/VMS analytics; Operator reviews events.
2. How they create: Analytics rules → New: godown, camera(s), analytic type (tripwire / intrusion / intelligent motion / other catalogue), zone/schedule, severity, Save draft. Events appear on the analytics event monitor as the feed delivers them.
3. How they edit: Draft/Returned rules editable; approved rule change is a new version. Event remarks only — raw event payload is not silently deleted.
4. How they send for approval: Rule submit to Surveillance Checker. Event escalation Submit creates/links a Module 09 incident.
5. How the approver sees pending items: Checker analytics-rule inbox. Escalated events appear in Module 09 incident inbox.
6. How the approver decides: Approve or reject rule. For events: Operator confirms false positive, or escalates; Supervisor decides the linked incident in Module 09.
7. How the maker/operator sees history: Rule versions; my reviewed events and escalations.
8. How the checker/auditor sees history: Approved rules; analytics event log with who reviewed or escalated.

### Functional Capabilities
- Configure analytics rule types (tripwire, intrusion, intelligent motion detection and catalogue extensions).
- Scope rules to godown and camera with optional schedule/zone.
- Maker–checker on rule go-live.
- Ingest and list analytics events with camera, time, type and severity.
- Review event with linked clip/snapshot when the stream/VMS provides it.
- Escalate confirmed events to Module 09 incidents; mark false positives with reason.
- Unit-scoped visibility by Post.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Analytics rule register | Medium |
| Analytics rule form (type, camera, zone/schedule) | Complex |
| Analytics rule maker–checker inbox | Medium |
| Analytics rule approval panel | Easy |
| Analytics event monitor | Complex |
| Analytics event detail / clip review | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft analytics rule | Medium |
| Submit analytics rule for checker | Complex |
| Approve or reject analytics rule | Complex |
| Ingest analytics event from CCTV/VMS | Very High |
| Query analytics events | Complex |
| Mark false positive | Easy |
| Escalate analytics event to incident | Complex |

### Inputs
Godown, camera, analytic type, zone/schedule, severity, event timestamp, optional clip/snapshot reference, review remarks.

### Outputs
Approved analytics rules; event log; false-positive marks; linked Module 09 incidents; searchable history.

### Business Rules
- Analytic types include at least tripwire, intrusion and intelligent motion detection as named in the tender camera specifications; further types may be added to the catalogue without a new module.
- Only approved cameras (F08-001) may be bound to rules.
- Camera/NVR analytics engines and field hardware remain out of application-software hours; CCC consumes events via the CCTV integration channel (F12-002).
- False-positive marks require a reason; events are not physically deleted.

### Validations
- Camera and analytic type mandatory on rule submit.
- Rule audience/scope must resolve to an approved godown.
- Escalate requires an existing event and Operator Post with escalate right.

### Calculations
Event ageing for monitor sorting; optional count of events by type/godown for Module 11 reports.

### Workflow
Rules: Draft → Submitted → Approved/Rejected. Events: Received → Reviewed (false positive) or Escalated → linked incident lifecycle in Module 09.

### Search Requirements
Rules by godown, camera, type, status. Events by godown, camera, type, severity, period, review status — scoped by acting Post.

### Documents
Optional snapshot/clip reference from VMS (embedded metadata, not a standalone DMS).

### Reports
Analytics event volume and false-positive rates via Module 11 (CCTV activity / exception reports).

### Notifications
Rule approval notifications to maker. New high-severity analytics events notify configured Posts via Module 09 alert rules when configured.

### Security
Surveillance and Vigilance Posts only; need-to-know by godown/unit scope; rule and event actions attributable to Person + Post.

### Integrations
CCTV/VMS analytics event channel (builds on F12-002 ONVIF/multi-vendor video integration).

### Dependencies
F08-001, F08-002, F12-002, Module 09 for escalation.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Field cameras provide the analytic detections listed in the tender; this estimate is CCC software to configure, receive, review and escalate those events.
- GPS/CCTV field hardware supply and install remain out of hours.

### Risks
Vendors that expose only basic motion without tripwire/intrusion APIs would force reduced analytic types or custom mapping effort.

### Non Functional Requirements
Event monitor remains usable under burst event load at State CCC; ingest is resilient with retry and audit of failed events.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Analytics rule register | UI | Medium | 6 |
| Analytics rule form (type, camera, zone/schedule) | UI | Complex | 12 |
| Analytics rule maker–checker inbox | UI | Medium | 6 |
| Analytics rule approval panel | UI | Easy | 4 |
| Analytics event monitor | UI | Complex | 12 |
| Analytics event detail / clip review | UI | Complex | 12 |
| Save draft analytics rule | API | Medium | 6 |
| Submit analytics rule for checker | API | Complex | 8 |
| Approve or reject analytics rule | API | Complex | 8 |
| Ingest analytics event from CCTV/VMS | API | Very High | 16 |
| Query analytics events | API | Complex | 8 |
| Mark false positive | API | Easy | 4 |
| Escalate analytics event to incident | API | Complex | 8 |
| Analytics rules and event log | DB | Complex | 6 |
| CCTV/VMS analytics event channel | Integration | Complex | 24 |
| Video Analytics Rules and Events feature tests | Testing | Very High | 12 |
| Video Analytics Rules and Events implementation documentation | Documentation | Complex | 4 |

**Feature total: 156 hours**
