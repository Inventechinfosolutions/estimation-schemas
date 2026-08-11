# F07-002 — Real-time Monitoring

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-002 |
| Feature Name | Real-time Monitoring |
| Module | 07 — Dashboards, Analytics, Real-time Monitoring & MIS |
| Description | Near real-time monitoring of intake, pending, SLA, and escalations. |
| Business Objective | Allow supervisors/admins to spot surges and breaches quickly. |
| Actors | Admin; Supervisor |

### User Journey

- User opens monitoring view → sees live/near-live counters and lists → refreshes or auto-refreshes → drills in.

### Functional Capabilities

- Near-live intake/pending/SLA/escalation monitors
- Auto-refresh interval per design

### Inputs

- Refresh interval
- Scope filters

### Outputs

- Monitoring tiles and alert lists

### Business Rules

- Scope by role/jurisdiction

### Validations

- None beyond filters

### Calculations

- Live counts

### Workflow

- N/A

### Search Requirements

- Quick filter on monitoring lists

### Documents

- None

### Reports

- None

### Notifications

- May complement Module 06 alerts

### Security

- Admin/Supervisor

### Integrations

- None (polling/push within app)

### Dependencies

- F05-002
- F05-003
- Module 03

### Assumptions

- Near-real-time acceptable; true streaming optional

### Risks

- True websocket streaming may expand if demanded

### Non Functional Requirements

- Refresh without full page reload

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Near-real-time monitoring console with auto-refresh | Very High | 16 |
| API | High-frequency monitoring aggregate APIs | Very High | 16 |
| Database | Monitoring-friendly indexes/views | Medium | 4 |
| Testing | Refresh and scope monitoring cases | Complex | 8 |
| Documentation | Real-time monitoring notes | Easy | 2 |

**Feature Total: 46 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
