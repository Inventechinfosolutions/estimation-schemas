# F11-002 — Analytical Dashboards KPIs and Scheduled Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-002 |
| **Feature Name** | Analytical Dashboards KPIs and Scheduled Reports |
| **Module** | 11 — Reports, MIS and Analytics |

### Description
Analytical KPI dashboards and scheduled automated report delivery to configured Posts.

### Business Objective
Ongoing analytics and automated MIS distribution.

### Actors
Maker: MIS Administrator (schedules). Checker: MIS Checker. Recipients: configured Posts.

### User Journey
1. Who creates: MIS Administrator creates schedule; users open analytics.
2. How they create: Schedule → New: report, frequency, audience, Save draft. Analytics: open KPI dashboard.
3. How they edit: Draft schedule editable; approved schedule new version.
4. How they send for approval: Schedule submit to checker.
5. How the approver sees pending items: Checker schedule inbox.
6. How the approver decides: Approve schedule.
7. How the maker sees history: Schedule versions and delivery log.
8. How the checker/auditor sees history: Approved schedules and delivery log.

### Functional Capabilities
- KPI analytics
- Scheduled reports
- Delivery log

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Analytical KPI dashboard | Very High |
| Schedule form | Medium |
| Delivery log | Medium |
| Schedule checker inbox | Medium |
| Schedule approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Query KPI analytics | Very High |
| Save schedule | Medium |
| Submit schedule | Complex |
| Approve schedule | Complex |
| Run scheduled dispatch | Complex |

### Inputs
KPI set, schedule frequency, audience.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Predictive/advanced analytics depth as agreed in FRS after award.

### Validations
- Audience not empty for schedule.

### Calculations
KPI aggregations.

### Workflow
Maker–checker on schedules.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
This feature.

### Notifications
Scheduled email.

### Security
MIS admin Posts.

### Integrations
Email.

### Dependencies
F11-001.

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
| Analytical KPI dashboard | UI | Very High | 16 |
| Schedule form | UI | Medium | 6 |
| Delivery log | UI | Medium | 6 |
| Schedule checker inbox | UI | Medium | 6 |
| Schedule approval | UI | Easy | 4 |
| Query KPI analytics | API | Very High | 16 |
| Save schedule | API | Medium | 6 |
| Submit schedule | API | Complex | 8 |
| Approve schedule | API | Complex | 8 |
| Run scheduled dispatch | API | Complex | 8 |
| Schedules and delivery log | DB | Medium | 4 |
| Email delivery of scheduled reports | Integration | Easy | 8 |
| Analytical Dashboards KPIs and Scheduled Reports feature tests | Testing | Very High | 12 |
| Analytical Dashboards KPIs and Scheduled Reports implementation documentation | Documentation | Medium | 3 |

**Feature total: 111 hours**
