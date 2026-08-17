# F08-005 — Payment forensic audit

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-005 |
| **Feature Name** | Payment forensic audit |
| **Module** | 08 — Settlement, Payment & Closure |

### Description
An authorised auditor or Administrator opens a claim or batch and retrieves who generated the batch, who recorded bank references, each status change, and closure — with Person, Post, timestamp and channel.

### Business Objective
Retrieve a payment-specific forensic trail that participates in the Module 01 audit store.

### Actors
Auditor; Administrator.

### User Journey
1. Authorised auditor or Administrator opens a claim or payment batch.
2. They retrieve who generated the batch, who recorded bank references, each status change, and closure.
3. Each event shows Person, Post, timestamp and channel.

### Functional Capabilities
- Payment/batch forensic viewer.
- Show generate, bank-reference, status-change and closure events.
- Attribute Person, Post, timestamp, channel.

### Inputs
Claim or batch identifier, date filters.

### Outputs
Payment forensic trail; contributes events to F01-010.

### Business Rules
- Payment events participate in the forensic audit trail (Module 01).
- Viewing the trail does not confer rights to generate a new batch.

### Validations
- Only auditor/Administrator Posts open this viewer.

### Calculations
None.

### Workflow
Open claim/batch → retrieve trail. Read-only.

### Search Requirements
Batch ID, claim, Person, date, event type.

### Documents
None.

### Reports
Payment forensic extract.

### Notifications
None.

### Security
Auditor access itself audited. No secret credential values in before/after.

### Integrations
Internal audit ingest to F01-010.

### Dependencies
F08-002, F08-003, F08-004, F01-010.

### Assumptions
- This is a payment-focused viewer complementary to the central register in F01-010.

### Risks
- Gaps in event coverage would fail Key Aspect 3 for payment.

### Non Functional Requirements
Payment privileged actions attributable and retrievable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Payment audit trail viewer | UI | Complex | 12 |
| Payment audit query operations | API | Complex | 8 |
| Payment audit persistence | DB | Medium | 4 |
| Internal audit ingest | Integration | Simple | 4 |
| Payment forensic tests | Testing | Complex | 8 |
| Payment forensic guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Central forensic register UI is estimated in F01-010; this feature is the payment/batch drill-down.
