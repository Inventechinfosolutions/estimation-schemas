# F01-010 — Baseline Roles & Permission Seed

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F01-010 |
| **Feature Name** | Baseline Roles & Permission Seed |
| **Module** | 01 — User & Role Management |

### Description
Provide an initial seed of SOW-indicative roles and a baseline permission matrix that can be reviewed, applied in each environment, and exported for BDA design sign-off.

### Business Objective
Accelerate go-live readiness and satisfy the SOW expectation that vendors produce a role–permission matrix for BDA approval.

### Actors
- Super Administrator
- BDA design authority / product owner (reviewers)
- Auditor

### User Journey
1. After fresh deployment, Super Admin opens **Baseline RBAC Seed**.
2. Reviews list of indicative roles (Commissioner, Estate Officer, Accounts Officer, Tenant Portal, etc.).
3. Applies seed (skipping already-existing role codes).
4. Adjusts matrix via F01-005 as needed.
5. Exports matrix for formal sign-off.

### Functional Capabilities
- Seed indicative roles from SOW §8.1
- Seed baseline permissions (conservative least-privilege starter set)
- Idempotent apply (do not duplicate role codes)
- Export sign-off pack (Excel/PDF)
- Mark seed version applied in environment

### Inputs
- Confirm apply action
- Environment selection (implicit)

### Outputs
- Created/updated baseline roles
- Seed application log
- Sign-off matrix export

### Business Rules
- Seeding never silently widens an already customized matrix unless admin chooses **Reset to baseline** (dangerous — confirm + reason).
- Tenant (Portal) baseline permissions limited to self-service capabilities.
- Super Administrator receives full configure access.

### Validations
- Confirm dialog before apply/reset
- Reason required for reset-to-baseline

### Calculations
None.

### Workflow
Review → Apply seed → Adjust (F01-005) → Export → BDA sign-off (offline).

### Search Requirements
N/A beyond role list.

### Documents
Role–Permission Matrix sign-off pack.

### Reports
Baseline vs Current matrix differential (nice-to-have; baseline export mandatory).

### Notifications
Optional notify auditors that seed/reset was applied.

### Security
- Only Super Admin can apply/reset seed
- Reset heavily audited

### Integrations
None.

### Dependencies
- F01-005 permission catalog must exist
- Module list stable enough for matrix columns

### Assumptions
- Indicative roles exactly from SOW; fine-tuning during design workshops expected.
- Starter permissions are conservative and will be refined; estimate includes producing the sign-off documentation pack.
- Not a substitute for F01-005 ongoing administration.

### Risks
- Premature seeding before module action catalog stabilizes causes rework.
- Reset-to-baseline mis-use in production.

### Non Functional Requirements
- Idempotent, repeatable across Dev/UAT/Prod
- Exportable artefacts for committee review

---

## Section 2 — Estimation Breakdown (Estimation Master)

Complexity drivers: idempotent seed, conservative baseline pack, sign-off documentation, reset safeguards.

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Baseline roles review / apply screen | UI | Easy | 4 |
| Seed baseline roles & permissions operation | API | Complex | 8 |
| Seed data structures | Database | Easy | 2 |
| Baseline RBAC verification tests | Testing | Medium | 6 |
| BDA role–permission matrix pack | Documentation | Complex | 4 |
| **Total** | | | **24** |

### Estimation Assumptions
- Documentation Complex includes BDA-facing role–permission matrix deliverable content, not only technical README.
