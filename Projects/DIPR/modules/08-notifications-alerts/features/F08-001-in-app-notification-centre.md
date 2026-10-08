# F08-001 — In-app notification centre

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F08-001 |
| Feature Name | In-app notification centre |
| Module | 08 — Notifications & Alerts |
| Description | Web/mobile in-app notifications for workflow and assignment events |
| Business Objective | Surface timely workflow, assignment, and PoD outcome alerts inside AMT web and mobile. |
| Actors | All entitled users; System |

### User Journey

- Event occurs → notification created → user sees badge on bell icon → opens centre → marks read → navigates to related record.

### Functional Capabilities

- Notification bell and unread count on web
- In-app feed on mobile field app for assignments and outcomes
- Deep links to campaign, task, or PoD context
- Mark read / mark all read

### Inputs

Event type; recipient user; payload summary; deep link target

### Outputs

In-app notification records and read state

### Business Rules

Only recipients entitled to underlying record receive notification
Retention of notifications per platform policy

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

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

Modules 03, 05, 06; F08-004 for preferences

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Web notification bell with unread badge | Easy | 4 |
| UI | Web notification centre drawer with list | Complex | 12 |
| UI | Notification detail/read expand row | Easy | 4 |
| UI | Mobile field in-app notification feed | Medium | 6 |
| UI | Mark all read action bar | Simple | 2 |
| API | Create in-app notification on platform events | Medium | 6 |
| API | List notifications with pagination | Easy | 4 |
| API | Mark single notification read | Simple | 2 |
| API | Mark all read for user | Simple | 2 |
| API | Unread count aggregate | Easy | 4 |
| Database | In-app notification entity store | Medium | 4 |
| Database | Per-user read state index | Easy | 2 |
| Testing | Event-to-in-app delivery mapping | Medium | 6 |
| Testing | Unread badge accuracy | Easy | 4 |
| Testing | Mobile feed parity | Medium | 6 |
| Documentation | In-app notification event catalogue | Easy | 2 |
| Documentation | Badge polling behaviour notes | Simple | 1 |

**Feature Total: 71 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
