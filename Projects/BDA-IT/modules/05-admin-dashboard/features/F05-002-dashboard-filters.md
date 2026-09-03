# F05-002 — Dashboard Filters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Dashboard Filters |
| **Module** | 05 — Admin Dashboard |

### Description
Admin filters the operational dashboard (and linked snapshot lists) by **type** (asset request vs ticket), **status**, and **date range**. Counts and the item list refresh to match the filter.

### Business Objective
Admin can focus on, for example, Open tickets this week without exporting data.

### Actors
Maker: Admin. Approver: none.

### User Journey
1. Who creates: Admin applies a filter on the dashboard already provided by F05-001.
2. How they create: Dashboard filter bar → choose type and/or status and/or date range → apply. Counts and list update.
3. How they edit: Admin changes or clears filters. No saved filter presets in this phase.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: Filtered Open counts are the pending work under that filter — still not a checker inbox.
6. How the approver decides: No decision on this feature.
7. How the applicant / maker sees history: Not applicable for Users. Admin sees the filtered current snapshot, not a filter-history log.
8. How the approver / auditor sees history: Same filtered snapshot; record-level history remains on the request or ticket.

### Functional Capabilities
- Filter by type (request, ticket, or both)
- Filter by status
- Filter by date range (raised date)
- Recalculate counts and list for the same filters
- Clear filters back to the default snapshot

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Dashboard filter bar | Medium |
| Filtered dashboard results | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Apply dashboard filters | Medium |
| Filtered counts | Medium |
| Filtered item list | Medium |

### Inputs
Type, status, date from, date to.

### Outputs
Filtered counts and list consistent with each other.

### Business Rules
- User role cannot use these filters (no dashboard access).
- Filtered counts must match the filtered list’s underlying records.
- Invalid date range (from after to) is refused.

### Validations
- Date from ≤ date to when both are set.
- Status values depend on type (Rejected only valid for requests).

### Calculations
Recount by status under the active filter.

### Workflow
None.

### Search Requirements
Type, status, date range as specified.

### Documents
None.

### Reports
None. No export in this phase.

### Notifications
None.

### Security
Admin only.

### Integrations
None.

### Dependencies
F05-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- No saved views, scheduled emails, or Excel export.
- Filter bar is billed separately from the F05-001 dashboard canvas.

### Risks
Combining type + status + date may confuse if Rejected is offered while type is Ticket; validation must hide or refuse that combination.

### Non Functional Requirements
Filter apply refreshes counts without a full page redesign; attributable Admin session only.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Dashboard filter bar | UI | Medium | 6 |
| Filtered dashboard results | UI | Medium | 6 |
| Apply dashboard filters | API | Medium | 6 |
| Filtered counts | API | Medium | 6 |
| Filtered item list | API | Medium | 6 |
| Filtered query support | DB | Easy | 2 |
| Dashboard filters tests | Testing | Medium | 6 |
| Dashboard filters implementation documentation | Documentation | Easy | 2 |

**Feature total: 40 hours**
