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
1. Where Claim Module 03 already has an attached-asset row for the same property, the Officer selects that existing row and links it.
2. Officer does not re-type FE/asset identity.
3. Claim keeps auction tracking and recovered funds; this record keeps GIS field valuation.

### Functional Capabilities
- Select and link an existing Claim Module 03 attached-asset row
- Refuse creating a claim attached-asset from this screen
- Preserve ownership: auction sale/deposit in Claim; GIS valuation here

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
|---|---|---|---:|
| Claim attached-asset link selector | UI | Easy | 4 |
| Link/unlink valuation to Claim row | API | Medium | 6 |
| Claim-asset link keys | Database | Easy | 2 |
| Claim Module 03 attached-asset consume | Integration | Medium | 16 |
| Claim-link tests | Testing | Complex | 8 |
| Claim-asset link guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Auction execution hours are not in this SOW; F07-007 is pack release only.
