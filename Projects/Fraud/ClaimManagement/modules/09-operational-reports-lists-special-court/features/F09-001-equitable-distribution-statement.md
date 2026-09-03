# F09-001 — Equitable distribution statement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Equitable distribution statement |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
An authorised Officer enters or loads the approved input format (recovered funds, approved claims and related fields) and generates the equitable distribution statement. The Officer downloads or files the output for Special Court use.

### Business Objective
Produce the equitable distribution statement required for Special Court filing from approved inputs, not by re-keying into an unrelated template.

### Actors
Authorised Officer; Competent Authority (view as authorised).

### User Journey
1. Who creates: Authorised Officer
2. How they create: Authorised Officer enters or loads the approved input format, including recovered funds, approved claims and related fields.
3. How they edit: Officer generates the equitable distribution statement.
4. How they send for approval: Officer downloads or files the output for Special Court use. Load approved inputs → generate → download/file. Human reviews before filing.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture/load the Authority-approved input format.
- Generate the equitable distribution statement.
- Download/file the output for Special Court.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Approved input format entry | Complex |
| Equitable distribution preview and download | Medium |
| Equitable distribution statement history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Equitable distribution generation | Very High |
| Update equitable distribution statement | Medium |
| Search equitable distribution statement | Medium |
| Read equitable distribution statement history | Easy |

### Inputs
Approved input format fields: recovered funds, approved claims and related fields as specified by the Authority.

### Outputs
Equitable distribution statement.

### Business Rules
- Payment and settlement figures used in court outputs must reconcile to recovered funds and approved claims.
- Vakalat/Caveat and legal drafts belong to the Legal SOW, not this statement.
- No generative drafting of court prose.

### Validations
- Required input-format fields present.
- Recovered figures reconcilable to Module 03 / F08-001.

### Calculations
Distribution arithmetic per the approved format.

### Workflow
Load approved inputs → generate → download/file. Human reviews before filing.

### Search Requirements
Generated statements by FE, period, run date.

### Documents
Generated statement file for filing.

### Reports
The equitable distribution statement.

### Notifications
None.

### Security
Only authorised Posts generate court-facing outputs. Need-to-know on settlement figures.

### Integrations
None (format is in-application unless the Authority later supplies a court e-filing channel).

### Dependencies
F08-001, F03-004, F07-005; Authority-approved input format.

### Assumptions
- Approved input format for equitable distribution is supplied by the Authority.

### Risks
- Hand-building the statement outside structured inputs would desynchronise from recovered/approved figures.

### Non Functional Requirements
Outputs from structured records. Figures reconcilable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Approved input format entry | UI | Complex | 12 |
| Equitable distribution preview and download | UI | Medium | 6 |
| Equitable distribution statement history | UI | Medium | 6 |
| Equitable distribution generation | API | Very High | 16 |
| Update equitable distribution statement | API | Medium | 6 |
| Search equitable distribution statement | API | Medium | 6 |
| Read equitable distribution statement history | API | Easy | 4 |
| Statement run persistence | DB | Medium | 4 |
| Equitable distribution statement feature tests | Testing | Complex | 8 |
| Equitable distribution statement implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **72** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
