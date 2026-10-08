# F08-003 — Access-Control Hardware Adapter

| Field | Value |
|-------|-------|
| Feature ID | F08-003 |
| Feature Name | Access-Control Hardware Adapter |
| Module | 08 — Integration Hub |
| Type | Technical |
| Notes | OPTIONAL / conditional |

## Feature Specification

### Description
Optional adapter enabling automated door access integration at equipped sites.

### Business Objective
Connect booking credentials to on-site access hardware without blocking unequipped sites.

### Actors
- Platform Administrator
- System

### User Journey
1. Administrator configures hardware endpoint for a site.
2. System syncs/revokes credentials through adapter when enabled.
3. Admin disables adapter per site.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Admin sees adapter logs.
8. Auditor sees enablement history.

### Functional Capabilities
- Per-site hardware config
- Sync credential
- Revoke credential
- Test connectivity
- Error log

### UI Screens
- Hardware adapter configuration screen
- Hardware connectivity test dialog
- Hardware adapter error log

### Logical API Operations
- Save hardware config
- Adapter sync credential
- Adapter revoke credential
- Test hardware connectivity

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Optional — sites without config unaffected
- Failures isolated

### Validations
- Endpoint URL/creds when enabling

### Calculations
- None beyond display counters

### Workflow
Disabled → Enabled → Syncing

### Search Requirements
Error log by site

### Documents
Vendor mapping notes

### Reports
None

### Notifications
Failure alerts optional

### Security
- Site-scoped secrets

### Integrations
Access-control hardware

### Dependencies
- None

### Assumptions
- Vendor protocol clarified at implementation

### Risks
- Multiple incompatible vendors

### Non Functional Requirements
- Async sync with retry

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Hardware adapter configuration screen | Complex | 12 |
| UI | Hardware connectivity test dialog | Easy | 4 |
| UI | Hardware adapter error log | Medium | 6 |
| API | Save hardware config | Medium | 6 |
| API | Adapter sync credential | Very High | 16 |
| API | Adapter revoke credential | Complex | 8 |
| API | Test hardware connectivity | Medium | 6 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Integration | External channel adapter work | Complex | 24 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Complex | 4 |

**Feature Total: 96 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Vendor protocol clarified at implementation / Multiple incompatible vendors.
