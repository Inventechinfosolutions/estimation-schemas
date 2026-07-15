# F09-003 — In-app Notification Center

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F09-003 |
| **Feature Name** | In-app Notification Center |
| **Module** | 09 — Notification Service |

### Description
Provide in-app notification center/alerts for officers and tenants (workflow tasks, payment results, notice copies, escalations) with unread badges and read-state.

### Business Objective
Surface time-sensitive actions inside CPMS even when SMS/email is delayed or unavailable.

### Actors
- All authenticated users (role-filtered), Tenant portal users

### User Journey
1. Event creates in-app notification for user(s)/role queue.
2. User sees bell badge → opens notification center.
3. Clicks item → marks read → navigates deep link to entity.

### Functional Capabilities
- Per-user inbox
- Unread count badge
- Mark read / mark all read
- Deep links to business entities
- Optional role broadcast (e.g., approvers)
- Retention/cleanup policy for old notifications

### Inputs
- Title, body, severity, recipient user/role, deep link, source ref

### Outputs
- In-app notification records; unread counts

### Business Rules
- Users only see own notifications (and permitted queue items).
- Complements SMS/email—not a replacement for statutory notice channels.

### Validations
- Recipient exists; deep link allow-list patterns

### Calculations
- Unread count

### Workflow
N/A.

### Search Requirements
Filter by read/unread, date, type.

### Documents
N/A.

### Reports
Optional engagement stats—not baseline.

### Notifications
N/A.

### Security
No cross-user inbox leakage; strip sensitive payloads.

### Integrations
None.

### Dependencies
F09-001 producers; Module 01 users; business deep links

### Assumptions
- Complex UI for polished notification center.
- Push mobile native notifications out of scope.

### Risks
- Notification spam — preference/category mute later if needed.

### Non Functional Requirements
- Near-real-time badge update (polling or light websocket—implementation choice)

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| In-app notification center UI | UI | Complex | 8 |
| Bell / unread badges | UI | Easy | 4 |
| In-app notify & read-state ops | API | Medium | 6 |
| In-app notification entities | Database | Medium | 4 |
| In-app notification tests | Testing | Medium | 6 |
| In-app notifications guide | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Realtime transport choice left to architecture; estimate assumes efficient polling acceptable.
