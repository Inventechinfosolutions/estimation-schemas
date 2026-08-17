# F07-001 — Valuation MIS report from valuer data

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Valuation MIS report from valuer data |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
An authorised Office user or CA selects a valuation report format, enters the asset code, and generates the report from data the valuer entered (not a blank). Photos and videos tagged in F05-009 appear on the report. The user can re-generate after a valuer correction; prior versions remain in history.

### Business Objective
Produce MIS/valuation reports from valuer-entered data, including tagged media, with version history.

### Actors
Office user (authorised); Competent Authority.

### User Journey
1. Authorised Office user or CA selects a valuation report format, enters the asset code, and generates the report from valuer-entered data (not a blank).
2. Photos and videos tagged in F05-009 appear on the report.
3. Re-generate after a valuer correction; prior versions remain in history.

### Functional Capabilities
- Generate report from valuer details by asset code
- Include tagged photos/videos
- Keep prior versions on regenerate

### Inputs
Report format; asset code.

### Outputs
Generated report; version history.

### Business Rules
- Not a blank template filled by the office as if it were the valuer
- Tagged media only from F05-009

### Validations
- Asset code populates an existing completed/available valuation
- Format is a configured valuation MIS format

### Calculations
None beyond presenting stored valuer calculations.

### Workflow
Select format → enter code → generate from valuer data → history on regenerate.

### Search Requirements
Asset code, report version, generated date.

### Documents
Generated valuation MIS report.

### Reports
The valuation MIS report (this feature).

### Notifications
None.

### Security
Authorised Office/CA; need-to-know on media.

### Integrations
Internal consume of valuer workings and F05-009 library.

### Dependencies
F05-007–F05-009; F06-005–F06-007 as applicable.

### Assumptions
- Report formats are those in Annexure-01 MIS/Admin report generation.

### Risks
Generating from incomplete unsigned forms.

### Non Functional Requirements
Version history retained.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Valuation MIS report generator | UI | Very High | 16 |
| Report from valuer data | API | Very High | 16 |
| Report version store | Database | Medium | 4 |
| Valuer-data and media consume | Integration | Simple | 4 |
| MIS report tests | Testing | Complex | 8 |
| Valuation MIS guide | Documentation | Complex | 4 |
| **Total** | | | **52** |

### Estimation Assumptions
- UI Very High 16 for report/dashboard-class generation.
