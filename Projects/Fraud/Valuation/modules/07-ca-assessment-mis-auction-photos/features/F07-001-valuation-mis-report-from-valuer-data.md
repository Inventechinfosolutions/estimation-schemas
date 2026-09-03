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
1. Who creates: Office user (authorised)
2. How they create: Authorised Office user or CA selects a valuation report format, enters the asset code, and generates the report from valuer-entered data (not a blank).
3. How they edit: Photos and videos tagged in F05-009 appear on the report.
4. How they send for approval: Re-generate after a valuer correction; prior versions remain in history. Select format → enter code → generate from valuer data → history on regenerate.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user (authorised) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user (authorised) opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Generate report from valuer details by asset code
- Include tagged photos/videos
- Keep prior versions on regenerate

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My valuation mis report from valuer data list / queue | Medium |
| Valuation MIS report generator | Very High |
| Valuation mis report from valuer data history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Report from valuer data | Very High |
| Update valuation mis report from valuer data | Medium |
| Search valuation mis report from valuer data | Medium |
| Read valuation mis report from valuer data history | Easy |

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
|---|---|---|---|
| My valuation mis report from valuer data list / queue | UI | Medium | 6 |
| Valuation MIS report generator | UI | Very High | 16 |
| Valuation mis report from valuer data history | UI | Medium | 6 |
| Report from valuer data | API | Very High | 16 |
| Update valuation mis report from valuer data | API | Medium | 6 |
| Search valuation mis report from valuer data | API | Medium | 6 |
| Read valuation mis report from valuer data history | API | Easy | 4 |
| Valuation mis report from valuer data persistence | DB | Medium | 4 |
| Valuer-data and media consume | Integration | Simple | 4 |
| Valuation MIS report from valuer data feature tests | Testing | Complex | 8 |
| Valuation MIS report from valuer data implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **80** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
