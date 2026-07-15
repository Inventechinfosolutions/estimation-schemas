# F13-004 — Aadhaar eKYC Connector (Optional)

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F13-004 |
| **Feature Name** | Aadhaar eKYC Connector (Optional) |
| **Module** | 13 — API / Integration Hub |

### Description
OPTIONAL: perform consent-based Aadhaar eKYC verification for eligible citizen journeys, subject to BDA, legal, and provider approval.
### Business Objective
Improve identity-verification confidence where lawful and approved.
### Actors
- Citizen; authorized officer; Super Administrator; compliance user
### User Journey
1. Citizen starts an eligible verification journey and provides consent. 2. BHMS requests eKYC verification through the approved provider. 3. The verified/failed outcome is recorded for the owning process.
### Functional Capabilities
- Consent capture, eligible-purpose selection, verification outcome handling, controlled retry, and audit history.
### Inputs
- Citizen consent, verification purpose, provider challenge/outcome, and owning case reference.
### Outputs
- Verified/not-verified status, provider reference, and consent/outcome history.
### Business Rules
- eKYC does not replace baseline registration unless BDA formally approves the change.
### Validations
- Consent, eligible purpose, provider response, retry eligibility, and ownership of the target record.
### Calculations
- Verification outcome counts only.
### Workflow
- Consent → verification request → outcome → approved process handoff or manual fallback.
### Search Requirements
- By citizen, purpose, date, verification status, and exception.
### Documents
- Consent evidence and provider outcome evidence where permitted.
### Reports
- Optional eKYC volume and exception report.
### Notifications
- Verification success/failure notice through Module 12 where configured.
### Security
- RBAC, least-privilege access, protected sensitive values, and auditable activity.
### Integrations
- Aadhaar eKYC — Medium (16).
### Dependencies
- Modules 01 and 06–07; F13-002.
### Assumptions
- **OPTIONAL commercial line item**; manual identity/document process remains the baseline.
### Risks
- Legal, policy, provider, or consent requirements may prevent implementation.
### Non Functional Requirements
- No sensitive identity values in operational logs, protected consent, and complete auditability.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| eKYC consent and verification view | UI | Medium | 6 |
| eKYC verification outcome operations | API | Complex | 8 |
| Consent and verification state | Database | Easy | 2 |
| Aadhaar eKYC integration | Integration | Medium | 16 |
| eKYC connector tests | Testing | Complex | 8 |
| eKYC guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. **OPTIONAL commercial line item**; manual identity/document process remains the baseline.
