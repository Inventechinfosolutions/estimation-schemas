# F06-006 — Property Tax Payments & Expenditure Link

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-006 |
| **Feature Name** | Property Tax Payments & Expenditure Link |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
Record property tax payments with challan/receipt uploads, payment history, and cross-link to expenditure when BDA pays tax (Module 07 reference).

### Business Objective
Evidence statutory tax payment and keep finance/expenditure views consistent.

### Actors
- Tax Officer, Accounts Officer

### User Journey
1. Officer opens assessment → Add Payment.
2. Enters amount, date, mode, challan refs; uploads challan/receipt.
3. Optionally creates/links Module 07 expenditure entry for Property Tax category.
4. Outstanding updates on assessment.

### Functional Capabilities
- Payment posting against assessment
- Challan and receipt upload
- Payment history by property
- Link/create expenditure reference (Module 07)
- Partial payments supported

### Inputs
- Assessment, amount, date, instrument/challan nos., documents, expenditure link

### Outputs
- Payment records; updated outstanding; optional expense ref

### Business Rules
- Payments cannot exceed outstanding without adjustment reason.
- Expenditure link is reference—not full AP payment run inside this module.
- Treasury integration optional Module 10 (not baseline here).

### Validations
- Amount > 0; assessment open; document type checks

### Calculations
- Running paid total; outstanding

### Workflow
Payment entry → Confirmed → (Optional expense link).

### Search Requirements
Payments by property, date, challan no., status.

### Documents
Challans/receipts (Module 08).

### Reports
Tax Payment History; paid vs due.

### Notifications
Optional payment confirmation internal.

### Security
RBAC; audit; document ACL.

### Integrations
Internal DMS (Simple); Internal expenditure link (Module 07).

### Dependencies
F06-005; Module 07; Module 08; F02-008 categories

### Assumptions
- Challans are uploaded scans; no e-challan scraping.

### Risks
- Double booking expense and tax payment — UI must show existing links.

### Non Functional Requirements
- Upload reliable for typical PDF/JPG sizes

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Tax payment entry & history UI | UI | Complex | 8 |
| Challan/receipt upload panel | UI | Medium | 6 |
| Tax payment & expenditure-link ops | API | Complex | 8 |
| Tax payment entities | Database | Medium | 4 |
| DMS challan/receipt handoff | Integration | Simple | 4 |
| Tax payment tests | Testing | Complex | 8 |
| Tax payment guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Module 07 expenditure feature owns expense CRUD; this estimates link/create hook.
