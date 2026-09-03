# F06-003 — Meeting Scheduling and Participant Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Meeting Scheduling and Participant Management |
| **Module** | 06 — Office & Administration (Visitor, Reception and Meetings) |

### Description
Organiser creates a meeting, invites Posts/Persons, submitting for room/host approval if required; participants see it; history of versions is kept.

### Business Objective
Controlled scheduling with participant list.

### Actors
Applicant: Organiser (Person in a Post with meeting Role). Approver: Room/admin Post if a room is booked; otherwise Submit publishes to invitees without a second approve. Other: Invitees. Auditor.

### User Journey
1. Who creates: Organiser (Person in a Post with meeting Role).
2. How they create: Organiser → New meeting: title, time, venue/room, agenda, add participants (Person/Post), Save draft.
3. How they edit: Draft editable. After publish, time/venue changes notify invitees and may require re-approve if room booked.
4. How they send for approval: Submit for room approval if room selected; else Publish to participants.
5. How the approver sees pending items: Room admin inbox. Invitees see My Meetings.
6. How the approver decides: Room admin Approve/Reject booking. Invitees Accept/Decline (not a financial approve).
7. How the applicant sees history: Organiser sees versions and RSVP counts.
8. How the approver sees history: Room admin sees booking decisions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own meeting history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My meeting register | Medium |
| Meeting form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver meeting inbox | Complex |
| Meeting decision panel (approve / reject / return) | Medium |
| My meeting history | Medium |
| Team meeting history (approver) | Medium |
| Participant picker | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft meeting | Medium |
| Update draft meeting | Medium |
| Submit meeting for approval | Complex |
| Withdraw meeting | Easy |
| Approver inbox query | Medium |
| Approve, reject or return meeting | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Title, start/end, venue, participants, agenda.

### Outputs
Persisted meeting with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own meeting.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- End after start.
- At least one participant.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Agenda attachment optional.

### Reports
Meetings by office/room.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Internal identity (Module 01) and notification service. Document store when attachments are required.

### Dependencies
Module 01 Person–Post–Role mapping (current Post and supervising Post). Notifications use the mapped Person of the supervising Post.

### Assumptions
- Supervising Post is maintained on the Post master (Module 01).
- Hours use Estimation Master values only, at capability grain (primary and secondary UI, one logical API, persistence, tests, documentation).

### Risks
Wrong supervising Post mapping would send the request to the wrong approver.

### Non Functional Requirements
Inbox and history screens remain usable under concurrent office load. Status history is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My meeting register | UI | Medium | 6 |
| Meeting form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver meeting inbox | UI | Complex | 12 |
| Meeting decision panel (approve / reject / return) | UI | Medium | 6 |
| My meeting history | UI | Medium | 6 |
| Team meeting history (approver) | UI | Medium | 6 |
| Participant picker | UI | Medium | 6 |
| Save draft meeting | API | Medium | 6 |
| Update draft meeting | API | Medium | 6 |
| Submit meeting for approval | API | Complex | 8 |
| Withdraw meeting | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return meeting | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Meeting record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on meeting status change | Integration | Simple | 4 |
| Meeting Scheduling and Participant Management feature tests | Testing | Complex | 8 |
| Meeting Scheduling and Participant Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
