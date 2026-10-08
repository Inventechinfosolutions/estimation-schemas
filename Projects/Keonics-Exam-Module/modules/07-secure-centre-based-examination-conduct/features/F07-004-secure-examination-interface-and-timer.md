# F07-004 — Secure Examination Interface and Timer

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | Secure Examination Interface and Timer |
| **Module** | 07 — Secure Centre-Based Examination Conduct |

### Description
Deliver the secure computer-based test interface: randomised paper version presentation, question text and options, next/previous and palette navigation, answered/unanswered status, continuous auto-save of responses, and a central server-authoritative timer that auto-stops and auto-submits on expiry, with controlled resume after brief interruption under centre session rules.

### Business Objective
Provide a reliable, fair, centre-only CBT experience with consistent timing and no loss of saved answers before lock/submit.

### Actors
- Candidate at centre (answers within the interface)
- Invigilator (monitors status; does not alter answers)
- Examination Administrator (investigates timer/session exceptions)
- Auditor (interface and timer event history via F07-006)

### User Journey
1. Who creates: After successful centre login (F07-003), the system creates the candidate’s live examination attempt workspace bound to their assigned paper version/order from Module 06; the candidate creates answers by selecting options.
2. How they create: Secure interface loads assigned version → candidate navigates questions → selects/clears options → responses auto-save → watches remaining time from central timer → on expiry system auto-submits; or candidate proceeds to manual submit (F07-005).
3. How they edit: Candidate may change answers until submit or auto-submit lock; each change auto-saves. Invigilators and administrators cannot edit candidate responses through this UI.
4. How they send for approval: Does not apply to answering. Manual submit confirmation is F07-005; timer expiry auto-submit is system-initiated without approval.
5. How the approver sees pending items: No approver inbox for answering. Invigilators see active/time-remaining status on the centre monitor (F07-002).
6. How the approver decides: No approval decision on answers.
7. How the applicant / maker sees history: Candidate sees answered/unanswered palette and last auto-save indicator during the attempt; after lock, answers are read-only via result flows (Module 08), not re-editable here.
8. How the approver / auditor sees history: Administrators/auditors review timer events, auto-save markers, resume events and navigation anomalies through activity recording (F07-006) and centre status.

### Functional Capabilities
- Secure CBT workspace showing question text and options for the assigned randomised version/order
- Next/previous navigation and question palette jump
- Answered / unanswered / not-visited status indicators
- Continuous auto-save of selected responses
- Central authoritative timer (not solely client clock) with remaining time display
- Time-expiry warning and auto-stop with auto-submit of last saved responses
- Block further answer changes after expiry/auto-submit
- Controlled reconnect/resume of interrupted session under approved rules without granting extra time beyond central clock
- Heartbeat / session keep-alive to detect abandoned clients
- Exam instructions overlay accessible without granting extra answering time beyond rules
- Prevent opening interface without valid centre session binding

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Secure CBT question workspace | Very High |
| Question navigation palette | Complex |
| Answered / unanswered status panel | Medium |
| Central timer and remaining-time display | Complex |
| Auto-save status indicator | Easy |
| Time-expiry warning dialog | Easy |
| Reconnect / resume examination screen | Complex |
| Examination instructions overlay | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Load assigned paper version for attempt | Complex |
| Fetch question by navigation index | Medium |
| Auto-save candidate response | Complex |
| Sync remaining time from central timer | Very High |
| Update answered / unanswered palette state | Medium |
| Auto-submit on timer expiry | Very High |
| Resume interrupted examination session | Complex |
| Session heartbeat keep-alive | Medium |
| Load navigation palette state | Medium |
| Load examination instructions for attempt | Easy |

### Inputs
Active exam session binding, navigation actions, selected option(s), client heartbeat, resume request.

### Outputs
Persisted responses (pre-lock), palette state, remaining time, auto-submit trigger to F07-005 lock path, resume state.

### Business Rules
- Paper content comes from Module 06 version assignment; candidate cannot choose version.
- Timer is central; client display is informational relative to server remaining time.
- On expiry, last saved responses are auto-submitted and further answers are blocked.
- Auto-save must not unlock a locked attempt.
- Resume must not reset the central timer or grant additional duration.
- Multiple simultaneous interfaces for the same attempt are prevented.
- Browser/session controls follow finally approved infrastructure hardening.

### Validations
- Session must be active, activated and within centre gate
- Response save rejected after lock/expiry
- Navigation limited to questions in the assigned paper
- Heartbeat failure follows approved timeout/resume policy

### Calculations
Remaining time = scheduled duration − elapsed central time (subject to approved pause rules, if any — default none).

### Workflow
Load paper → answer with auto-save → timer runs → either manual submit (F07-005) or auto-submit on expiry → lock. No approval.

### Search Requirements
Staff search of active attempts by centre/session is on F07-002; this feature focuses on the candidate workspace.

### Documents
None; questions/options are examination content, not downloadable documents during attempt.

### Reports
None owned; attempt timing feeds activity and evaluation.

### Notifications
None during answering (avoid distraction); staff alerts remain F09-003 if configured for anomalies.

### Security
Centre session binding required; no copying aids beyond approved lockdown; responses attributable to candidate attempt; staff cannot alter answers.

### Integrations
None.

### Dependencies
Modules 06 (paper versions), F07-001–F07-003, F07-005 (submit/lock), F07-006 (events), F08-001 (consumes locked responses).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Secure CBT workspace and central timer sync are Very High effort.
- Subjective/descriptive answering is out of scope.

### Risks
Client clock manipulation if central sync is weak.
Network drops during auto-save causing candidate distress (mitigated by resume and last-saved guarantee).

### Non Functional Requirements
Auto-save latency suitable for rapid option changes; timer sync accurate under concurrent centre load; interface usable on approved centre workstation browsers.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Secure CBT question workspace | UI | Very High | 16 |
| Question navigation palette | UI | Complex | 12 |
| Answered / unanswered status panel | UI | Medium | 6 |
| Central timer and remaining-time display | UI | Complex | 12 |
| Auto-save status indicator | UI | Easy | 4 |
| Time-expiry warning dialog | UI | Easy | 4 |
| Reconnect / resume examination screen | UI | Complex | 12 |
| Examination instructions overlay | UI | Medium | 6 |
| Load assigned paper version for attempt | API | Complex | 8 |
| Fetch question by navigation index | API | Medium | 6 |
| Auto-save candidate response | API | Complex | 8 |
| Sync remaining time from central timer | API | Very High | 16 |
| Update answered / unanswered palette state | API | Medium | 6 |
| Auto-submit on timer expiry | API | Very High | 16 |
| Resume interrupted examination session | API | Complex | 8 |
| Session heartbeat keep-alive | API | Medium | 6 |
| Load navigation palette state | API | Medium | 6 |
| Load examination instructions for attempt | API | Easy | 4 |
| Attempt response and timer state entities | DB | Complex | 6 |
| Secure examination interface and timer tests | Testing | Very High | 12 |
| Secure examination interface and timer implementation documentation | Documentation | Complex | 4 |

**Feature total: 178 hours**
