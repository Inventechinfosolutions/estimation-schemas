# F16-002 — AFS and Supporting Document Upload

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-002 |
| **Feature Name** | AFS and Supporting Document Upload |
| **Module** | 16 — External / Institution Interaction |

### Description
Institution user uploads Annual Financial Statement and supporting files, submits to KSAAD; audit officer acknowledges or returns.

### Business Objective
Institution-originated FY pack.

### Actors
Applicant: Institution user with Submit AFS function. Approver: KSAAD audit officer for that jurisdiction (acknowledge/return, not 'approve accounts'). Other: Institution Administrator. Auditor.

### User Journey
1. Who creates: Institution user with Submit AFS function.
2. How they create: Portal → AFS → New year, upload AFS and supporting docs, Save draft.
3. How they edit: Draft/Returned editable. After Submit freeze until Return.
4. How they send for approval: Submit to KSAAD. Appears in staff AFS inbox.
5. How the approver sees pending items: KSAAD officer AFS inbox by institution/year. Institution sees status on portal.
6. How the approver decides: Acknowledge receipt, Return for correction, or Record not acceptable with reason.
7. How the applicant sees history: Institution sees submissions and returns.
8. How the approver sees history: Officer sees acknowledged packs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own AFS submission history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My AFS submission register | Medium |
| Afs submission form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver AFS submission inbox | Complex |
| Afs submission decision panel (approve / reject / return) | Medium |
| My AFS submission history | Medium |
| Team AFS submission history (approver) | Medium |
| AFS upload form | Complex |
| Staff AFS inbox | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft AFS submission | Medium |
| Update draft AFS submission | Medium |
| Submit AFS submission for approval | Complex |
| Withdraw AFS submission | Easy |
| Approver inbox query | Medium |
| Approve, reject or return AFS submission | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Year, files, remarks.

### Outputs
Persisted AFS submission with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own AFS submission.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Year mandatory.
- AFS file mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
AFS and supporting via DMS.

### Reports
Institutions missing AFS for a year.

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
| My AFS submission register | UI | Medium | 6 |
| Afs submission form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver AFS submission inbox | UI | Complex | 12 |
| Afs submission decision panel (approve / reject / return) | UI | Medium | 6 |
| My AFS submission history | UI | Medium | 6 |
| Team AFS submission history (approver) | UI | Medium | 6 |
| AFS upload form | UI | Complex | 12 |
| Staff AFS inbox | UI | Medium | 6 |
| Save draft AFS submission | API | Medium | 6 |
| Update draft AFS submission | API | Medium | 6 |
| Submit AFS submission for approval | API | Complex | 8 |
| Withdraw AFS submission | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return AFS submission | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Afs submission record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on AFS submission status change | Integration | Simple | 4 |
| AFS and Supporting Document Upload feature tests | Testing | Complex | 8 |
| AFS and Supporting Document Upload implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
