# F07-001 — Authorised Centre Access Enforcement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Authorised Centre Access Enforcement |
| **Module** | 07 — Secure Centre-Based Examination Conduct |

### Description
Gate every examination start so that only a registered, eligible candidate at their allotted authorised centre, on an authorised computer/network during an active scheduled session, after invigilator activation and without a prior completion, can enter the CBT. Deny home, personal device, wrong centre, wrong city/network, inactive session and unauthorised workstation attempts with attributable denial records.

### Business Objective
Uphold the Department’s centre-only CBT policy so examinations cannot be taken from unauthorised locations, devices or centres.

### Actors
- Invigilator / Centre user (initiates gate checks when seating a candidate)
- Candidate at centre (subject of access checks; cannot bypass)
- Examination Administrator (reviews denial patterns)
- Auditor (reads denial and environment evidence)

### User Journey
1. Who creates: The system creates an access-gate decision when an invigilator or candidate attempts to open an examination session for a given registration, centre and schedule slot; invigilators trigger the check from the centre console; unattended remote attempts create denial records only.
2. How they create: Invigilator selects the candidate (or candidate presents exam credentials after seating). The gate validates allocation, schedule window, centre identity, authorised environment signals, session activation and completion status, then allows or denies entry.
3. How they edit: Gate rules and authorised-centre bindings are maintained in masters (Module 03) and activation (F07-002); this feature does not edit registrations. Invigilators may re-run the gate after correcting seating, activation or environment issues.
4. How they send for approval: Submit/approval does not apply — access is an automated allow/deny decision, not a maker–checker document.
5. How the approver sees pending items: There is no approver inbox. Administrators see a denial register and failed-gate queue for operational follow-up.
6. How the approver decides: There is no approval decision on this feature. Only an Administrator may later review denials; they cannot override “already completed” or wrong-centre denials without changing underlying allocation/session data elsewhere.
7. How the applicant / maker sees history: Invigilators see per-candidate gate results and recent denials for their centre; candidates see only a clear denial message (no internal rule codes).
8. How the approver / auditor sees history: Examination Administrator and auditors search denial events by centre, examination, date, reason code and actor, with environment metadata retained for investigation.

### Functional Capabilities
- Pre-start validation chain: registration eligibility, centre allotment match, scheduled date/time window, centre and session active, invigilator activation present, not already completed
- Authorised environment enforcement: deny home/personal device/other network/city, wrong centre, unauthorised computer; allow only authorised computer at allotted centre
- Explicit deny messaging for each failure class without leaking sensitive internals to the candidate
- Attributable recording of every allow and deny with centre, session, device/network signals where available
- Centre-scoped visibility of denials for invigilators; cross-centre search for administrators
- Block examination start until all gate checks pass
- Support re-check after invigilator activation or environment remediation
- Align with finally approved IP/device/browser controls without shrinking centre-only scope

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Pre-exam access gate checklist | Complex |
| Access denial notice (candidate/invigilator) | Easy |
| Centre environment status panel | Medium |
| Unauthorised attempt denial register | Medium |
| Administrator denial investigation view | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Validate candidate eligibility and completion status | Complex |
| Validate centre allocation match | Complex |
| Validate schedule window and session active | Medium |
| Validate authorised environment | Complex |
| Evaluate full access gate decision | Complex |
| Record access allow or denial | Medium |
| Search denial register | Medium |
| Load environment status for workstation | Easy |

### Inputs
Candidate registration / exam credential context, allotted centre, schedule/session identifiers, invigilator activation state, workstation/environment signals (as finally approved), attempt timestamp, actor identity.

### Outputs
Allow or deny decision with reason class, denial register entries, environment status snapshot for the attempt, auditor-readable history.

### Business Rules
- Examination start is denied unless all of: registered and eligible; allotted to this centre; within scheduled date/time; authorised system/network/device; centre and session active; invigilator-validated/activated; not already completed.
- Home, personal device, other network/city, wrong centre and unauthorised computer attempts are always denied.
- Centre users see only their centre’s denial and gate data; administrators may see all centres.
- Exact IP/device/browser mechanism is finalised with Department/infrastructure; the business rule remains centre-only CBT.
- Passing the gate does not itself start timing; login and interface features consume the allow decision.

### Validations
- Required identifiers present before gate evaluation
- Session not outside schedule window
- Environment signals present when the approved model requires them
- Denial reason always recorded when access is refused

### Calculations
None beyond pass/fail of discrete gate conditions.

### Workflow
No maker–checker approval. Linear gate evaluation → allow (hand off to F07-003/F07-004) or deny (stop with message and audit).

### Search Requirements
Denial register by centre, examination, date/time range, reason class, candidate registration number, workstation identifier.

### Documents
None generated; may display hall-ticket centre name for confirmation only.

### Reports
Denial counts feed centre day views (F07-002) and admin MIS (Module 09); this feature owns the denial register screen.

### Notifications
Optional staff alert on repeated denials is owned by F09-003 if configured; not required to complete the gate.

### Security
Centre-scoped invigilator access; administrator investigation access; candidates cannot view other candidates’ denials; environment metadata restricted to staff/auditor roles.

### Integrations
None as a separate channel; consumes centre/session masters and activation state from sibling features.

### Dependencies
Modules 01 (staff/centre scope), 03 (centre/session masters), 05 (allocation/schedule/credentials), F07-002 (activation), F07-006 (activity recording of denials).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Device/IP binding product choice is configuration, not a new hardware procurement estimate.
- Multiple simultaneous sessions are blocked in concert with F07-003.

### Risks
Weak network/device controls at centres can undermine enforcement even if software gates are correct.
Misconfigured centre–workstation mapping causes false denials and exam-day disruption.

### Non Functional Requirements
Gate evaluation completes within interactive time on exam-day concurrency; every decision is attributable and retained for the Department’s audit retention period.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Pre-exam access gate checklist | UI | Complex | 12 |
| Access denial notice (candidate/invigilator) | UI | Easy | 4 |
| Centre environment status panel | UI | Medium | 6 |
| Unauthorised attempt denial register | UI | Medium | 6 |
| Administrator denial investigation view | UI | Complex | 12 |
| Validate candidate eligibility and completion status | API | Complex | 8 |
| Validate centre allocation match | API | Complex | 8 |
| Validate schedule window and session active | API | Medium | 6 |
| Validate authorised environment | API | Complex | 8 |
| Evaluate full access gate decision | API | Complex | 8 |
| Record access allow or denial | API | Medium | 6 |
| Search denial register | API | Medium | 6 |
| Load environment status for workstation | API | Easy | 4 |
| Access gate and denial entities | DB | Complex | 6 |
| Authorised centre access enforcement tests | Testing | Complex | 8 |
| Authorised centre access enforcement implementation documentation | Documentation | Medium | 3 |

**Feature total: 111 hours**
