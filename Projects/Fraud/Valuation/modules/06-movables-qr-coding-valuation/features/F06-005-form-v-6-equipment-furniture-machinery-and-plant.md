# F06-005 — Form V-6 — equipment, furniture, machinery and plant

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Form V-6 — equipment, furniture, machinery and plant |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The Valuer completes V-6 (purpose, date, owners, description and purpose of plant, line-wise code, description, make, model/year, original and present market price, depreciation, market value) and declares personal inspection and no interest with digital signature (F05-010).

### Business Objective
Issue Form V-6 from tabulated movables with digital declaration.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer completes V-6 from tabulated equipment/furniture/machinery/plant rows (codes, make, model/year, original and present market price, depreciation, market value).
3. How they edit: Declares personal inspection and no interest with digital signature (F05-010).
4. How they send for approval: Declares personal inspection and no interest with digital signature (F05-010). Complete V-6 → sign (F05-010) → CA available.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Complete Form V-6 from eValueM tabulation
- Digital declaration via F05-010
- No generative drafting

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My form v-6 — equipment, furniture, machinery and plant list / queue | Medium |
| Form V-6 working | Complex |
| Form v-6 — equipment, furniture, machinery and plant history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| V-6 assemble | Complex |
| Update form v-6 — equipment, furniture, machinery and plant | Medium |
| Search form v-6 — equipment, furniture, machinery and plant | Medium |
| Read form v-6 — equipment, furniture, machinery and plant history | Easy |

### Inputs
V-6 fields; tabulated rows; digital signature.

### Outputs
Issued Form V-6.

### Business Rules
- Reads F06-001/F06-002 rather than re-keying codes/condition
- Unsigned cannot go to CA

### Validations
- Line-wise codes from tree
- Digital declaration present

### Calculations
Depreciation and present market value as entered/applied by the valuer on V-6.

### Workflow
Complete V-6 → sign (F05-010) → CA available.

### Search Requirements
Asset/seizure, Form V-6.

### Documents
Form V-6.

### Reports
Form V-6.

### Notifications
In-app if unsigned.

### Security
Assigned valuer.

### Integrations
F05-010 digital signature consume.

### Dependencies
F06-001; F06-002; F05-010; F07-001.

### Assumptions
- V-6 template from Annexure-01.

### Risks
Plant included on V-4 mines form instead of V-6.

### Non Functional Requirements
Issued snapshot.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My form v-6 — equipment, furniture, machinery and plant list / queue | UI | Medium | 6 |
| Form V-6 working | UI | Complex | 12 |
| Form v-6 — equipment, furniture, machinery and plant history | UI | Medium | 6 |
| V-6 assemble | API | Complex | 8 |
| Update form v-6 — equipment, furniture, machinery and plant | API | Medium | 6 |
| Search form v-6 — equipment, furniture, machinery and plant | API | Medium | 6 |
| Read form v-6 — equipment, furniture, machinery and plant history | API | Easy | 4 |
| Form v-6 — equipment, furniture, machinery and plant persistence | DB | Medium | 4 |
| Digital-declaration consume | Integration | Easy | 8 |
| Form V-6 — equipment, furniture, machinery and plant feature tests | Testing | Complex | 8 |
| Form V-6 — equipment, furniture, machinery and plant implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
