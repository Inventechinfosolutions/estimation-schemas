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
1. Who creates: Office user
2. How they create: Office user opens an eligible 3(2) asset (F03-004) that is not deactivated (F03-009).
3. How they edit: User selects an Approved Valuer from the professional master (F02-001) and records Assignment Number, Assignment Date and assigned property details.
4. How they send for approval: Linked valuer Person sees the asset in the assigned list (F04-002 / F09-002). Select eligible asset → select valuer → save assignment → valuer list updates; reassign → rights move.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record. On reassign, the previous valuer loses the asset on next open unless the Authority keeps a read-only history copy.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Assign eligible 3(2) asset to a valuer master/Person
- Record Assignment Number, Assignment Date and assigned property details
- Reassign with previous valuer loss of open rights (history copy if Authority requires)
- Exclude deactivated assets and assets not 3(2) prepared

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My assign asset to approved valuer list / queue | Medium |
| Valuer assignment form | Medium |
| Assign asset to approved valuer history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Assignment transaction and reassign | Complex |
| Update assign asset to approved valuer | Medium |
| Search assign asset to approved valuer | Medium |
| Read assign asset to approved valuer history | Easy |

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
|---|---|---|---|
| My assign asset to approved valuer list / queue | UI | Medium | 6 |
| Valuer assignment form | UI | Medium | 6 |
| Assign asset to approved valuer history | UI | Medium | 6 |
| Assignment transaction and reassign | API | Complex | 8 |
| Update assign asset to approved valuer | API | Medium | 6 |
| Search assign asset to approved valuer | API | Medium | 6 |
| Read assign asset to approved valuer history | API | Easy | 4 |
| Assign asset to approved valuer persistence | DB | Medium | 4 |
| Valuer-master eligibility consume | Integration | Simple | 4 |
| Assign asset to approved valuer feature tests | Testing | Medium | 6 |
| Assign asset to approved valuer implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **58** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
