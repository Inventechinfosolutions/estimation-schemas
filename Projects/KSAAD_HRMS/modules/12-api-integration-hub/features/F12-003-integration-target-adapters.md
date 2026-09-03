# F12-003 — Integration Target Adapters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-003 |
| **Feature Name** | Integration Target Adapters |
| **Module** | 12 — API Integration Hub |

### Description
Administrator enables a target adapter (HRMS/audit/external) with endpoint mapping; checker approves; tests recorded in history.

### Business Objective
Controlled adapters, not one-off scripts.

### Actors
Applicant: Integration Administrator. Checker. Operator runs connectivity test. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Integration Administrator. Checker. Operator runs connectivity test.
2. How they create: Opens Adapters → select target type → fill connection parameters, Save draft.
3. How they edit: Draft editable. Live adapter change is a new version.
4. How they send for approval: Submit version. Test connection before/after approve.
5. How the approver sees pending items: Checker adapter inbox.
6. How the approver decides: Approve or reject. Disable adapter is checked.
7. How the applicant sees history: Adapter versions and test results.
8. How the approver sees history: Approvals.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own adapter configuration history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My adapter configuration register | Medium |
| Adapter configuration form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver adapter configuration inbox | Complex |
| Adapter configuration decision panel (approve / reject / return) | Medium |
| My adapter configuration history | Medium |
| Team adapter configuration history (approver) | Medium |
| Adapter form | Complex |
| Connectivity test result | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft adapter configuration | Medium |
| Update draft adapter configuration | Medium |
| Submit adapter configuration for approval | Complex |
| Withdraw adapter configuration | Easy |
| Approver inbox query | Medium |
| Approve, reject or return adapter configuration | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Test connectivity | Medium |
| Activate adapter version | Complex |

### Inputs
Target type, connection parameters, version.

### Outputs
Persisted adapter configuration with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own adapter configuration.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Required parameters by target type.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Target ICD.

### Reports
Adapters by status.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Target adapter connectivity

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
| My adapter configuration register | UI | Medium | 6 |
| Adapter configuration form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver adapter configuration inbox | UI | Complex | 12 |
| Adapter configuration decision panel (approve / reject / return) | UI | Medium | 6 |
| My adapter configuration history | UI | Medium | 6 |
| Team adapter configuration history (approver) | UI | Medium | 6 |
| Adapter form | UI | Complex | 12 |
| Connectivity test result | UI | Easy | 4 |
| Save draft adapter configuration | API | Medium | 6 |
| Update draft adapter configuration | API | Medium | 6 |
| Submit adapter configuration for approval | API | Complex | 8 |
| Withdraw adapter configuration | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return adapter configuration | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Test connectivity | API | Medium | 6 |
| Activate adapter version | API | Complex | 8 |
| Adapter configuration record, status history and attachments metadata | DB | Medium | 4 |
| Target adapter connectivity | Integration | Easy | 8 |
| Integration Target Adapters feature tests | Testing | Complex | 8 |
| Integration Target Adapters implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **153** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
