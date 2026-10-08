# F03-004 — Budget & spend tracking

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-004 |
| Feature Name | Budget & spend tracking |
| Module | 03 — Campaign Management |
| Description | Record planned budget and track channel-wise spend against the campaign for DIPR oversight. |
| Business Objective | Support transparency on planned versus actual advertising expenditure by print, digital, and outdoor channel. |
| Actors | Campaign Officer; Manager; Auditor (read) |

### User Journey

- Officer enters planned budget by channel and optional budget head → records actual spend lines as invoices/media orders are confirmed → views variance summary on campaign → Manager reviews channel chart before approval renewals.

### Functional Capabilities

- Planned budget entry by channel (and budget head if enabled)
- Actual spend line register with date, amount, vendor, channel, reference note
- Variance summary (planned vs actual) on campaign financial tab
- Channel-wise spend chart for quick review
- Lock edits on closed campaigns except auditor notes

### Inputs

- Planned amounts by channel; spend line amount, date, channel, vendor, description, reference

### Outputs

- Budget plan and spend history; variance metrics for reporting

### Business Rules

- Spend lines cannot attach to draft-unapproved campaigns unless policy allows planning mode
- Totals roll up to campaign level for Module 07 dashboards
- Currency single-tenant (INR assumed unless DIPR states otherwise)

### Validations

- Non-negative amounts; mandatory channel on each line

### Calculations

- Channel and campaign totals; variance = planned − actual (or reverse per DIPR convention documented)

### Workflow

- Plan → spend entry ongoing → campaign closed freezes totals

### Search Requirements

- Filter campaigns by overspend flag (actual > planned)

### Documents

- Optional scan reference on spend line (metadata)

### Reports

- Channel spend export via Module 07

### Notifications

- Optional threshold alert when spend exceeds planned (Module 08)

### Security

- Financial update permission separated from generic campaign update where configured

### Integrations

- None (no payment gateway)

### Dependencies

- F03-001; vendor master F02-002

### Assumptions

- Actuals manually entered unless future ERP feed via Module 09

### Risks

- Manual entry errors until reconciliation integration exists

### Non Functional Requirements

- Spend register paginated; aggregations performant for reporting extracts

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign budget header summary panel | Medium | 6 |
| UI | Budget line-item spend entry grid | Complex | 12 |
| UI | Spend vs budget variance summary card | Easy | 4 |
| UI | Vendor-wise spend breakdown chart | Medium | 6 |
| UI | Budget revision request form | Medium | 6 |
| UI | Spend locked after campaign closed banner | Simple | 2 |
| API | Get budget and spend summary for campaign | Medium | 6 |
| API | CRUD budget line items | Medium | 6 |
| API | Record actual spend entry with validation | Complex | 8 |
| API | Calculate variance and burn rate | Medium | 6 |
| API | Enforce spend lock on closed campaign | Easy | 4 |
| Database | Budget header and line-item storage | Medium | 4 |
| Database | Spend transaction log | Easy | 2 |
| Database | Budget revision history | Easy | 2 |
| Testing | Over-budget warning rules | Medium | 6 |
| Testing | Closed campaign spend entry blocked | Easy | 4 |
| Testing | Line-item totals reconciliation | Medium | 6 |
| Documentation | Budget tracking notes for finance liaison | Easy | 2 |
| Documentation | UAT variance spot-check script | Easy | 2 |

**Feature Total: 94 hours**

### Estimation Assumptions

- Multi-currency and tax engine excluded from baseline.
