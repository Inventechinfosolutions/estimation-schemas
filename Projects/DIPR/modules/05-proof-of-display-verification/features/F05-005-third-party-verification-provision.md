# F05-005 — Third-party verification provision

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-005 |
| Feature Name | Third-party verification provision |
| Module | 05 — Proof-of-Display Capture & Verification |
| Description | Integrate optional third-party verification when DIPR provides APIs and credentials for external PoD validation services. |
| Business Objective | Allow DIPR to augment manual verification with an external provider without forking core PoD storage. |
| Actors | DIPR Administrator; PoD Verifier; Integration support |

### User Journey

- Administrator configures third-party connector endpoints and credentials → on accepted/manual pending PoD, operator triggers or auto-submits to provider → async callback or polling updates external status on PoD → verifier sees external badge alongside manual decision → campaign rollup includes external outcome when present.

### Functional Capabilities

- Connector settings screen (enable, base URL, auth, mapping)
- Outbound submit of PoD reference and media pointer per provider contract
- Inbound callback or polling handler for status and score/reason
- External verification status badge on PoD and register
- Manual retry and dead-letter view for failed submissions
- Reconciliation list of in-flight external requests

### Inputs

- Provider credentials, submit triggers, callback payloads

### Outputs

- External verification reference, status, timestamps on PoD

### Business Rules

- Feature disabled until DIPR names provider and supplies test credentials
- External outcome informative unless DIPR policy makes it binding
- No PoD binary sent if policy requires on-prem-only; configurable

### Validations

- Credential test button before enable

### Calculations

- None

### Workflow

- Submit → pending external → completed/failed → optional manual verify still required

### Search Requirements

- Filter register by external status

### Documents

- Provider response payload stored as audit attachment (metadata)

### Reports

- External vs manual outcomes in Module 07

### Notifications

- Alert on external failure (Module 08)

### Security

- Secrets vaulted; outbound TLS; PII minimization per DIPR guidance

### Integrations

- Third-party verification API (provider TBD by DIPR)

### Dependencies

- F05-001 PoD records; Module 09 may host shared connector patterns

### Assumptions

- One primary provider interface in baseline; adapter pattern for others

### Risks

- Provider API delay blocks UAT until DIPR contract signed

### Non Functional Requirements

- Async processing; no blocking verifier UI on outbound calls

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Third-party verifier organisation register | Medium | 6 |
| UI | API credential issue and revoke panel | Medium | 6 |
| UI | Outbound PoD queue for external verification | Easy | 4 |
| UI | External status webhook monitor dashboard | Medium | 6 |
| UI | Manual reconcile external decision screen | Medium | 6 |
| API | Register third-party verifier client | Medium | 6 |
| API | Push PoD package to external verifier | Complex | 8 |
| API | Receive callback/webhook verification decision | Complex | 8 |
| API | Reconcile conflicting internal/external decisions | Medium | 6 |
| API | Rotate third-party API credentials | Easy | 4 |
| Integration | External verifier REST adapter (auth, mapping) | Medium | 16 |
| Database | External verifier client registry | Easy | 2 |
| Database | Outbound/inbound integration message log | Medium | 4 |
| Testing | Push and callback happy path | Complex | 8 |
| Testing | Auth failure and retry behaviour | Medium | 6 |
| Testing | Reconcile with internal manual verify | Medium | 6 |
| Documentation | Third-party verification integration runbook | Medium | 3 |

**Feature Total: 105 hours**

### Estimation Assumptions

- Provider licensing fees and their product UI are out of scope; AMT provides provision only.
