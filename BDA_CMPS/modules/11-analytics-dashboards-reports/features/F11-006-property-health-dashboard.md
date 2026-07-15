# F11-006 — Property Health Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-006 |
| **Feature Name** | Property Health Dashboard |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Property health dashboard for high expense / low revenue properties, vacancy trend, lease expiry pipeline, and utility consumption trend; widgets update from live status/dates (M8-AC4).

### Business Objective
Highlight at-risk assets and upcoming lease actions for management intervention.

### Actors
- Estate leadership, Accounts, executives

### User Journey
1. Open Health Dashboard.
2. Review outlier properties, vacancy trend, expiry pipeline, utility trend.
3. Drill to vacancy/lease/expense detail.

### Functional Capabilities
- High expense / low revenue lists (thresholds configurable)
- Vacancy trend chart
- Lease expiry pipeline (lead buckets)
- Utility consumption trend (where readings exist)
- Live status/date driven (M8-AC4)

### Inputs
- Filters; threshold params

### Outputs
- Health widgets and lists

### Business Rules
- Lease expiry and vacancy trend from Modules 03–04 live data (M8-AC4).
- Thresholds configurable via parameters.

### Validations
Threshold ≥ 0.

### Calculations
- Trend series; expiry bucket membership; expense/revenue ratios

### Workflow
N/A.

### Search Requirements
Outlier lists searchable/filterable.

### Documents
None.

### Reports
Links to vacancy/expiry reports.

### Notifications
Optional threshold alerts via Module 09 (not required baseline).

### Security
Scoped.

### Integrations
None.

### Dependencies
F11-001; Modules 03–06

### Assumptions
- Utility trend empty-state when no readings.

### Risks
- Noisy outliers if thresholds wrong—tune in UAT.

### Non Functional Requirements
- Trend queries efficient (pre-agg if needed)

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Property health dashboard UI | UI | Very High | 16 |
| Health trend KPI ops | API | Complex | 8 |
| Trend snapshot support | Database | Medium | 4 |
| Property health tests | Testing | Complex | 8 |
| Property health guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Very High dashboard UI with multiple widgets.
