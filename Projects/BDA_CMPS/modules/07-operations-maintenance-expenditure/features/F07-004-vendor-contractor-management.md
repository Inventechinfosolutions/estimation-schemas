# F07-004 — Vendor & Contractor Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-004 |
| **Feature Name** | Vendor & Contractor Management |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Maintain vendor/contractor registry with GST, PAN, bank details, agreements/AMC contracts, basic performance history/rating, and blacklist/inactive status.

### Business Objective
Provide a controlled supplier base for work assignment and expenditure.

### Actors
- Maintenance Officer, Accounts Officer, Chief Engineer, Super Admin

### User Journey
1. Officer registers vendor with statutory and bank details.
2. Uploads agreements/AMC; sets validity.
3. Assigns work from maintenance/expenditure features.
4. May blacklist/deactivate with reason; rate performance basically.

### Functional Capabilities
- Vendor CRUD
- GST, PAN, bank details
- Agreements & AMC with validity dates
- Performance history and basic rating
- Blacklist / inactive status
- Search/export vendor register
- Prevent assignment if blacklisted

### Inputs
- Vendor identity, tax IDs, bank, agreements, rating, status

### Outputs
- Vendor master; AMC register

### Business Rules
- Full e-procurement/e-tender out of scope.
- Blacklisted vendors cannot receive new work orders/expenses.
- AMC expiry alerts via Module 09 (optional).

### Validations
- GST/PAN format; unique vendor code
- Bank fields when payment linkage required

### Calculations
- Simple average rating from recorded scores

### Workflow
Optional approval for vendor onboarding (F02-009).

### Search Requirements
By name, GSTIN, status, AMC expiry, trade category.

### Documents
Agreements/AMC (Module 08).

### Reports
Vendor Register; AMC Report; Vendor Performance (Module 11).

### Notifications
AMC expiry reminders.

### Security
Mask bank accounts by role; RBAC; audit blacklist.

### Integrations
Internal DMS (Simple).

### Dependencies
Modules 01, 08, 09; consumed by F07-002/005/006

### Assumptions
- Vendor portal self-registration not baseline (officer-managed).
- Rating is basic—not full balanced scorecard.

### Risks
- Duplicate vendors by GST — uniqueness rules needed.

### Non Functional Requirements
- Excel export; PII masking for bank details

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Vendor register list + search | UI | Complex | 8 |
| Vendor profile / AMC / blacklist forms | UI | Complex | 8 |
| Vendor CRUD + status ops | API | Complex | 8 |
| Vendor & contract entities | Database | Medium | 4 |
| DMS agreement handoff | Integration | Simple | 4 |
| Vendor management tests | Testing | Complex | 8 |
| Vendor management guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Work assignment UX primarily F07-002; vendor master here.
