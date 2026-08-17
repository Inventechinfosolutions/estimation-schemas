# F03-005 — Search and update rights / physical status

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-005 |
| **Feature Name** | Search and update rights / physical status |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
An Officer searches by FE name, address or keyword within allotted FEs, opens the asset, and updates rights and physical status. The system appends history (who, when, previous status, new status). A later CA assessment still shows the current physical status.

### Business Objective
Find office assets within allotted FEs and keep an auditable rights/physical-status trail.

### Actors
Office user; Competent Authority (reads current status).

### User Journey
1. Officer searches by FE name, address or keyword within allotted FEs.
2. Officer opens the asset and updates rights and physical status.
3. System appends history (who, when, previous status, new status).
4. Later CA assessment shows the current physical status.

### Functional Capabilities
- Search by FE name, address and keywords within allotted FEs
- Update rights and physical status with history
- Show current physical status on CA assessment

### Inputs
Search terms; new rights text; new physical status.

### Outputs
Search results; updated status; history rows.

### Business Rules
- Search is scoped to allotted FEs unless CA/admin override (F03-008)
- History is append-only

### Validations
- Asset in scope
- New status from F02-006 physical-status list where used

### Calculations
None.

### Workflow
Search → open → update status → append history → CA sees current.

### Search Requirements
FE name, address, keyword, unique property code, physical status.

### Documents
None beyond the asset pack.

### Reports
Rights / physical-status change extract.

### Notifications
None.

### Security
Allotted-FE scope; status change attributable to Office Person.

### Integrations
Internal CA consume of current status.

### Dependencies
F03-001; F03-008; F02-006; F07-002.

### Assumptions
- Physical status values come from F02-006 where configured.

### Risks
Keyword search over-returning assets outside intended FE if scope fails.

### Non Functional Requirements
History retained; search responsive for office volumes.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Immovable asset search (allotted FE) | UI | Medium | 6 |
| Rights and physical-status update | UI | Easy | 4 |
| Search and status-history | API | Medium | 6 |
| Status history | Database | Medium | 4 |
| Internal status consume | Integration | Simple | 4 |
| Search/status tests | Testing | Complex | 8 |
| Search and status note | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Claim title/e-Khata workflow is out of scope.
