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
1. Who creates: Officer
2. How they create: Officer triggers Aadhaar verification through the existing online service and records PAN verification.
3. How they edit: Until Aadhaar verification succeeds, Officer cannot treat Aadhaar name or Aadhaar-linked mobile as identity proof.
4. How they send for approval: Unverified capture remains visible as unverified only. Trigger verify → record result → proof-eligibility. Human confirmation of the recorded result.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer proceeds with other proofs if Aadhaar remains unverified.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Trigger Aadhaar verification via the existing online service.
- Record PAN verification.
- Block treating unverified Aadhaar name or Aadhaar-linked mobile as identity proof.
- Show unverified capture as unverified only.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Aadhaar/PAN verification panel | Medium |
| Unverified-not-proof banner | Easy |
| Aadhaar and pan verification history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Verification recording operations | Complex |
| Update aadhaar and pan verification | Medium |
| Search aadhaar and pan verification | Medium |
| Read aadhaar and pan verification history | Easy |

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
| Aadhaar and pan verification history | UI | Medium | 6 |
| Verification recording operations | API | Complex | 8 |
| Update aadhaar and pan verification | API | Medium | 6 |
| Search aadhaar and pan verification | API | Medium | 6 |
| Read aadhaar and pan verification history | API | Easy | 4 |
| Verification status persistence | DB | Medium | 4 |
| Existing Aadhaar online verification service | Integration | Complex | 24 |
| Aadhaar and PAN verification feature tests | Testing | Very High | 12 |
| Aadhaar and PAN verification implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **84** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
