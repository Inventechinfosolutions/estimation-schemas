# F10-009 — Aadhaar eKYC Connector (Optional)

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-009 |
| **Feature Name** | Aadhaar eKYC Connector (Optional) |
| **Module** | 10 — API / Integration Hub |

### Description
Optional Aadhaar eKYC integration subject to legal/BDA approval, to verify tenant identity and populate KYC attributes with compliance controls.

### Business Objective
Strengthen tenant onboarding KYC where legally permitted.

### Actors
- Estate officers, Tenants (consent), Tech admin, Compliance

### User Journey
1. During tenant registration, initiate eKYC with consent.
2. Hub completes provider flow; returns verified attributes.
3. Module 04 stores permitted fields; evidence refs in DMS.

### Functional Capabilities
- eKYC session start/complete
- Consent capture & audit
- Attribute mapping to tenant profile
- Failure/fallback to manual KYC

### Inputs
- Consent; Aadhaar reference as legally allowed (never store full Aadhaar unprotected)

### Outputs
- Verified name/KYC flags; evidence vault refs

### Business Rules
- Subject to legal approval; optional.
- Follow UIDAI/MeitY guidelines; mask Aadhaar display (Module 01/04).
- Manual KYC remains baseline.

### Validations
- Consent mandatory; purpose limitation

### Calculations
None.

### Workflow
Consent → eKYC → Map → Store flags.

### Search Requirements
Ops search sessions by status/date (no Aadhaar search).

### Documents
Compliance design pack.

### Reports
eKYC success/fail counts.

### Notifications
Result to officer/tenant.

### Security
Highest sensitivity; encryption; no Aadhaar in logs; strict retention.

### Integrations
Aadhaar eKYC — **Complex (24)** Multi-system + compliance.

### Dependencies
F10-001; Modules 01, 04, 08

### Assumptions
- ASA/AUA or eligible channel determined by BDA legal.
- Testing Very High for compliance scenarios.

### Risks
- Regulatory rejection voids feature—keep optional.
- Estimate provisional until partner selected.

### Non Functional Requirements
- Hardened session security; short TTL

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| eKYC initiation UX hooks | UI | Medium | 6 |
| eKYC facade & result handling | API | Complex | 8 |
| eKYC session entities | Database | Medium | 4 |
| Aadhaar eKYC integration | Integration | Complex | 24 |
| eKYC connector tests | Testing | Very High | 12 |
| eKYC compliance guide | Documentation | Complex | 4 |
| **Total** | | | **58** |

### Estimation Assumptions
- Optional; do not include in mandatory go-live sum unless approved.
