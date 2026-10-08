# F03-005 — Vendor assignment

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F03-005 |
| Feature Name | Vendor assignment |
| Module | 03 — Campaign Management |
| Description | Assign vendors/agencies to campaigns and maintain assignment history for accountability. |
| Business Objective | Clarify which agency executes each campaign channel and preserve history when assignments change mid-flight. |
| Actors | Campaign Officer; Vendor User (read assigned); Administrator |

### User Journey

- Officer opens approved campaign → Vendor assignment panel → selects primary vendor per channel or overall → saves → prior assignment moves to history → vendor users see campaign in their limited register → reassignment requires reason.

### Functional Capabilities

- Assign/reassign vendor with effective date and role (primary/secondary)
- Assignment history grid with user, timestamp, reason
- Unassign with confirmation when no open PoD tasks depend on vendor
- Vendor workload hint (count of active assignments) on picker

### Inputs

- Vendor reference, channel scope, effective date, assignment reason

### Outputs

- Current assignment snapshot; historical rows

### Business Rules

- Only active vendors (F02-002) selectable
- Vendor users limited to campaigns where their agency is assigned
- Reassignment does not delete prior PoD captured under old vendor context

### Validations

- Mandatory vendor and effective date on assign

### Calculations

- Active assignment count per vendor (display only)

### Workflow

- Assign → (optional reassign) → close on campaign completion

### Search Requirements

- Campaign register filter by assigned vendor

### Documents

- None

### Reports

- Vendor workload report in Module 07

### Notifications

- Notify vendor contacts on new assignment (Module 08)

### Security

- Assignment action requires campaign update or dedicated assign permission

### Integrations

- None

### Dependencies

- F02-002; F03-001; F01 vendor role scoping

### Assumptions

- One primary vendor per channel is typical but not enforced as hard rule

### Risks

- Missed reassignment leaves vendor seeing stale campaigns

### Non Functional Requirements

- History grid paginated for long-running campaigns

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Campaign vendor assignment panel | Medium | 6 |
| UI | Vendor picker with channel capability filter | Medium | 6 |
| UI | Assignment scope matrix (district/channel) | Medium | 6 |
| UI | Remove vendor assignment confirmation | Simple | 2 |
| UI | Vendor assignment change history list | Easy | 4 |
| API | List vendor assignments for campaign | Easy | 4 |
| API | Assign vendor with district/channel scope | Medium | 6 |
| API | Update assignment scope | Medium | 6 |
| API | Remove assignment with active PoD guard | Easy | 4 |
| API | Validate vendor active and channel-capable | Medium | 6 |
| Database | Campaign–vendor assignment junction | Easy | 2 |
| Database | District and channel scope flags | Easy | 2 |
| Testing | Inactive vendor blocked on assign | Medium | 6 |
| Testing | Outdoor capability mismatch rejected | Medium | 6 |
| Testing | Duplicate assignment prevented | Easy | 4 |
| Documentation | Campaign vendor assignment guide | Easy | 2 |

**Feature Total: 72 hours**

### Estimation Assumptions

- Sub-contractor chains below primary vendor are out of scope.
