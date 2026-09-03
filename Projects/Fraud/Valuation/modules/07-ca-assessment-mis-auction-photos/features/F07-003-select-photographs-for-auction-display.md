# F07-003 — Select photographs for auction display

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Select photographs for auction display |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
On the CA report, the CA selects which tagged photographs may be shown at auction. Unselected photos remain in the valuation file but are not marked for auction display. Claim Management uses this selection after release (F07-007); this application does not run the auction.

### Business Objective
Let the CA choose auction-display photographs without executing auction sale in this application.

### Actors
Competent Authority.

### User Journey
1. Who creates: Competent Authority
2. How they create: On the CA report the CA selects which tagged photographs (F05-009) may be shown at auction.
3. How they edit: Unselected photos remain in the valuation file but are not marked for auction display.
4. How they send for approval: Claim uses the selection after F07-007 release. This application does not run the auction. Open CA report → pick photos → save selection → release later in F07-007.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Competent Authority works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Competent Authority opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Select tagged photographs for auction display
- Leave unselected photos in the valuation file
- Do not execute auction sale or recovered-fund deposit

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My select photographs for auction display list / queue | Medium |
| Auction-display photo picker | Complex |
| Select photographs for auction display history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Display-selection persist | Easy |
| Update select photographs for auction display | Medium |
| Search select photographs for auction display | Medium |
| Read select photographs for auction display history | Easy |

### Inputs
Tagged photograph set; selection ticks.

### Outputs
Auction-display selection flags.

### Business Rules
- Picker uses tagged library only
- Auction sale stays in Claim Module 03
- Release is F07-007

### Validations
- Photo is tagged in F05-009

### Calculations
Count of selected display photos.

### Workflow
Open CA report → pick photos → save selection → release later in F07-007.

### Search Requirements
Asset, selected for auction display yes/no.

### Documents
Selected photographs (flags).

### Reports
Auction-display photo list for the pack.

### Notifications
None.

### Security
CA Post; photos remain need-to-know until Claim publishes per Claim SOW.

### Integrations
Internal tagged library consume.

### Dependencies
F05-009; F07-007; Claim Module 03 (after release).

### Assumptions
- Minimum four GIS photos exist on inspection even if CA selects a subset for display.

### Risks
Selecting untagged or non-GIS photos if filters fail.

### Non Functional Requirements
Selection identifiable for Claim after release.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My select photographs for auction display list / queue | UI | Medium | 6 |
| Auction-display photo picker | UI | Complex | 12 |
| Select photographs for auction display history | UI | Medium | 6 |
| Display-selection persist | API | Easy | 4 |
| Update select photographs for auction display | API | Medium | 6 |
| Search select photographs for auction display | API | Medium | 6 |
| Read select photographs for auction display history | API | Easy | 4 |
| Select photographs for auction display persistence | DB | Medium | 4 |
| Tagged library consume | Integration | Simple | 4 |
| Select photographs for auction display feature tests | Testing | Medium | 6 |
| Select photographs for auction display implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
