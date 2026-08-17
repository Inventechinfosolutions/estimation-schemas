# F07-007 — Release accepted valuation pack to Claim for auction

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-007 |
| **Feature Name** | Release accepted valuation pack to Claim for auction |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
After CA Accept, an authorised Officer or CA releases the pack to Claim Management Module 03: unique seized-property code, accepted report, selected auction-display photographs, and the linked attached-asset row (F03-007) if present. Claim uses this for auction tracking and recovered funds. This feature does not record auction sale or deposit. A pack that is not Accepted cannot be released.

### Business Objective
Hand off the accepted GIS valuation pack and display photos to Claim without running the auction here.

### Actors
Office user (authorised); Competent Authority.

### User Journey
1. After CA Accept, authorised Officer or CA releases the pack to Claim Module 03: unique seized-property code, accepted report, selected auction-display photographs, and linked attached-asset row (F03-007) if present.
2. Claim uses this for auction tracking and recovered funds.
3. This feature does not record auction sale or deposit. Non-Accepted packs cannot be released.

### Functional Capabilities
- Release accepted pack (code, report, selected photos, Claim link if any)
- Refuse release unless CA Accept
- Do not record auction sale or recovered-fund deposit

### Inputs
Accepted valuation; confirm release.

### Outputs
Released pack identifier for Claim; Claim can open without re-keying the property code.

### Business Rules
- Accept is prerequisite
- Auction sale stays in Claim
- No re-key of unique property code

### Validations
- Decision is Accept
- Unique seized-property code present
- Selected photos identifiable

### Calculations
None.

### Workflow
Confirm Accept → assemble pack → release to Claim Module 03 → Claim opens by property code.

### Search Requirements
Released yes/no, property code, Claim row.

### Documents
Accepted report; selected photographs (handoff).

### Reports
Release register.

### Notifications
In-app release confirmation; Claim-side notices are Claim SOW.

### Security
Authorised Officer/CA; RBAC on common DB.

### Integrations
Claim Management Module 03 pack handoff (multi-system mapping, retry) — not auction execution.

### Dependencies
F07-004 Accept; F07-003; F02-003; F03-007; Claim Module 03.

### Assumptions
- Common-database linkage rules with Claim are agreed.

### Risks
Release without Claim row (F03-007 missing) needs an agreed Claim create-or-queue behaviour — default: release with code even if unlinked, flagged.

### Non Functional Requirements
Idempotent release; no duplicate packs for the same Accept without history.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Claim pack release confirmation | UI | Easy | 4 |
| Accepted pack assemble | API | Complex | 8 |
| Release record | Database | Medium | 4 |
| Claim Module 03 pack handoff | Integration | Complex | 24 |
| Release tests | Testing | Complex | 8 |
| Claim release guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Integration Complex 24 for Claim handoff. Auction sale hours excluded.
