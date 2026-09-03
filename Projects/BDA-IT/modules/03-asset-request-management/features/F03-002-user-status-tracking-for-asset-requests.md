# F03-002 — User Status Tracking for Asset Requests

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | User Status Tracking for Asset Requests |
| **Module** | 03 — Asset Request Management |

### Description
The User lists and opens **their own** asset requests and sees current status (Open, In progress, Closed, Rejected) including a simple status timeline after Admin updates.

### Business Objective
The requester can check progress in the application without calling or emailing IT.

### Actors
Maker: User viewing own requests. Approver: none.

### User Journey
1. Who creates: The User does not create records here; they open requests they already raised (F03-001).
2. How they create: Not applicable — tracking is view-only.
3. How they edit: User cannot edit or change status. They only open list and detail.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: There is no approver inbox on this feature.
6. How the approver decides: There is no decision on this feature.
7. How the applicant / maker sees history: My asset requests list → open detail → see current status and status timeline (when Admin moved Open → In progress → Closed/Rejected).
8. How the approver / auditor sees history: Admin uses F03-003, not this user-scoped view.

### Functional Capabilities
- List own requests only
- Filter own list by status
- Open read-only detail with type, description, attachment, status
- Show status timeline on the detail

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My asset requests list | Medium |
| My asset request detail | Easy |
| Request status timeline | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search my asset requests | Medium |
| Read my asset request | Easy |
| Read request status history | Easy |

### Inputs
Own account; optional status filter.

### Outputs
User-scoped list and detail; current status and timeline.

### Business Rules
- A User never sees another user’s asset requests.
- Admin using user functions still sees only their own list here; all-records view is F03-003.

### Validations
- Detail is refused if the request is not owned by the signed-in User (Admin all-records is a different feature).

### Calculations
None.

### Workflow
View-only.

### Search Requirements
Filter own requests by status and date.

### Documents
Show the optional attachment already stored on the request (no new upload here).

### Reports
None.

### Notifications
None. Status is visible in the list/detail.

### Security
User-scoped read. No status change.

### Integrations
None.

### Dependencies
F03-001; status values written by F03-003.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Cross-user visibility is never granted to the User role.

### Risks
If users expect email when status changes, that is out of scope and may cause operational follow-up.

### Non Functional Requirements
List remains usable as a user’s request count grows through normal office use.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| My asset requests list | UI | Medium | 6 |
| My asset request detail | UI | Easy | 4 |
| Request status timeline | UI | Simple | 2 |
| Search my asset requests | API | Medium | 6 |
| Read my asset request | API | Easy | 4 |
| Read request status history | API | Easy | 4 |
| User-scoped request indexes | DB | Easy | 2 |
| User asset request tracking tests | Testing | Medium | 6 |
| User status tracking for asset requests implementation documentation | Documentation | Easy | 2 |

**Feature total: 36 hours**
