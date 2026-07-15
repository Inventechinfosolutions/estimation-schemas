# F05-001 — Scheduled Demand Generation

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-001 |
| **Feature Name** | Scheduled Demand Generation |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Generate rent and related demands automatically for billing cycles via bulk bill runs by complex/property group, applying charge components including rent, advance, arrears carry, penalties, GST, interest, misc, parking, and CAM/lease-linked charges, with exception reporting (M4-AC1, M4-AC2).

### Business Objective
Automate accurate periodic revenue demands for all active leases to maximize collection readiness and reduce manual billing errors.

### Actors
- Accounts Officer, Revenue Officer
- Auditor (read-only after post)
- System scheduler

### User Journey
1. Officer opens Bill Run console for a billing period/cycle.
2. Selects scope (all / complex / property group) and reviews eligible leases.
3. Runs simulate or generate; reviews exception report (skipped leases, rule gaps).
4. Posts demands; tenants see dues; notices can be triggered (F05-008).

### Functional Capabilities
- Scheduled/on-demand bulk bill run
- Charge components: Monthly Rent, Advance Rent, Arrears, Penalties, GST, Interest, Miscellaneous, Parking rent, CAM/other lease-linked charges
- Apply Module 02 rent revision, penalty, GST rules by effective date
- Exception report for failures/skips
- Idempotent protection (no duplicate demand for same lease+period+charge type unless reversal path)
- Demand register search/export

### Inputs
- Billing period, cut-off params, scope filters, run options (simulate/post)

### Outputs
- Posted demands with charge lines
- Exception report
- Run audit log

### Business Rules
- Only active leases with billing commencement (Module 04 handover) are included (M4-AC1).
- GST and penalty calculations match configured rules (M4-AC2).
- Posted periods locked except via credit note/cancellation (F05-003).
- Utility recoveries may arrive as charge lines from Module 06 posting—not calculated here.

### Validations
- Period open; cut-off respected; lease eligibility
- Rule availability for charge types

### Calculations
- Rent from lease/effective amendment
- Penalty/interest per F02-005 and dues age
- GST per F02-007 by charge type
- Component totals and demand grand total

### Workflow
Draft run → Simulate → Review exceptions → Post → Locked demands.

### Search Requirements
Demands by period, lease, tenant, complex, status, amount range.

### Documents
Demand PDF optional via Module 08.

### Reports
Bill Run Summary; Exception Report; Demand Register (feeds Module 11).

### Notifications
Optional run completion; tenant demand notices via F05-008/Module 09.

### Security
RBAC; SoD simulate vs post if configured; full financial audit.

### Integrations
None external (rules internal). ERP push optional Module 10 later.

### Dependencies
Modules 02, 04; F02-004/005/007/011; Module 08/09

### Assumptions
- Financial engine complexity justifies dual Very High API rows (generation + calc).
- Bill run UI = Very High (wizard/console).
- Full GL not in scope.

### Risks
- Incorrect rule effective dating causes systematic under/over billing — heavy UAT pack required.
- Large portfolio performance for bill run — must be batch/async.

### Non Functional Requirements
- Bill run sized to BDA volume; progress/status visible
- Reconcile-able ledgers for closed test period

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Bill run console & exception review | UI | Very High | 16 |
| Demand register / demand detail views | UI | Complex | 8 |
| Scheduled bulk demand generation engine | API | Very High | 16 |
| GST/penalty/interest calculate operations | API | Very High | 16 |
| Demand & charge-line schema | Database | Complex | 6 |
| Bill run & calculation tests | Testing | Very High | 12 |
| Billing run operations guide | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- Testing Very High for financial correctness scenarios from BDA samples.
