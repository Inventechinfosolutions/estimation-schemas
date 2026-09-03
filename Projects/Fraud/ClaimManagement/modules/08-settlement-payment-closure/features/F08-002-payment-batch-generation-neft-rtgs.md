# F08-002 — Payment batch generation (NEFT / RTGS)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Payment batch generation (NEFT / RTGS) |
| **Module** | 08 — Settlement, Payment & Closure |

### Description
The Officer selects approved claims with a net payable, chooses NEFT or RTGS, and generates a payment batch. The system creates a batch ID and lists the included claims and amounts for the Officer to confirm before transfer.

### Business Objective
Generate confirmable NEFT/RTGS payment batches from approved net payable claims.

### Actors
Officer; Competent Authority (oversee/release as policy requires).

### User Journey
1. Who creates: Officer
2. How they create: Officer selects approved claims that have a net payable.
3. How they edit: Officer chooses NEFT or RTGS and generates a payment batch.
4. How they send for approval: System creates a batch ID and lists included claims and amounts. Select claims → choose mode → generate batch → confirm list → transfer recording in F08-003.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer confirms the list before transfer through the Authority’s approved banking arrangements.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Select approved claims with net payable.
- Choose NEFT or RTGS.
- Generate batch ID and confirmation list.
- Hold confirmation before transfer.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Payment batch builder | Very High |
| Batch confirmation register | Medium |
| Payment batch generation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Batch generation operations | Very High |
| Update payment batch generation | Medium |
| Search payment batch generation | Medium |
| Read payment batch generation history | Easy |

### Inputs
Approved claims, net payable, payment mode (NEFT/RTGS).

### Outputs
Payment batch ID; included claims and amounts; confirmation record.

### Business Rules
- Only approved (not Pending Clarification / rejected) claims with net payable are batchable.
- Bank core payment gateway product is out of scope; batching uses Authority-approved banking arrangements.
- Valuer billing is Valuation SOW, not this feature.

### Validations
- Refund account present (and penny-drop recorded if policy requires).
- Mode is NEFT or RTGS.

### Calculations
Batch total = sum of included net payable.

### Workflow
Select claims → choose mode → generate batch → confirm list → transfer recording in F08-003.

### Search Requirements
Batch ID, mode, status, FE, date.

### Documents
Batch confirmation list.

### Reports
Payment batch register.

### Notifications
On-screen confirmation; not a claimant marketing mail.

### Security
Batch generate/confirm is privileged and audited (who generated the batch).

### Integrations
None in this feature beyond preparing the batch for Authority banking arrangements (status returns in F08-003).

### Dependencies
F08-001; F04-003 refund account; F04-007 penny-drop as policy requires.

### Assumptions
- Transfer execution uses the Authority’s approved banking arrangements, not a vendor payment-gateway product.

### Risks
- Including non-approved claims would pay ineligible amounts.

### Non Functional Requirements
Batch list must be reviewable before transfer. Actions attributable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Payment batch builder | UI | Very High | 16 |
| Batch confirmation register | UI | Medium | 6 |
| Payment batch generation history | UI | Medium | 6 |
| Batch generation operations | API | Very High | 16 |
| Update payment batch generation | API | Medium | 6 |
| Search payment batch generation | API | Medium | 6 |
| Read payment batch generation history | API | Easy | 4 |
| Payment batch persistence | DB | Complex | 6 |
| Payment batch generation (NEFT / RTGS) feature tests | Testing | Very High | 12 |
| Payment batch generation (NEFT / RTGS) implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **82** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
