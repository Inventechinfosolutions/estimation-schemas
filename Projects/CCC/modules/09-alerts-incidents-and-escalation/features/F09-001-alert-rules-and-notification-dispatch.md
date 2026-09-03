# F09-001 — Alert Rules and Notification Dispatch

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Alert Rules and Notification Dispatch |
| **Module** | 09 — Alerts, Incidents and Escalation |

### Description
Administrator configures alert rules for route deviation, unauthorized stoppage, delay, device tampering, unauthorized RFID/ANPR, camera down; system dispatches in-app/SMS/email to Posts.

### Business Objective
Real-time exception awareness.

### Actors
Maker: Alert Administrator. Checker: Alert Checker. Recipients: mapped Posts.

### User Journey
1. Who creates: Alert Administrator.
2. How they create: Alert rules → New: event type, thresholds, audience Posts, channels, Save draft.
3. How they edit: Draft/Returned editable; live change is new version.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker alert-rule inbox.
6. How the approver decides: Approve or reject rule.
7. How the maker sees history: Rule versions and send log.
8. How the checker/auditor sees history: Approved rules and dispatch log.

### Functional Capabilities
- Rule configuration
- Multi-channel dispatch
- Send log

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Alert rule register | Medium |
| Alert rule form | Complex |
| Alert send log | Medium |
| Alert rule inbox | Medium |
| Alert rule approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save alert rule | Complex |
| Submit rule | Complex |
| Approve rule | Complex |
| Dispatch alert | Very High |
| Query send log | Medium |

### Inputs
Event type, threshold, audience, channel.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Audience Posts resolve to mapped Persons.

### Validations
- Audience not empty.
- Event type from catalogue.

### Calculations
Threshold comparisons.

### Workflow
Maker–checker on rules; runtime auto-dispatch.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Alert volume.

### Notifications
This feature.

### Security
Admin Posts for rules.

### Integrations
SMS/email.

### Dependencies
Module 01, 05–08.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Alert rule register | UI | Medium | 6 |
| Alert rule form | UI | Complex | 12 |
| Alert send log | UI | Medium | 6 |
| Alert rule inbox | UI | Medium | 6 |
| Alert rule approval | UI | Easy | 4 |
| Save alert rule | API | Complex | 8 |
| Submit rule | API | Complex | 8 |
| Approve rule | API | Complex | 8 |
| Dispatch alert | API | Very High | 16 |
| Query send log | API | Medium | 6 |
| Alert rules and dispatch log | DB | Complex | 6 |
| SMS gateway and email for alerts | Integration | Medium | 16 |
| Alert Rules and Notification Dispatch feature tests | Testing | Very High | 12 |
| Alert Rules and Notification Dispatch implementation documentation | Documentation | Medium | 3 |

**Feature total: 117 hours**
