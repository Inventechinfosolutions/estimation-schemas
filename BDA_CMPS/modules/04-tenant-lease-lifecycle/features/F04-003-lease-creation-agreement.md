# F04-003 — Lease Creation & Agreement

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-003 |
| **Feature Name** | Lease Creation & Agreement |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Create lease records from approved applications with period, rent, escalation, grace, penalty/deposit rule links, multi-unit/parking linkage, and agreement generation/upload; enforce activation gates.

### Business Objective
Establish the contractual lease as the backbone for deposits, handover, billing commencement, and renewals.

### Actors
- Estate Officer, Property Manager, Accounts Officer
- Approvers

### User Journey
1. Officer creates lease from approved application.
2. Enters lease number (system/BDA), period, monthly rent, escalation, grace, rule links, special conditions.
3. Links one or more units and parking bays.
4. Generates/uploads lease agreement.
5. System blocks activation until KYC + approval + deposit (or waiver) satisfied (M3-AC1).

### Functional Capabilities
- Lease register CRUD (pre-active / active states)
- Link rent revision / penalty / deposit rules (Module 02)
- Multi-unit and parking bay linkage
- Agreement PDF generate from template and/or upload signed copy
- Activation checklist (KYC, application approved, deposit/waiver)
- Search/export lease register

### Inputs
- Lease terms, unit links, rule refs, agreement file/template data

### Outputs
- Lease record; agreement artefact; activation status

### Business Rules
- Lease cannot be activated without required KYC, approved application, and deposit collection or approved waiver (M3-AC1).
- Recurring demand generation is Module 05; this feature signals billing commencement eligibility after handover (F04-004).
- Amendments after activation use F04-005.

### Validations
- End date > start date; rent ≥ 0; at least one unit
- Rule refs active as of lease start

### Calculations
- Suggested deposit from deposit rule + rent (display; collection in F04-007)

### Workflow
Draft lease → validations → await deposit/handover → Active (post F04-004).

### Search Requirements
By lease no., tenant, unit, status, expiry window.

### Documents
Lease agreement, annexures (Module 08).

### Reports
Lease Register.

### Notifications
Activation / pending gate alerts.

### Security
RBAC; audit; document controls.

### Integrations
Template render may use notice/doc services (internal).

### Dependencies
F04-001/002; F02-004/005/006; Module 08; F04-007 deposit; F04-004 handover

### Assumptions
- Agreement generation = merge template to PDF; advanced CLM/e-sign optional later.
- Billing engine not included.

### Risks
- Activating without deposit waiver controls causes revenue leakage.

### Non Functional Requirements
- Large form performance acceptable; PDF download stable

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Lease register list | UI | Complex | 8 |
| Lease create/edit (terms, units, rules) | UI | Very High | 16 |
| Agreement generate/upload panel | UI | Medium | 6 |
| Lease CRUD + activation gates | API | Very High | 16 |
| Lease & linkage schema | Database | Complex | 6 |
| Lease creation tests | Testing | Very High | 12 |
| Lease creation guide | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Activation gate engine contributes to Very High API complexity.
