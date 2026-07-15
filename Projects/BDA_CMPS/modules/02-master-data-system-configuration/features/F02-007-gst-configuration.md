# F02-007 — GST Configuration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-007 |
| **Feature Name** | GST Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain effective-dated GST configuration including HSN/SAC (if applicable), tax rates, and taxability by charge type for rent and related charges.

### Business Objective
Ensure billing can apply correct GST treatment as rates/policy change over time (M1-AC2).

### Actors
- Super Administrator, Accounts Officer

### User Journey
1. Admin maintains GST rates and charge-type taxability matrix.
2. Sets effective dates.
3. Billing resolves GST for demand lines using active config.

### Functional Capabilities
- HSN/SAC references (as applicable)
- Tax rates with effective dating
- Taxability by charge type (rent, penalty, CAM, etc.)
- Activate/deactivate, search, export
- Simple tax preview on sample taxable value

### Inputs
- Charge type, HSN/SAC, rate, CGST/SGST/IGST split as applicable, dates, status

### Outputs
- Versioned GST config
- Preview tax break-up

### Business Rules
- Effective-dated rates apply to new demand generation per billing date policy.
- Exempt/nil-rated charge types supported.
- Posted demands not auto-amended by later rate changes.

### Validations
- Rate ranges; sum of components = total where split used
- Date integrity; charge type required

### Calculations
- Tax amount preview = taxable value × rate (and splits)

### Workflow
Optional activation approval for rate changes.

### Search Requirements
By charge type, HSN/SAC, status, date.

### Documents
None.

### Reports
GST Configuration Register.

### Notifications
Alert Accounts on rate activation.

### Security
Tight configure permission; full audit.

### Integrations
None (no GSTN portal return filing in scope).

### Dependencies
Charge types from billing catalogue / F02-008 income-related types; Module 05 consumer.

### Assumptions
- No GSTR filing module; configuration for demand calculation only.
- Interstate IGST scenarios supported if BDA requires; confirm during design.

### Risks
- Incorrect taxability mapping causes compliance issues—needs Accounts sign-off.

### Non Functional Requirements
- Clear version history for audit

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| GST configuration screens | UI | Complex | 8 |
| GST config + effective dating APIs | API | Complex | 8 |
| GST rate / taxability entities | Database | Medium | 4 |
| GST config tests | Testing | Complex | 8 |
| GST configuration guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Does not include GST returns, e-invoicing, or GSTN integration.
