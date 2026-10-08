# F05-004 — Examination Credential Generation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-004 |
| **Feature Name** | Examination Credential Generation |
| **Module** | 05 — Scheduling, Allocation, Hall Tickets and Examination Credentials |

### Description
Generate examination Login ID and Password for scheduled, allocated candidates and communicate them securely through the approved communication mechanism (SMS/email/portal as configured). Credentials are for the centre-based examination path and are distinct from candidate portal OTP login (Module 02).

### Business Objective
Ensure every eligible scheduled candidate receives usable examination credentials in time for centre conduct, with controlled regeneration and full issue audit.

### Actors
Maker: Examination Administrator (generate/communicate). Applicant: Candidate (receives credentials). Approver: none. Auditor: Examination Administrator (issue history).

### User Journey
1. Who creates: Examination Administrator triggers credential generation for a published schedule’s allocated candidates.
2. How they create: Credential generation control → select schedule/cohort → generate Login ID/Password → confirm communication → system dispatches via approved channel and/or shows masked notice in portal/hall ticket as configured.
3. How they edit: Credentials are not freely edited; regeneration is an exception path with reason, invalidating prior secrets per policy.
4. How they send for approval: Does not apply — generation/communication is administrator action, not a checker workflow.
5. How the approver sees pending items: No approver inbox; exception regenerate requests are handled by administrator on the regenerate form.
6. How the approver decides: No approval decision; regenerate is an admin exception action with audit.
7. How the applicant / maker sees history: Candidate sees masked credential notice / delivery status as disclosed; cannot view raw password history beyond current policy.
8. How the approver / auditor sees history: Credential issue history shows generation, communication and regenerate events without exposing password plaintext in logs.

### Functional Capabilities
- Generate unique examination Login ID and Password for allocated scheduled candidates.
- Bind credentials to candidate, schedule/session and allotted centre context.
- Communicate credentials via approved mechanism (SMS/email/portal).
- Mask password display in administrative screens after issue.
- Support controlled regeneration with reason and prior credential invalidation.
- Prevent generation for candidates lacking schedule/allocation.
- Align with hall ticket credential information fields where applicable (F05-003).
- Track communication success/failure for operational follow-up.
- Ensure credentials are intended only for authorised centre session path (enforced in Module 07).
- Audit generation, communication and regeneration without storing recoverable plaintext beyond secure secret storage practice.
- Distinct from Module 02 OTP portal credentials.

### UI Screens
| Screen | Purpose |
|---|---|
| Examination credential generation control screen | Admin generate for schedule/cohort |
| Credential communication confirmation screen | Confirm dispatch channel and cohort |
| Candidate credential notice screen (masked) | Portal notice of issue/delivery status |
| Credential regenerate exception form | Regenerate with reason |
| Credential issue history screen | Audit of generate/communicate/regenerate |

### Logical API operations
| Operation | Purpose |
|---|---|
| Generate examination credentials batch | Create Login ID/Password for cohort |
| Communicate examination credentials | Dispatch via approved channels |
| Get credential issue status for candidate | Return masked status to portal/admin |
| Regenerate examination credentials | Invalidate prior and issue new |
| Get credential issue history | Return audit trail without plaintext secrets |

### Inputs
Allocated candidates; schedule; communication channel configuration; regenerate reason; administrator identity.

### Outputs
Credential records (securely stored); communication dispatch results; masked candidate notice; issue history.

### Business Rules
- Generate only for scheduled and allocated candidates.
- Credentials usable only in authorised session path (Module 07 enforces).
- Regeneration invalidates previous password per policy.
- Portal OTP credentials are never reused as examination credentials.
- Communication uses Department-approved channels only.

### Validations
- Eligibility: allocation + schedule present.
- Regenerate requires reason.
- Admin privilege required for generate/regenerate.

### Calculations
None (optional random password generation is technical, not a business fee calculation).

### Workflow
Allocation committed → generate credentials → communicate → candidate receives notice → regenerate only on exception. No checker inbox.

### Search Requirements
Admin search by registration number, Login ID, schedule, communication status.

### Documents
None (may appear as fields on hall ticket via F05-003).

### Reports
Credential issued / communication failure counts feed Module 09.

### Notifications
Credential communication is a core output of this feature via SMS/email/portal integration.

### Security
Hash/secure storage of passwords; no plaintext in audit logs; admin masked views; rate-limit regenerate; separate from portal OTP secrets.

### Integrations
**SMS / email (approved communication mechanism)** for secure credential delivery — Integration **Medium (16)** for auth, mapping and retry on notification channels used for credentials.

### Dependencies
F05-001, F05-002; Module 02 is separate login; consumed by Module 07 exam login.

### Assumptions
- Exact password complexity and Login ID format approved by Department.
- Notification gateway availability as facilitated; Medium integration covers credential dispatch mapping/retry.
- Hall ticket layout updates remain primarily F05-003.

### Risks
SMS delay or wrong mobile causes entry-day failures; weak regenerate controls risk credential abuse.

### Non Functional Requirements
Secure secret handling; reliable dispatch with retry; clear candidate instructions; auditable issue trail.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Examination credential generation control screen | UI | Medium | 6 |
| Credential communication confirmation screen | UI | Easy | 4 |
| Candidate credential notice screen (masked) | UI | Medium | 6 |
| Credential regenerate exception form | UI | Medium | 6 |
| Credential issue history screen | UI | Easy | 4 |
| Generate examination credentials batch | API | Complex | 8 |
| Communicate examination credentials | API | Complex | 8 |
| Get credential issue status for candidate | API | Easy | 4 |
| Regenerate examination credentials | API | Complex | 8 |
| Get credential issue history | API | Easy | 4 |
| Examination credential secure persistence | Database | Medium | 4 |
| SMS/email credential communication channel | Integration | Medium | 16 |
| Examination credential generation tests | Testing | Complex | 8 |
| Examination credential generation documentation | Documentation | Medium | 3 |

**Feature total: 89 hours**

### Estimation Assumptions
- Communication Integration billed Medium (16), not Payment/KGID Very High.
- Centre-day login enforcement remains Module 07.
