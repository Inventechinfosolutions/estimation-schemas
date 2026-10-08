# F09-001 — Administrator Operational Dashboard

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Administrator Operational Dashboard |
| **Module** | 09 — Dashboards, Reports, Notifications and Audit |

### Description
Provide Examination Administrators with an operational dashboard covering registrations by type, pending and fee-paid counts, examination-wise and centre-wise volumes, scheduled/completed exams, pass/fail statistics and certificate generation status, with period filters, drill-downs and snapshot export for monitoring.

### Business Objective
Give administrators real-time (or near real-time) visibility to run the examination lifecycle without waiting for ad-hoc spreadsheet extracts.

### Actors
- Examination Administrator (primary user)
- Read-only oversight roles if mapped
- Auditor (may view same figures with audit of exports)
- Centre invigilators use F07-002, not this admin dashboard

### User Journey
1. Who creates: The system derives dashboard figures from registration, schedule, conduct, result and certificate records; administrators create filtered views and optional snapshot exports, not the underlying transactions.
2. How they create: Open administrator dashboard → select period/examination filters → review KPI tiles and centre/examination breakdowns → drill into a tile’s underlying count list → optionally export a snapshot.
3. How they edit: Dashboard numbers are not manually edited; filters and saved views (if provided) are the only user adjustments.
4. How they send for approval: Does not apply — monitoring only.
5. How the approver sees pending items: No approval inbox. “Pending registration” and similar tiles are operational queues for navigation into owning modules, not maker–checker.
6. How the approver decides: No decision on this feature.
7. How the applicant / maker sees history: Administrators can re-open prior period filters and snapshot export history.
8. How the approver / auditor sees history: Same dashboard with attributable snapshot exports; figures must reconcile to underlying records for the chosen period.

### Functional Capabilities
- Overall registration monitoring: by type, pending, fee-paid
- Examination-wise and centre-wise counts
- Scheduled vs completed examination monitoring
- Pass/fail statistics from published/evaluated results per approved source rule
- Certificate generation status monitoring
- Period filter and drill-down into count constituents
- Dashboard snapshot export view
- Reconciliation posture: figures match underlying records for chosen period (acceptance)
- Role-gated admin access (not centre-scoped inventory)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Administrator operational dashboard | Very High |
| Registration KPI panel | Complex |
| Schedule and centre monitor | Complex |
| Result and pass fail panel | Complex |
| Certificate status panel | Medium |
| Period filter and drill-down | Complex |
| Dashboard snapshot export view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Aggregate registration KPIs | Complex |
| Aggregate schedule and centre counts | Complex |
| Aggregate result statistics | Complex |
| Aggregate certificate status | Medium |
| Drill-down by examination or centre | Complex |
| Load dashboard for selected period | Medium |
| Export dashboard snapshot | Complex |
| List snapshot export history | Easy |

### Inputs
Period start/end, examination filter, centre filter, drill-down tile selection, export request.

### Outputs
KPI aggregates, drill-down lists, snapshot files, export history.

### Business Rules
- Dashboard is administrator-scoped; centre users do not see cross-centre admin KPIs here.
- Pass/fail statistics use the approved source (evaluated vs published) consistently and document that choice in assumptions.
- Counts for a period reconcile to underlying registration and examination records.
- Drill-down lists respect the same filters as the parent tile.

### Validations
- Valid date range
- Role authorisation for dashboard and export
- Filter combinations that return empty sets show empty state, not errors

### Calculations
Sums and rates (e.g. pass percentage) from underlying transactional data for the filter context.

### Workflow
No approval. Open → filter → monitor → optional drill/export.

### Search Requirements
Drill-down search within tile lists by registration number / examination / centre as applicable.

### Documents
Snapshot export in approved format (Excel/PDF as finally approved for snapshots).

### Reports
Detailed statutory/operational reports are F09-002; this feature is the monitoring dashboard.

### Notifications
None required for viewing; threshold alerts if any are F09-003.

### Security
Administrator role required; exports attributable; no candidate PII beyond what admin modules already permit.

### Integrations
None.

### Dependencies
Modules 01–08 as data sources.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Administrator operational dashboard UI is Very High effort.
- Pass/fail tile uses published results when publication exists, else evaluated — confirmed at build with Department.

### Risks
Stale caches causing non-reconciliation — prefer query definitions that match report logic where possible.
Over-heavy real-time refresh under load — near real-time acceptable if documented.

### Non Functional Requirements
Dashboard usable under concurrent admin users during peak registration and result days; drill-downs paginated.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Administrator operational dashboard | UI | Very High | 16 |
| Registration KPI panel | UI | Complex | 12 |
| Schedule and centre monitor | UI | Complex | 12 |
| Result and pass fail panel | UI | Complex | 12 |
| Certificate status panel | UI | Medium | 6 |
| Period filter and drill-down | UI | Complex | 12 |
| Dashboard snapshot export view | UI | Medium | 6 |
| Aggregate registration KPIs | API | Complex | 8 |
| Aggregate schedule and centre counts | API | Complex | 8 |
| Aggregate result statistics | API | Complex | 8 |
| Aggregate certificate status | API | Medium | 6 |
| Drill-down by examination or centre | API | Complex | 8 |
| Load dashboard for selected period | API | Medium | 6 |
| Export dashboard snapshot | API | Complex | 8 |
| List snapshot export history | API | Easy | 4 |
| Dashboard aggregate support structures | DB | Medium | 4 |
| Administrator operational dashboard tests | Testing | Very High | 12 |
| Administrator operational dashboard implementation documentation | Documentation | Complex | 4 |

**Feature total: 152 hours**
