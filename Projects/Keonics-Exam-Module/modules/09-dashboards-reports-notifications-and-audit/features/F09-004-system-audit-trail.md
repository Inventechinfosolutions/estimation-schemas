# F09-004 — System Audit Trail

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | System Audit Trail |
| **Module** | 09 — Dashboards, Reports, Notifications and Audit |

### Description
Maintain a first-class, searchable audit trail of critical registration, data change, KGID verification, document upload, fees, allocation, scheduling, questions, paper generation, exam login/start/submit, results, certificates, cancellations and administrative actions — each with user, date/time and activity — including detail views and export for statutory review.

### Business Objective
Ensure critical actions listed in the SOW are attributable and retained for operational investigation and statutory audit.

### Actors
- System (records audit events from Modules 01–08)
- Examination Administrator (searches and exports)
- Auditor / oversight role (read-only full trail)
- Ordinary candidates do not browse the system audit UI

### User Journey
1. Who creates: The system creates audit records when critical actions occur across the examination lifecycle; administrators do not manually forge audit rows. Optional “reason” fields on administrative actions are captured from the acting user.
2. How they create: Source modules emit audit events → append to audit store → administrators open audit search → filter by activity type/actor/date/entity → open detail → optionally export an audit pack.
3. How they edit: Audit trail is append-only; no silent edits or deletes of historical rows. Corrections appear as new compensating actions in source modules, which generate new audit events.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No approver inbox. Critical activity filter board highlights recent high-risk action types for monitoring.
6. How the approver decides: No decision on audit rows.
7. How the applicant / maker sees history: Actors see business history in owning features; the system audit UI is for administrators/auditors. Candidate-facing history remains in portal status views.
8. How the approver / auditor sees history: Full search, detail and export with user, date/time, activity, and entity references for the SOW-listed critical actions.

### Functional Capabilities
- Record audit events for: registration, data change, KGID verification, document upload, fees, allocation, scheduling, questions, paper generation, exam login/start/submit, results, certificates, cancellations, administrative actions
- Capture user (or system), date/time and activity on each event
- Audit trail search with rich filters
- Audit event detail view
- Critical activity filter board
- Actor activity history
- Audit pack export
- Append-only retention aligned to Department policy
- Tamper-evident posture (integrity checks / controlled storage assumptions)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Audit trail search | Complex |
| Audit event detail | Medium |
| Critical activity filter board | Medium |
| Actor activity history | Easy |
| Audit export view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Record audit event | Complex |
| Search audit by entity actor and date | Complex |
| Load audit event detail | Easy |
| Filter critical activity types | Medium |
| Load actor activity history | Medium |
| Export audit pack | Complex |
| Verify audit integrity marker | Complex |
| List auditable activity catalogue | Simple |

### Inputs
Activity type, actor identity, timestamp, entity references (registration, examination, certificate, etc.), before/after summary where approved, export criteria.

### Outputs
Append-only audit store, search results, detail records, exported audit packs.

### Business Rules
- Critical actions listed in the source appear with actor and timestamp (acceptance).
- Candidates cannot modify audit records.
- Centre-scoped staff do not receive cross-centre audit export by default.
- Sensitive values (passwords, OTP, full payment tokens) are masked or omitted per security policy.
- Module 07 activity recording (F07-006) remains the deep exam-day trail; this feature ensures cross-module critical actions are in the enterprise audit.

### Validations
- Activity type from catalogue
- Actor and timestamp mandatory
- Export role authorisation

### Calculations
None.

### Workflow
Source action → append audit → search/detail/export. No approval.

### Search Requirements
By user/actor, date/time range, activity type, registration number, examination, centre, certificate number, administrative action class.

### Documents
Exported audit pack in approved format.

### Reports
Audit extracts support statutory needs; operational MIS remains F09-002.

### Notifications
Optional alert on integrity failure or mass administrative changes via F09-003 if configured.

### Security
Read restricted to Administrator/Auditor roles; export audited; append-only writes from trusted application path.

### Integrations
None.

### Dependencies
All modules as event sources; complements F07-006 for exam-day depth.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Exact field-level before/after payloads are summarised for high-volume events to control storage.
- Hosting retention and WORM storage are infrastructure decisions outside pure application hours except integrity marker support.

### Risks
Incomplete instrumentation if a module omits emit calls — mitigate with activity catalogue checklist in testing.
High volume from question edits — aggregate where approved without losing actor/time.

### Non Functional Requirements
Recording path non-blocking for user actions; search performance on multi-month ranges with indexes; retention per Department policy.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Audit trail search | UI | Complex | 12 |
| Audit event detail | UI | Medium | 6 |
| Critical activity filter board | UI | Medium | 6 |
| Actor activity history | UI | Easy | 4 |
| Audit export view | UI | Medium | 6 |
| Record audit event | API | Complex | 8 |
| Search audit by entity actor and date | API | Complex | 8 |
| Load audit event detail | API | Easy | 4 |
| Filter critical activity types | API | Medium | 6 |
| Load actor activity history | API | Medium | 6 |
| Export audit pack | API | Complex | 8 |
| Verify audit integrity marker | API | Complex | 8 |
| List auditable activity catalogue | API | Simple | 2 |
| System audit trail store | DB | Complex | 6 |
| System audit trail tests | Testing | Complex | 8 |
| System audit trail implementation documentation | Documentation | Medium | 3 |

**Feature total: 101 hours**
