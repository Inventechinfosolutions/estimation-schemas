# F05-001 — Request and Ticket Snapshot

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Request and Ticket Snapshot |
| **Module** | 05 — Admin Dashboard |

### Description
After Admin login, a simple dashboard shows **counts** of asset requests and tickets by status, plus a short list of recent or open items with a path to the full record.

### Business Objective
Admin can see open versus closed work without opening each register blindly.

### Actors
Maker: Admin. Approver: none. User role: not permitted.

### User Journey
1. Who creates: Admin does not create requests here; the dashboard reads existing requests and tickets.
2. How they create: Not applicable. Admin opens (or lands on) the operational dashboard.
3. How they edit: Dashboard figures are not edited. Admin drills through to a request or ticket to act (F03-003 / F04-003).
4. How they send for approval: Does not apply.
5. How the approver sees pending items: There is no checker inbox. Open counts and the recent/open list are the Admin work snapshot.
6. How the approver decides: No approval on this feature. Decisions remain status changes on the record.
7. How the applicant / maker sees history: Users do not see this dashboard; they use their own lists.
8. How the approver / auditor sees history: Admin sees current counts and can open a row to the record’s history.

### Functional Capabilities
- Count asset requests by Open, In progress, Closed, Rejected
- Count tickets by Open, In progress, Closed
- Show a short recent/open list mixing or grouping requests and tickets
- Open the related record from a dashboard row

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Admin operational dashboard | Very High |
| Recent open items list | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Request counts by status | Medium |
| Ticket counts by status | Medium |
| Recent open items | Medium |
| Open record from dashboard | Simple |

### Inputs
Admin session (no user input required for the default snapshot).

### Outputs
Counts by status; recent/open list; navigation to the request or ticket.

### Business Rules
- User role must not see this dashboard or all-user data.
- Counts must match the underlying registers for the same unfiltered snapshot.
- Rejected appears only on request counts.

### Validations
- Dashboard is refused for User role.

### Calculations
Counts of requests and tickets grouped by status.

### Workflow
None.

### Search Requirements
Default snapshot is unfiltered; filtered view is F05-002.

### Documents
None.

### Reports
Operational snapshot only; not a scheduled MIS pack.

### Notifications
None.

### Security
Admin only.

### Integrations
None.

### Dependencies
F03-003, F04-003 (records and statuses); F01-003 (Admin session).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Dashboard is a simple operational view, not GIS or executive analytics.
- Drill-through reuses admin detail screens billed under F03-003 / F04-003; this feature bills the open-from-dashboard operation only.

### Risks
If volumes grow far beyond typical BDA IT office use, count queries may need later optimisation (not in this estimate).

### Non Functional Requirements
Dashboard loads in reasonable time on the BDA office network for typical concurrent Admin use.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Admin operational dashboard | UI | Very High | 16 |
| Recent open items list | UI | Medium | 6 |
| Request counts by status | API | Medium | 6 |
| Ticket counts by status | API | Medium | 6 |
| Recent open items | API | Medium | 6 |
| Open record from dashboard | API | Simple | 2 |
| Dashboard aggregation indexes | DB | Easy | 2 |
| Request and ticket snapshot tests | Testing | Complex | 8 |
| Request and ticket snapshot implementation documentation | Documentation | Medium | 3 |

**Feature total: 55 hours**
