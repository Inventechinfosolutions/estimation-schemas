# F03-009 — Vacancy Management & Pipeline

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-009 |
| **Feature Name** | Vacancy Management & Pipeline |
| **Module** | 03 — Property & Asset Inventory |

### Description
Track vacant units with vacant-since date, expected revenue loss, marketing status, inspection readiness, proposed rent, and ready-for-allocation flags; provide pipeline views for estate managers (M2-AC3).

### Business Objective
Reduce vacancy leakage by making vacant stock, duration, and estimated loss visible and actionable for allotment handoff to Module 04.

### Actors
- Estate Officer, Property Manager
- Inspectors (readiness updates)
- Executives (pipeline summary)

### User Journey
1. Unit becomes Vacant (status lifecycle / lease termination).
2. System sets vacant-since; officer updates marketing status, proposed rent, inspection readiness.
3. Expected revenue loss updates from proposed/last rent × vacant days.
4. When ready-for-allocation is set, unit appears in Module 04 availability.

### Functional Capabilities
- Vacancy pipeline board/list (filters by complex, duration, marketing status)
- Fields: vacant since, marketing status, inspection status/readiness, proposed rent, ready-for-allocation
- Expected revenue loss calculation
- Vacancy report export (duration + loss) — M2-AC3
- Optional make-ready checklist link to inspections (Module 07) by reference

### Inputs
- Marketing status, proposed rent, inspection readiness, ready flag, notes

### Outputs
- Updated vacancy attributes
- Pipeline views
- Vacancy report

### Business Rules
- vacant_since set when entering Vacant; cleared when leaving Vacant.
- expected_revenue_loss = (proposed_rent or last_rent) × vacant_days (document source priority).
- Ready-for-allocation requires configured readiness gates (e.g., inspection OK) — configurable.
- Marketing status changes may require approval (per SOW workflow examples).

### Validations
- Proposed rent ≥ 0
- Ready flag only if status is Vacant (and gates pass)

### Calculations
- vacant_days = today − vacant_since
- expected_revenue_loss as above

### Workflow
Vacant → Make-ready / Market → Ready for Allocation → (Module 04 Application).
Marketing status change approval optional via F02-009.

### Search Requirements
Pipeline filters: duration buckets, marketing status, ready flag, complex, loss range.

### Documents
Marketing notes/photos optional via F03-006.

### Reports
Vacancy Report (unit, duration, estimated loss).

### Notifications
Alerts for long-vacant units (threshold configurable) via Module 09.

### Security
RBAC + scope; audit ready-flag and marketing changes.

### Integrations
None mandatory (inspection module reference only).

### Dependencies
F03-002, F03-004; Module 04 allotment; Module 07 inspection optional; Module 09

### Assumptions
- Last rent may come from Module 04/05 historical lease; if absent, proposed rent required for loss calc.
- Pipeline UI = Very High (workspace/board style).

### Risks
- Loss KPI debates (last vs proposed rent) — freeze formula with BDA.
- Double handling with Module 04 availability screens — share APIs, distinct UX owners.

### Non Functional Requirements
- Pipeline usable for daily estate operations
- Excel/PDF export of vacancy report

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Vacancy pipeline workspace | UI | Very High | 16 |
| Vacancy detail / make-ready fields | UI | Complex | 8 |
| Vacancy tracking & loss calculation ops | API | Complex | 8 |
| Vacancy attributes schema | Database | Medium | 4 |
| Vacancy management tests | Testing | Complex | 8 |
| Vacancy management guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Allotment application capture estimated in Module 04, not here.
