# F10-006 — Accounting / ERP Connector (Optional)

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-006 |
| **Feature Name** | Accounting / ERP Connector (Optional) |
| **Module** | 10 — API / Integration Hub |

### Description
Optional connector to push collections and expenses (and related journals) to an external Accounting/ERP system via APIs, with mapping and sync monitoring.

### Business Objective
Avoid dual data entry into BDA’s finance systems when approved for Phase 3.

### Actors
- Tech admin, Accounts, System

### User Journey
1. CPMS posts payment/expense events.
2. Hub maps to ERP chart/docs and pushes.
3. Failures retry; Accounts reviews sync monitor.

### Functional Capabilities
- Outbound push of collections/expenses
- Field mapping configuration
- Sync status & reprocess
- Optional inbound master sync (cost centers)—light if needed

### Inputs
- Domain events; mapping config

### Outputs
- ERP document refs; sync logs

### Business Rules
- Full GL replacement out of scope—hooks only.
- **Optional line item** for commercial proposal.

### Validations
- Mapping completeness before enable

### Calculations
None.

### Workflow
Event → Map → Push → Confirm.

### Search Requirements
Sync errors by date/type.

### Documents
Mapping workbook.

### Reports
Sync failure report.

### Notifications
Sync failure alerts.

### Security
Scoped ERP credentials; audit pushes.

### Integrations
Accounting/ERP — **Very High (40)**.

### Dependencies
F10-001; Modules 05/07 event feeds

### Assumptions
- Target ERP identified during engagement; if unknown, treat as provisional estimate.
- Not in Phase 1 mandatory scope.

### Risks
- ERP variance high until system chosen—quote as optional provisional.

### Non Functional Requirements
- Near-real-time or nightly batch modes configurable

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| ERP mapping & sync monitor UI | UI | Complex | 8 |
| ERP push/pull facade | API | Complex | 8 |
| ERP sync entities | Database | Medium | 4 |
| Accounting/ERP integration | Integration | Very High | 40 |
| ERP connector tests | Testing | Very High | 12 |
| ERP connector guide | Documentation | Complex | 4 |
| **Total** | | | **76** |

### Estimation Assumptions
- Optional; exclude from mandatory go-live total if Phase 3.
