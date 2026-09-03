# F08-002 — Observation Recording and Evidence Capture

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Observation Recording and Evidence Capture |
| **Module** | 08 — Field Audit Execution & Reporting |

### Description
Team member records an observation against the assignment, attaches evidence, in-charge reviews before it can go to the report.

### Business Objective
Attributed observations with evidence.

### Actors
Applicant: Allocated team member creates observation. Approver: In-charge auditor (first review). Not the CA report approval (that is F08-004). Other: Supervisor (read). Auditor of system.

### User Journey
1. Who creates: Allocated team member creates observation.
2. How they create: Opens assignment → Observations → New: title, criterion, narrative, amount if any, attach evidence, Save draft.
3. How they edit: Draft/Returned by in-charge editable by author. After in-charge Accept, freeze for report drafting.
4. How they send for approval: Submit to in-charge.
5. How the approver sees pending items: In-charge observation inbox.
6. How the approver decides: Accept, return, or drop (with reason). Dropped observations stay in history but not in draft report by default.
7. How the applicant sees history: Author sees own observations and decisions.
8. How the approver sees history: In-charge sees all observations on the assignment.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own audit observation history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My audit observation register | Medium |
| Audit observation form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver audit observation inbox | Complex |
| Audit observation decision panel (approve / reject / return) | Medium |
| My audit observation history | Medium |
| Team audit observation history (approver) | Medium |
| Evidence attach on observation | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft audit observation | Medium |
| Update draft audit observation | Medium |
| Submit audit observation for approval | Complex |
| Withdraw audit observation | Easy |
| Approver inbox query | Medium |
| Approve, reject or return audit observation | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Title, criterion, narrative, amount, evidence.

### Outputs
Persisted audit observation with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own audit observation.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Narrative mandatory.
- Assignment link mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Evidence via DMS.

### Reports
Observation register by assignment.

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
| My audit observation register | UI | Medium | 6 |
| Audit observation form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver audit observation inbox | UI | Complex | 12 |
| Audit observation decision panel (approve / reject / return) | UI | Medium | 6 |
| My audit observation history | UI | Medium | 6 |
| Team audit observation history (approver) | UI | Medium | 6 |
| Evidence attach on observation | UI | Medium | 6 |
| Save draft audit observation | API | Medium | 6 |
| Update draft audit observation | API | Medium | 6 |
| Submit audit observation for approval | API | Complex | 8 |
| Withdraw audit observation | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return audit observation | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Audit observation record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on audit observation status change | Integration | Simple | 4 |
| Observation Recording and Evidence Capture feature tests | Testing | Complex | 8 |
| Observation Recording and Evidence Capture implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
