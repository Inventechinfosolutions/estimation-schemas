# F05-001 — Digital Job Card Creation and Work Capture

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Digital Job Card Creation and Work Capture |
| **Module** | 05 — Digital Job Card and Fitment |

### Description
Mechanical Clerk or Tech. Supervisor opens a Digital Job Card for Routine, Preventive, Breakdown, Accident, Reconditioning, Body Repair or FC, capturing RFP mandatory fields including driver-reported vs mechanic-confirmed defect.

### Business Objective
Eliminate paper job cards (FR-M-05 to 08, 13).

### Actors
Applicant: Mechanical Clerk or Tech. Supervisor mapped to the Depot/CWS Post. Approver: Tech. Supervisor (if clerk creates) or Depot Manager / Workshop in-charge for release. Other: Mechanic (named on the card). Store Clerk sees linked issues. Auditor.

### User Journey
1. Who creates: Mechanical Clerk or Tech. Supervisor mapped to the Depot/CWS Post.
2. How they create: Job Cards → New: type, depot/workshop, vehicle (make/model auto), KM at intake, mechanic, section, defects, work description, Save draft. Status Open.
3. How they edit: Open/In Progress/Pending Spares editable for work and spares lines. Completed cards are not edited.
4. How they send for approval: Submit for supervisor digital sign-off when work is ready. Status moves In Progress / Pending Spares from stores linkage.
5. How the approver sees pending items: Supervisor job-card inbox: Open/In Progress/Pending Spares for their unit.
6. How the approver decides: Supervisor does not close here if F05-003 owns closure; they confirm work details or return. Closure is F05-003.
7. How the applicant sees history: My job cards and vehicle history.
8. How the approver sees history: Team job cards.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own job card history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My job card register | Medium |
| Job card form (create and edit) | Very High |
| Submit confirmation | Simple |
| Approver job card inbox | Complex |
| Job card decision panel (approve / reject / return) | Medium |
| My job card history | Medium |
| Team job card history (approver) | Medium |
| Job card workbench (tabs) | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft job card | Medium |
| Update draft job card | Medium |
| Submit job card for approval | Complex |
| Withdraw job card | Easy |
| Approver inbox query | Medium |
| Approve, reject or return job card | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Auto-update job card status | Complex |

### Inputs
All Digital Job Card header, vehicle, mechanic, work, spares, labour fields per RFP table.

### Outputs
Persisted job card with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own job card.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Vehicle and type mandatory.
- Driver defect and mechanic defect captured separately when type is breakdown/accident.

### Calculations
None on create (labour hours on F05-003).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional photos of defect.

### Reports
Job Cards Register.

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
| My job card register | UI | Medium | 6 |
| Job card form (create and edit) | UI | Very High | 16 |
| Submit confirmation | UI | Simple | 2 |
| Approver job card inbox | UI | Complex | 12 |
| Job card decision panel (approve / reject / return) | UI | Medium | 6 |
| My job card history | UI | Medium | 6 |
| Team job card history (approver) | UI | Medium | 6 |
| Job card workbench (tabs) | UI | Very High | 16 |
| Save draft job card | API | Medium | 6 |
| Update draft job card | API | Medium | 6 |
| Submit job card for approval | API | Complex | 8 |
| Withdraw job card | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return job card | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Auto-update job card status | API | Complex | 8 |
| Job card record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on job card status change | Integration | Simple | 4 |
| Digital Job Card Creation and Work Capture feature tests | Testing | Very High | 12 |
| Digital Job Card Creation and Work Capture implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
