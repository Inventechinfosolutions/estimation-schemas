# F12-001 — Integration Framework and Authentication Mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-001 |
| **Feature Name** | Integration Framework and Authentication Mapping |
| **Module** | 12 — API Integration Hub |

### Description
Integration Administrator registers a trusted client, maps credentials to a technical Post, checker approves before go-live.

### Business Objective
No anonymous integrations.

### Actors
Applicant: Integration Administrator creates. Integration Checker approves. Runtime calls use the mapped technical identity. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Integration Administrator creates. Integration Checker approves. Runtime calls use the mapped technical identity.
2. How they create: Opens Integration clients → New: name, auth type, scopes, maps to a technical Post, Save draft.
3. How they edit: Draft editable. After approve, secret rotation is a checked event.
4. How they send for approval: Submit client for checker.
5. How the approver sees pending items: Checker integration-client inbox.
6. How the approver decides: Approve (activate) or reject. Disable is a separate checked action.
7. How the applicant sees history: Client versions and rotations.
8. How the approver sees history: Approvals and disables.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own integration client registration history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My integration client registration register | Medium |
| Integration client registration form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver integration client registration inbox | Complex |
| Integration client registration decision panel (approve / reject / return) | Medium |
| My integration client registration history | Medium |
| Team integration client registration history (approver) | Medium |
| Client form | Complex |
| Secret rotation dialog | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft integration client registration | Medium |
| Update draft integration client registration | Medium |
| Submit integration client registration for approval | Complex |
| Withdraw integration client registration | Easy |
| Approver inbox query | Medium |
| Approve, reject or return integration client registration | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Register client | Very High |
| Rotate credential | Complex |

### Inputs
Name, auth type, scopes, technical Post.

### Outputs
Persisted integration client registration with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own integration client registration.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Technical Post mandatory.
- Scope not empty.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Interface note.

### Reports
Active clients.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Trusted client authentication channel

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

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
| My integration client registration register | UI | Medium | 6 |
| Integration client registration form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver integration client registration inbox | UI | Complex | 12 |
| Integration client registration decision panel (approve / reject / return) | UI | Medium | 6 |
| My integration client registration history | UI | Medium | 6 |
| Team integration client registration history (approver) | UI | Medium | 6 |
| Client form | UI | Complex | 12 |
| Secret rotation dialog | UI | Easy | 4 |
| Save draft integration client registration | API | Medium | 6 |
| Update draft integration client registration | API | Medium | 6 |
| Submit integration client registration for approval | API | Complex | 8 |
| Withdraw integration client registration | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return integration client registration | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Register client | API | Very High | 16 |
| Rotate credential | API | Complex | 8 |
| Integration client registration record, status history and attachments metadata | DB | Medium | 4 |
| Trusted client authentication channel | Integration | Medium | 16 |
| Integration Framework and Authentication Mapping feature tests | Testing | Very High | 12 |
| Integration Framework and Authentication Mapping implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **175** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
