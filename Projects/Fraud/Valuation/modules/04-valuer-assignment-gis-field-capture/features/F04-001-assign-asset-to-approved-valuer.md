# F04-001 — Assign asset to approved valuer

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Assign asset to approved valuer |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
An Office user opens an eligible 3(2) asset, selects an Approved Valuer from the professional master, and records Assignment Number, Assignment Date and assigned property details. Additional allotted names/mobiles are recorded in F04-008. The linked valuer Person then sees that asset in their assigned list. The Officer can reassign; the previous valuer loses the asset on the next open unless the Authority keeps a read-only history copy.

### Business Objective
Bind an eligible 3(2) asset to an approved valuer Person so field work can start.

### Actors
Office user; Approved Valuer.

### User Journey
1. Office user opens an eligible 3(2) asset (F03-004) that is not deactivated (F03-009).
2. User selects an Approved Valuer from the professional master (F02-001) and records Assignment Number, Assignment Date and assigned property details.
3. Linked valuer Person sees the asset in the assigned list (F04-002 / F09-002).
4. On reassign, the previous valuer loses the asset on next open unless the Authority keeps a read-only history copy.

### Functional Capabilities
- Assign eligible 3(2) asset to a valuer master/Person
- Record Assignment Number, Assignment Date and assigned property details
- Reassign with previous valuer loss of open rights (history copy if Authority requires)
- Exclude deactivated assets and assets not 3(2) prepared

### Inputs
Eligible asset; Valuer Code / master; Assignment Number; Assignment Date; assigned property details.

### Outputs
Assignment record; valuer assigned list membership; previous valuer exclusion on reassign.

### Business Rules
- Unassigned assets do not appear in the valuer dropdown (F04-002)
- Team names/mobiles are F04-008, not a second login directory
- Need-to-know follows this assignment (F01-003)

### Validations
- Asset 3(2) prepared and active
- Valuer master active and linked to a shared Person
- Assignment Number unique as the Authority requires

### Calculations
None (Time Taken uses Assignment Date in F07-006).

### Workflow
Select eligible asset → select valuer → save assignment → valuer list updates; reassign → rights move.

### Search Requirements
Assignment Number, valuer, asset, assignment date.

### Documents
None beyond the asset pack.

### Reports
Assignment register.

### Notifications
In-app presence on the valuer’s assigned list; no standalone notification product.

### Security
Office assigns; valuer cannot self-assign an unassigned asset.

### Integrations
Internal valuer master and 3(2) eligibility.

### Dependencies
F02-001; F03-004; F03-009; F01-003; F04-008.

### Assumptions
- Read-only history copy after reassign is an Authority choice.

### Risks
Reassignment without history copy loses the previous valuer’s working if not submitted.

### Non Functional Requirements
Assignment is attributable to the Office Person; CA Time Taken uses Assignment Date.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Valuer assignment form | UI | Medium | 6 |
| Assignment transaction and reassign | API | Complex | 8 |
| Assignment record | Database | Medium | 4 |
| Valuer-master eligibility consume | Integration | Simple | 4 |
| Assignment tests | Testing | Medium | 6 |
| Assignment note | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Visit/stage/team are F04-008; GIS capture is F04-006.
