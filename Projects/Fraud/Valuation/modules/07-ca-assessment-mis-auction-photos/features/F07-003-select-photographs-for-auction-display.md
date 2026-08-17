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
1. On the CA report the CA selects which tagged photographs (F05-009) may be shown at auction.
2. Unselected photos remain in the valuation file but are not marked for auction display.
3. Claim uses the selection after F07-007 release. This application does not run the auction.

### Functional Capabilities
- Select tagged photographs for auction display
- Leave unselected photos in the valuation file
- Do not execute auction sale or recovered-fund deposit

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
|---|---|---|---:|
| Auction-display photo picker | UI | Complex | 12 |
| Display-selection persist | API | Easy | 4 |
| Selection flags | Database | Easy | 2 |
| Tagged library consume | Integration | Simple | 4 |
| Photo-picker tests | Testing | Medium | 6 |
| Auction-display photo note | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- No auction-sale hours. GIS ingest remains F04-006.
