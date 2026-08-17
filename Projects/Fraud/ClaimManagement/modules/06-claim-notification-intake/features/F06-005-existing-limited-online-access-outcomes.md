# F06-005 — Existing limited online access outcomes

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Existing limited online access outcomes |
| **Module** | 06 — Claim Notification & Intake |

### Description
If the Authority’s limited online access system already captures an OOK pack, the Officer retrieves or receives that outcome into this application so the claim still has linked FE, scheme, investment, validated fields and uploads. The Officer does not send the claimant to a new mass public portal.

### Business Objective
Cover existing limited-access OOK outcomes in this application without building a mass public portal.

### Actors
Officer; Administrator (interface configuration as needed).

### User Journey
1. Officer identifies an OOK pack already captured in the Authority’s limited online access system.
2. Officer retrieves or receives that outcome into this application.
3. The claim is linked to imported FE, scheme, investment, validated fields and uploads.
4. Officer does not send the claimant to a new mass public portal.

### Functional Capabilities
- Retrieve or receive limited-access outcomes.
- Link FE, scheme, investment, fields and uploads on the claim.
- Avoid a second unofficial claim ledger or mass portal rebuild.

### Inputs
Existing limited-access outcome payload / reference.

### Outputs
Claim in this application with linked FE/scheme/investment and uploads, still subject to completeness rules.

### Business Rules
- Business outcomes must be covered; may be integrated rather than rebuilt as a mass portal.
- Retrieved packs still cannot be treated as submitted if mandatory pack/fields are missing (F06-004).

### Validations
- Linked FE/scheme must be imported references.
- Completeness checked before status = submitted.

### Calculations
None beyond completeness via F06-004.

### Workflow
Retrieve/receive → map to claim → validate pack → submitted or gap list.

### Search Requirements
Existing outcome reference, depositor, FE.

### Documents
Uploads as supplied by the existing limited-access system.

### Reports
Ingest run / unmatched outcome list.

### Notifications
On-screen ingest result.

### Security
Authorised Officer only. Ingest audited. Need-to-know on packs.

### Integrations
Existing limited online access system.

### Dependencies
F06-004, F02, F04, F05.

### Assumptions
- The Authority confirms whether integration or constrained-path re-implementation is the primary OOK channel; both outcomes are covered.

### Risks
- Building a new mass portal would violate the SOW channel model.

### Non Functional Requirements
No duplicate island of claim data; official domain not .org as primary identity.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Limited-access outcome retrieve/link screen | UI | Medium | 6 |
| Outcome ingest operations | API | Complex | 8 |
| Ingested-outcome persistence | DB | Medium | 4 |
| Existing limited online access system | Integration | Medium | 16 |
| Limited-access outcome tests | Testing | Complex | 8 |
| Limited-access outcome notes | Documentation | Medium | 3 |
| **Total** | | | **45** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Medium is mapping + retry to the existing limited-access system, not a public portal rebuild.
