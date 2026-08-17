# F03-002 — Title, e-Khata and dues tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Title, e-Khata and dues tracking |
| **Module** | 03 — Asset Attachment & Recovered Funds |

### Description
On an existing asset, the Officer updates title-transfer status, records e-Khata creation progress, and enters dues obtained and paid with dates, until Khata is created. The Officer cannot mark auction complete unless this path is recorded as required.

### Business Objective
Track title, e-Khata and dues so auction completion cannot be claimed without the required path.

### Actors
Officer.

### User Journey
1. Officer opens an existing attached asset.
2. Officer updates title-transfer status and e-Khata creation progress.
3. Officer enters dues obtained and dues paid with dates until Khata is created.
4. If the required path is not recorded, the Officer cannot mark auction complete (F03-004).

### Functional Capabilities
- Title-transfer status on the asset.
- e-Khata creation progress.
- Dues obtained and paid with dates.
- Block auction-complete when the required title/e-Khata/dues path is missing.

### Inputs
Title-transfer status, e-Khata progress, dues obtained, dues paid, dates.

### Outputs
Updated title/e-Khata/dues trail on the asset; gate for auction complete.

### Business Rules
- Auction complete is refused unless this path is recorded as required by Authority policy.
- Dues entries carry dates; they are not free-text-only.

### Validations
- Dues paid cannot be recorded without a date.
- Status values are from the Authority’s title/e-Khata set.

### Calculations
Running dues obtained versus paid if both are entered.

### Workflow
Update title → e-Khata progress → dues → Khata created; then auction complete may be allowed (F03-004).

### Search Requirements
Assets by title status, e-Khata progress, outstanding dues flag.

### Documents
Supporting title/e-Khata papers via F03-005.

### Reports
Dues and e-Khata progress extract.

### Notifications
None required.

### Security
Officer Post only for updates; audit who changed status and dues.

### Integrations
None (no GIS Khata system assumed unless the Authority later provides one).

### Dependencies
F03-001.

### Assumptions
- Exact Khata/e-Khata steps follow Authority practice; this feature records them, it does not replace the revenue department system.

### Risks
- Marking auction complete without this path would break recovery evidence for settlement.

### Non Functional Requirements
Dates and status history remain auditable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Title, e-Khata and dues tracker | UI | Complex | 12 |
| Dues and title-path operations | API | Complex | 8 |
| Title/dues persistence | DB | Medium | 4 |
| Title/e-Khata path tests | Testing | Medium | 6 |
| Title and dues note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Auction milestone UI is estimated in F03-004; this feature estimates the gate data.
