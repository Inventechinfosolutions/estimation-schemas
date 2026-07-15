# F05-006 — Payment Allocation Engine

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-006 |
| **Feature Name** | Payment Allocation Engine |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Allocate payments (full/partial) across demand lines using configurable priority (e.g., penalty → interest → arrears → current) with preview and controlled override (M4-AC4).

### Business Objective
Ensure consistent application of money to dues categories per BDA policy.

### Actors
- Accounts Officer, System (auto on online/offline pay)

### User Journey
1. Payment amount captured (F05-004/005).
2. System proposes allocation by priority rules.
3. Officer may adjust if permitted; confirm.
4. Line balances and demand statuses update.

### Functional Capabilities
- Configurable allocation priority
- Auto-allocate for portal/online by default
- Preview before post (officer channel)
- Support unallocated residual (advance/on-account) if policy allows
- Reverse allocation on bounce/credit as linked events

### Inputs
- Payment amount, candidate demands, rule set, optional manual edits

### Outputs
- Allocation lines; updated outstanding

### Business Rules
- Partial payment allocation follows configured priority rules (M4-AC4).
- Default example: penalty → interest → arrears → current (configurable).
- Manual override requires permission + reason.

### Validations
- Sum allocations = payment (or residual policy)
- Cannot allocate to cancelled demands

### Calculations
- Waterfall allocation across sorted open lines

### Workflow
Propose → (Adjust) → Commit.

### Search Requirements
Allocation inquiry by payment/demand.

### Documents
None.

### Reports
Allocation exception log.

### Notifications
None mandatory.

### Security
Override permission tightly controlled; audit.

### Integrations
None.

### Dependencies
F05-001 demand lines; F05-004/005 payments; F02-011 params

### Assumptions
- Very High API for financial allocation engine.
- Testing Very High for matrix of priorities × partials × GST lines.

### Risks
- GST-inclusive line allocation ambiguity — design with Accounts.

### Non Functional Requirements
- Deterministic, explainable allocation results

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Allocation preview / override UI | UI | Complex | 8 |
| Payment allocation engine ops | API | Very High | 16 |
| Allocation rule/result entities | Database | Medium | 4 |
| Allocation engine tests | Testing | Very High | 12 |
| Allocation rules guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Core shared by all collection channels.
