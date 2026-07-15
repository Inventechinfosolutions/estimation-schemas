# F05-003 — Credit Notes & Demand Cancellation

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-003 |
| **Feature Name** | Credit Notes & Demand Cancellation |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Support credit notes and demand cancellation with maker-checker controls so posted billing errors or waivers are corrected without deleting audit history.

### Business Objective
Provide controlled financial corrections while preserving reconcile-able ledgers (M4-AC5).

### Actors
- Accounts Officer (maker), Approver (checker), Auditor

### User Journey
1. Maker selects demand/lines to credit or cancel.
2. Enters reason and amounts.
3. Checker approves/rejects.
4. Ledger updates; outstanding recalculated; portal reflects change.

### Functional Capabilities
- Full or partial credit note against demand lines
- Demand cancellation (void) where no payment applied / with rules when partially paid
- Maker-checker enforced
- Link to original demand; immutable audit
- Block destroy/delete of posted demands

### Inputs
- Target demand, credit amounts, reason codes, approval action

### Outputs
- Credit note document/number
- Updated demand balances

### Business Rules
- Credit notes / demand cancellation require maker-checker.
- Cannot credit more than outstanding line balance.
- Paid portions follow refund/adjustment policy (may link deposit/Module 05 payment reversal patterns).

### Validations
- Maker ≠ checker (SoD F01-007)
- Reason mandatory; amount limits

### Calculations
- Net demand balance after credits

### Workflow
Request → Checker approve → Post credit/cancel.

### Search Requirements
By credit note no., demand, date, status.

### Documents
Credit note PDF (Module 08).

### Reports
Credit Note Register.

### Notifications
Approval tasks.

### Security
Strict SoD; full audit; no silent edits.

### Integrations
Optional ERP credit push later (Module 10).

### Dependencies
F05-001/002; F01-007; F02-009; Module 08

### Assumptions
- Refund of already-realized cash is separate collection reversal path under F05-004/005.

### Risks
- Incorrect credits distort collection % — report exclusion rules needed.

### Non Functional Requirements
- Credit note numbering from system parameters (F02-011)

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Credit note / cancel request UI | UI | Complex | 8 |
| Maker-checker credit/cancel ops | API | Complex | 8 |
| Credit note entities | Database | Medium | 4 |
| Credit/cancel tests | Testing | Complex | 8 |
| Credit note guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Complex financial correction paths with SoD.
