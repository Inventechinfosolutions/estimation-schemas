# F08-004 — Audit Report Review and Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-004 |
| **Feature Name** | Audit Report Review and Approval |
| **Module** | 08 — Field Audit Execution & Reporting |

### Description
Reviewing officer and then competent authority see the draft in an inbox, comment, return or approve for issue.

### Business Objective
Maker–checker–authority on the report.

### Actors
Applicant: In-charge who submitted the draft. Approver: Reviewing officer then competent authority as per template (sequential). Other: Auditor.

### User Journey
1. Who creates: In-charge who submitted the draft.
2. How they create: Approvers do not create the report. They open Review inbox.
3. How they edit: Reviewer cannot silently rewrite the report; they Return with comments or Approve. In-charge edits on Return (F08-003).
4. How they send for approval: Already submitted. Each level Approve sends to next level or to issuance-ready.
5. How the approver sees pending items: Each approver level has an inbox of drafts at their step.
6. How the approver decides: Approve, Return, or Reject (rare, with reason). Parallel comments stored on the version.
7. How the applicant sees history: In-charge sees each level's decision.
8. How the approver sees history: Each officer sees items they decided.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own audit report review history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My audit report review register | Medium |
| Audit report review form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver audit report review inbox | Very High |
| Audit report review decision panel (approve / reject / return) | Medium |
| My audit report review history | Medium |
| Team audit report review history (approver) | Medium |
| Review inbox | Very High |
| Comment thread on draft | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft audit report review | Medium |
| Update draft audit report review | Medium |
| Submit audit report review for approval | Complex |
| Withdraw audit report review | Easy |
| Approver inbox query | Medium |
| Approve, reject or return audit report review | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Decision, comments, level.

### Outputs
Persisted audit report review with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own audit report review.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Comments mandatory on Return.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Reviewed draft version.

### Reports
Pendency by review level.

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
| My audit report review register | UI | Medium | 6 |
| Audit report review form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver audit report review inbox | UI | Very High | 16 |
| Audit report review decision panel (approve / reject / return) | UI | Medium | 6 |
| My audit report review history | UI | Medium | 6 |
| Team audit report review history (approver) | UI | Medium | 6 |
| Review inbox | UI | Very High | 16 |
| Comment thread on draft | UI | Medium | 6 |
| Save draft audit report review | API | Medium | 6 |
| Update draft audit report review | API | Medium | 6 |
| Submit audit report review for approval | API | Complex | 8 |
| Withdraw audit report review | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return audit report review | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Audit report review record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on audit report review status change | Integration | Simple | 4 |
| Audit Report Review and Approval feature tests | Testing | Complex | 8 |
| Audit Report Review and Approval implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **145** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
