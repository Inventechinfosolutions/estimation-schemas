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
1. Tally (F04-005) finds a disagreement (for example Aadhaar spelling versus passbook name).
2. The system creates a mismatch query on the depositor/claim.
3. Officer opens the query and records resolution or sends it for claimant/staff response.
4. Officer cannot treat the identity as clean until the query is closed per policy.

### Functional Capabilities
- Auto-create mismatch query from tally disagreements.
- Officer resolution or send for response.
- Block clean-identity treatment until closed per policy.

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
| Query generation and closure workflow operations | API | Very High | 16 |
| Mismatch query persistence | DB | Medium | 4 |
| Mismatch query tests | Testing | Complex | 8 |
| Mismatch query guide | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Workflow API is Very High because auto-generate plus blocking closure is not standard CRUD.
