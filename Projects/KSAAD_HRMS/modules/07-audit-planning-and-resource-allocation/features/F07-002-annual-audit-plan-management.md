# F07-002 — Annual Audit Plan Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Annual Audit Plan Management |
| **Module** | 07 — Audit Planning & Resource Allocation |

### Description
Planning officer builds the annual plan (institutions, slots), submits to competent Post; versions are kept.

### Business Objective
Approved plan before allocation and field work.

### Actors
Applicant: Audit Planning Officer. Approver: Competent planning authority (JD/Director class Post as configured). Other: ROs/LACs (read of their slice). Auditor.

### User Journey
1. Who creates: Audit Planning Officer.
2. How they create: Opens Annual plans → New year, adds rows (institution, proposed quarter, team size), Save draft.
3. How they edit: Draft/Returned editable. After approve, amendments are a new version submitted again.
4. How they send for approval: Submit plan version.
5. How the approver sees pending items: Approver plan inbox.
6. How the approver decides: Approve, reject or return. Approve freezes that version for allocation (F07-003).
7. How the applicant sees history: Plan versions and decisions.
8. How the approver sees history: Approved plans.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own annual audit plan history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My annual audit plan register | Medium |
| Annual audit plan form (create and edit) | Very High |
| Submit confirmation | Simple |
| Approver annual audit plan inbox | Very High |
| Annual audit plan decision panel (approve / reject / return) | Medium |
| My annual audit plan history | Medium |
| Team annual audit plan history (approver) | Medium |
| Plan grid | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft annual audit plan | Medium |
| Update draft annual audit plan | Medium |
| Submit annual audit plan for approval | Complex |
| Withdraw annual audit plan | Easy |
| Approver inbox query | Medium |
| Approve, reject or return annual audit plan | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Year, institution rows, quarter, remarks.

### Outputs
Persisted annual audit plan with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own annual audit plan.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Year unique unless versioned.
- Each row has an institution.

### Calculations
Counts of institutions by quarter.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Plan approval note.

### Reports
Plan vs not-yet-allocated.

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
| My annual audit plan register | UI | Medium | 6 |
| Annual audit plan form (create and edit) | UI | Very High | 16 |
| Submit confirmation | UI | Simple | 2 |
| Approver annual audit plan inbox | UI | Very High | 16 |
| Annual audit plan decision panel (approve / reject / return) | UI | Medium | 6 |
| My annual audit plan history | UI | Medium | 6 |
| Team annual audit plan history (approver) | UI | Medium | 6 |
| Plan grid | UI | Very High | 16 |
| Save draft annual audit plan | API | Medium | 6 |
| Update draft annual audit plan | API | Medium | 6 |
| Submit annual audit plan for approval | API | Complex | 8 |
| Withdraw annual audit plan | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return annual audit plan | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Annual audit plan record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on annual audit plan status change | Integration | Simple | 4 |
| Annual Audit Plan Management feature tests | Testing | Complex | 8 |
| Annual Audit Plan Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **143** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
