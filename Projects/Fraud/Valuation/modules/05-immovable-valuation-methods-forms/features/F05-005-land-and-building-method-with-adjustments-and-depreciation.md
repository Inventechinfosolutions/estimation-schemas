# F05-005 — Land and Building method with adjustments and depreciation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-005 |
| **Feature Name** | Land and Building method with adjustments and depreciation |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
Where the FRS applicability tests hold, the Valuer derives land value from comparables (order of preference; minimum three), applies tabulated adjustment factors (location ±5% bands, time-gap/NPV or 18–24% p.a. if no instances, shape, size, FAR steps, side open, co-ownership 5–12.5%, tenure, encumbrance deferment up to 30%, unearned increase, 10% depressing effect), computes building as PWD-PAR reproduction minus depreciation (structure class from F02-007) plus builder’s efforts at 3% of B, using Le = L − Lf and Q = 0.9 × R × Le / I when p = 10%. Each override is reasoned. Property value is A + E.

### Business Objective
Run the land-and-building method with FRS default calculation rules, recorded overrides, and certified-class depreciation.

### Actors
Approved Valuer.

### User Journey
1. Where FRS applicability tests hold, the Valuer derives land value from comparables (order of preference; minimum three, or recorded basis where instances are absent — Form V-1 item 34).
2. Valuer applies tabulated adjustment/influence factors as in the FRS.
3. Building is PWD-PAR reproduction minus depreciation from F02-007 plus builder’s efforts at 3% of B, using Le = L − Lf and Q = 0.9 × R × Le / I when p = 10%.
4. Each override is reasoned. Property value is A + E. No generative AI.

### Functional Capabilities
- Applicability tests then land value from comparables (min. 3 or recorded basis)
- Apply FRS adjustment/influence factor table
- Building reproduction minus depreciation plus builder’s efforts @ 3% of B
- Compute Le, straight-line depreciation and Q as in the FRS; property value A + E
- Record reason on every override

### Inputs
Comparables; factor selections/overrides; PWD-PAR reproduction; structure class; p/residual as applicable.

### Outputs
Land-and-building working; property value A + E.

### Business Rules
- FRS percentages and formulae are default calculation rules, not unsupervised AI
- Minimum three sale instances or recorded basis where absent
- Structure class from F02-007

### Validations
- Applicability tests recorded
- Three comparables or basis
- Override reasons
- Class selected

### Calculations
Land adjustments per FRS bands; building B then E with builder’s efforts 3% of B; Le = L − Lf; Q = 0.9 × R × Le / I when p = 10%; property value A + E.

### Workflow
Tests → comparables → factors → building depreciation → A + E → save working.

### Search Requirements
Asset, method = land and building.

### Documents
Optional comparable sale copies.

### Reports
Land-and-building working extract.

### Notifications
None.

### Security
Assigned valuer; overrides attributable.

### Integrations
F02-007 structure class consume.

### Dependencies
F02-007; F05-001; F05-007.

### Assumptions
- PWD-PAR rates as used by the Authority are available to the valuer as reference data, not scraped unsupervised.

### Risks
Factor stacking; missing comparables; formula mis-application.

### Non Functional Requirements
Every override stored; calculation snapshot on the working.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Land-and-building method working | UI | Very High | 16 |
| Land-and-building valuation engine | API | Very High | 16 |
| L&B factors and depreciation store | Database | Very High | 10 |
| Structure-class consume | Integration | Simple | 4 |
| Land-and-building tests | Testing | Very High | 12 |
| Land-and-building method guide | Documentation | Very High | 6 |
| **Total** | | | **64** |

### Estimation Assumptions
- Method engine API Very High 16 as directed. UI Very High 16 for the factor/depreciation workspace.
