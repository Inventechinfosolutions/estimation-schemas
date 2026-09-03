# F03-007 — Link to Claim attached-asset record

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-007 |
| **Feature Name** | Link to Claim attached-asset record |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
Where the common database already has a Claim Module 03 attached-asset row for the same property, the Officer links this valuation asset to that row (select existing, do not re-type). Claim settlement continues to own auction tracking and recovered funds; this record owns GIS field valuation.

### Business Objective
Connect GIS valuation to the Claim attached-asset row without duplicate identity or running the auction here.

### Actors
Office user.

### User Journey
1. Who creates: Office user
2. How they create: Where Claim Module 03 already has an attached-asset row for the same property, the Officer selects that existing row and links it.
3. How they edit: Officer does not re-type FE/asset identity.
4. How they send for approval: Claim keeps auction tracking and recovered funds; this record keeps GIS field valuation. Search Claim attached-asset → select → save link.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Select and link an existing Claim Module 03 attached-asset row
- Refuse creating a claim attached-asset from this screen
- Preserve ownership: auction sale/deposit in Claim; GIS valuation here

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My link to claim attached-asset record list / queue | Medium |
| Claim attached-asset link selector | Easy |
| Link to claim attached-asset record history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Link/unlink valuation to Claim row | Medium |
| Update link to claim attached-asset record | Medium |
| Search link to claim attached-asset record | Medium |
| Read link to claim attached-asset record history | Easy |

### Inputs
Claim attached-asset identifier; valuation asset identifier.

### Outputs
Link between valuation asset and Claim attached-asset row.

### Business Rules
- Select existing, do not re-type
- Auction sale and recovered-fund deposit remain Claim Module 03
- Release of accepted pack is F07-007, not this link alone

### Validations
- Claim row exists
- Link unique unless the Authority allows many-to-one with reason

### Calculations
None.

### Workflow
Search Claim attached-asset → select → save link.

### Search Requirements
Claim attached-asset id, unique seized-property code, FE.

### Documents
None.

### Reports
Valuation assets linked / unlinked to Claim.

### Notifications
None.

### Security
Common database subject to RBAC; cannot open Claim settlement functions from this link.

### Integrations
Claim Management Module 03 attached-asset reference (auth, mapping, retry).

### Dependencies
Claim Module 03; F02-005; F07-007.

### Assumptions
- Common-database linkage rules with Claim are agreed before go-live.

### Risks
Linking the wrong Claim row sends the later release pack to the wrong settlement asset.

### Non Functional Requirements
No re-key of FE identity; link is auditable.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My link to claim attached-asset record list / queue | UI | Medium | 6 |
| Claim attached-asset link selector | UI | Easy | 4 |
| Link to claim attached-asset record history | UI | Medium | 6 |
| Link/unlink valuation to Claim row | API | Medium | 6 |
| Update link to claim attached-asset record | API | Medium | 6 |
| Search link to claim attached-asset record | API | Medium | 6 |
| Read link to claim attached-asset record history | API | Easy | 4 |
| Link to claim attached-asset record persistence | DB | Medium | 4 |
| Claim Module 03 attached-asset consume | Integration | Medium | 16 |
| Link to Claim attached-asset record feature tests | Testing | Complex | 8 |
| Link to Claim attached-asset record implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **69** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
