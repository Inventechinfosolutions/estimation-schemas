# F05-003 — SLA Tracking & Aging

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-003 |
| Feature Name | SLA Tracking & Aging |
| Module | 05 — Workflow Automation, Escalation & SLA Tracking |
| Description | Track SLA timers, breaches, and aging for open complaints. |
| Business Objective | Make service-level risk visible to staff and supervisors. |
| Actors | Operator; Supervisor; Admin |

### User Journey

- System starts SLA on applicable event → clocks age → UI shows remaining/breached → breach may escalate.

### Functional Capabilities

- SLA clock start/pause/stop per FRS
- Aging and breach indicators
- Aging list/views

### Inputs

- SLA config
- Complaint timestamps/events

### Outputs

- Remaining time / breached flag
- Aging views

### Business Rules

- SLA source F02-003
- Breach triggers escalation/notify per config

### Validations

- Clock events consistent

### Calculations

- Remaining SLA = due − now (business calendar if FRS)

### Workflow

- Start → age → warn/breach → escalate/close stop

### Search Requirements

- Filter by nearing breach / breached

### Documents

- None

### Reports

- Feeds Module 07 monitoring

### Notifications

- SLA warning/breach via Module 06

### Security

- Role-based visibility

### Integrations

- None

### Dependencies

- F02-003
- F05-001

### Assumptions

- Business calendar rules in FRS if needed

### Risks

- Calendar complexity underestimated

### Non Functional Requirements

- Accurate timers; performant aging queries

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | SLA aging indicators and aging worklist views | Very High | 16 |
| API | SLA clock services and aging queries | Complex | 8 |
| Database | SLA instance timers and breach flags | Complex | 6 |
| Testing | Timer, breach, and aging scenarios | Complex | 8 |
| Documentation | SLA tracking notes | Medium | 3 |

**Feature Total: 41 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
