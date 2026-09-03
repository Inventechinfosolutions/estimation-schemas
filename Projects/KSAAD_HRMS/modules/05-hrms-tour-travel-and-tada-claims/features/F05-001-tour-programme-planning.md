# F05-001 — Tour Programme Planning

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Tour Programme Planning |
| **Module** | 05 — HRMS Tour, Travel & TA/DA Claims |

### Description
Staff member (or supervisor) plans a tour; supervising Post approves the plan before travel/TA.

### Business Objective
Approved tour plan before claims.

### Actors
Applicant: Person mapped to a Post (field staff) or supervisor planning for a team. Approver: Supervising Post. Other: Team members listed on the tour (read). Auditor.

### User Journey
1. Who creates: Person mapped to a Post (field staff) or supervisor planning for a team.
2. How they create: Applicant opens My Tours → New, itinerary dates, places, purpose, linked audit assignment if any, members, Save draft.
3. How they edit: Draft/Returned editable. Approved tours change only via a revision request (new version).
4. How they send for approval: Submit to supervising Post.
5. How the approver sees pending items: Supervisor Tour inbox.
6. How the approver decides: Approve, reject or return. Approved tour becomes selectable on TA/DA (F05-002).
7. How the applicant sees history: My Tours with versions and decisions.
8. How the approver sees history: Team tours decided.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own tour programme history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tour programme register | Medium |
| Tour programme form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver tour programme inbox | Complex |
| Tour programme decision panel (approve / reject / return) | Medium |
| My tour programme history | Medium |
| Team tour programme history (approver) | Medium |
| Itinerary grid | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft tour programme | Medium |
| Update draft tour programme | Medium |
| Submit tour programme for approval | Complex |
| Withdraw tour programme | Easy |
| Approver inbox query | Medium |
| Approve, reject or return tour programme | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Dates, places, purpose, members, linked assignment.

### Outputs
Persisted tour programme with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own tour programme.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Dates mandatory.
- At least one member.
- End ≥ start.

### Calculations
Tour days = inclusive dates.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional tour sanction note.

### Reports
Approved tours by office.

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
| My tour programme register | UI | Medium | 6 |
| Tour programme form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver tour programme inbox | UI | Complex | 12 |
| Tour programme decision panel (approve / reject / return) | UI | Medium | 6 |
| My tour programme history | UI | Medium | 6 |
| Team tour programme history (approver) | UI | Medium | 6 |
| Itinerary grid | UI | Complex | 12 |
| Save draft tour programme | API | Medium | 6 |
| Update draft tour programme | API | Medium | 6 |
| Submit tour programme for approval | API | Complex | 8 |
| Withdraw tour programme | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return tour programme | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Tour programme record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on tour programme status change | Integration | Simple | 4 |
| Tour Programme Planning feature tests | Testing | Complex | 8 |
| Tour Programme Planning implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **131** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
