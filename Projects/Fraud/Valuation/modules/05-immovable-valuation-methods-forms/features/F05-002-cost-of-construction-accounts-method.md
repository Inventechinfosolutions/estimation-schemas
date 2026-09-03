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
1. Who creates: Approved Valuer
2. How they create: For a building where accounts are used, the Valuer enters materials-cost report, labour-cost report, and construction start and completion dates.
3. How they edit: Valuer selects a structure class from F02-007 for depreciation (economic life and residual/scrap).
4. How they send for approval: Valuer enters likely market value and the certificate that accounts and vouchers were produced. Enter accounts → select class → compute depreciation → certify → save working.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record. Save stores the working for the statutory form (F05-007).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Enter materials and labour cost reports and construction dates
- Depreciate using F02-007 class (override only with reason)
- Record likely market value and accounts/vouchers certificate
- Store working for Form V-1 / related forms

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My cost of construction — accounts method list / queue | Medium |
| Accounts method working | Complex |
| Cost of construction — accounts method history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Accounts and depreciation engine | Very High |
| Update cost of construction — accounts method | Medium |
| Search cost of construction — accounts method | Medium |
| Read cost of construction — accounts method history | Easy |

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
|---|---|---|---|
| My cost of construction — accounts method list / queue | UI | Medium | 6 |
| Accounts method working | UI | Complex | 12 |
| Cost of construction — accounts method history | UI | Medium | 6 |
| Accounts and depreciation engine | API | Very High | 16 |
| Update cost of construction — accounts method | API | Medium | 6 |
| Search cost of construction — accounts method | API | Medium | 6 |
| Read cost of construction — accounts method history | API | Easy | 4 |
| Cost of construction — accounts method persistence | DB | Medium | 4 |
| Structure-class consume | Integration | Simple | 4 |
| Cost of construction — Accounts method feature tests | Testing | Very High | 12 |
| Cost of construction — Accounts method implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **80** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
