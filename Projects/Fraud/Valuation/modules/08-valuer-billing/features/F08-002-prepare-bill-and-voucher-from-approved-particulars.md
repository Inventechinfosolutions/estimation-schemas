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
1. Who creates: Billing officer
2. How they create: In the billing window the officer reviews populated valuer basics and assignment.
3. How they edit: Applies Rates of Valuation and Incidental Costs from F02-001, enters bill details, and generates the bill and voucher.
4. How they send for approval: Changing a rate on the bill requires a recorded reason and does not silently rewrite the valuer master. Review populate → apply rates → enter details → generate bill and voucher.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Billing officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Billing officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Populate valuer basics and assignment
- Apply master rates and incidental costs
- Generate bill and voucher
- Rate override on bill with reason only

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My prepare bill and voucher from approved particulars list / queue | Medium |
| Bill and voucher working | Complex |
| Prepare bill and voucher from approved particulars history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Rate apply and voucher generate | Complex |
| Update prepare bill and voucher from approved particulars | Medium |
| Search prepare bill and voucher from approved particulars | Medium |
| Read prepare bill and voucher from approved particulars history | Easy |

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
|---|---|---|---|
| My prepare bill and voucher from approved particulars list / queue | UI | Medium | 6 |
| Bill and voucher working | UI | Complex | 12 |
| Prepare bill and voucher from approved particulars history | UI | Medium | 6 |
| Rate apply and voucher generate | API | Complex | 8 |
| Update prepare bill and voucher from approved particulars | API | Medium | 6 |
| Search prepare bill and voucher from approved particulars | API | Medium | 6 |
| Read prepare bill and voucher from approved particulars history | API | Easy | 4 |
| Prepare bill and voucher from approved particulars persistence | DB | Medium | 4 |
| Valuer-master rates consume | Integration | Simple | 4 |
| Prepare bill and voucher from approved particulars feature tests | Testing | Complex | 8 |
| Prepare bill and voucher from approved particulars implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
