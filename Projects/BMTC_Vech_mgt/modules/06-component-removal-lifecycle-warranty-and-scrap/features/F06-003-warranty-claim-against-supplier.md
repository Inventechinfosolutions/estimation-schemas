# F06-003 — Warranty Claim against Supplier

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Warranty Claim against Supplier |
| **Module** | 06 — Component Removal, Lifecycle, Warranty and Scrap |

### Description
When condition is Under Warranty, a claim is opened against the supplier and tracked to closure.

### Business Objective
FR-M-18, FR-X-03.

### Actors
Applicant: Store / Mechanical Clerk. Approver: Stores Officer / COSP Post as configured. Other: Supplier (status only if later portal; not in this estimate). Auditor.

### User Journey
1. Who creates: Store / Mechanical Clerk.
2. How they create: From removal → Raise warranty claim: supplier, item, vehicle, claim reason, Save draft.
3. How they edit: Draft/Returned editable. After submit, status updates are remarks, not silent field edits.
4. How they send for approval: Submit to Stores Officer.
5. How the approver sees pending items: Warranty claim inbox.
6. How the approver decides: Accept claim file, Return, or Record settlement/reject from supplier with remarks.
7. How the applicant sees history: Claim timeline.
8. How the approver sees history: Decided claims.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own warranty claim history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My warranty claim register | Medium |
| Warranty claim form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver warranty claim inbox | Complex |
| Warranty claim decision panel (approve / reject / return) | Medium |
| My warranty claim history | Medium |
| Team warranty claim history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft warranty claim | Medium |
| Update draft warranty claim | Medium |
| Submit warranty claim for approval | Complex |
| Withdraw warranty claim | Easy |
| Approver inbox query | Medium |
| Approve, reject or return warranty claim | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Supplier, item, vehicle, claim status, remarks.

### Outputs
Persisted warranty claim with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own warranty claim.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Item must be warranty-tagged on item master or removal.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Claim papers attachments (embedded).

### Reports
Open warranty claims.

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
| My warranty claim register | UI | Medium | 6 |
| Warranty claim form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver warranty claim inbox | UI | Complex | 12 |
| Warranty claim decision panel (approve / reject / return) | UI | Medium | 6 |
| My warranty claim history | UI | Medium | 6 |
| Team warranty claim history (approver) | UI | Medium | 6 |
| Save draft warranty claim | API | Medium | 6 |
| Update draft warranty claim | API | Medium | 6 |
| Submit warranty claim for approval | API | Complex | 8 |
| Withdraw warranty claim | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return warranty claim | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Warranty claim record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on warranty claim status change | Integration | Simple | 4 |
| Warranty Claim against Supplier feature tests | Testing | Complex | 8 |
| Warranty Claim against Supplier implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
