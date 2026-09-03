# F01-007 — Joiner-Mover-Leaver and Post Reassignment Governance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-007 |
| **Feature Name** | Joiner-Mover-Leaver and Post Reassignment Governance |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Administrator processes joiner (new mapping), mover (end one Post, start another) and leaver (deactivate Person / end mappings) with history retained.

### Business Objective
Prevent orphaned access when people join, move office or leave.

### Actors
Applicant: Access Administrator or HR Establishment Officer raising the JML request against a Person. Approver: Access Checker. Other: The Person concerned (notified). Auditor.

### User Journey
1. Who creates: Access Administrator or HR Establishment Officer raising the JML request against a Person.
2. How they create: Administrator opens JML → New request, selects Person, event type (Joiner / Mover / Leaver), target Post(s), effective date, reason.
3. How they edit: Draft/Returned requests can be edited. After Submit, only Withdraw (before decision) is allowed.
4. How they send for approval: Submit sends to Access Checker. On approval, mappings are ended/created and leaver Person is set Inactive.
5. How the approver sees pending items: Checker opens JML inbox by event type and office.
6. How the approver decides: Checker confirms the Person, Posts and effective date, Approves or Rejects with remarks.
7. How the applicant sees history: Administrator opens the Person's JML history (all join/move/leave events).
8. How the approver sees history: Checker/auditor open the same history including who approved.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own joiner–mover–leaver request history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My joiner–mover–leaver request register | Medium |
| Joiner–mover–leaver request form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver joiner–mover–leaver request inbox | Complex |
| Joiner–mover–leaver request decision panel (approve / reject / return) | Medium |
| My joiner–mover–leaver request history | Medium |
| Team joiner–mover–leaver request history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft joiner–mover–leaver request | Medium |
| Update draft joiner–mover–leaver request | Medium |
| Submit joiner–mover–leaver request for approval | Complex |
| Withdraw joiner–mover–leaver request | Easy |
| Approver inbox query | Medium |
| Approve, reject or return joiner–mover–leaver request | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Apply mapping end/start on approval | Complex |

### Inputs
Person, event type, from Post, to Post, effective date, reason, remarks.

### Outputs
Persisted joiner–mover–leaver request with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own joiner–mover–leaver request.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Leaver ends all current mappings and sets Person Inactive; historical actions remain attributable.
- Mover sets effective-to on the old mapping and creates a new mapping; credentials are not copied between Persons.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Effective date mandatory.
- Mover requires from and to Post.
- Leaver requires reason.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Joining/relieving order attachment.

### Reports
Joiners, movers, leavers in a period.

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
| My joiner–mover–leaver request register | UI | Medium | 6 |
| Joiner–mover–leaver request form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver joiner–mover–leaver request inbox | UI | Complex | 12 |
| Joiner–mover–leaver request decision panel (approve / reject / return) | UI | Medium | 6 |
| My joiner–mover–leaver request history | UI | Medium | 6 |
| Team joiner–mover–leaver request history (approver) | UI | Medium | 6 |
| Save draft joiner–mover–leaver request | API | Medium | 6 |
| Update draft joiner–mover–leaver request | API | Medium | 6 |
| Submit joiner–mover–leaver request for approval | API | Complex | 8 |
| Withdraw joiner–mover–leaver request | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return joiner–mover–leaver request | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Apply mapping end/start on approval | API | Complex | 8 |
| Joiner–mover–leaver request record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on joiner–mover–leaver request status change | Integration | Simple | 4 |
| Joiner-Mover-Leaver and Post Reassignment Governance feature tests | Testing | Complex | 8 |
| Joiner-Mover-Leaver and Post Reassignment Governance implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **127** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
