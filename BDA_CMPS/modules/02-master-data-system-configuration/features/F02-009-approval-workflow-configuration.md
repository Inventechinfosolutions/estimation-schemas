# F02-009 — Approval Workflow Configuration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-009 |
| **Feature Name** | Approval Workflow Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Configure multi-level approval workflows by transaction type and amount threshold (property creation, lease, refunds, write-offs, expenditure above threshold, vacancy marketing status changes, etc.).

### Business Objective
Enable maker-checker and multi-level approvals without a standalone BPM product, meeting M1-AC3.

### Actors
- Super Administrator
- Process owners (Accounts, Estate) as reviewers of config
- Business modules (runtime consumers)

### User Journey
1. Admin selects transaction type.
2. Defines approval levels, roles/queues, and amount thresholds.
3. Activates definition with effective date.
4. Business modules route submissions using active definition.

### Functional Capabilities
- Workflow definitions per transaction type
- Multi-level steps mapped to roles (Module 01)
- Amount threshold conditions
- Activate/deactivate and version/effective date
- Clone definition
- Preview routing for sample amount/role

### Inputs
- Transaction type, steps, roles, thresholds, SLA/escalation flags (light), status, effective dates

### Outputs
- Active workflow definitions
- Routing preview
- Config export for sign-off

### Business Rules
- One active definition per transaction type (or per type+sub-type) overlapping a date.
- Runtime approval engine remains inside business modules using this configuration (no separate Workflow Engine module).
- Changes apply to newly submitted transactions; in-flight follow policy (complete on old version vs migrate — configurable default: old version).

### Validations
- At least one step; roles must exist
- Threshold bands non-overlapping where used
- No empty approver role

### Calculations
- Threshold band resolution for sample amount

### Workflow
N/A (this feature configures workflows; does not run them).

### Search Requirements
By transaction type, status, effective date.

### Documents
Workflow configuration matrix export.

### Reports
Active Workflow Catalogue.

### Notifications
Optional notify impacted role owners on activation (via Module 09).

### Security
Only Super Admin / Configure Workflow permission; full audit.

### Integrations
None (runtime notify later via Module 09).

### Dependencies
Module 01 roles; consumed by Modules 03–07.

### Assumptions
- Not a full BPMN engine; configurable sequential multi-level approvals with thresholds.
- Parallel multi-approver voting out of baseline unless requested.
- Very High UI for designer.

### Risks
- Over-complex real BDA org chart vs simple role steps may require iteration.
- In-flight version policy disputes.

### Non Functional Requirements
- Config usable without developer intervention
- Export for committee sign-off

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Workflow definition list | UI | Medium | 6 |
| Approval workflow designer (levels/thresholds) | UI | Very High | 16 |
| Workflow definition CRUD | API | Complex | 8 |
| Workflow definition entities | Database | Medium | 4 |
| Workflow config tests | Testing | Very High | 12 |
| Approval workflow config guide | Documentation | Complex | 4 |
| **Total** | | | **50** |

### Estimation Assumptions
- Runtime approval screens/effort belong to each business module’s features; this estimates configuration only.
- Testing Very High for matrix of transaction types × thresholds.
