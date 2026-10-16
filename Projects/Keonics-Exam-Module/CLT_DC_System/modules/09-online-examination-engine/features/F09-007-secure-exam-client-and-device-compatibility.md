# F09-007 — Secure Exam Client & Device Compatibility

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-007 |
| Feature Name | Secure Exam Client & Device Compatibility |
| Module | 09 — Online Examination Engine |
| Module Type | Business |
| Release | Go-live |

### Description
Secure exam client (lockdown browser / kiosk mode) for centre terminals on Windows, Linux and macOS: full-screen lock, blocking of other applications, shortcuts, print screen, clipboard and virtual machines; terminal registration; version enforcement; screen and webcam capture hooks for proctoring; and a hardened browser mode for supported browsers where the client cannot be installed.

### Business Objective
Provide device and OS agnostic delivery with strong exam security.

### Actors
- Centre Operator
- Candidate
- Service Provider operations

### User Journey
1. **Who creates:** The centre operator installs and registers the client on terminals.
2. **How they create:** Terminals register with centre and IP; readiness reports version.
3. **How they edit:** Updates are pushed centrally; old versions blocked.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Operations see terminal versions.
6. **How the approver decides:** Operations block or allow versions.
7. **How the applicant / maker sees history:** Candidates use the locked client.
8. **How the approver / auditor sees history:** Auditors see client events (user_agent ExamBrowser per Annexure 9).

### Functional Capabilities
- Full-screen kiosk lock
- Application and shortcut blocking
- Clipboard, print-screen and VM detection
- Terminal registration
- Version enforcement and auto-update
- Proctoring capture hooks
- Hardened browser fallback
- Multi-OS builds

### UI Screens
- Client launcher and registration
- Client status / error screens
- Terminal version console

### Logical API Operations
- Register terminal
- Version check and update
- Client integrity attestation
- Client event logging

### Inputs
- Terminal details

### Outputs
- Registered locked terminals

### Business Rules
- Tests only through registered client or approved browser mode

### Validations
- Client signature

### Calculations
- None

### Workflow
Unregistered → Registered → Active

### Search Requirements
- Terminals

### Documents
- None

### Reports
- Terminal versions

### Notifications
- Outdated client alerts

### Security
- Signed binaries; integrity attestation

### Integrations
- OS APIs

### Dependencies
- F02-002
- F10-001
- F10-003

### Assumptions
- Centres allow client installation

### Risks
- OS updates breaking lockdown

### Non Functional Requirements
- Client start under 10 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Client launcher and registration | Medium | 6 |
| UI | Client status / error screens | Easy | 4 |
| UI | Terminal version console | Easy | 4 |
| API | Register terminal | Medium | 6 |
| API | Version check and update | Medium | 6 |
| API | Client integrity attestation | Complex | 8 |
| API | Client event logging | Medium | 6 |
| Database | Terminal and client version registry | Easy | 2 |
| Integration | Operating system lockdown integration (Windows, Linux, macOS) | Very High | 40 |
| Testing | Lockdown and escape tests per OS | Very High | 12 |
| Testing | Compatibility tests | Complex | 8 |
| Documentation | Client installation guide | Medium | 3 |
| Documentation | Supported configuration matrix | Easy | 2 |

**Feature Total: 107 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 26 | 2 | 40 | 20 | 5 | **107** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Multi-OS lockdown rated Very High
