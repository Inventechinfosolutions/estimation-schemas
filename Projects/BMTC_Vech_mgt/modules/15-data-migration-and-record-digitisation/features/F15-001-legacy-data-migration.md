# F15-001 — Legacy Data Migration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-001 |
| **Feature Name** | Legacy Data Migration |
| **Module** | 15 — Data Migration and Record Digitisation |

### Description
Service Provider plans cleansing, test loads, validation with BMTC, and cutover from existing IT systems before Go-Live.

### Business Objective
RFP Data Migration section.

### Actors
Applicant: Migration lead configures mappings. BMTC officers validate samples. Checker signs validation. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Migration lead configures mappings. BMTC officers validate samples. Checker signs validation.
2. How they create: Migration → New run: source, entity (vehicle, item, stock, etc.), mapping, Save draft, Test load.
3. How they edit: Draft mapping editable. Posted production load is reversed only with a new run.
4. How they send for approval: Test load then Submit production load for BMTC validation sign-off.
5. How the approver sees pending items: BMTC validator inbox; Checker go-live data sign-off.
6. How the approver decides: Accept sample / full validation or Return.
7. How the applicant sees history: Run log: counts, errors.
8. How the approver sees history: Signed validations.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own migration run history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My migration run register | Medium |
| Migration run form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver migration run inbox | Complex |
| Migration run decision panel (approve / reject / return) | Medium |
| My migration run history | Medium |
| Team migration run history (approver) | Medium |
| Mapping | Very High |
| Validation checklist | Complex |
| Run monitor | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft migration run | Medium |
| Update draft migration run | Medium |
| Submit migration run for approval | Complex |
| Withdraw migration run | Easy |
| Approver inbox query | Medium |
| Approve, reject or return migration run | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Test load | Very High |
| Production load | Very High |
| Record validation sign-off | Medium |

### Inputs
Source, entity, mapping, counts.

### Outputs
Persisted migration run with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own migration run.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Pre-bid: source volume about 9 GB in MySQL. Hosting is bidder-provided (Module 16); this feature is mapping, test/production load and BMTC validation.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Test load required before production.

### Calculations
Read/inserted/error counts.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Migration plan and sign-off.

### Reports
Exception list.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Internal identity (Module 01) and notification service. Document store when attachments are required.

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
| My migration run register | UI | Medium | 6 |
| Migration run form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver migration run inbox | UI | Complex | 12 |
| Migration run decision panel (approve / reject / return) | UI | Medium | 6 |
| My migration run history | UI | Medium | 6 |
| Team migration run history (approver) | UI | Medium | 6 |
| Mapping | UI | Very High | 16 |
| Validation checklist | UI | Complex | 12 |
| Run monitor | UI | Medium | 6 |
| Save draft migration run | API | Medium | 6 |
| Update draft migration run | API | Medium | 6 |
| Submit migration run for approval | API | Complex | 8 |
| Withdraw migration run | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return migration run | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Test load | API | Very High | 16 |
| Production load | API | Very High | 16 |
| Record validation sign-off | API | Medium | 6 |
| Migration run record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on migration run status change | Integration | Simple | 4 |
| Legacy Data Migration feature tests | Testing | Very High | 12 |
| Legacy Data Migration implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **195** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
