# F01-006 — Institution and External Identity with Scoped Access

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-006 |
| **Feature Name** | Institution and External Identity with Scoped Access |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Institution Administrator requests access for an auditee-institution user. Access is scoped to that institution, not to staff Posts.

### Business Objective
Give auditee institutions a constrained login without mixing them into staff Person–Post mappings.

### Actors
Applicant: Institution Administrator (once the institution is onboarded) or KSAAD Access Administrator for the first institution admin. Approver: KSAAD Access Checker / designated institutional-access Post. Other: Institution user (uses the login after activation). Auditor.

### User Journey
1. Who creates: Institution Administrator (once the institution is onboarded) or KSAAD Access Administrator for the first institution admin.
2. How they create: KSAAD Administrator (first admin) or Institution Administrator opens Institution users → New user, enters name, official email, institution, and requested functions (submit AFS, reply to para, view report/fee).
3. How they edit: Draft registrations can be edited. After approval, profile updates (email) go through the same checker. Institution users cannot be mapped to staff Posts.
4. How they send for approval: Submit sends the registration to the KSAAD Access Checker.
5. How the approver sees pending items: Checker opens Institution-user inbox filtered by institution.
6. How the approver decides: Checker approves (activation credentials issued) or rejects with remarks.
7. How the applicant sees history: Institution Administrator sees users of their institution and status history.
8. How the approver sees history: KSAAD Checker/auditor sees all institution-user decisions and cannot see staff Person internals from this screen.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own institution user registration history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My institution user registration register | Medium |
| Institution user registration form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver institution user registration inbox | Complex |
| Institution user registration decision panel (approve / reject / return) | Medium |
| My institution user registration history | Medium |
| Team institution user registration history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft institution user registration | Medium |
| Update draft institution user registration | Medium |
| Submit institution user registration for approval | Complex |
| Withdraw institution user registration | Easy |
| Approver inbox query | Medium |
| Approve, reject or return institution user registration | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Name, email, mobile, institution, requested functions, status.

### Outputs
Persisted institution user registration with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own institution user registration.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Institution users never inherit staff Post Roles.
- Data scope is the linked auditee institution only.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Institution mandatory.
- Email unique within institution users.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional authorisation letter.

### Reports
Active institution users by institution.

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
| My institution user registration register | UI | Medium | 6 |
| Institution user registration form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver institution user registration inbox | UI | Complex | 12 |
| Institution user registration decision panel (approve / reject / return) | UI | Medium | 6 |
| My institution user registration history | UI | Medium | 6 |
| Team institution user registration history (approver) | UI | Medium | 6 |
| Save draft institution user registration | API | Medium | 6 |
| Update draft institution user registration | API | Medium | 6 |
| Submit institution user registration for approval | API | Complex | 8 |
| Withdraw institution user registration | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return institution user registration | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Institution user registration record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on institution user registration status change | Integration | Simple | 4 |
| Institution and External Identity with Scoped Access feature tests | Testing | Complex | 8 |
| Institution and External Identity with Scoped Access implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
