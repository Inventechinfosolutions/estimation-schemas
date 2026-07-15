# F01-007 — Segregation of Duties Controls

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-007 |
| **Feature Name** | Segregation of Duties Controls |
| **Module** | 01 — User & Role Management |

### Description
Configure and enforce segregation-of-duties (SoD) constraints so conflicting privileges (e.g., demand creation vs collection vs refund approval) cannot be held by the same user contrary to policy.

### Business Objective
Meet SOW access principle for segregation of duties on sensitive finance actions and reduce fraud/error risk.

### Actors
- Super Administrator
- Auditor
- Accounts / Revenue supervisors (policy stakeholders)
- System (enforcement at role assignment and optionally at transaction time)

### User Journey
1. Admin defines SoD conflict pairs (permission A conflicts with permission B) or role pairs.
2. Admin attempts to assign conflicting roles/permissions to a user.
3. System blocks or warns based on rule severity (Block/Warn).
4. Auditor reviews SoD conflict report periodically.

### Functional Capabilities
- Maintain SoD rules (conflict pairs, severity, active flag)
- Evaluate conflicts on role assignment and permission matrix changes
- Optional runtime check before sensitive transactions (hook for Modules 05/07)
- SoD violation report/export

### Inputs
- Rule name, conflicting permissions/roles, severity (Block/Warn), status

### Outputs
- Validation error/warning on conflicting assignment
- SoD rules register and violation report

### Business Rules
- Baseline conflicts include: Demand create vs Collection post; Collection vs Refund approve; Write-off approve vs Demand create (final list confirmed with BDA).
- Block severity prevents save; Warn allows save with reason + audit.
- Super Administrator break-glass assignment requires reason capture.

### Validations
- Rule uniqueness
- Both sides of conflict must reference valid permissions/roles
- Reason mandatory on warn override

### Calculations
None.

### Workflow
Rule change may require dual control (optional). Assignment conflict handling as above.

### Search Requirements
- Search SoD rules
- Search users with warnings/overrides

### Documents
SoD policy matrix export.

### Reports
SoD Conflicts; Users with Overrides.

### Notifications
Alert auditor on Block override attempts / Warn overrides.

### Security
- Only Super Admin maintains SoD rules
- All overrides audited with reason

### Integrations
None.

### Dependencies
- F01-005 permission catalog
- F01-004 assignment flows
- Downstream finance modules for runtime hooks

### Assumptions
- Initial rule pack is small (finance-focused) and configurable.
- Full GRC SoD products are out of scope; lightweight configurable conflicts only.
- Enterprise enforcement and tests included.

### Risks
- Incomplete conflict catalog leaves residual risk.
- Overly strict rules may block legitimate dual-hat officers in smaller offices — needs BDA policy decisions.

### Non Functional Requirements
- Evaluation overhead negligible on user save
- Exportable reports for audit

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: configurable conflict model, block/warn behavior, assignment-time enforcement, audit overrides.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| SoD rules configuration screen | UI | Complex | 8 |
| SoD rule maintain & evaluate operations | API | Complex | 8 |
| SoD rule entities | Database | Easy | 2 |
| SoD conflict tests | Testing | Complex | 8 |
| SoD policy documentation | Documentation | Medium | 3 |
| **Total** | | | **29** |

### Estimation Assumptions
- Runtime transaction hooks in billing modules are thin checks calling shared evaluate API; major billing UX remains in Module 05 estimates.
