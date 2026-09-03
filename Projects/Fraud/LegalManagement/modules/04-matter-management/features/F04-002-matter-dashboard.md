# F04-002 — Matter dashboard

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Matter dashboard |
| **Module** | 04 — Matter Management |

### Description
The user opens the matter and sees in one place: tasks, documents, communication and messages, activities, team members, client contacts, court hearings, time entries and key dates, and can search within that matter.

### Business Objective
Give Legal Cell and advocates a single hub per matter so court work is not scattered across disconnected screens.

### Actors
Legal Cell; Advocate; Competent Authority (review).

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens a matter from search or My Matters.
3. How they edit: Matter Hub Dashboard shows tasks, documents, communication and messages, activities, team members, client contacts, court hearings, time entries and key dates.
4. How they send for approval: User searches within that matter. Open matter → dashboard aggregate → in-matter search or drill-in.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. User drills into an item (task, document, hearing) without leaving the matter context.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Matter Hub Dashboard
- In-Matter Search panel
- Integrated tiles/lists: tasks, documents, communication, activities, team, client contacts, hearings, time, key dates
- Drill-through to the owning feature without losing matter context
- Not a standalone DMS or BPM product

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Matter Hub Dashboard | Very High |
| In-Matter Search panel | Medium |
| Matter dashboard history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Dashboard aggregation operations | Very High |
| Update matter dashboard | Medium |
| Search matter dashboard | Medium |
| Read matter dashboard history | Easy |

### Inputs
Matter identity; in-matter search text.

### Outputs
Aggregated matter view; in-matter search hits.

### Business Rules
- Opening a matter shows the listed work objects in one dashboard.
- Visibility of each tile still follows F01-002/F01-003 and task assignment.
- Does not display Claim settlement payment status or eValueI GIS maps.

### Validations
- Matter must exist and be visible to the Post; in-matter search scoped to that matter only.

### Calculations
Counts (open tasks, overdue key dates) as display totals.

### Workflow
Open matter → dashboard aggregate → in-matter search or drill-in.

### Search Requirements
Within matter: task, document, message, hearing, contact, key date, activity.

### Documents
Document list from F04-004 (embedded).

### Reports
None (F04-007 is separate reports).

### Notifications
Overdue key dates indicated on the dashboard (alerts owned with F04-006).

### Security
Need-to-know; Limited folder contents hidden from non-members.

### Integrations
Tasks/docs/comms/hearings/time/dates consume (Medium).

### Dependencies
F04-001; F04-004–F04-006; F05; F06; F07; F09-005 consumes the same hub on Android.

### Assumptions
- Child objects are created in their features; this feature is the hub and in-matter search.

### Risks
Slow aggregation on large matters; tiles must degrade gracefully if a child module is delayed in phasing.

### Non Functional Requirements
Court-day responsiveness; consistent with Android matter dashboard (F09-005) in content, not a second data model.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Matter Hub Dashboard | UI | Very High | 16 |
| In-Matter Search panel | UI | Medium | 6 |
| Matter dashboard history | UI | Medium | 6 |
| Dashboard aggregation operations | API | Very High | 16 |
| Update matter dashboard | API | Medium | 6 |
| Search matter dashboard | API | Medium | 6 |
| Read matter dashboard history | API | Easy | 4 |
| Matter dashboard persistence | DB | Medium | 4 |
| Tasks, documents, communication, hearings, time and key dates consume | Integration | Medium | 16 |
| Matter dashboard feature tests | Testing | Very High | 12 |
| Matter dashboard implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **96** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
