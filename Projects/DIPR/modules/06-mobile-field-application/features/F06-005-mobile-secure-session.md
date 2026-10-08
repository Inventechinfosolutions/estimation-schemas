# F06-005 — Mobile secure session

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-005 |
| Feature Name | Mobile secure session |
| Module | 06 — Mobile Field Application |
| Description | Secure login/session handling for field devices aligned to access policy |
| Business Objective | Protect field app access consistent with DIPR RBAC, optional MFA, and session policies. |
| Actors | Field Personnel; System; Admin |

### User Journey

- User authenticates on mobile → receives session → works within timeout → re-auth prompt on expiry or policy violation → logout clears local sensitive cache.

### Functional Capabilities

- Mobile login aligned to User & Access Management (Module 01)
- Token refresh and idle timeout handling
- Optional MFA step when enabled
- Device registration label for support
- Secure logout wiping queued secrets per policy

### Inputs

Credentials; MFA token when required; device identifier

### Outputs

Authenticated session scoped to field permissions

### Business Rules

Session length and lockout follow platform access policy
Failed login throttling aligned to Module 01

### Validations

- N/A

### Calculations

- None

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

Credentials not stored in plain text; TLS for all auth traffic; jailbreak/root detection if required by DIPR

### Integrations

Platform identity services (Module 01); optional SSO

### Dependencies

Module 01 User & Access Management

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Mobile login screen aligned to AMT branding | Easy | 4 |
| UI | Session timeout warning modal | Simple | 2 |
| UI | Re-authentication prompt on policy violation | Easy | 4 |
| UI | Secure logout confirmation clearing cache | Simple | 2 |
| API | Mobile login and token issuance | Medium | 6 |
| API | Token refresh on idle boundary | Easy | 4 |
| API | Device registration label submit | Easy | 4 |
| API | Secure logout and session revoke | Easy | 4 |
| Integration | Module 01 identity and MFA handoff | Medium | 16 |
| Integration | Optional SSO deep-link return handling | Easy | 8 |
| Database | Device session registration record | Simple | 1 |
| Testing | Session expiry and re-auth flow | Medium | 6 |
| Testing | Failed login throttle alignment | Medium | 6 |
| Testing | Logout clears sensitive local cache | Easy | 4 |
| Documentation | Mobile session policy notes | Easy | 2 |

**Feature Total: 73 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
