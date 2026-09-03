# F05-002 — TA/DA Claim Capture

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | TA/DA Claim Capture |
| **Module** | 05 — HRMS Tour, Travel & TA/DA Claims |

### Description
After an approved tour (or admissible journey), the Person captures fare, DA and other heads on a claim linked to the tour.

### Business Objective
Structured claim capture before evidence and approval.

### Actors
Applicant: The travelling Person (or HR on behalf with reason). Approver: Not in this feature — capture/save only; submit is after evidence (F05-003) and decision in F05-004. A completeness checker may Return the capture. Other: Auditor.

### User Journey
1. Who creates: The travelling Person (or HR on behalf with reason).
2. How they create: Applicant opens My TA/DA → New, selects approved tour, adds lines (head, amount, date), Save draft. Totals calculate.
3. How they edit: Draft/Returned lines can be added/edited/deleted. After Submit (F05-003) freeze.
4. How they send for approval: Save is not approval. Applicant proceeds to evidence (F05-003) then Submit.
5. How the approver sees pending items: No approver inbox here. Incomplete drafts stay with the applicant.
6. How the approver decides: Not applicable until F05-004.
7. How the applicant sees history: Draft and submitted claims list with totals.
8. How the approver sees history: N/A until F05-004; supervisor will see submitted claims there.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own TA/DA claim history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My TA/DA claim register | Medium |
| Ta/da claim form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver TA/DA claim inbox | Complex |
| Ta/da claim decision panel (approve / reject / return) | Medium |
| My TA/DA claim history | Medium |
| Team TA/DA claim history (approver) | Medium |
| Claim line grid | Complex |
| Claim total panel | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft TA/DA claim | Medium |
| Update draft TA/DA claim | Medium |
| Submit TA/DA claim for approval | Complex |
| Withdraw TA/DA claim | Easy |
| Approver inbox query | Medium |
| Approve, reject or return TA/DA claim | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Recalculate claim total | Medium |

### Inputs
Tour, claim lines (head, amount, date), advance if any.

### Outputs
Persisted TA/DA claim with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own TA/DA claim.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Tour must be approved.
- Each line amount > 0.

### Calculations
Total = sum(lines) − advances. DA days may use tour days × rate from catalogue.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None in this feature (evidence is F05-003).

### Reports
Draft claims ageing.

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
| My TA/DA claim register | UI | Medium | 6 |
| Ta/da claim form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver TA/DA claim inbox | UI | Complex | 12 |
| Ta/da claim decision panel (approve / reject / return) | UI | Medium | 6 |
| My TA/DA claim history | UI | Medium | 6 |
| Team TA/DA claim history (approver) | UI | Medium | 6 |
| Claim line grid | UI | Complex | 12 |
| Claim total panel | UI | Easy | 4 |
| Save draft TA/DA claim | API | Medium | 6 |
| Update draft TA/DA claim | API | Medium | 6 |
| Submit TA/DA claim for approval | API | Complex | 8 |
| Withdraw TA/DA claim | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return TA/DA claim | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Recalculate claim total | API | Medium | 6 |
| Ta/da claim record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on TA/DA claim status change | Integration | Simple | 4 |
| TA/DA Claim Capture feature tests | Testing | Complex | 8 |
| TA/DA Claim Capture implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **141** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
