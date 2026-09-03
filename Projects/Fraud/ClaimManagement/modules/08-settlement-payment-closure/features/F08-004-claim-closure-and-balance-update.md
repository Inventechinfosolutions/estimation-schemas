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
1. Who creates: Officer
2. How they create: When payment status is success as policy requires, Officer (or the system on that status) updates claim status to closed.
3. How they edit: Investment balance is updated and payment history is appended.
4. How they send for approval: If payment is failed or reversed, the claim stays open; Officer cannot close it as settled. Success → close + balance + history. Fail/reverse → remain open. No silent close.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Close claim on success per policy.
- Update investment balance and append payment history.
- Block settled-closure on failed or reversed payment.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Closure confirmation | Medium |
| Block settled-close on fail/reverse | Easy |
| Claim closure and balance update history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Closure and balance operations | Very High |
| Update claim closure and balance update | Medium |
| Search claim closure and balance update | Medium |
| Read claim closure and balance update history | Easy |

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
| Claim closure and balance update history | UI | Medium | 6 |
| Closure and balance operations | API | Very High | 16 |
| Update claim closure and balance update | API | Medium | 6 |
| Search claim closure and balance update | API | Medium | 6 |
| Read claim closure and balance update history | API | Easy | 4 |
| Closure and balance persistence | DB | Complex | 6 |
| Claim closure and balance update feature tests | Testing | Complex | 8 |
| Claim closure and balance update implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
