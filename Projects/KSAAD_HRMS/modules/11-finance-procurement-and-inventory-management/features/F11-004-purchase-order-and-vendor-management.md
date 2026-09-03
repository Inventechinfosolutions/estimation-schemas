# F11-004 — Purchase Order and Vendor Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-004 |
| **Feature Name** | Purchase Order and Vendor Management |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Purchase officer maintains vendor (checked) and raises PO against approved indent; competent Post approves PO.

### Business Objective
PO and vendor control.

### Actors
Applicant: Purchase officer. Vendor master create is included as a checked sub-flow. Approver: Purchase checker / competent Post. Other: Vendor (no login unless later ordered). Auditor.

### User Journey
1. Who creates: Purchase officer. Vendor master create is included as a checked sub-flow.
2. How they create: Vendor: Vendors → New (name, PAN/GST, bank), submit to checker. PO: select approved indent + vendor, lines, rates, Save draft.
3. How they edit: Draft PO editable. Approved PO amendment is a new version.
4. How they send for approval: Submit vendor or PO.
5. How the approver sees pending items: Checker vendor inbox and PO inbox.
6. How the approver decides: Approve/reject vendor or PO.
7. How the applicant sees history: Vendor changes and PO versions.
8. How the approver sees history: Approved POs/vendors.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own purchase order history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My purchase order register | Medium |
| Purchase order form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver purchase order inbox | Complex |
| Purchase order decision panel (approve / reject / return) | Medium |
| My purchase order history | Medium |
| Team purchase order history (approver) | Medium |
| Vendor form | Complex |
| PO form | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft purchase order | Medium |
| Update draft purchase order | Medium |
| Submit purchase order for approval | Complex |
| Withdraw purchase order | Easy |
| Approver inbox query | Medium |
| Approve, reject or return purchase order | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Remaining indent qty | Medium |

### Inputs
Vendor fields; PO: indent, vendor, lines, rates, delivery date.

### Outputs
Persisted purchase order with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own purchase order.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Vendor unique PAN if provided.
- PO qty cannot exceed remaining indent qty.

### Calculations
PO line value = qty × rate. Remaining indent qty = approved indent − ordered.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Quotations optional.

### Reports
PO register.

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
| My purchase order register | UI | Medium | 6 |
| Purchase order form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver purchase order inbox | UI | Complex | 12 |
| Purchase order decision panel (approve / reject / return) | UI | Medium | 6 |
| My purchase order history | UI | Medium | 6 |
| Team purchase order history (approver) | UI | Medium | 6 |
| Vendor form | UI | Complex | 12 |
| PO form | UI | Complex | 12 |
| Save draft purchase order | API | Medium | 6 |
| Update draft purchase order | API | Medium | 6 |
| Submit purchase order for approval | API | Complex | 8 |
| Withdraw purchase order | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return purchase order | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Remaining indent qty | API | Medium | 6 |
| Purchase order record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on purchase order status change | Integration | Simple | 4 |
| Purchase Order and Vendor Management feature tests | Testing | Complex | 8 |
| Purchase Order and Vendor Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **149** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
