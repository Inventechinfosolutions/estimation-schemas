# F04-009 — Aadhaar and PAN verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-009 |
| **Feature Name** | Aadhaar and PAN verification |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer triggers Aadhaar verification through the existing online service and records PAN verification. Until Aadhaar verification succeeds, the Officer cannot treat Aadhaar name or Aadhaar-linked mobile as identity proof. Unverified capture remains visible as unverified only.

### Business Objective
Require existing online Aadhaar verification (and PAN verification) before Aadhaar is relied on as identity proof.

### Actors
Officer; auditor (sees unverified versus verified status).

### User Journey
1. Officer triggers Aadhaar verification through the existing online service and records PAN verification.
2. Until Aadhaar verification succeeds, Officer cannot treat Aadhaar name or Aadhaar-linked mobile as identity proof.
3. Unverified capture remains visible as unverified only.
4. Officer proceeds with other proofs if Aadhaar remains unverified.

### Functional Capabilities
- Trigger Aadhaar verification via the existing online service.
- Record PAN verification.
- Block treating unverified Aadhaar name or Aadhaar-linked mobile as identity proof.
- Show unverified capture as unverified only.

### Inputs
Aadhaar number/reference, PAN, existing-service result, PAN verification result.

### Outputs
Verified/unverified flags on the profile; proof-eligibility status.

### Business Rules
- Unverified Aadhaar is not treated as identity proof.
- Capture of Aadhaar and PAN without verification is not sufficient.
- Aadhaar-linked mobile is not proof until Aadhaar verification succeeds.

### Validations
- Verification result must be stored before “verified” is shown.
- UI must not present unverified Aadhaar as a green proof tick.

### Calculations
None.

### Workflow
Trigger verify → record result → proof-eligibility. Human confirmation of the recorded result.

### Search Requirements
Verified / unverified Aadhaar or PAN status on the depositor.

### Documents
Service result artefacts as available.

### Reports
Unverified-Aadhaar still-in-use exception list.

### Notifications
On-screen unverified banner.

### Security
Aadhaar/PAN handling per official rules. Verification events audited.

### Integrations
Aadhaar online verification (existing service); PAN verification to be provided.

### Dependencies
F04-003 capture; F04-005 tally must honour unverified status.

### Assumptions
- Existing Aadhaar online verification service is available to the Authority.
- PAN verification channel will be provided.

### Risks
- Treating unverified Aadhaar as proof would break SOW acceptance criterion 14 and website-review item 5.

### Non Functional Requirements
Unverified state must be unmistakable on staff screens.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Aadhaar/PAN verification panel | UI | Medium | 6 |
| Unverified-not-proof banner | UI | Easy | 4 |
| Verification recording operations | API | Complex | 8 |
| Verification status persistence | DB | Medium | 4 |
| Existing Aadhaar online verification service | Integration | Complex | 24 |
| Aadhaar/PAN verification tests | Testing | Very High | 12 |
| Aadhaar/PAN verification guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Complex is the existing Aadhaar service plus PAN verification recording, not a new UIDAI product build.
- Testing Very High because the unverified-not-proof rule must not be bypassed.
