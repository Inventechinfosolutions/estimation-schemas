# F10-002 — Inspection Report and Receipt Voucher

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-002 |
| **Feature Name** | Inspection Report and Receipt Voucher |
| **Module** | 10 — Stores Receipt and Inspection |

### Description
Inspector accepts or rejects goods (IR). On acceptance, RV is generated, linked to CPO/LPO, and stock updates after section confirmation.

### Business Objective
FR-S-02 to 04.

### Actors
Applicant: Inspector / Stores Officer. Approver: Section confirmation Post for stock update; Stores Officer for IR if inspector is distinct. Other: Purchase (PO link). Auditor.

### User Journey
1. Who creates: Inspector / Stores Officer.
2. How they create: Open submitted gate entry → IR: accept/reject qty, remarks, Save draft.
3. How they edit: Draft/Returned editable. After RV, IR not silently changed.
4. How they send for approval: Submit IR. On accept, system prepares RV linked to PO; section confirms to update Central Stores stock.
5. How the approver sees pending items: Section confirmation inbox; Stores Officer IR inbox.
6. How the approver decides: Accept/reject on IR. Confirm RV posting.
7. How the applicant sees history: IR/RV timeline.
8. How the approver sees history: Posted RVs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own inspection report history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My inspection report register | Medium |
| Inspection report form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver inspection report inbox | Complex |
| Inspection report decision panel (approve / reject / return) | Medium |
| My inspection report history | Medium |
| Team inspection report history (approver) | Medium |
| IR form | Complex |
| RV view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft inspection report | Medium |
| Update draft inspection report | Medium |
| Submit inspection report for approval | Complex |
| Withdraw inspection report | Easy |
| Approver inbox query | Medium |
| Approve, reject or return inspection report | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Generate RV | Complex |
| Update Central Stores stock | Complex |

### Inputs
Accepted/rejected qty, PO, remarks.

### Outputs
Persisted inspection report with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own inspection report.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Accepted + rejected = gate qty.
- Accept requires PO link when PO exists.

### Calculations
Stock += accepted qty on confirmation.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
IR/RV prints.

### Reports
Pending inspections; RV register.

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
| My inspection report register | UI | Medium | 6 |
| Inspection report form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver inspection report inbox | UI | Complex | 12 |
| Inspection report decision panel (approve / reject / return) | UI | Medium | 6 |
| My inspection report history | UI | Medium | 6 |
| Team inspection report history (approver) | UI | Medium | 6 |
| IR form | UI | Complex | 12 |
| RV view | UI | Medium | 6 |
| Save draft inspection report | API | Medium | 6 |
| Update draft inspection report | API | Medium | 6 |
| Submit inspection report for approval | API | Complex | 8 |
| Withdraw inspection report | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return inspection report | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Generate RV | API | Complex | 8 |
| Update Central Stores stock | API | Complex | 8 |
| Inspection report record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on inspection report status change | Integration | Simple | 4 |
| Inspection Report and Receipt Voucher feature tests | Testing | Complex | 8 |
| Inspection Report and Receipt Voucher implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **153** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
