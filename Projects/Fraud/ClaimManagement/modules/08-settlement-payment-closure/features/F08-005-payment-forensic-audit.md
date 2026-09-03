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
1. Who creates: Auditor
2. How they create: Authorised auditor or Administrator opens a claim or payment batch.
3. How they edit: They retrieve who generated the batch, who recorded bank references, each status change, and closure.
4. How they send for approval: Each event shows Person, Post, timestamp and channel. Open claim/batch → retrieve trail. Read-only.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Auditor works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Auditor opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Payment/batch forensic viewer.
- Show generate, bank-reference, status-change and closure events.
- Attribute Person, Post, timestamp, channel.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My payment forensic audit list / queue | Medium |
| Payment audit trail viewer | Complex |
| Payment forensic audit history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Payment audit query operations | Complex |
| Update payment forensic audit | Medium |
| Search payment forensic audit | Medium |
| Read payment forensic audit history | Easy |

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
| My payment forensic audit list / queue | UI | Medium | 6 |
| Payment audit trail viewer | UI | Complex | 12 |
| Payment forensic audit history | UI | Medium | 6 |
| Payment audit query operations | API | Complex | 8 |
| Update payment forensic audit | API | Medium | 6 |
| Search payment forensic audit | API | Medium | 6 |
| Read payment forensic audit history | API | Easy | 4 |
| Payment audit persistence | DB | Medium | 4 |
| Internal audit ingest | Integration | Simple | 4 |
| Payment forensic audit feature tests | Testing | Complex | 8 |
| Payment forensic audit implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
