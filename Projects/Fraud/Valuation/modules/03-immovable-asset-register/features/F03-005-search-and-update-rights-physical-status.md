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
1. Who creates: Office user
2. How they create: Officer searches by FE name, address or keyword within allotted FEs.
3. How they edit: Officer opens the asset and updates rights and physical status.
4. How they send for approval: System appends history (who, when, previous status, new status). Search → open → update status → append history → CA sees current.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record. Later CA assessment shows the current physical status.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Search by FE name, address and keywords within allotted FEs
- Update rights and physical status with history
- Show current physical status on CA assessment

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Immovable asset search (allotted FE) | Medium |
| Rights and physical-status update | Easy |
| Search and update rights / physical status history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Search and status-history | Medium |
| Update search and update rights / physical status | Medium |
| Search search and update rights / physical status | Medium |
| Read search and update rights / physical status history | Easy |

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
|---|---|---|---|
| Immovable asset search (allotted FE) | UI | Medium | 6 |
| Rights and physical-status update | UI | Easy | 4 |
| Search and update rights / physical status history | UI | Medium | 6 |
| Search and status-history | API | Medium | 6 |
| Update search and update rights / physical status | API | Medium | 6 |
| Search search and update rights / physical status | API | Medium | 6 |
| Read search and update rights / physical status history | API | Easy | 4 |
| Search and update rights / physical status persistence | DB | Medium | 4 |
| Internal status consume | Integration | Simple | 4 |
| Search and update rights / physical status feature tests | Testing | Complex | 8 |
| Search and update rights / physical status implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
