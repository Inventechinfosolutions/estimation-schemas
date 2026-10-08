# F04-006 — Administrator Registration Verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-006 |
| **Feature Name** | Administrator Registration Verification |
| **Module** | 04 — Candidate Registration and Fee Payment |

### Description
Examination Administrators review, verify and approve (or return/reject) candidate registrations where verification is configured — especially Type 2 competent-authority documents and any Department-required checks on Type 1 packs — using an admin inbox, registration detail review, document viewer and decision actions with full history.

### Business Objective
Provide controlled administrative assurance over registrations before they are treated as fully verified for operational processes that depend on verified status.

### Actors
Maker: Candidate (completed registration from F04-001–F04-005). Approver: Examination Administrator. Auditor: senior Examination Administrator / audit role via history.

### User Journey
1. Who creates: The candidate creates the registration; the administrator does not create the application but creates verification decisions on completed registrations.
2. How they create: Administrator opens verification inbox → selects a pending registration → reviews identity, examination, preferences, payment and (for Type 2) competent-authority document → records decision.
3. How they edit: Administrator may update verification remarks before finalising; after decision, reverse/amend only under configured re-open rules with audit.
4. How they send for approval: Candidate completion (F04-005) places the registration into the pending verification queue when verification is configured — no separate candidate “send to admin” beyond completing registration.
5. How the approver sees pending items: Administrator Registration Verification Inbox lists pending/returned items with filters by type, examination and age.
6. How the approver decides: Approve (verified), Return for correction, or Reject (with reason) per configured outcomes; decision stored with actor and timestamp.
7. How the applicant / maker sees history: Candidate sees verification status and remarks (as disclosed) on registration status (F04-005).
8. How the approver / auditor sees history: Verification history screen shows prior decisions, remarks and actors for the registration.

### Functional Capabilities
- Configurable requirement for admin verification (especially Type 2 document checks).
- Pending verification inbox with filters (type, examination, status, date).
- Open full registration pack for review.
- Embedded document viewer for competent-authority upload.
- Record approve / return / reject with mandatory reason on negative outcomes.
- Update registration verification status visible to candidate.
- Prevent unverified registrations from progressing in processes that require verified flag (as configured).
- Admin search across registrations beyond pending queue.
- Maintain complete verification decision history.
- Role-restrict verification actions to Examination Administrator privileges (Module 01).
- Audit all review opens and decisions.
- Support bulk triage filters without bulk silent approve (decisions remain explicit per record unless Department later approves batch rules).

### UI Screens
| Screen | Purpose |
|---|---|
| Administrator registration verification inbox | Queue of pending/returned registrations |
| Registration detail review screen | Full pack for scrutiny |
| Competent authority document viewer screen | View embedded Type 2 document |
| Verification decision form screen | Approve / return / reject with remarks |
| Verification decision history screen | Prior decisions and actors |
| Administrator registration search screen | Locate registrations beyond inbox filters |

### Logical API operations
| Operation | Purpose |
|---|---|
| List pending registrations for verification | Inbox query with filters |
| Get registration pack for review | Return full pack including document refs |
| Approve registration verification | Mark verified |
| Return or reject registration verification | Negative outcome with reason |
| Search administrator registrations | Broader search for support/ops |
| Get verification decision history | Return decision trail |

### Inputs
Registration number; verification decision; remarks/reason; administrator identity; filters.

### Outputs
Updated verification status; decision audit records; candidate-visible status change; queue refresh.

### Business Rules
- Verification applies where configured (notably Type 2 document presence and acceptability).
- Reject/return require reason.
- Only Examination Administrator role may decide.
- Payment success is prerequisite for completed registrations entering the queue; verification does not replace payment gate.
- KGID confirmation remains candidate-side (F04-001); admin may still review Type 1 packs if configured.

### Validations
- Decision code valid; reason mandatory for return/reject.
- Registration must be in a verifiable state.
- Actor must hold verification privilege.

### Calculations
None.

### Workflow
Registration confirmed (F04-005) → pending verification (if configured) → admin reviews → approve / return / reject → candidate status updated → history retained. If verification is not configured for a path, registrations skip pending queue.

### Search Requirements
By registration number, KGID/employee ID, name, mobile, organisation, examination, verification status, date range.

### Documents
View competent-authority document (embedded from F04-002); no separate DMS.

### Reports
Pending/verified/rejected counts feed Module 09.

### Notifications
Verification outcome notifications via Module 09 as configured.

### Security
Admin-only inbox and decisions; centre/invigilator users have no verification rights; full audit trail.

### Integrations
None.

### Dependencies
F04-001–F04-005; Module 01 administrator privileges; Module 09 for notifications/MIS.

### Assumptions
- Exact mandatory verification paths finalised with Department; feature supports configured on/off per type.
- Document viewing is embedded; not a DMS product.
- Hours independent of payment/KGID integration rows.

### Risks
Backlog if document quality is poor; unclear return reasons increase rework cycles.

### Non Functional Requirements
Responsive inbox at registration volume; durable decision audit; clear candidate-visible status labels.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Administrator registration verification inbox | UI | Complex | 12 |
| Registration detail review screen | UI | Complex | 12 |
| Competent authority document viewer screen | UI | Medium | 6 |
| Verification decision form screen | UI | Medium | 6 |
| Verification decision history screen | UI | Easy | 4 |
| Administrator registration search screen | UI | Medium | 6 |
| List pending registrations for verification | API | Medium | 6 |
| Get registration pack for review | API | Medium | 6 |
| Approve registration verification | API | Complex | 8 |
| Return or reject registration verification | API | Complex | 8 |
| Search administrator registrations | API | Medium | 6 |
| Get verification decision history | API | Easy | 4 |
| Verification decision persistence | Database | Medium | 4 |
| Administrator registration verification tests | Testing | Complex | 8 |
| Administrator registration verification documentation | Documentation | Medium | 3 |

**Feature total: 99 hours**

### Estimation Assumptions
- No payment/KGID integration hours on this feature.
- Document upload remains on F04-002; this feature only reviews/associates decisions.
