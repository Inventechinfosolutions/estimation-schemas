# F09-001 — Secure REST API gateway

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F09-001 |
| Feature Name | Secure REST API gateway |
| Module | 09 — Integration Hub |
| Description | Authenticated REST APIs for agreed AMT data exchange |
| Business Objective | Expose documented, authenticated APIs for authorized exchange of AMT data with DIPR systems. |
| Actors | Integration Developer; External system; Admin |

### User Journey

- Admin registers API client → client obtains token → calls agreed resources → gateway validates authZ → returns payload → call audited.

### Functional Capabilities

- Authenticated access to agreed resources (campaigns, assets, PoD status, masters as scoped)
- Rate limiting and request auditing
- Versioned API surface documented for DIPR
- Sandbox mode when test environment provided

### Inputs

Client credentials; resource identifiers; payloads per agreed contract

### Outputs

JSON responses; audit entries

### Business Rules

Deny-by-default; scopes mapped to client registration
Only agreed fields exposed externally

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

TLS; token-based auth; scope-limited clients

### Integrations

- None

### Dependencies

Module 01; Module 10 encryption controls

### Assumptions

- Requirements as per SoW_AMT_Detailed.md

### Risks

- Scope clarification with DIPR during requirements

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | API client register form | Easy | 4 |
| UI | Client scope assignment matrix | Medium | 6 |
| UI | Client secret rotate confirmation | Simple | 2 |
| API | External campaign read resource handler | Complex | 8 |
| API | External PoD status read resource handler | Complex | 8 |
| API | External vendor assignment read handler | Medium | 6 |
| API | Client credentials token exchange | Complex | 8 |
| Integration | Gateway rate limiting middleware | Medium | 16 |
| Integration | OAuth2/client credential auth middleware | Medium | 16 |
| Database | API client registry | Medium | 4 |
| Database | Issued token metadata | Easy | 2 |
| Testing | AuthZ scope negative tests | Complex | 8 |
| Testing | Rate limit breach response | Medium | 6 |
| Testing | Contract smoke for agreed entities | Complex | 8 |
| Documentation | External API consumer guide | Complex | 4 |
| Documentation | Client onboarding checklist | Easy | 2 |

**Feature Total: 108 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
