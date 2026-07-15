# F07-005 — CA Status Sync to Site Master
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F07-005 |
| **Feature Name** | CA Status Sync to Site Master |
| **Module** | 07 — CA Site Management |
### Description
Reflect approved CA availability, reservation, occupancy, expiry, and release status on the authoritative site master.
### Business Objective
Give officers and dashboards an accurate site-level view without manually reconciling the CA register.
### Actors
CA Officer; Site Master User; Auditor.
### User Journey
An approved CA lifecycle event changes the CA case; the system derives the corresponding site-master CA status, shows the source case and history, and flags any failed reflection for correction.
### Functional Capabilities
Status mapping, site-master status history, reconciliation list, and authorised resync action.
### Inputs
CA registration, proposal reservation, approved order, renewal/closure event, and mapped status.
### Outputs
Current CA status on site record, update history, and exception list.
### Business Rules
Only approved/effective CA events change site master; manual override is restricted and audited; site status does not replace the CA case record.
### Validations
Valid source event, configured status mapping, and current site link.
### Calculations
CA available/reserved/occupied totals by status.
### Workflow
CA event approved → status reflected → reconciliation exception if reflection fails → authorised reprocess.
### Search Requirements
Site, CA case, target status, update time, exception state.
### Documents
Source order/closure record link.
### Reports
CA-to-site reconciliation and status summary.
### Notifications
Failed reflection alert through Module 11.
### Security
CA and site-master write permissions; audit of status changes.
### Integrations
Internal site-master synchronization (Simple).
### Dependencies
F07-001 through F07-004; Module 04.
### Assumptions
Status mappings are finalized by BDA.
### Risks
Misconfigured mappings can misstate availability.
### Non Functional Requirements
Idempotent update handling and traceable reconciliation.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Site-status history and reconciliation list | UI | Complex | 8 |
| Status mapping/reprocess controls | UI | Medium | 6 |
| Derived status and reconciliation processing | API | Complex | 8 |
| Status history persistence | Database | Medium | 4 |
| Site-master synchronization | Integration | Simple | 4 |
| Sync/reconciliation tests | Testing | Complex | 8 |
| Status-sync guide | Documentation | Easy | 2 |
| **Total** | | | **40** |
