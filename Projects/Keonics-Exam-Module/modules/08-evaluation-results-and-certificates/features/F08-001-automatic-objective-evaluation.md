# F08-001 — Automatic Objective Evaluation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Automatic Objective Evaluation |
| **Module** | 08 — Evaluation, Results and Certificates |

### Description
Automatically score locked objective CBT responses against the answer key for the candidate’s paper version, applying configurable marks, optional negative marking, totals, percentage and pass/fail rules, and persist evaluation outcomes with an administrator console for batch runs, exceptions and score detail review.

### Business Objective
Produce consistent, rule-based objective results immediately after response lock without manual marking.

### Actors
- System (primary scorer on lock handoff)
- Examination Administrator (runs/re-runs batches, reviews exceptions)
- Auditor (evaluation history)
- Candidate does not interact until publication (F08-002)

### User Journey
1. Who creates: The system creates evaluation outcomes when a locked attempt is handed off from F07-005; administrators may create batch re-evaluation runs for exception queues when keys/rules are corrected under controlled policy.
2. How they create: On lock → load version answer key → classify each response correct/incorrect/unanswered → apply marks and negative marking → compute total, percentage, pass/fail → persist. Administrators open evaluation console to monitor batches and open score detail.
3. How they edit: Scores are not hand-edited. Rule/key corrections trigger controlled re-run that writes a new evaluation version or superseding outcome per approved policy; prior outcome retained in history.
4. How they send for approval: Automatic scoring itself has no maker–checker. Publication of results to candidates is a separate feature (F08-002).
5. How the approver sees pending items: No scoring approver inbox. Exception/re-run queue is an administrator operational list, not a Department approval inbox.
6. How the approver decides: No pass/fail approval decision by an officer for objective papers; pass/fail is calculated from configured rules.
7. How the applicant / maker sees history: Administrators see evaluation register and per-candidate score detail/history of re-runs. Candidates see outcomes only after F08-002 publication.
8. How the approver / auditor sees history: Auditors view evaluation timestamps, key/version references, rule set applied, and re-run lineage.

### Functional Capabilities
- Score against answer key for the assigned paper version/order
- Classify correct, incorrect and unanswered
- Apply positive marks and configurable negative marks if enabled
- Compute total marks, percentage and pass/fail from examination parameters
- Persist evaluation outcome linked to attempt, registration and examination
- Evaluation run console for monitoring automatic and batch runs
- Scoring rules preview for the examination parameters in force
- Exception / re-run queue when key integrity or handoff issues occur
- Candidate score detail for administrators (pre-publication)
- Ensure scoring matches configured key and rules (acceptance)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Evaluation run console | Complex |
| Scoring rules preview | Medium |
| Evaluation results batch register | Medium |
| Candidate score detail | Complex |
| Evaluation exception and re-run queue | Medium |
| Evaluation history for attempt | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Load answer key for paper version | Complex |
| Score responses correct incorrect unanswered | Very High |
| Apply negative marking rules | Complex |
| Compute total percentage and pass fail | Complex |
| Persist evaluation outcome | Complex |
| Re-run evaluation for exceptions | Complex |
| Search evaluation register | Medium |
| Load candidate score detail | Medium |

### Inputs
Locked responses, paper version/answer key, examination marking and pass parameters, batch selection for re-run.

### Outputs
Per-question outcome classifications, total marks, percentage, pass/fail, evaluation record, exception queue items.

### Business Rules
- Objective scoring only; no subjective marking in this phase.
- Key must match the version/order served to the candidate (Module 06 integrity).
- Unanswered treated per configured marks (typically zero; negative marking does not apply to unanswered unless explicitly configured).
- Pass/fail uses configured pass marks/percentage.
- Ineligible or incomplete attempts without lock are not scored as passed.
- Re-run does not alter locked responses; only recomputes from key/rules.

### Validations
- Locked attempt required before evaluation
- Answer key present for version
- Parameter set present for marks/pass/negative marking
- Re-run authorised to Examination Administrator role only

### Calculations
Per-question marks; sum totals; percentage = total × 100 / max marks; pass if threshold met; negative marks subtracted when applicable.

### Workflow
Lock handoff → auto-evaluate → persist → ready for publication rules. Exception → admin re-run → supersede per policy. No approval of individual scores.

### Search Requirements
Evaluation register by examination, centre, date, pass/fail, exception status, registration number.

### Documents
None (score sheets not required for objective auto-mark).

### Reports
Feeds result publication and Module 09 pass/fail statistics.

### Notifications
None until publication/certificate stages unless admin alert on batch failure via F09-003.

### Security
Pre-publication scores visible only to authorised administrators; centre invigilators do not see mark breakdowns unless Department grants read-only later.

### Integrations
None.

### Dependencies
Modules 03 (parameters), 06 (keys/versions), F07-005 (locked responses); F08-002 consumes outcomes.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Scoring engine API is Very High due to version-aware key mapping and rule combinations.

### Risks
Key/version mismatch yields wrong scores — mitigated by Module 06 integrity and exception queue.
Late key correction after publication requires coordinated unpublish (F08-002) and re-publish policy.

### Non Functional Requirements
Batch evaluation of a full session completes within approved operational window; every outcome stores rule/key references for audit.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Evaluation run console | UI | Complex | 12 |
| Scoring rules preview | UI | Medium | 6 |
| Evaluation results batch register | UI | Medium | 6 |
| Candidate score detail | UI | Complex | 12 |
| Evaluation exception and re-run queue | UI | Medium | 6 |
| Evaluation history for attempt | UI | Easy | 4 |
| Load answer key for paper version | API | Complex | 8 |
| Score responses correct incorrect unanswered | API | Very High | 16 |
| Apply negative marking rules | API | Complex | 8 |
| Compute total percentage and pass fail | API | Complex | 8 |
| Persist evaluation outcome | API | Complex | 8 |
| Re-run evaluation for exceptions | API | Complex | 8 |
| Search evaluation register | API | Medium | 6 |
| Load candidate score detail | API | Medium | 6 |
| Evaluation outcome entities | DB | Complex | 6 |
| Automatic objective evaluation tests | Testing | Very High | 12 |
| Automatic objective evaluation implementation documentation | Documentation | Complex | 4 |

**Feature total: 136 hours**
