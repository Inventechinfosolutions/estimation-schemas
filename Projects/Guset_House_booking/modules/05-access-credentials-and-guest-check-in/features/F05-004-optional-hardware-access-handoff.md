# F05-004 — Optional Hardware Access Handoff

| Field | Value |
|-------|-------|
| Feature ID | F05-004 |
| Feature Name | Optional Hardware Access Handoff |
| Module | 05 — Access Credentials & Guest Check-in |
| Type | Business |
| Notes | OPTIONAL / conditional |

## Feature Specification

### Description
Where supported, presents booking credentials to access-control hardware for automated door access.

### Business Objective
Enable automated entry at equipped sites without making hardware mandatory everywhere.

### Actors
- System
- Site Administrator
- Employee Guest

### User Journey
1. Administrator enables hardware mode for a site when adapter configured.
2. On credential issuance/check-in, system pushes or validates credential with hardware adapter.
3. Admin may disable hardware mode; fallback to QR/manual key.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Admin sees hardware sync status per booking/site.
8. Auditor sees hardware enablement and sync errors.

### Functional Capabilities
- Enable hardware per site
- Sync credential to hardware
- Revoke credential on cancel/regenerate
- Show sync status
- Fallback messaging

### UI Screens
- Site hardware enablement screen
- Hardware sync status panel
- Sync failure alert dialog

### Logical API Operations
- Enable site hardware mode
- Sync credential to hardware
- Revoke hardware credential
- Get hardware sync status

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Only sites with adapter config
- Failure must not block core booking
- Revoke on cancel/regenerate

### Validations
- Hardware endpoint configured

### Calculations
- None beyond display counters

### Workflow
SiteHardwareEnabled → CredentialSynced | SyncFailed

### Search Requirements
Filter sync failures

### Documents
Site IT setup notes

### Reports
None

### Notifications
Alert admin on persistent sync failure

### Security
- Secure adapter credentials
- Least privilege

### Integrations
F08-003

### Dependencies
- F05-001
- F08-003

### Assumptions
- Hardware protocols vary; adapter abstracts vendor

### Risks
- Vendor lock-in / flaky devices

### Non Functional Requirements
- Sync async with retry

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Site hardware enablement screen | Medium | 6 |
| UI | Hardware sync status panel | Medium | 6 |
| UI | Sync failure alert dialog | Simple | 2 |
| API | Enable site hardware mode | Medium | 6 |
| API | Sync credential to hardware | Very High | 16 |
| API | Revoke hardware credential | Complex | 8 |
| API | Get hardware sync status | Easy | 4 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Complex | 4 |

**Feature Total: 62 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Hardware protocols vary; adapter abstracts vendor / Vendor lock-in / flaky devices.
