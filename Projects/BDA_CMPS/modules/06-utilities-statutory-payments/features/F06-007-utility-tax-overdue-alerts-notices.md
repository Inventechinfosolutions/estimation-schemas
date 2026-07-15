# F06-007 — Utility & Tax Overdue Alerts & Notices

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-007 |
| **Feature Name** | Utility & Tax Overdue Alerts & Notices |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
Identify overdue utility and property tax items for dashboards and notice candidates, with optional batch notice generation and alerts (M5-AC4).

### Business Objective
Ensure timely payment of statutory and utility dues through visibility and automated reminders.

### Actors
- Utility Officer, Tax Officer, Accounts Officer
- System scheduler

### User Journey
1. Scheduler/officer views overdue worklist (utility bills + tax assessments past due).
2. Items flagged for Module 11 dashboards.
3. Officer generates utility/tax due notices from templates for internal owners and/or tenants (when recovery-related).
4. Delivery via Module 09; status logged.

### Functional Capabilities
- Overdue detection for utilities and tax
- Worklist with filters (type, property, days overdue)
- Notice candidate selection & batch send
- Dashboard feed flags (Module 11 consumes)
- Alert thresholds configurable

### Inputs
- As-of date, filters, notice template/channel

### Outputs
- Overdue lists; notices; dashboard indicators

### Business Rules
- Overdue utility/tax items appear on dashboards and notice candidates (M5-AC4).
- Tenant-facing recovery notices only when recovery dues exist (else internal BDA payment reminders).

### Validations
- Preview cohort before send

### Calculations
- days_overdue = as_of − due_date

### Workflow
Detect → Review → Notify → Log.

### Search Requirements
Overdue by type, days band, location/property.

### Documents
Notice PDFs (Module 08).

### Reports
Overdue Utility Report; Overdue Tax Report.

### Notifications
Module 09 SMS/email/in-app.

### Security
RBAC + scope; audit batches.

### Integrations
Notification Service (Simple).

### Dependencies
F06-003/005; F02-010; Modules 08–09, 11

### Assumptions
- Dashboard widgets estimated in Module 11; this supplies candidates/APIs.
- Rent overdue remains Module 05.

### Risks
- Alert noise — cadence configuration required.

### Non Functional Requirements
- Nightly overdue refresh job acceptable

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Overdue utilities/tax worklist | UI | Complex | 8 |
| Notice candidate batch UI | UI | Medium | 6 |
| Overdue detect & notice candidate ops | API | Medium | 6 |
| Overdue snapshot support | Database | Easy | 2 |
| Notification handoff | Integration | Simple | 4 |
| Overdue alert tests | Testing | Medium | 6 |
| Overdue alerts guide | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Does not include Module 11 widget UI hours.
