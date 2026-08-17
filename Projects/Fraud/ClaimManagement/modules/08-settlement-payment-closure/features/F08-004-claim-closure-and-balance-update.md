# F08-004 — Claim closure and balance update

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-004 |
| **Feature Name** | Claim closure and balance update |
| **Module** | 08 — Settlement, Payment & Closure |

### Description
When payment status is success as policy requires, the Officer (or the system on that status) updates claim status to closed, updates investment balance and appends payment history. A failed or reversed payment leaves the claim open; the Officer cannot close it as settled.

### Business Objective
Close settled claims only on successful payment, and keep failed/reversed payments from being marked settled.

### Actors
Officer.

### User Journey
1. When payment status is success as policy requires, Officer (or the system on that status) updates claim status to closed.
2. Investment balance is updated and payment history is appended.
3. If payment is failed or reversed, the claim stays open; Officer cannot close it as settled.

### Functional Capabilities
- Close claim on success per policy.
- Update investment balance and append payment history.
- Block settled-closure on failed or reversed payment.

### Inputs
Payment status, claim, investment balances, policy success rule.

### Outputs
Closed or still-open claim; updated investment balance; payment history row.

### Business Rules
- Failed or reversed payments do not close the claim.
- Successful settlement updates claim status, investment balance and payment history and closes the claim.

### Validations
- Closure-as-settled is refused unless status meets the success rule.

### Calculations
Investment balance after payment.

### Workflow
Success → close + balance + history. Fail/reverse → remain open. No silent close.

### Search Requirements
Claim status (open/closed), last payment status.

### Documents
None.

### Reports
Closed versus open-after-fail list.

### Notifications
On-screen refusal if Officer attempts settled-close on fail/reverse.

### Security
Closure is privileged and audited.

### Integrations
None.

### Dependencies
F08-003; F05 investment balance.

### Assumptions
- Policy defines whether partial NEFT success on a batch closes only successful lines.

### Risks
- Closing on failed payment would falsely report settlement to court outputs.

### Non Functional Requirements
Balance and history updates are auditable and consistent with payment status.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Closure confirmation | UI | Medium | 6 |
| Block settled-close on fail/reverse | UI | Easy | 4 |
| Closure and balance operations | API | Very High | 16 |
| Closure and balance persistence | DB | Complex | 6 |
| Closure tests | Testing | Complex | 8 |
| Closure guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.
- API Very High covers financial balance update and the hard block on fail/reverse close.
