# F06-007 — Form V-8 — art and handicrafts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-007 |
| **Feature Name** | Form V-8 — art and handicrafts |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The Valuer completes V-8 (description, material, dimensions and weight, base value, additions for hand-crafted, antiquity and rarity, total) and declares personal inspection and no interest with digital signature (F05-010).

### Business Objective
Issue Form V-8 with craft/antiquity/rarity additions and digital declaration.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Valuer completes V-8 description, material, dimensions and weight, base value, and additions for hand-crafted, antiquity and rarity.
3. How they edit: Declares personal inspection and no interest with digital signature (F05-010).
4. How they send for approval: Declares personal inspection and no interest with digital signature (F05-010). Complete V-8 → sign → CA available.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Form V-8 with base value and listed additions
- Digital declaration F05-010
- No generative appraisal narrative

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My form v-8 — art and handicrafts list / queue | Medium |
| Form V-8 working | Complex |
| Form v-8 — art and handicrafts history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| V-8 assemble with additions | Complex |
| Update form v-8 — art and handicrafts | Medium |
| Search form v-8 — art and handicrafts | Medium |
| Read form v-8 — art and handicrafts history | Easy |

### Inputs
V-8 fields; additions; digital signature.

### Outputs
Issued Form V-8.

### Business Rules
- Additions are valuer-entered
- Unsigned cannot go to CA

### Validations
- Total consistent with base + additions as stored
- Digital declaration

### Calculations
Total = base value + hand-crafted + antiquity + rarity additions as entered.

### Workflow
Complete V-8 → sign → CA available.

### Search Requirements
Seizure, Form V-8.

### Documents
Form V-8.

### Reports
Form V-8.

### Notifications
In-app if unsigned.

### Security
Assigned valuer.

### Integrations
F05-010 consume.

### Dependencies
F06-001; F06-002; F05-010.

### Assumptions
- V-8 template from Annexure-01.

### Risks
Unjustified rarity additions without stored reason if the Authority later requires reason — record remarks on the form.

### Non Functional Requirements
Issued snapshot.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My form v-8 — art and handicrafts list / queue | UI | Medium | 6 |
| Form V-8 working | UI | Complex | 12 |
| Form v-8 — art and handicrafts history | UI | Medium | 6 |
| V-8 assemble with additions | API | Complex | 8 |
| Update form v-8 — art and handicrafts | API | Medium | 6 |
| Search form v-8 — art and handicrafts | API | Medium | 6 |
| Read form v-8 — art and handicrafts history | API | Easy | 4 |
| Form v-8 — art and handicrafts persistence | DB | Medium | 4 |
| Digital-declaration consume | Integration | Easy | 8 |
| Form V-8 — art and handicrafts feature tests | Testing | Complex | 8 |
| Form V-8 — art and handicrafts implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **72** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
