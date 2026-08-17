# F08-002 — Prepare bill and voucher from approved particulars

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Prepare bill and voucher from approved particulars |
| **Module** | 08 — Valuer Billing |

### Description
In the billing window the officer reviews populated valuer basics and assignment, applies Rates of Valuation and Incidental Costs from F02-001, enters bill details, and generates the bill and voucher. Changing a rate on the bill requires a recorded reason; it does not silently rewrite the valuer master.

### Business Objective
Prepare bill and voucher from the approved valuer-master rates after CA Accept.

### Actors
Billing officer; Office user (authorised).

### User Journey
1. In the billing window the officer reviews populated valuer basics and assignment.
2. Applies Rates of Valuation and Incidental Costs from F02-001, enters bill details, and generates the bill and voucher.
3. Changing a rate on the bill requires a recorded reason and does not silently rewrite the valuer master.

### Functional Capabilities
- Populate valuer basics and assignment
- Apply master rates and incidental costs
- Generate bill and voucher
- Rate override on bill with reason only

### Inputs
Bill details; master rates; optional override with reason.

### Outputs
Bill and voucher documents on the assignment.

### Business Rules
- Uses valuer master rates unless authorised override with reason
- Does not rewrite F02-001 on override
- Only inside Accept gate (F08-001)

### Validations
- Window opened under Accept
- Rates source recorded (master vs override)

### Calculations
Bill amounts from rates/incidental costs and entered particulars (no payment engine).

### Workflow
Review populate → apply rates → enter details → generate bill and voucher.

### Search Requirements
Valuer Code, assignment, bill id.

### Documents
Valuer bill; voucher.

### Reports
Bill and voucher.

### Notifications
None.

### Security
Billing officer; override attributable.

### Integrations
Valuer-master rates consume (F02-001).

### Dependencies
F08-001; F02-001; F04-001.

### Assumptions
- Treasury disbursement is out of scope unless later ordered.

### Risks
Silent rate rewrite of the master — this feature must not do that.

### Non Functional Requirements
Bill stores the rates used.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Bill and voucher working | UI | Complex | 12 |
| Rate apply and voucher generate | API | Complex | 8 |
| Bill and voucher store | Database | Medium | 4 |
| Valuer-master rates consume | Integration | Simple | 4 |
| Bill/voucher tests | Testing | Complex | 8 |
| Bill and voucher guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Online submit and hard-copy upload are F08-003.
