# F06-006 — Form V-7 — gemstones, precious metals and jewellery

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-006 |
| **Feature Name** | Form V-7 — gemstones, precious metals and jewellery |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The Valuer completes V-7 (item description, unit, gross/net weight, stone and metal values, special enhancement, explanation of rates, purity-testing methods actually adopted from the FRS list: digital weighing, XRF/touchstone, diamond loupe/CVD, gemstone loupe) and Sub-Annexures I and II. Declaration of personal inspection and no interest with digital signature (F05-010) is required.

### Business Objective
Issue Form V-7 with recorded purity-testing methods and sub-annexures, digitally declared.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer completes V-7 including weights, stone and metal values, special enhancement, explanation of rates, and purity-testing methods actually adopted (digital weighing, XRF/touchstone, diamond loupe/CVD, gemstone loupe).
3. How they edit: Completes Sub-Annexures I and II.
4. How they send for approval: Declares personal inspection and no interest with digital signature (F05-010). Complete V-7 + sub-annexures → sign → CA available.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Form V-7 with stone/metal values and rate explanation
- Record purity-testing methods actually adopted from the FRS list
- Sub-Annexures I and II
- Digital declaration F05-010

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My form v-7 — gemstones, precious metals and jewellery list / queue | Medium |
| Form V-7 working | Very High |
| Form v-7 — gemstones, precious metals and jewellery history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| V-7 and sub-annexure assemble | Very High |
| Update form v-7 — gemstones, precious metals and jewellery | Medium |
| Search form v-7 — gemstones, precious metals and jewellery | Medium |
| Read form v-7 — gemstones, precious metals and jewellery history | Easy |

### Inputs
V-7 fields; methods adopted; sub-annexures; digital signature.

### Outputs
Issued Form V-7 with sub-annexures.

### Business Rules
- Methods are those actually adopted, not a generated list
- No generative AI

### Validations
- At least one purity-testing method recorded
- Sub-annexures complete as FRS requires
- Digital declaration

### Calculations
Stone/metal values and totals as entered/applied by the valuer.

### Workflow
Complete V-7 + sub-annexures → sign → CA available.

### Search Requirements
Seizure, Form V-7.

### Documents
Form V-7; Sub-Annexures I and II.

### Reports
Form V-7.

### Notifications
In-app if methods or signature missing.

### Security
Assigned valuer; jewellery values need-to-know.

### Integrations
F05-010 consume.

### Dependencies
F06-001; F06-002; F05-010.

### Assumptions
- FRS purity-testing list is the allowed set.

### Risks
Claiming methods not actually used.

### Non Functional Requirements
Methods stored on the issued form.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My form v-7 — gemstones, precious metals and jewellery list / queue | UI | Medium | 6 |
| Form V-7 working | UI | Very High | 16 |
| Form v-7 — gemstones, precious metals and jewellery history | UI | Medium | 6 |
| V-7 and sub-annexure assemble | API | Very High | 16 |
| Update form v-7 — gemstones, precious metals and jewellery | API | Medium | 6 |
| Search form v-7 — gemstones, precious metals and jewellery | API | Medium | 6 |
| Read form v-7 — gemstones, precious metals and jewellery history | API | Easy | 4 |
| Form v-7 — gemstones, precious metals and jewellery persistence | DB | Medium | 4 |
| Digital-declaration consume | Integration | Easy | 8 |
| Form V-7 — gemstones, precious metals and jewellery feature tests | Testing | Very High | 12 |
| Form V-7 — gemstones, precious metals and jewellery implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **88** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
