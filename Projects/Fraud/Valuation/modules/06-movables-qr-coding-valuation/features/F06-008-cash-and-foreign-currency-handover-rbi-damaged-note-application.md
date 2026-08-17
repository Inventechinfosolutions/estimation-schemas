# F06-008 — Cash and foreign currency handover; RBI damaged-note application

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-008 |
| **Feature Name** | Cash and foreign currency handover; RBI damaged-note application |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
An Officer or assigned Valuer records cash/FCY quantity, value and damage observed at handover. Where notes are damaged, the user generates the application to RBI to replace damaged notes in the appropriate stored format, from those particulars, and files it against the seizure. Generative AI shall not draft the application text.

### Business Objective
Record cash/FCY at handover and generate the RBI damaged-note application from stored particulars and format.

### Actors
Office user; Approved Valuer.

### User Journey
1. Officer or assigned Valuer records cash/FCY quantity, value and damage observed at handover.
2. Where notes are damaged, the user generates the RBI replacement application in the appropriate stored format from those particulars and files it against the seizure.
3. Generative AI shall not draft the application text.

### Functional Capabilities
- Record cash and FCY quantity, value, damage at handover
- Generate RBI damaged-note application from stored format and particulars
- File the application against the seizure
- No generative drafting

### Inputs
Currency; quantity; value; damage observed; stored RBI format identifier.

### Outputs
Handover record; generated RBI application file on the seizure.

### Business Rules
- Application text comes from stored format + particulars, not a generative model
- RBI format is as used by the Authority (dependency)

### Validations
- Quantity/value present
- Damage flag drives application generate
- Format template present

### Calculations
Value as entered; no FX engine unless the Authority supplies rates as static reference.

### Workflow
Record handover → if damaged, generate from template → file on seizure.

### Search Requirements
Seizure, cash/FCY, damaged yes/no, application filed.

### Documents
RBI damaged-note application.

### Reports
Cash/FCY handover register.

### Notifications
In-app if damaged but application not filed.

### Security
Need-to-know; cash values attributable.

### Integrations
RBI application format fill (mapping from stored particulars; not a live RBI gateway unless later ordered).

### Dependencies
Authority-supplied RBI format; parent seizure; Module 01 access.

### Assumptions
- RBI format is supplied; this is not a live RBI API unless later ordered.

### Risks
Wrong format version; generative drafting if controls fail.

### Non Functional Requirements
Generated file stored with the seizure; template version recorded.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Cash/FCY handover | UI | Complex | 12 |
| RBI application generate from stored format | API | Very High | 16 |
| Handover and application store | Database | Medium | 4 |
| RBI format fill | Integration | Medium | 16 |
| Cash/FCY and RBI tests | Testing | Complex | 8 |
| Cash/FCY and RBI guide | Documentation | Complex | 4 |
| **Total** | | | **60** |

### Estimation Assumptions
- API Very High 16 for format generation (import/export class). Not a payment gateway Very High 40.
