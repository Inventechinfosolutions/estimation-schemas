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
1. Officer opens a unique depositor profile.
2. Officer selects imported FE and imported scheme (not free-text).
3. Officer enters customer ID, bond/MOU, deposit receipt, dates, deposit amount, promised interest and amount already received, then saves.
4. Officer reopens the record and sees the full investment history for that depositor, FE and scheme.

### Functional Capabilities
- Capture investment against imported FE and scheme only.
- Record customer ID, bond/MOU, deposit receipt, dates, amounts, promised interest, amount received.
- Show full investment history on reopen.

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
| Investment persistence | DB | Complex | 6 |
| Investment capture tests | Testing | Complex | 8 |
| Investment capture guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Auto-calculation of interest/outstanding is F05-002.
