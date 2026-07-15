# F03-004 — Property Status Lifecycle

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F03-004 |
| **Feature Name** | Property Status Lifecycle |
| **Module** | 03 — Property & Asset Inventory |

### Description
Manage audited status transitions for properties/units across Vacant, Occupied, Under Maintenance, Reserved, Auctioned, Under Litigation, and Blocked, with configurable approvals.

### Business Objective
Control allotment eligibility and portfolio health reporting through a governed status model (M2-AC5).

### Actors
- Estate Officer, Property Manager
- Approvers (as configured)
- Module 04 lease process (system transitions to Occupied/Vacant)

### User Journey
1. Officer requests status change with reason and supporting dates/docs.
2. System validates allowed transition matrix.
3. Routes for approval if required.
4. On success, status updates; history retained; vacancy fields update when entering Vacant.

### Functional Capabilities
- Transition matrix (configurable defaults)
- Reason, effective date, remarks mandatory on controlled transitions
- Approval integration (F02-009)
- Full status history timeline
- System-driven transitions from lease handover/termination (API events from Module 04)
- Litigation: status + key dates + document links only (no case management)

### Inputs
- From/to status, reason, dates, attachments refs, approval action

### Outputs
- Updated status
- History entries
- Downstream vacancy/occupancy recalculation triggers

### Business Rules
- Occupied primarily via active lease handover (Module 04).
- Reserved = soft hold pending allotment; expiry of reserve configurable.
- Auctioned = post-auction capture status only (no bidding portal).
- Under Litigation / Blocked prevent new allotment.
- Under Maintenance may optionally block allotment.
- All transitions audited.

### Validations
- Transition allowed by matrix
- Approver authorization
- Cannot force Occupied without lease reference (except controlled data-migration role)

### Calculations
None (occupancy % in F03-007; vacancy loss in F03-009).

### Workflow
Request → (Approve) → Apply → Audit; or system auto-apply from lease events.

### Search Requirements
Filter inventory by status; history by date/user.

### Documents
Supporting docs via Module 08 (orders, litigation notes).

### Reports
Status Change Register; feeds Module 11.

### Notifications
Approval and completion alerts (Module 09).

### Security
RBAC; SoD if status impacts revenue eligibility; full audit.

### Integrations
None (internal lease events).

### Dependencies
F02-009; F03-001/002; Module 04; Module 08/09

### Assumptions
- Default transition matrix provided and adjustable in config (parameters or admin table).
- Testing Very High due to matrix × approval paths.

### Risks
- Manual Occupied overrides create billing inconsistencies — restrict tightly.

### Non Functional Requirements
- Immediate consistency for allotment availability checks

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Status change dialog + history view | UI | Complex | 8 |
| Status transition & approval operations | API | Complex | 8 |
| Status history entities | Database | Medium | 4 |
| Status lifecycle tests | Testing | Very High | 12 |
| Status lifecycle guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Approvals use Module 02 definitions; this estimates transition engine + UI + history.
