# F01-003 — Optional SSO integration

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F01-003 |
| Feature Name | Optional SSO integration |
| Module | 01 — User & Access Management |
| Description | Integrate with DIPR IdP (SAML/OIDC/LDAP as confirmed) when enabled for staff sign-in to AMT. |
| Business Objective | Allow DIPR to centralize identity for staff while keeping optional local accounts for vendors and field users if required. |
| Actors | DIPR Administrator; Staff User |

### User Journey

- Administrator enables SSO, enters IdP metadata and attribute mapping → Staff user clicks “Sign in with DIPR” → redirected to IdP → on success, AMT provisions or links user and applies roles from mapping rules → user lands on entitled home.

### Functional Capabilities

- SSO configuration screen (enable flag, protocol selection, endpoints, certificates)
- Attribute mapping (email, name, employee ID) to AMT user fields
- Just-in-time user link or create for mapped roles
- Fallback local login when SSO disabled or for excluded user types
- Error handling for IdP downtime and invalid assertions

### Inputs

- IdP metadata, client credentials, attribute map, default role mapping rules, enable/disable flag

### Outputs

- Federated session established; linked AMT user record
- SSO login success/failure audit events

### Business Rules

- SSO can be toggled without code change
- Vendor and field accounts may remain local-only per DIPR policy
- Deactivated AMT users cannot complete SSO login even if IdP succeeds

### Validations

- Valid certificate/metadata before enabling; required attributes present on assertion

### Calculations

- None

### Workflow

- Disabled → Configured → Enabled → Login via IdP → Session

### Search Requirements

- None (admin configuration)

### Documents

- IdP metadata upload

### Reports

- None

### Notifications

- None

### Security

- Signed assertions only; secure storage of secrets; no password stored for pure SSO users

### Integrations

- DIPR identity provider (SAML 2.0 / OIDC / LDAP as confirmed)

### Dependencies

- F01-001 User accounts; F01-002 Roles for mapping

### Assumptions

- DIPR provides test IdP and production metadata before UAT
- Protocol choice finalized in Phase 1

### Risks

- IdP attribute changes break JIT provisioning without coordination

### Non Functional Requirements

- SSO round-trip within acceptable login SLA; clear operator messaging on failure

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | SSO IdP configuration screen (metadata, certificates) | Medium | 6 |
| UI | IdP attribute-to-AMT field mapping grid | Medium | 6 |
| UI | Login page SSO entry and federation error states | Easy | 4 |
| UI | SSO link status panel on user profile | Simple | 2 |
| UI | JIT provision dry-run test panel | Medium | 6 |
| API | Initiate federated login (auth request) | Complex | 8 |
| API | Consume IdP callback and issue AMT session | Complex | 8 |
| API | JIT create or link user from IdP attributes | Medium | 6 |
| API | SSO configuration CRUD | Medium | 6 |
| API | Apply default role on first SSO login | Easy | 4 |
| Integration | IdP protocol adapter (auth, mapping, retry) | Medium | 16 |
| Database | SSO external identity link on user | Easy | 2 |
| Database | SSO configuration store | Simple | 1 |
| Testing | SSO happy-path login | Medium | 6 |
| Testing | Certificate expiry and invalid signature | Medium | 6 |
| Testing | Deactivated user blocked at SSO | Easy | 4 |
| Testing | JIT role assignment edge cases | Medium | 6 |
| Documentation | SSO setup runbook for DIPR IT | Easy | 2 |
| Documentation | UAT federation sign-off checklist | Easy | 2 |

**Feature Total: 101 hours**

### Estimation Assumptions

- One primary protocol implemented; additional protocol treated as configuration variant, not duplicate build.
- Full enterprise IAM replacement is out of scope.
