# F08-002 — Result Publication

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Result Publication |
| **Module** | 08 — Evaluation, Results and Certificates |

### Description
Publish evaluated results to the candidate login according to configured publication rules and approved disclosure fields (name, registration, examination, date, marks, percentage, pass/fail and other approved fields), with administrator controls to publish, withhold or retract batches and a portal result view for candidates.

### Business Objective
Release results to candidates in a controlled, auditable way without exposing non-approved fields or unpublished scores.

### Actors
- Examination Administrator (publication control)
- Candidate (views published result on portal)
- Auditor (publication history)
- No Department checker inbox unless later mandated

### User Journey
1. Who creates: Examination Administrators create publication batches from evaluated attempts that meet publication rules; the system creates candidate-visible result records on successful publish.
2. How they create: Open publication console → filter examination/session → preview disclosure fields under rules → publish batch → candidates see result on portal. Withhold keeps scores admin-only.
3. How they edit: Administrators may withhold or retract a published batch under policy (e.g. key error), which hides candidate view until re-publish; field values are not free-edited — they come from evaluation outcomes.
4. How they send for approval: Publication is an administrator operational release. No multi-level approval inbox in the current SOW; if Department later requires dual control, it would extend this feature.
5. How the approver sees pending items: There is no approver inbox. “Ready to publish” is an administrator worklist of evaluated-unpublished attempts.
6. How the approver decides: No separate approver; the administrator decides publish / withhold / retract within role privileges.
7. How the applicant / maker sees history: Candidates see current published result and, if provided, prior published versions only when policy shows them. Administrators see publication batch history.
8. How the approver / auditor sees history: Auditors see who published/withheld/retracted what, when, with rule set and field disclosure snapshot.

### Functional Capabilities
- Publication rules application (what can be released, when, for which examination)
- Publication console for batch release of evaluated results
- Candidate portal result view limited to approved fields
- Withhold and retract/unpublish controls
- Publication batch history
- Block candidate visibility of unevaluated or withheld results
- Align displayed fields: name, registration, examination, date, marks, percentage, pass/fail, other approved fields
- Drive certificate eligibility visibility only after publish if rules require published pass

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Publication rules configuration view | Medium |
| Result publication console | Complex |
| Candidate portal result view | Medium |
| Publication batch history | Easy |
| Withhold and unpublish notice | Easy |
| Ready-to-publish worklist | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Validate publication eligibility | Complex |
| Publish results batch | Complex |
| Load candidate published result | Medium |
| Withhold or retract publication | Complex |
| Search publication history | Medium |
| Apply field disclosure rules | Medium |
| List ready-to-publish attempts | Medium |

### Inputs
Evaluation outcomes, publication rules, examination/session filters, publish/withhold/retract action, actor identity.

### Outputs
Published result records, candidate portal view model, batch history, withhold/retract events.

### Business Rules
- Only evaluated attempts can be published.
- Candidate login shows results only after publication per rules.
- Non-approved personal or operational fields are never shown on portal result view.
- Retract hides portal result and may block certificate download until resolved.
- Centre invigilators do not publish results.

### Validations
- Batch contains only eligible evaluated attempts
- Disclosure rules resolved before publish
- Retract requires reason code for audit

### Calculations
None beyond displaying evaluated totals/percentage/pass-fail.

### Workflow
Evaluated → ready list → publish/withhold → candidate visibility. Retract → hidden → optional re-publish after F08-001 re-run.

### Search Requirements
Batches by examination/date/status; candidate result by registration; ready-to-publish filters.

### Documents
None required; optional printable result statement if Department approves later (not default).

### Reports
Published/pass/fail counts feed Module 09.

### Notifications
Result-available notifications owned by F09-003 on publish events.

### Security
Pre-publish scores admin-only; portal ownership isolation for candidate result; publication actions attributable.

### Integrations
None directly; notification channel is F09-003.

### Dependencies
F08-001; Module 02 (candidate portal); F08-003 may require published pass.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Publication rules configuration UI is in this feature as business control, not a separate SOW ID.

### Risks
Premature publish before key verification.
Partial batch publish confusion — console must show clear batch boundaries.

### Non Functional Requirements
Portal result retrieval is fast for concurrent post-publish traffic; publication actions fully audited.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Publication rules configuration view | UI | Medium | 6 |
| Result publication console | UI | Complex | 12 |
| Candidate portal result view | UI | Medium | 6 |
| Publication batch history | UI | Easy | 4 |
| Withhold and unpublish notice | UI | Easy | 4 |
| Ready-to-publish worklist | UI | Medium | 6 |
| Validate publication eligibility | API | Complex | 8 |
| Publish results batch | API | Complex | 8 |
| Load candidate published result | API | Medium | 6 |
| Withhold or retract publication | API | Complex | 8 |
| Search publication history | API | Medium | 6 |
| Apply field disclosure rules | API | Medium | 6 |
| List ready-to-publish attempts | API | Medium | 6 |
| Result publication entities | DB | Medium | 4 |
| Result publication tests | Testing | Complex | 8 |
| Result publication implementation documentation | Documentation | Medium | 3 |

**Feature total: 101 hours**
