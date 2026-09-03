# F04-006 — Auto mismatch query generation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-006 |
| **Feature Name** | Auto mismatch query generation |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
When tally finds disagreement (for example Aadhaar spelling versus passbook name), the system creates a mismatch query on the depositor/claim. The Officer opens the query, records resolution or sends it for claimant/staff response, and cannot treat the identity as clean until it is closed per policy.

### Business Objective
Force a tracked mismatch query whenever tally disagrees, and block “clean identity” until it is closed.

### Actors
Officer; assisting staff; OOK claimant (own-pack response where applicable).

### User Journey
1. Who creates: Officer
2. How they create: Tally (F04-005) finds a disagreement (for example Aadhaar spelling versus passbook name).
3. How they edit: The system creates a mismatch query on the depositor/claim.
4. How they send for approval: Officer opens the query and records resolution or sends it for claimant/staff response. Auto-create → Officer work / claimant-staff response → close or remain blocking. Embedded workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer cannot treat the identity as clean until the query is closed per policy.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Auto-create mismatch query from tally disagreements.
- Officer resolution or send for response.
- Block clean-identity treatment until closed per policy.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Mismatch query register | Complex |
| Query resolution form | Medium |
| Auto mismatch query generation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Query generation and closure workflow operations | Very High |
| Update auto mismatch query generation | Medium |
| Search auto mismatch query generation | Medium |
| Read auto mismatch query generation history | Easy |

### Inputs
Differing fields/sources, Officer remarks, response documents/text.

### Outputs
Open/closed mismatch query; identity-clean flag per policy.

### Business Rules
- Identity is not treated as clean while a required mismatch query is open.
- Queries are structured records, not informal notes only.

### Validations
- Close requires resolution remarks (and papers if policy requires).

### Calculations
None.

### Workflow
Auto-create → Officer work / claimant-staff response → close or remain blocking. Embedded workflow.

### Search Requirements
Open queries by depositor, claim, field, status.

### Documents
Response papers attached to the query.

### Reports
Open mismatch query list.

### Notifications
In-application query for staff; OOK own-pack prompt when that channel applies.

### Security
Query content is KYC-class. Closure is attributable.

### Integrations
None.

### Dependencies
F04-005; F01-008 if OOK responds on own pack.

### Assumptions
- Authority policy defines which differs are blocking versus advisory.

### Risks
- Manual bypass of the clean-identity gate would undermine unique-profile integrity.

### Non Functional Requirements
Workflow is embedded; query list usable during claim windows.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Mismatch query register | UI | Complex | 12 |
| Query resolution form | UI | Medium | 6 |
| Auto mismatch query generation history | UI | Medium | 6 |
| Query generation and closure workflow operations | API | Very High | 16 |
| Update auto mismatch query generation | API | Medium | 6 |
| Search auto mismatch query generation | API | Medium | 6 |
| Read auto mismatch query generation history | API | Easy | 4 |
| Mismatch query persistence | DB | Medium | 4 |
| Auto mismatch query generation feature tests | Testing | Complex | 8 |
| Auto mismatch query generation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
