# F05-010 — Expert Valuer assignment and digital declaration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-010 |
| **Feature Name** | Expert Valuer assignment and digital declaration |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
An Office user or Registered Valuer appoints an Expert Valuer on the assignment (linked shared Person / professional master — not a second login directory). On Forms V-1 to V-8 the Registered Valuer, and the Expert Valuer if appointed, complete the no-interest and personal-inspection declaration and apply a digital signature. A form without the Registered Valuer’s digital declaration cannot be submitted to the CA.

### Business Objective
Optional Expert Valuer plus mandatory Registered Valuer digital declaration before CA review, reused on V-1–V-8.

### Actors
Office user; Registered Valuer; Expert Valuer.

### User Journey
1. Who creates: Office user
2. How they create: Office user or Registered Valuer appoints an Expert Valuer on the assignment (linked shared Person / professional master, not a second login directory).
3. How they edit: On Forms V-1 to V-8 the Registered Valuer, and the Expert Valuer if appointed, complete no-interest and personal-inspection declaration and apply a digital signature.
4. How they send for approval: A form without the Registered Valuer’s digital declaration cannot be submitted to the CA. V-6–V-8 (Module 06) use this same declaration/sign. Optional appoint Expert → complete declaration → digital sign → allow CA submit.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Appoint Expert Valuer on the assignment via shared Person / professional master
- Digital signature on declaration for V-1 to V-8
- Block CA submit without Registered Valuer digital declaration
- Require Expert declaration/sign when appointed

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Expert Valuer appointment | Easy |
| Digital declaration and sign | Very High |
| Expert valuer assignment and digital declaration history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Dual declaration and digital signature | Very High |
| Update expert valuer assignment and digital declaration | Medium |
| Search expert valuer assignment and digital declaration | Medium |
| Read expert valuer assignment and digital declaration history | Easy |

### Inputs
Expert Valuer Person/master; declaration text (true information, no interest, personal inspection date); digital signature.

### Outputs
Appointment; signed declarations on the form; blocked unsigned submit.

### Business Rules
- Expert is optional; Registered Valuer digital declaration is mandatory to submit to CA
- Not a second login directory
- Applies to V-1–V-4 and V-6–V-8

### Validations
- Expert linked to shared Person if appointed
- Registered Valuer signature present before CA submit
- Both signatures when Expert appointed

### Calculations
None.

### Workflow
Optional appoint Expert → complete declaration → digital sign → allow CA submit.

### Search Requirements
Assignment, Expert appointed yes/no, signed yes/no.

### Documents
Digital declaration on the statutory form.

### Reports
Unsigned forms pending CA.

### Notifications
In-app block on unsigned submit.

### Security
Signature attributable to shared Person; no shared credentials.

### Integrations
Digital signature / PKI as Authority-approved (multi-step mapping, retry, signer identity) — not a public e-sign marketplace experiment.

### Dependencies
F02-001; F01-001; F05-007; F05-008; F06-005–F06-007.

### Assumptions
- Authority names the digital-signature mechanism; hours assume an approved signing capability is available.

### Risks
PKI/onboarding delay; Expert appointed but unsigned.

### Non Functional Requirements
Unsigned forms never reach CA queue; signature audit with the form.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Expert Valuer appointment | UI | Easy | 4 |
| Digital declaration and sign | UI | Very High | 16 |
| Expert valuer assignment and digital declaration history | UI | Medium | 6 |
| Dual declaration and digital signature | API | Very High | 16 |
| Update expert valuer assignment and digital declaration | API | Medium | 6 |
| Search expert valuer assignment and digital declaration | API | Medium | 6 |
| Read expert valuer assignment and digital declaration history | API | Easy | 4 |
| Expert valuer assignment and digital declaration persistence | DB | Medium | 4 |
| Digital signature / PKI | Integration | Complex | 24 |
| Expert Valuer assignment and digital declaration feature tests | Testing | Very High | 12 |
| Expert Valuer assignment and digital declaration implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **102** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
