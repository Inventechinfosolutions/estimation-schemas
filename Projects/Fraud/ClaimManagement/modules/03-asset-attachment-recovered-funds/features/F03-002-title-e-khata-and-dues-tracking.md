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
1. Who creates: Officer
2. How they create: Officer opens an existing attached asset.
3. How they edit: Officer updates title-transfer status and e-Khata creation progress.
4. How they send for approval: Officer enters dues obtained and dues paid with dates until Khata is created. Update title → e-Khata progress → dues → Khata created; then auction complete may be allowed (F03-004).
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. If the required path is not recorded, the Officer cannot mark auction complete (F03-004).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Title-transfer status on the asset.
- e-Khata creation progress.
- Dues obtained and paid with dates.
- Block auction-complete when the required title/e-Khata/dues path is missing.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My title, e-khata and dues tracking list / queue | Medium |
| Title, e-Khata and dues tracker | Complex |
| Title, e-khata and dues tracking history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Dues and title-path operations | Complex |
| Update title, e-khata and dues tracking | Medium |
| Search title, e-khata and dues tracking | Medium |
| Read title, e-khata and dues tracking history | Easy |

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
| My title, e-khata and dues tracking list / queue | UI | Medium | 6 |
| Title, e-Khata and dues tracker | UI | Complex | 12 |
| Title, e-khata and dues tracking history | UI | Medium | 6 |
| Dues and title-path operations | API | Complex | 8 |
| Update title, e-khata and dues tracking | API | Medium | 6 |
| Search title, e-khata and dues tracking | API | Medium | 6 |
| Read title, e-khata and dues tracking history | API | Easy | 4 |
| Title/dues persistence | DB | Medium | 4 |
| Title, e-Khata and dues tracking feature tests | Testing | Medium | 6 |
| Title, e-Khata and dues tracking implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
