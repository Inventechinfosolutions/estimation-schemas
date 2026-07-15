# F02-004 — Rent Revision Rule Configuration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-004 |
| **Feature Name** | Rent Revision Rule Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Configure effective-dated rent revision rules supporting periodic percentage, slab-based, or fixed schedule models for application to new lease billings/revisions.

### Business Objective
Allow BDA to change escalation policy over time without code changes, correctly applied to new bill runs (M1-AC2).

### Actors
- Super Administrator, Accounts Officer, Estate Officer

### User Journey
1. Admin creates a rent revision rule with method and parameters.
2. Sets effective-from / effective-to.
3. Links applicability (lease type / property category as configured).
4. Activates rule; prior versions remain for history.
5. Billing/lease modules resolve the rule in force for a date.

### Functional Capabilities
- Rule types: periodic %, slab-based, fixed schedule
- Effective dating / versioning
- Activate/deactivate
- Simulation preview (sample rent → revised rent) preferred
- Search and export rule catalogue

### Inputs
- Rule code/name, method, parameters, slabs/schedule rows, effective dates, applicability filters, status

### Outputs
- Versioned rule definitions
- Preview result
- Lookup for Modules 04–05

### Business Rules
- Only one active rule per applicability bucket overlapping a date (or explicit priority).
- Future-dated rules allowed; past versions immutable except status notes.
- Changes apply to **new** bill runs / revisions per SOW—not silent rewrite of posted history.

### Validations
- Effective-from required; to ≥ from
- Slabs contiguous/non-overlapping
- Percentage/amount ranges sane

### Calculations
- Preview revised rent from base amount and rule method

### Workflow
Optional approval before activating high-impact rule (F02-009).

### Search Requirements
By code, method, status, effective date, lease type.

### Documents
None.

### Reports
Rule Catalogue export.

### Notifications
Optional alert to Accounts when new rule activated.

### Security
Configure permission; audit all versions.

### Integrations
None.

### Dependencies
F02-003; consumed by Modules 04–05.

### Assumptions
- Evaluation engine consumed by billing estimated partly here (rule ops) and partly in Module 05 bill run.
- Very High UI for dynamic rule designer.

### Risks
- Ambiguous overlapping applicability causes wrong escalation.
- Complex slab schedules need strong UAT cases from BDA.

### Non Functional Requirements
- Preview response interactive
- Version history always viewable

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Rent revision rule list | UI | Medium | 6 |
| Rent revision rule designer (%, slab, schedule) | UI | Very High | 16 |
| Rule CRUD + effective dating | API | Complex | 8 |
| Rule evaluation support operations | API | Complex | 8 |
| Rule version entities | Database | Medium | 4 |
| Rent revision rule tests | Testing | Very High | 12 |
| Rent revision configuration guide | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Rule designer UI = Very High (dynamic UI).
- Posted invoice reverse-calculation out of scope.
