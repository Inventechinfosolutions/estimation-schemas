# F04-002 — Rescan and Defect Closure

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Rescan and Defect Closure |
| **Module** | 04 — Quality Control and Physical Return |

### Description
Track QC failures to rescan and a new QC pass at no extra commercial cost, including leftover/error work identified during or after the contract period.

### Business Objective
Failed images are not left in the delivered set.

### Actors
Maker: Operator (rescan); QC operator (re-check). Approver: none.

### User Journey
1. Who creates: System opens a defect when QC fails; Operator works it.
2. How they create: Defect register → open fail → rescan (updates F03) → QC repeats → Close defect on pass.
3. How they edit: Add note if Department asked a specific fix.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox; Supervisor uses open-defect register.
6. How the approver decides: No decision.
7. How the maker sees history: Defect timeline.
8. How the auditor sees history: Same.

### Functional Capabilities
- Open defects from QC fail
- Link rescan production
- Close only after QC pass
- Search open defects

### UI Screens
| Screen | Complexity |
|---|---|
| Defect register | Medium |
| Rescan closure form | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Open defect | Medium |
| Close defect after rescan | Medium |
| Search defects | Easy |

### Inputs
Unique ID, defect reason (from QC), closure note.

### Outputs
Closed defect; file eligible for metadata/upload path.

### Business Rules
- Cannot close without subsequent QC pass.
- No extra payment line.

### Validations
- Closure requires pass QC record newer than fail.

### Calculations
None.

### Workflow
Fail → rescan → QC; no checker.

### Search Requirements
Open vs closed, date.

### Documents
Updated PDF/A.

### Reports
Open defects on MIS.

### Notifications
None.

### Security
Operators and QC; Supervisor sees all.

### Integrations
None.

### Dependencies
F04-001, F03-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
Defects parked until contract end.

### Non Functional Requirements
Open-defect list on Supervisor landing.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Defect register | UI | Medium | 6 |
| Rescan closure form | UI | Easy | 4 |
| Open defect | API | Medium | 6 |
| Close defect after rescan | API | Medium | 6 |
| Search defects | API | Easy | 4 |
| Defect records | DB | Easy | 2 |
| Rescan and defect closure tests | Testing | Medium | 6 |
| Rescan and defect closure implementation documentation | Documentation | Easy | 2 |

**Feature total: 36 hours**
