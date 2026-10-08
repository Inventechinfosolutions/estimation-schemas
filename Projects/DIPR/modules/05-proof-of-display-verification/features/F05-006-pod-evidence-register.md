# F05-006 — PoD evidence register

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F05-006 |
| Feature Name | PoD evidence register |
| Module | 05 — Proof-of-Display Capture & Verification |
| Description | Searchable register of PoD evidence with campaign, site, and verification status for operations and audit. |
| Business Objective | Single pane for DIPR to monitor PoD pipeline volume, outcomes, and evidence retrieval during reviews. |
| Actors | Campaign Officer; PoD Verifier; Manager; Auditor |

### User Journey

- User opens PoD Evidence register → filters by campaign, district/site, verification status, rule failures, date → opens row detail → exports CSV slice for audit pack → drill from campaign rollup (F03-007) lands with filters pre-applied.

### Functional Capabilities

- Register columns: campaign, site, capture time, GPS summary, validation outcome, verification status, external status
- Rich filters including batch job ID and verifier
- Detail drawer linking to verification history and creative compare
- Export metadata slice (not bulk media) within row limits
- Bulk status chips for quick filter (pending, accepted, rejected, rework)

### Inputs

- Filter criteria; export request

### Outputs

- Paginated register; export file

### Business Rules

- Media download from register respects F04-005 and PoD access rules
- Auditors read-only; cannot change verification from register

### Validations

- Export caps enforced

### Calculations

- Optional column aggregates (counts by status on filtered set)

### Workflow

- Read-only navigation hub to action screens (F05-003)

### Search Requirements

- Full filter set above; saved views optional stretch via user presets (same as F04-004 pattern, light)

### Documents

- CSV export

### Reports

- Primary source for Module 07 compliance reports

### Notifications

- None from register itself

### Security

- Campaign/vendor scoping on rows

### Integrations

- None

### Dependencies

- All F05 capture and verification features

### Assumptions

- Media bulk export is separate controlled process outside register

### Risks

- Large register without indexes slows compliance reviews

### Non Functional Requirements

- Indexed queries for date and campaign; pagination mandatory

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | PoD evidence register with status filters | Medium | 6 |
| UI | Evidence detail with metadata stamp panel | Medium | 6 |
| UI | Chain-of-custody timeline on evidence | Easy | 4 |
| UI | Bulk verification status filter chips | Easy | 4 |
| UI | Register export for audit evidence pack | Medium | 6 |
| UI | Tamper/rule-fail indicator column | Simple | 2 |
| API | Search PoD evidence register | Medium | 6 |
| API | Get evidence detail with media references | Medium | 6 |
| API | Export register slice for audit | Medium | 6 |
| API | Append custody event on evidence access | Easy | 4 |
| Database | Evidence register denormalized view | Medium | 4 |
| Database | Custody event append log | Easy | 2 |
| Testing | Filter by campaign and verification status | Medium | 6 |
| Testing | Export cap and field mask by role | Medium | 6 |
| Testing | Custody events recorded on download | Easy | 4 |
| Documentation | PoD evidence register audit guide | Easy | 2 |

**Feature Total: 74 hours**

### Estimation Assumptions

- Map view of PoD pins deferred to Module 07 analytics unless DIPR prioritizes here.
