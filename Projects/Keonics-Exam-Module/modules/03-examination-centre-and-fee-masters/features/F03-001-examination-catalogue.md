# F03-001 — Examination Catalogue

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Examination Catalogue |
| **Module** | 03 — Examination, Centre and Fee Masters |

### Description
Examination Administrators create and manage the catalogue of examinations that may be opened for candidate registration, including published display details candidates see when selecting an examination. The Administrator opens the catalogue register, creates an examination with name and display attributes, maintains status (Draft / Open for registration / Closed / Inactive), and publishes or withdraws examinations from the candidate registration selection list. Detailed scoring, duration, randomisation and certificate eligibility parameters are configured under F03-004 against the examination created here. Fee amounts belong to F03-003; centre capacity belongs to F03-002.

### Business Objective
Maintain a controlled catalogue of examinations open for registration with accurate published details so candidates only register against Department-approved, currently open examinations.

### Actors
Examination Administrator (catalogue owner); Candidate (consumes published open examinations during registration); Auditor (read-only catalogue history).

### User Journey
1. Who creates: Examination Administrator with examination-master privilege.
2. How they create: Open Examination catalogue register → New examination → enter examination name, code/short name, description, category tags if used, registration window dates, display instructions summary → save as Draft → later mark Open for registration when ready.
3. How they edit: Search catalogue → open examination → update display details or registration window → save; closing registration removes it from candidate selection while retaining historical registrations against it.
4. How they send for approval: Submit/approval does not apply by default; Administrator publishes Open status directly. If Department later requires maker–checker for opening registration, that would be a policy add-on—not assumed here.
5. How the approver sees pending items: There is no approver inbox; Draft vs Open vs Closed statuses are filtered on the catalogue register.
6. How the approver decides: There is no separate approval decision; Open/Closed is an administrative status change with audit.
7. How the applicant / maker sees history: Administrator opens catalogue change history on the examination (who changed status, display fields, when).
8. How the approver / auditor sees history: Auditor opens the same history and may filter by status transitions (especially Open/Closed).

### Functional Capabilities
- Maintain examination catalogue register with create, view, update, search and status filters.
- Capture examination identity and published display details (name, code, description, summary instructions, registration window).
- Control Open for registration vs Closed / Inactive so only open examinations appear in candidate selection (Module 04).
- Prevent hard-delete of examinations that already have registrations; allow deactivate/close instead.
- Preview published details as candidates would see them.
- Link each catalogue entry to later parameter configuration (F03-004) without duplicating scoring fields here.
- Enforce unique examination code/name rules per Department policy.
- Show registration-window validity on the register for operational control.
- Support listing currently open examinations for Administrator monitoring.
- Audit all create/update/status changes with actor and timestamp.
- Allow search by name, code, status and registration window dates.
- Retain closed examinations for historical reporting and hall-ticket/result linkage.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination catalogue register and search | Complex |
| Examination create / edit form | Complex |
| Open / close registration status control | Medium |
| Candidate-facing published detail preview | Medium |
| Currently open examinations monitor | Easy |
| Catalogue change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create examination catalogue entry | Complex |
| Update examination display details | Medium |
| Open or close examination for registration | Medium |
| Search examination catalogue | Medium |
| List examinations open for registration | Easy |
| Read catalogue change history | Easy |
| Validate examination identity uniqueness | Medium |

### Inputs
Examination name; code/short name; description; published summary/instructions excerpt; registration open/close dates; status; Administrator remarks.

### Outputs
Persisted examination catalogue records; Open list consumable by registration; published detail preview; change history; uniqueness validation results.

### Business Rules
- Only Active/Open examinations are available for candidate preference/registration selection.
- Closing registration must not delete historical registrations, schedules or results linked to the examination.
- Display details shown to candidates must match the published catalogue fields (not draft-only notes).
- Examination parameter packs (F03-004) attach to a catalogue examination; catalogue create is prerequisite.
- Unique examination code within the system (or within Department-defined scope).

### Validations
- Name and code mandatory; code unique.
- Registration close date not before open date when both provided.
- Cannot set Open if mandatory linked masters/parameters are incomplete when Department requires readiness check (soft warning or hard block as configured).
- Cannot delete examination with dependent registrations.
- Status values limited to allowed set (Draft/Open/Closed/Inactive).

### Calculations
None beyond derived “currently open” flag from status and registration window dates.

### Workflow
Create Draft → edit display details → Open for registration → Close when window ends or Administrator closes → retain for history. No maker–checker inbox by default.

### Search Requirements
Name, code, status, registration window from/to, updated by, updated date.

### Documents
None as catalogue attachments in SOW; instructions text may be stored as published content fields (full rich instructions may live in F03-004).

### Reports
Catalogue listing export (open/closed examinations) for Administrator operations.

### Notifications
Optional notify when examination opens/closes if Module 09 templates configured; not required for catalogue CRUD itself.

### Security
Only Examination Administrators with examination-master privilege may mutate catalogue; candidates have read of published open examinations only via registration flow; all status changes audited.

### Integrations
None for this feature.

### Dependencies
Consumed by F03-004 (parameters), F03-003 (fee rules may reference examination), Module 04 (examination selection), Module 05 (scheduling).

### Assumptions
- “Open for registration” is controlled here; seat capacity remains on centres (F03-002).
- Hours use Estimation Master; each named screen and logical API billed independently.
- No payment or KGID channel in this feature.

### Risks
- Opening an examination before parameters/fee rules are ready could allow incomplete registrations.
- Duplicate examination codes would confuse reports and hall tickets.
- Accidental close during active registration window needs clear operational confirmation.

### Non Functional Requirements
Catalogue search must remain responsive for expected examination volumes; Open list used at registration peaks must be consistent (no stale Open after close beyond short cache TTL); status changes attributable with audit.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Examination catalogue register and search | UI | Complex | 12 |
| Examination create / edit form | UI | Complex | 12 |
| Open / close registration status control | UI | Medium | 6 |
| Candidate-facing published detail preview | UI | Medium | 6 |
| Currently open examinations monitor | UI | Easy | 4 |
| Catalogue change history | UI | Medium | 6 |
| Create examination catalogue entry | API | Complex | 8 |
| Update examination display details | API | Medium | 6 |
| Open or close examination for registration | API | Medium | 6 |
| Search examination catalogue | API | Medium | 6 |
| List examinations open for registration | API | Easy | 4 |
| Read catalogue change history | API | Easy | 4 |
| Validate examination identity uniqueness | API | Medium | 6 |
| Examination catalogue persistence | DB | Medium | 4 |
| Examination catalogue feature tests | Testing | Complex | 8 |
| Examination catalogue implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **101** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- No Integration row — no external channel.
- Parameter, fee and centre details are estimated in sibling features, not collapsed into this catalogue feature.
