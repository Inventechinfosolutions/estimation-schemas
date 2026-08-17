# F05-002 — Cost of construction — Accounts method

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Cost of construction — Accounts method |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
For a building where accounts are used, the Valuer enters materials-cost report, labour-cost report, construction start and completion dates, depreciation using a class from the certified structure-classification master (F02-007) (economic life and residual/scrap), likely market value, and the certificate that accounts and vouchers were produced. Saving stores the working for the statutory form.

### Business Objective
Complete the accounts method of cost of construction with certified-class depreciation, not a one-off invented life.

### Actors
Approved Valuer.

### User Journey
1. For a building where accounts are used, the Valuer enters materials-cost report, labour-cost report, and construction start and completion dates.
2. Valuer selects a structure class from F02-007 for depreciation (economic life and residual/scrap).
3. Valuer enters likely market value and the certificate that accounts and vouchers were produced.
4. Save stores the working for the statutory form (F05-007).

### Functional Capabilities
- Enter materials and labour cost reports and construction dates
- Depreciate using F02-007 class (override only with reason)
- Record likely market value and accounts/vouchers certificate
- Store working for Form V-1 / related forms

### Inputs
Materials-cost report; labour-cost report; start/completion dates; structure class; likely market value; accounts certificate; optional override reason.

### Outputs
Accounts-method working stored for the statutory form.

### Business Rules
- Depreciation uses certified structure classification, not a typed one-off life unless override with reason
- Adjustment percentages and depreciation are default calculation rules the valuer applies or overrides with recorded reason — not unsupervised AI
- Generative AI shall not invent accounts

### Validations
- Class selected from F02-007
- Dates coherent
- Certificate recorded when accounts method is used

### Calculations
Depreciation from economic life and residual/scrap on the selected class; likely market value as entered/derived per FRS accounts method (valuer-applied, not AI).

### Workflow
Enter accounts → select class → compute depreciation → certify → save working.

### Search Requirements
Asset, method = accounts, class.

### Documents
Accounts/vouchers produced certificate (recorded); supporting files optional embedded.

### Reports
Accounts-method working extract.

### Notifications
None.

### Security
Assigned valuer; working attributable.

### Integrations
Structure-class consume from F02-007.

### Dependencies
F02-007; F05-001; F05-007.

### Assumptions
- FRS accounts-method formulae are applied as default rules with recorded overrides.

### Risks
Missing vouchers; wrong structure class.

### Non Functional Requirements
Store class values used at calculation time on the working.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Accounts method working | UI | Complex | 12 |
| Accounts and depreciation engine | API | Very High | 16 |
| Accounts working and depreciation store | Database | Complex | 6 |
| Structure-class consume | Integration | Simple | 4 |
| Accounts-method tests | Testing | Very High | 12 |
| Accounts method guide | Documentation | Complex | 4 |
| **Total** | | | **54** |

### Estimation Assumptions
- Method engine API Very High 16 as directed. Comparable built-up method is F05-003.
