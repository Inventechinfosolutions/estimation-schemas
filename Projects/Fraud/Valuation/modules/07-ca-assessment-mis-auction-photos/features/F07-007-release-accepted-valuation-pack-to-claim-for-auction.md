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
1. Who creates: Office user (authorised)
2. How they create: After CA Accept, authorised Officer or CA releases the pack to Claim Module 03: unique seized-property code, accepted report, selected auction-display photographs, and linked attached-asset row (F03-007) if present.
3. How they edit: Claim uses this for auction tracking and recovered funds.
4. How they send for approval: This feature does not record auction sale or deposit. Non-Accepted packs cannot be released. Confirm Accept → assemble pack → release to Claim Module 03 → Claim opens by property code.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user (authorised) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user (authorised) opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Release accepted pack (code, report, selected photos, Claim link if any)
- Refuse release unless CA Accept
- Do not record auction sale or recovered-fund deposit

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My release accepted valuation pack to claim for auction list / queue | Medium |
| Claim pack release confirmation | Easy |
| Release accepted valuation pack to claim for auction history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Accepted pack assemble | Complex |
| Update release accepted valuation pack to claim for auction | Medium |
| Search release accepted valuation pack to claim for auction | Medium |
| Read release accepted valuation pack to claim for auction history | Easy |

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
|---|---|---|---|
| My release accepted valuation pack to claim for auction list / queue | UI | Medium | 6 |
| Claim pack release confirmation | UI | Easy | 4 |
| Release accepted valuation pack to claim for auction history | UI | Medium | 6 |
| Accepted pack assemble | API | Complex | 8 |
| Update release accepted valuation pack to claim for auction | API | Medium | 6 |
| Search release accepted valuation pack to claim for auction | API | Medium | 6 |
| Read release accepted valuation pack to claim for auction history | API | Easy | 4 |
| Release accepted valuation pack to claim for auction persistence | DB | Medium | 4 |
| Claim Module 03 pack handoff | Integration | Complex | 24 |
| Release accepted valuation pack to Claim for auction feature tests | Testing | Complex | 8 |
| Release accepted valuation pack to Claim for auction implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
