# F06-003 — Utility Bill Lifecycle

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-003 |
| **Feature Name** | Utility Bill Lifecycle |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
Record and track utility bills (Electricity, Water, DG, CAM, Sewage, others) including bill amount, due date, payment status, and uploads—for both BDA-paid property bills and informational tracking.

### Business Objective
Centralize utility statutory/operational payment tracking to avoid missed dues and support expenditure linkage.

### Actors
- Utility Officer, Accounts Officer, Property Manager

### User Journey
1. Officer creates utility bill for property/meter/period.
2. Enters amount, due date; uploads bill PDF; links reading if metered.
3. Updates payment status and uploads receipt when paid.
4. Overdue items surface for notices/dashboard (F06-007 / Module 11).

### Functional Capabilities
- Utility types as configured
- Bill register with due/paid/outstanding
- Upload bills/receipts (Module 08)
- Link to meter reading (F06-002) when applicable
- Modes: (i) BDA-paid recoverable, (ii) informational property-level tracking
- Search/export

### Inputs
- Type, property/meter, period, amounts, due date, attachments, payment status

### Outputs
- Utility bill records; payment history on bill

### Business Rules
- External portal auto-fetch out of scope.
- Payment of BDA-paid bills may create/link expenditure in Module 07 (reference).
- Recovery to tenant handled in F06-004 when enabled—not automatic on bill save unless configured.

### Validations
- Amount ≥ 0; due date present; duplicate period warnings

### Calculations
- Optional amount suggestion from units × rate if rate card configured (simple); else manual amount

### Workflow
Draft → Confirmed → Paid/Part-paid/Overdue.

### Search Requirements
By type, property, due date, status, overdue flag.

### Documents
Bills/receipts in Module 08.

### Reports
Utility Bill Register; overdue utilities.

### Notifications
Overdue alerts via F06-007.

### Security
RBAC + scope; audit status changes.

### Integrations
Internal DMS (Simple).

### Dependencies
F06-001/002; Modules 07–09; F02 utility types

### Assumptions
- Simple optional rate×units; not a full tariff engine like DISCOM billing.
- Very large tariff slabs out of baseline.

### Risks
- Mixing recoverable vs informational without clear flags causes wrong tenant charging.

### Non Functional Requirements
- Clear status badges; Excel export

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Utility bill register & detail | UI | Complex | 8 |
| Utility bill create/edit + uploads | UI | Complex | 8 |
| Utility bill lifecycle ops | API | Complex | 8 |
| Utility bill entities | Database | Medium | 4 |
| DMS bill/receipt handoff | Integration | Simple | 4 |
| Utility bill tests | Testing | Complex | 8 |
| Utility bill guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Two Complex UIs: register and bill form with uploads.
