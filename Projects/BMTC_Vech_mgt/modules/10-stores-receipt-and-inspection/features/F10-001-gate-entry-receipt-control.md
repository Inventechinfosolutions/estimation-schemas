# F10-001 — Gate Entry (Receipt Control)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-001 |
| **Feature Name** | Gate Entry (Receipt Control) |
| **Module** | 10 — Stores Receipt and Inspection |

### Description
Central Stores clerk records every incoming consignment: vendor, item, quantity, date.

### Business Objective
FR-S-01.

### Actors
Applicant: Central Stores Receipt Clerk. Approver: Stores Officer (completeness check) if configured; else F10-002 owns quality decision. Other: Security/gate. Auditor.

### User Journey
1. Who creates: Central Stores Receipt Clerk.
2. How they create: Receipts → Gate entry → New: vendor, PO reference if known, item, qty, date, Save draft.
3. How they edit: Draft/Returned editable. After IR started, header frozen.
4. How they send for approval: Submit for IR (F10-002). Optional checker confirm of gate qty.
5. How the approver sees pending items: Inspection inbox receives submitted gate entries.
6. How the approver decides: This feature records arrival. Quality accept/reject is F10-002.
7. How the applicant sees history: Gate entry history.
8. How the approver sees history: Submitted arrivals.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own gate entry history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My gate entry register | Medium |
| Gate entry form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver gate entry inbox | Complex |
| Gate entry decision panel (approve / reject / return) | Medium |
| My gate entry history | Medium |
| Team gate entry history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft gate entry | Medium |
| Update draft gate entry | Medium |
| Submit gate entry for approval | Complex |
| Withdraw gate entry | Easy |
| Approver inbox query | Medium |
| Approve, reject or return gate entry | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Vendor, item, qty, date, PO ref.

### Outputs
Persisted gate entry with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own gate entry.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Qty > 0.
- Vendor and item mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Delivery challan attachment.

### Reports
Inbound consignments.

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
| My gate entry register | UI | Medium | 6 |
| Gate entry form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver gate entry inbox | UI | Complex | 12 |
| Gate entry decision panel (approve / reject / return) | UI | Medium | 6 |
| My gate entry history | UI | Medium | 6 |
| Team gate entry history (approver) | UI | Medium | 6 |
| Save draft gate entry | API | Medium | 6 |
| Update draft gate entry | API | Medium | 6 |
| Submit gate entry for approval | API | Complex | 8 |
| Withdraw gate entry | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return gate entry | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Gate entry record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on gate entry status change | Integration | Simple | 4 |
| Gate Entry (Receipt Control) feature tests | Testing | Complex | 8 |
| Gate Entry (Receipt Control) implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
