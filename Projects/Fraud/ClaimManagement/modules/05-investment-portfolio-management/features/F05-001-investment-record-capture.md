# F05-001 — Investment record capture

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Investment record capture |
| **Module** | 05 — Investment Portfolio Management |

### Description
An Officer opens a depositor, selects imported FE and scheme, and enters customer ID, bond/MOU, deposit receipt, dates, deposit amount, promised interest and amount already received, then saves. The same Officer can reopen the record and see the full investment history for that depositor, FE and scheme.

### Business Objective
Capture complete investment history against imported FE/scheme so verification and settlement have a structured portfolio.

### Actors
Officer.

### User Journey
1. Who creates: Officer
2. How they create: Officer opens a unique depositor profile.
3. How they edit: Officer selects imported FE and imported scheme (not free-text).
4. How they send for approval: Officer enters customer ID, bond/MOU, deposit receipt, dates, deposit amount, promised interest and amount already received, then saves. Select depositor/FE/scheme → enter fields → save → history available. Direct save with audit.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer reopens the record and sees the full investment history for that depositor, FE and scheme.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Capture investment against imported FE and scheme only.
- Record customer ID, bond/MOU, deposit receipt, dates, amounts, promised interest, amount received.
- Show full investment history on reopen.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Investment capture form | Complex |
| Investment history register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Investment capture operations | Complex |
| Update investment record capture | Medium |
| Search investment record capture | Medium |
| Read investment record capture history | Easy |

### Inputs
Depositor, imported FE, imported scheme, customer ID, bond/MOU, receipt, dates, deposit amount, promised interest, amount received.

### Outputs
Investment record; history for that depositor/FE/scheme.

### Business Rules
- Only imported schemes may be selected (F02-003).
- No local FE dossier; FIR/seized lookup is F05-007 via existing app.
- No generative filling of investment narratives.

### Validations
- FE and scheme mandatory and imported.
- Dates and amounts required as policy specifies.

### Calculations
Interest and outstanding are F05-002 after save.

### Workflow
Select depositor/FE/scheme → enter fields → save → history available. Direct save with audit.

### Search Requirements
Depositor, FE, scheme, customer ID, receipt, dates.

### Documents
Deposit receipt / bond / MOU images as supporting papers.

### Reports
Investment history on the depositor; FE-wise views later in F09.

### Notifications
None.

### Security
Portfolio is need-to-know. Actions attributable to Person in Post.

### Integrations
None (FE/scheme are imported references).

### Dependencies
F04-002, F02-001, F02-003.

### Assumptions
- Interest-paid-as-principal-repaid is applied in F05-002 where the Authority’s rule requires it.

### Risks
- Free-text schemes would break notification eligibility checks.

### Non Functional Requirements
Searchable FE/scheme dropdowns. Complete history supports verification and settlement.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Investment capture form | UI | Complex | 12 |
| Investment history register | UI | Medium | 6 |
| Investment capture operations | API | Complex | 8 |
| Update investment record capture | API | Medium | 6 |
| Search investment record capture | API | Medium | 6 |
| Read investment record capture history | API | Easy | 4 |
| Investment persistence | DB | Complex | 6 |
| Investment record capture feature tests | Testing | Complex | 8 |
| Investment record capture implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **59** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
