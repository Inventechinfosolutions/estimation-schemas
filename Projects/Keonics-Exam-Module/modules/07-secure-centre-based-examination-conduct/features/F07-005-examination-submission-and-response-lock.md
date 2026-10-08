# F07-005 — Examination Submission and Response Lock

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-005 |
| **Feature Name** | Examination Submission and Response Lock |
| **Module** | 07 — Secure Centre-Based Examination Conduct |

### Description
Enable the candidate to review an answered/unanswered summary, confirm voluntary submission, irrevocably lock responses, and hand off the locked attempt to automatic evaluation; also complete the same lock path for timer-driven auto-submit without allowing further changes.

### Business Objective
Close the examination attempt cleanly so scoring uses a final, immutable response set.

### Actors
- Candidate at centre (manual submit with confirmation)
- System (auto-submit on expiry via F07-004)
- Invigilator (views submitted/locked status; cannot unlock)
- Examination Administrator (exception visibility only)
- Auditor (submission and lock history)

### User Journey
1. Who creates: The candidate creates a manual submission by confirming the summary; the system creates an auto-submission when the central timer expires; both paths create a locked attempt record.
2. How they create: From secure interface → open submission summary → review answered/unanswered counts → confirm submit → responses lock → success view; or timer expiry triggers lock without candidate confirmation.
3. How they edit: After lock, responses cannot be edited. Before confirm, candidate may return to the interface to change answers (F07-004). There is no staff edit of locked answers.
4. How they send for approval: Candidate confirmation is a self-confirmation dialog, not a Department approval workflow. Auto-submit has no confirmation step.
5. How the approver sees pending items: No approver inbox for submissions. Invigilators see submitted/locked on the centre status board; evaluation ownership moves to Module 08.
6. How the approver decides: No approval decision to accept/reject a submission; lock is final for objective CBT.
7. How the applicant / maker sees history: Candidate sees submission success / already submitted notice and cannot re-enter answering; portal later shows results when published.
8. How the approver / auditor sees history: Staff/auditors see submit time, manual vs auto-submit flag, actor/system initiator, and lock timestamp with full attribution.

### Functional Capabilities
- Submission summary with answered/unanswered (and not-visited if tracked) counts
- Explicit confirmation before manual submit
- Irrevocable response lock on confirm or auto-submit
- Reject any post-lock answer change attempts
- Initiate evaluation handoff for locked attempts
- Distinguish manual submit vs timer auto-submit in status and history
- Invigilator-visible submission status for centre candidates
- Already-submitted / forced-lock notices for late reopen attempts
- Preserve final response set for scoring and audit

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Submission summary (answered / unanswered) | Complex |
| Submit confirmation dialog | Easy |
| Submission success and locked view | Medium |
| Already submitted / forced lock notice | Easy |
| Invigilator submission status board | Medium |
| Administrator submission exception view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Build submission summary counts | Medium |
| Confirm and submit examination | Complex |
| Lock responses irrevocably | Complex |
| Process timer auto-submit lock | Complex |
| Initiate evaluation handoff | Complex |
| Query submission and lock status | Easy |
| Reject post-lock response changes | Medium |
| Search centre submission status | Medium |

### Inputs
Active attempt identifier, candidate confirmation, auto-submit trigger from timer, final saved responses.

### Outputs
Locked attempt, submission timestamp and mode, evaluation handoff signal, status for centre dashboard and candidate notice.

### Business Rules
- Manual submit requires confirmation showing answered/unanswered summary.
- Lock is irrevocable for the attempt; no unlock by invigilator.
- Auto-submit uses last saved responses and locks immediately.
- Evaluation (F08-001) starts only after successful lock.
- Duplicate submit requests are idempotent once locked.
- Candidates who never started are not auto-submitted as completed unless Department defines a separate absent closure (out of this feature’s default).

### Validations
- Submit only for active, unlocked attempts belonging to the authenticated session
- Confirmation required for manual path
- Auto-submit only when timer expiry is authoritative
- Post-lock writes rejected

### Calculations
Counts of answered, unanswered and (if applicable) not-visited questions from palette state.

### Workflow
Summary → confirm (manual) or expiry (auto) → lock → evaluation handoff. No Department approval.

### Search Requirements
Centre submission status by session/candidate; administrator search by examination/date/mode (manual/auto).

### Documents
None.

### Reports
Submitted/locked counts on centre dashboard and Module 09 examination reports.

### Notifications
Result/certificate notifications are Module 09 after evaluation/publication — not at submit time unless configured.

### Security
Only the authenticated candidate session (or system timer) may submit; staff cannot submit on behalf of candidate through this feature; lock events attributable.

### Integrations
None.

### Dependencies
F07-004 (interface/timer), F07-006 (record submit), F08-001 (evaluation).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Partial answer sets are valid to submit; scoring handles unanswered per rules.

### Risks
Candidate accidental early submit (mitigated by confirmation summary).
Handoff failure delaying evaluation (requires exception view and retry).

### Non Functional Requirements
Lock operation is transactional with response finalisation; duplicate submit under double-click is safe.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Submission summary (answered / unanswered) | UI | Complex | 12 |
| Submit confirmation dialog | UI | Easy | 4 |
| Submission success and locked view | UI | Medium | 6 |
| Already submitted / forced lock notice | UI | Easy | 4 |
| Invigilator submission status board | UI | Medium | 6 |
| Administrator submission exception view | UI | Medium | 6 |
| Build submission summary counts | API | Medium | 6 |
| Confirm and submit examination | API | Complex | 8 |
| Lock responses irrevocably | API | Complex | 8 |
| Process timer auto-submit lock | API | Complex | 8 |
| Initiate evaluation handoff | API | Complex | 8 |
| Query submission and lock status | API | Easy | 4 |
| Reject post-lock response changes | API | Medium | 6 |
| Search centre submission status | API | Medium | 6 |
| Submission and response lock entities | DB | Medium | 4 |
| Examination submission and response lock tests | Testing | Complex | 8 |
| Examination submission and response lock implementation documentation | Documentation | Medium | 3 |

**Feature total: 107 hours**
