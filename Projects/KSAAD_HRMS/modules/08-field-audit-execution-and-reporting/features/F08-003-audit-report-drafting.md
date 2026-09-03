# F08-003 — Audit Report Drafting

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Audit Report Drafting |
| **Module** | 08 — Field Audit Execution & Reporting |

### Description
In-charge compiles accepted observations into a draft report, edits narrative, submits to review chain.

### Business Objective
One draft report from accepted observations.

### Actors
Applicant: In-charge auditor. Approver: Reviewing officer (F08-004). This feature includes Submit to review. Other: Team (read). Auditor.

### User Journey
1. Who creates: In-charge auditor.
2. How they create: Opens assignment → Generate draft from accepted observations, then edits chapters on the draft form, Save.
3. How they edit: Draft/Returned from review editable. After Submit to review, freeze until Return.
4. How they send for approval: Submit draft to reviewing Post (F08-004 inbox).
5. How the approver sees pending items: Not the final CA inbox; in-charge sees validation errors on generate.
6. How the approver decides: System blocks Submit if no accepted observations when policy requires at least one or if mandatory chapters empty.
7. How the applicant sees history: Draft versions.
8. How the approver sees history: Reviewer sees versions in F08-004.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own audit report draft history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My audit report draft register | Medium |
| Audit report draft form (create and edit) | Very High |
| Submit confirmation | Simple |
| Approver audit report draft inbox | Complex |
| Audit report draft decision panel (approve / reject / return) | Medium |
| My audit report draft history | Medium |
| Team audit report draft history (approver) | Medium |
| Draft report editor | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft audit report draft | Medium |
| Update draft audit report draft | Medium |
| Submit audit report draft for approval | Complex |
| Withdraw audit report draft | Easy |
| Approver inbox query | Medium |
| Approve, reject or return audit report draft | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Generate draft from observations | Very High |

### Inputs
Chapters, included observations, narrative.

### Outputs
Persisted audit report draft with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own audit report draft.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Mandatory chapters present.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Draft stored as versioned document.

### Reports
Assignments without draft.

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
| My audit report draft register | UI | Medium | 6 |
| Audit report draft form (create and edit) | UI | Very High | 16 |
| Submit confirmation | UI | Simple | 2 |
| Approver audit report draft inbox | UI | Complex | 12 |
| Audit report draft decision panel (approve / reject / return) | UI | Medium | 6 |
| My audit report draft history | UI | Medium | 6 |
| Team audit report draft history (approver) | UI | Medium | 6 |
| Draft report editor | UI | Very High | 16 |
| Save draft audit report draft | API | Medium | 6 |
| Update draft audit report draft | API | Medium | 6 |
| Submit audit report draft for approval | API | Complex | 8 |
| Withdraw audit report draft | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return audit report draft | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Generate draft from observations | API | Very High | 16 |
| Audit report draft record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on audit report draft status change | Integration | Simple | 4 |
| Audit Report Drafting feature tests | Testing | Complex | 8 |
| Audit Report Drafting implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **155** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
