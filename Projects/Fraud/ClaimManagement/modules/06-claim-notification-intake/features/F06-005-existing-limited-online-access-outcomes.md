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
1. Who creates: Officer
2. How they create: Officer identifies an OOK pack already captured in the Authority’s limited online access system.
3. How they edit: Officer retrieves or receives that outcome into this application.
4. How they send for approval: The claim is linked to imported FE, scheme, investment, validated fields and uploads. Retrieve/receive → map to claim → validate pack → submitted or gap list.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer does not send the claimant to a new mass public portal.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Retrieve or receive limited-access outcomes.
- Link FE, scheme, investment, fields and uploads on the claim.
- Avoid a second unofficial claim ledger or mass portal rebuild.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My existing limited online access outcomes list / queue | Medium |
| Limited-access outcome retrieve/link screen | Medium |
| Existing limited online access outcomes history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Outcome ingest operations | Complex |
| Update existing limited online access outcomes | Medium |
| Search existing limited online access outcomes | Medium |
| Read existing limited online access outcomes history | Easy |

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
| My existing limited online access outcomes list / queue | UI | Medium | 6 |
| Limited-access outcome retrieve/link screen | UI | Medium | 6 |
| Existing limited online access outcomes history | UI | Medium | 6 |
| Outcome ingest operations | API | Complex | 8 |
| Update existing limited online access outcomes | API | Medium | 6 |
| Search existing limited online access outcomes | API | Medium | 6 |
| Read existing limited online access outcomes history | API | Easy | 4 |
| Ingested-outcome persistence | DB | Medium | 4 |
| Existing limited online access system | Integration | Medium | 16 |
| Existing limited online access outcomes feature tests | Testing | Complex | 8 |
| Existing limited online access outcomes implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **73** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
