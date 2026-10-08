# F07-003 — Examination Login at Centre

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Examination Login at Centre |
| **Module** | 07 — Secure Centre-Based Examination Conduct |

### Description
Allow the candidate to log in at the allotted centre using system-generated examination Login ID and Password, only when centre, session, timing, activation and authorised-environment gates succeed, then bind the candidate to a single active examination session and present pre-start instructions before the secure interface opens.

### Business Objective
Separate exam-day credentials from portal OTP login and ensure login succeeds only under authorised centre conditions with one active session.

### Actors
- Candidate at centre (logs in with exam credentials)
- Invigilator (assists seating; views login failures for their centre)
- Examination Administrator (investigates login anomalies)
- Auditor (login event history)

### User Journey
1. Who creates: The candidate creates a login attempt by entering examination Login ID and Password at the centre workstation after invigilator seating/activation; the system creates the authenticated exam session on success.
2. How they create: Open exam login screen on authorised workstation → enter credentials → system validates candidate, centre, session, timing, activation and environment → show pre-start instructions → proceed to CBT interface (F07-004).
3. How they edit: Credentials are system-generated (Module 05); candidates do not edit Login ID/Password here. Failed attempts may be retried within approved limits; invigilators may trigger credential re-issue only via Module 05 processes, not by editing login records ad hoc.
4. How they send for approval: Does not apply — login is authentication, not an approval submission.
5. How the approver sees pending items: No approver inbox. Invigilators see login failure/success status on the centre roster; administrators see anomaly queues.
6. How the approver decides: No approval decision.
7. How the applicant / maker sees history: Candidate sees success path into the exam or a denial message; invigilators see recent login attempts for centre candidates.
8. How the approver / auditor sees history: Administrators/auditors search login attempts by centre, candidate, outcome, workstation and time, including concurrent-session blocks.

### Functional Capabilities
- Examination login with system-generated Login ID/Password (distinct from portal OTP)
- Validate candidate identity, allotted centre, active session, schedule timing and invigilator activation before success
- Bind successful login to authorised workstation/session context
- Prevent multiple simultaneous examination sessions for the same candidate
- Pre-start instructions and acknowledgement before paper delivery
- Clear failure messages for wrong credentials, wrong centre, inactive session, not activated, outside window, already completed
- Record login success/failure events for F07-006
- Invigilator-visible login status on centre candidate context

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Examination login screen | Medium |
| Login validation feedback and denial | Easy |
| Pre-start instructions and acknowledgement | Medium |
| Concurrent session block notice | Simple |
| Invigilator login attempt status panel | Easy |
| Administrator login anomaly view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Authenticate examination credentials | Complex |
| Validate centre session timing and activation for login | Complex |
| Bind candidate to authorised exam session | Complex |
| Enforce single active examination session | Complex |
| Record login attempt outcome | Medium |
| Load pre-start instructions | Easy |
| Search login attempts for centre | Medium |
| Release or expire abandoned login session | Medium |

### Inputs
Examination Login ID, Password, centre/workstation context, session identifiers, acknowledgement of instructions.

### Outputs
Authenticated exam session binding, denial outcomes, login attempt history, handoff token/context to secure interface (logical, not technical design).

### Business Rules
- Portal OTP credentials cannot start the CBT; only examination credentials issued under Module 05.
- Login succeeds only when F07-001 gate conditions and F07-002 activation are satisfied.
- Already completed or locked examinations cannot log in again.
- Concurrent second login is blocked; first session policy (resume vs force-logout) follows finally approved rules with F07-004 resume.
- Centre staff cannot view raw passwords; only status of attempts.

### Validations
- Credentials format and lockout/retry limits as approved
- Centre mismatch always fails
- Outside schedule window always fails
- Missing activation always fails

### Calculations
None.

### Workflow
Enter credentials → validate → deny or acknowledge instructions → open secure interface. No approval.

### Search Requirements
Login attempts by candidate, centre, outcome, date/time; anomaly filter for repeated failures.

### Documents
Pre-start instructions content from examination parameters.

### Reports
Login success/failure counts contribute to centre dashboard and audit.

### Notifications
Credential delivery remains Module 05 / F09-003; this feature does not re-send passwords by default.

### Security
Credential verification with lockout; session binding; centre scope for invigilator views; no password display in UI.

### Integrations
None.

### Dependencies
Modules 05 (credentials), F07-001, F07-002, F07-004, F07-006.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Browser/session hardening follows finally approved infrastructure choices.

### Risks
Credential sharing among candidates if invigilators do not verify identity (mitigated by F07-002 verification).
Abandoned sessions without clean release may block legitimate resume.

### Non Functional Requirements
Login path must remain available under exam-start surge; failed attempts are rate-limited without denying the whole centre.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Examination login screen | UI | Medium | 6 |
| Login validation feedback and denial | UI | Easy | 4 |
| Pre-start instructions and acknowledgement | UI | Medium | 6 |
| Concurrent session block notice | UI | Simple | 2 |
| Invigilator login attempt status panel | UI | Easy | 4 |
| Administrator login anomaly view | UI | Medium | 6 |
| Authenticate examination credentials | API | Complex | 8 |
| Validate centre session timing and activation for login | API | Complex | 8 |
| Bind candidate to authorised exam session | API | Complex | 8 |
| Enforce single active examination session | API | Complex | 8 |
| Record login attempt outcome | API | Medium | 6 |
| Load pre-start instructions | API | Easy | 4 |
| Search login attempts for centre | API | Medium | 6 |
| Release or expire abandoned login session | API | Medium | 6 |
| Exam login session and attempt entities | DB | Medium | 4 |
| Examination login at centre tests | Testing | Complex | 8 |
| Examination login at centre implementation documentation | Documentation | Medium | 3 |

**Feature total: 97 hours**
