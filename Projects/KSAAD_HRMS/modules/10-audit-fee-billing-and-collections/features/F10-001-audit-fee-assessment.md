# F10-001 — Audit Fee Assessment

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-001 |
| **Feature Name** | Audit Fee Assessment |
| **Module** | 10 — Audit Fee, Billing and Collections |

### Description
Officer computes/records fee from rules and institution FY data; checker approves assessment before billing.

### Business Objective
Auditable fee before invoice.

### Actors
Applicant: Fee/accounts officer. Approver: Accounts checker / competent Post. Other: Institution (sees after approve, F16-005). Auditor.

### User Journey
1. Who creates: Fee/accounts officer.
2. How they create: Opens institution/year → Assess fee, system proposes amount from catalogue rules, officer adjusts with reason if allowed, Save draft.
3. How they edit: Draft/Returned editable. After approve, revision is a new assessment version.
4. How they send for approval: Submit assessment.
5. How the approver sees pending items: Checker assessment inbox.
6. How the approver decides: Approve or return.
7. How the applicant sees history: Assessment versions.
8. How the approver sees history: Approved assessments.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own fee assessment history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My fee assessment register | Medium |
| Fee assessment form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver fee assessment inbox | Complex |
| Fee assessment decision panel (approve / reject / return) | Medium |
| My fee assessment history | Medium |
| Team fee assessment history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft fee assessment | Medium |
| Update draft fee assessment | Medium |
| Submit fee assessment for approval | Complex |
| Withdraw fee assessment | Easy |
| Approver inbox query | Medium |
| Approve, reject or return fee assessment | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Propose fee from rules | Very High |

### Inputs
Institution, year, fee head, amount, rule reference, exception reason.

### Outputs
Persisted fee assessment with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own fee assessment.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Amount ≥ 0.
- Institution and year mandatory.

### Calculations
Proposed fee from configured rule on FY data; exception amount requires reason.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Assessment note.

### Reports
Assessed vs billed.

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
| My fee assessment register | UI | Medium | 6 |
| Fee assessment form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver fee assessment inbox | UI | Complex | 12 |
| Fee assessment decision panel (approve / reject / return) | UI | Medium | 6 |
| My fee assessment history | UI | Medium | 6 |
| Team fee assessment history (approver) | UI | Medium | 6 |
| Save draft fee assessment | API | Medium | 6 |
| Update draft fee assessment | API | Medium | 6 |
| Submit fee assessment for approval | API | Complex | 8 |
| Withdraw fee assessment | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return fee assessment | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Propose fee from rules | API | Very High | 16 |
| Fee assessment record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on fee assessment status change | Integration | Simple | 4 |
| Audit Fee Assessment feature tests | Testing | Complex | 8 |
| Audit Fee Assessment implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **135** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
