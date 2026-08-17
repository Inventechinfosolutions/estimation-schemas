# F03-004 — Auction tracking and recovered funds

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Auction tracking and recovered funds |
| **Module** | 03 — Asset Attachment & Recovered Funds |

### Description
The Officer records auction milestones (including e-Governance consultation points) and the recovered amount. A settlement Officer later uses that recovered total when calculating available settlement fund; the two figures must match. Auction sale execution and recovered funds live here; Valuation only selects display photos and releases the pack.

### Business Objective
Track auction progress and lock recovered amount as the Module 03 total that settlement must reconcile to.

### Actors
Officer; settlement Officer; Competent Authority.

### User Journey
1. Officer records auction milestones, including e-Governance consultation points, on the asset.
2. Officer cannot mark auction complete if title/e-Khata/dues path is required and missing (F03-002).
3. Officer records the recovered amount.
4. Settlement Officer later uses that recovered total in F08-001; the figures must match.

### Functional Capabilities
- Auction milestone tracking including e-Governance consultation points.
- Record recovered amount on the asset / FE recovery total.
- Expose recovered total to settlement as the figure that must match available settlement fund.

### Inputs
Milestones, e-Governance consultation points, recovered amount, dates.

### Outputs
Auction status; recovered amount used by Module 08.

### Business Rules
- Recovered amount used in settlement must match this module’s totals.
- Failed GIS valuation is not performed here.
- Auction complete respects F03-002 path rules.

### Validations
- Recovered amount is numeric and dated.
- Milestone sequence follows the Authority’s auction path.

### Calculations
Sum of recovered amounts to FE / programme recovered total for settlement.

### Workflow
Milestones → (optional e-Governance points) → recovered amount → available to F08-001.

### Search Requirements
Assets by auction milestone, recovered amount present/absent, FE.

### Documents
Auction-related papers via F03-005; display photos from Valuation pack when linked.

### Reports
Recovered funds extract for settlement Officers.

### Notifications
None required beyond on-screen save confirmation.

### Security
Recovered amount changes are privileged and audited (forensic trail).

### Integrations
None to a public e-auction portal unless the Authority later specifies one; e-Governance consultation is recorded as milestones.

### Dependencies
F03-001, F03-002; consumed by F08-001.

### Assumptions
- Banking of recovered funds is recorded as amounts here; bank core systems are out of scope.

### Risks
- Mismatch between this recovered total and F08-001 would break court-facing settlement figures.

### Non Functional Requirements
Recovered figures are structured and reconcilable. Actions attributable to Person in Post.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Auction milestone tracker | UI | Complex | 12 |
| Recovered funds register | UI | Medium | 6 |
| Auction and recovered-amount operations | API | Very High | 16 |
| Auction and recovered-funds persistence | DB | Complex | 6 |
| Auction and recovered-funds tests | Testing | Very High | 12 |
| Auction and recovered-funds guide | Documentation | Complex | 4 |
| **Total** | | | **56** |

### Estimation Assumptions
- Uses Estimation Master values only.
- API Very High covers recovered-total integrity for settlement, not a payment gateway (out of scope).
