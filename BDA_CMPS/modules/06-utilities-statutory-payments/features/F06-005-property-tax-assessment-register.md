# F06-005 — Property Tax Assessment Register

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-005 |
| **Feature Name** | Property Tax Assessment Register |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
Maintain property tax assessments with assessment details, tax amount, due date, and computed outstanding so the register shows assessment, due, paid, and outstanding per property (M5-AC3).

### Business Objective
Track statutory property tax obligations for BDA commercial assets and prevent missed payments.

### Actors
- Tax Officer, Accounts Officer, Property Manager

### User Journey
1. Tax Officer creates assessment for a property (year/period).
2. Enters assessed amount, due date, assessment authority refs.
3. Payments posted in F06-006 update paid/outstanding.
4. Register and dashboards show outstanding (M5-AC3/M5-AC4).

### Functional Capabilities
- Assessment CRUD by property and period
- Fields: assessment details, tax amount, due date, status
- Outstanding = assessment − payments − adjustments
- Search/filter/export property tax register
- History of assessments per property

### Inputs
- Property, period, assessment refs, amount, due date, notes

### Outputs
- Assessment records; outstanding balances

### Business Rules
- Municipal tax calculation engine out of scope—record BDA’s assessed amounts.
- One active assessment per property+period unless revision/supplement allowed with versioning.
- Overdue assessments appear on notice candidates (F06-007).

### Validations
- Amount ≥ 0; unique property+period baseline
- Property in scope

### Calculations
- outstanding = assessed − paid − waived/adjusted

### Workflow
Draft → Confirmed → (Part)Paid / Overdue / Closed.

### Search Requirements
By property, period, status, overdue, amount range.

### Documents
Assessment notices optional upload (Module 08).

### Reports
Property Tax Register; Outstanding Tax by property (M5-AC3).

### Notifications
Via F06-007.

### Security
RBAC + scope; audit.

### Integrations
None.

### Dependencies
Module 03 property; F02 tax types; F06-006

### Assumptions
- No BBMP portal integration baseline.
- Revisions handled as adjusted assessment versions with audit.

### Risks
- Multi-demand tax components (library cess etc.) — model as lines if BDA requires during design.

### Non Functional Requirements
- Register export Excel; clear outstanding column

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Property tax assessment register | UI | Complex | 8 |
| Assessment create/edit form | UI | Complex | 8 |
| Assessment CRUD + outstanding ops | API | Complex | 8 |
| Tax assessment schema | Database | Medium | 4 |
| Property tax assessment tests | Testing | Complex | 8 |
| Property tax assessment guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Assessment and payment split across F06-005/006 for clarity.
