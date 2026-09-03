# F09-002 — Special Court filing report

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Special Court filing report |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
Using the same class of approved inputs, the Officer generates the Special Court filing report, reviews it on screen, and produces the filing copy. The Officer does not re-key the settlement figures by hand into an unrelated template.

### Business Objective
Produce the Special Court filing report from the same class of approved inputs used for equitable distribution.

### Actors
Officer.

### User Journey
1. Who creates: Officer
2. How they create: Officer uses the same class of approved inputs as F09-001.
3. How they edit: Officer generates the Special Court filing report and reviews it on screen.
4. How they send for approval: Officer produces the filing copy without re-keying settlement figures into an unrelated template. Load inputs → generate → review → filing copy.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Generate Special Court filing report from approved inputs.
- On-screen review.
- Produce filing copy without manual re-key of settlement figures.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Special Court report generate and preview | Complex |
| Filing copy produce | Easy |
| Special court filing report history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Special Court report generation | Very High |
| Update special court filing report | Medium |
| Search special court filing report | Medium |
| Read special court filing report history | Easy |

### Inputs
Same class of approved inputs (recovered funds, approved claims and related fields).

### Outputs
Special Court filing report / filing copy.

### Business Rules
- Same class of inputs as equitable distribution.
- Legal Management court petitions/orders are a separate SOW and are not duplicated here.
- No generative legal drafting.

### Validations
- Input-format completeness.
- Figures reconcilable to settlement/recovery.

### Calculations
Report assembly per approved format.

### Workflow
Load inputs → generate → review → filing copy.

### Search Requirements
Reports by FE, period, run date.

### Documents
Filing copy.

### Reports
The Special Court filing report.

### Notifications
None.

### Security
Authorised Posts only. Court-facing outputs are need-to-know.

### Integrations
None.

### Dependencies
F09-001 inputs; F08; F03; Authority format.

### Assumptions
- Approved Special Court report format is supplied by the Authority.

### Risks
- Re-keying into a side template would break reconciliation.

### Non Functional Requirements
On-screen review before filing copy. Structured generation.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Special Court report generate and preview | UI | Complex | 12 |
| Filing copy produce | UI | Easy | 4 |
| Special court filing report history | UI | Medium | 6 |
| Special Court report generation | API | Very High | 16 |
| Update special court filing report | API | Medium | 6 |
| Search special court filing report | API | Medium | 6 |
| Read special court filing report history | API | Easy | 4 |
| Filing report persistence | DB | Medium | 4 |
| Special Court filing report feature tests | Testing | Complex | 8 |
| Special Court filing report implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
