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
1. Who creates: Office user
2. How they create: Officer or assigned Valuer records cash/FCY quantity, value and damage observed at handover.
3. How they edit: Where notes are damaged, the user generates the RBI replacement application in the appropriate stored format from those particulars and files it against the seizure.
4. How they send for approval: Generative AI shall not draft the application text. Record handover → if damaged, generate from template → file on seizure.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record cash and FCY quantity, value, damage at handover
- Generate RBI damaged-note application from stored format and particulars
- File the application against the seizure
- No generative drafting

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My cash and foreign currency handover; rbi damaged-note application list / queue | Medium |
| Cash/FCY handover | Complex |
| Cash and foreign currency handover; rbi damaged-note application history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| RBI application generate from stored format | Very High |
| Update cash and foreign currency handover; rbi damaged-note application | Medium |
| Search cash and foreign currency handover; rbi damaged-note application | Medium |
| Read cash and foreign currency handover; rbi damaged-note application history | Easy |

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
|---|---|---|---|
| My cash and foreign currency handover; rbi damaged-note application list / queue | UI | Medium | 6 |
| Cash/FCY handover | UI | Complex | 12 |
| Cash and foreign currency handover; rbi damaged-note application history | UI | Medium | 6 |
| RBI application generate from stored format | API | Very High | 16 |
| Update cash and foreign currency handover; rbi damaged-note application | API | Medium | 6 |
| Search cash and foreign currency handover; rbi damaged-note application | API | Medium | 6 |
| Read cash and foreign currency handover; rbi damaged-note application history | API | Easy | 4 |
| Cash and foreign currency handover; rbi damaged-note application persistence | DB | Medium | 4 |
| RBI format fill | Integration | Medium | 16 |
| Cash and foreign currency handover; RBI damaged-note application feature tests | Testing | Complex | 8 |
| Cash and foreign currency handover; RBI damaged-note application implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **88** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
