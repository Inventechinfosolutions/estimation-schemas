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
1. Who creates: Approved Valuer
2. How they create: Where FRS applicability tests hold, the Valuer derives land value from comparables (order of preference; minimum three, or recorded basis where instances are absent — Form V-1 item 34).
3. How they edit: Valuer applies tabulated adjustment/influence factors as in the FRS.
4. How they send for approval: Building is PWD-PAR reproduction minus depreciation from F02-007 plus builder’s efforts at 3% of B, using Le = L − Lf and Q = 0.9 × R × Le / I when p = 10%. Tests → comparables → factors → building depreciation → A + E → save working.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record. Each override is reasoned. Property value is A + E. No generative AI.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Applicability tests then land value from comparables (min. 3 or recorded basis)
- Apply FRS adjustment/influence factor table
- Building reproduction minus depreciation plus builder’s efforts @ 3% of B
- Compute Le, straight-line depreciation and Q as in the FRS; property value A + E
- Record reason on every override

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My land and building method with adjustments and depreciation list / queue | Medium |
| Land-and-building method working | Very High |
| Land and building method with adjustments and depreciation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Land-and-building valuation engine | Very High |
| Update land and building method with adjustments and depreciation | Medium |
| Search land and building method with adjustments and depreciation | Medium |
| Read land and building method with adjustments and depreciation history | Easy |

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
|---|---|---|---|
| My land and building method with adjustments and depreciation list / queue | UI | Medium | 6 |
| Land-and-building method working | UI | Very High | 16 |
| Land and building method with adjustments and depreciation history | UI | Medium | 6 |
| Land-and-building valuation engine | API | Very High | 16 |
| Update land and building method with adjustments and depreciation | API | Medium | 6 |
| Search land and building method with adjustments and depreciation | API | Medium | 6 |
| Read land and building method with adjustments and depreciation history | API | Easy | 4 |
| Land and building method with adjustments and depreciation persistence | DB | Medium | 4 |
| Structure-class consume | Integration | Simple | 4 |
| Land and Building method with adjustments and depreciation feature tests | Testing | Very High | 12 |
| Land and Building method with adjustments and depreciation implementation documentation | Documentation | Very High | 6 |
| **Total** | | | **86** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
