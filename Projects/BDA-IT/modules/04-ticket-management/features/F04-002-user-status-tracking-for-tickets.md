# F04-002 — User Status Tracking for Tickets

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | User Status Tracking for Tickets |
| **Module** | 04 — Ticket Management |

### Description
The User lists and opens **their own** tickets and sees current status (Open, In progress, Closed) including a simple status timeline after Admin updates.

### Business Objective
The requester can check ticket progress in the application without calling or emailing IT.

### Actors
Maker: User viewing own tickets. Approver: none.

### User Journey
1. Who creates: The User does not create records here; they open tickets they already raised (F04-001).
2. How they create: Not applicable — tracking is view-only.
3. How they edit: User cannot edit or change status.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: There is no approver inbox on this feature.
6. How the approver decides: There is no decision on this feature.
7. How the applicant / maker sees history: My tickets list → open detail → see current status and status timeline.
8. How the approver / auditor sees history: Admin uses F04-003, not this user-scoped view.

### Functional Capabilities
- List own tickets only
- Filter own list by status
- Open read-only detail with category, description, attachment, status
- Show status timeline on the detail

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tickets list | Medium |
| My ticket detail | Easy |
| Ticket status timeline | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search my tickets | Medium |
| Read my ticket | Easy |
| Read ticket status history | Easy |

### Inputs
Own account; optional status filter.

### Outputs
User-scoped list and detail; current status and timeline.

### Business Rules
- A User never sees another user’s tickets.
- Admin using user functions still sees only their own list here.

### Validations
- Detail is refused if the ticket is not owned by the signed-in User.

### Calculations
None.

### Workflow
View-only.

### Search Requirements
Filter own tickets by status and date.

### Documents
Show the optional attachment already stored on the ticket.

### Reports
None.

### Notifications
None.

### Security
User-scoped read. No status change.

### Integrations
None.

### Dependencies
F04-001; status values written by F04-003.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
If users expect email when a ticket is closed, that is out of scope.

### Non Functional Requirements
List remains usable as a user’s ticket count grows through normal office use.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| My tickets list | UI | Medium | 6 |
| My ticket detail | UI | Easy | 4 |
| Ticket status timeline | UI | Simple | 2 |
| Search my tickets | API | Medium | 6 |
| Read my ticket | API | Easy | 4 |
| Read ticket status history | API | Easy | 4 |
| User-scoped ticket indexes | DB | Easy | 2 |
| User ticket tracking tests | Testing | Medium | 6 |
| User status tracking for tickets implementation documentation | Documentation | Easy | 2 |

**Feature total: 36 hours**
