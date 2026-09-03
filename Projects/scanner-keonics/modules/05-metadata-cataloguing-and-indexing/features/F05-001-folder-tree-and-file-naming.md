# F05-001 — Folder Tree and File Naming

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Folder Tree and File Naming |
| **Module** | 05 — Metadata, Cataloguing and Indexing |

### Description
Apply the Department-approved folder tree and file name to each unique ID’s PDF/A so storage matches DMG / e-Office digitisation practice.

### Business Objective
Staff can find files on disk the same way they will in e-Office.

### Actors
Maker: Operator / Supervisor. Approver: none. Department may supply the pattern.

### User Journey
1. Who creates: Supervisor records the approved pattern once; Operator applies it per file.
2. How they create: Naming configuration → save pattern → on a file, apply path and generated or entered name → Save.
3. How they edit: Department may change pattern; new files follow new pattern; old paths remain.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox.
6. How the approver decides: No decision.
7. How the maker sees history: Current path/name on the file.
8. How the auditor sees history: Same.

### Functional Capabilities
- Store Department-approved naming pattern
- Apply path and file name per unique ID
- Unique name validation

### UI Screens
| Screen | Complexity |
|---|---|
| Naming configuration | Easy |
| Apply path and name form | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Save naming pattern | Medium |
| Apply path and name | Medium |
| Validate unique file name | Medium |

### Inputs
Pattern, unique ID, name components.

### Outputs
Storage path and file name.

### Business Rules
- Name uniqueness within the tree.
- Pattern comes from Department, not invented by operators.

### Validations
- Path and name mandatory before metadata complete.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
By path/name.

### Documents
PDF/A stored at that logical path.

### Reports
None.

### Notifications
None.

### Security
Supervisor edits pattern; Operators apply.

### Integrations
None.

### Dependencies
F03-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
Department delays the approved format.

### Non Functional Requirements
Simple pattern, not a full records-classification product.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Naming configuration | UI | Easy | 4 |
| Apply path and name form | UI | Medium | 6 |
| Save naming pattern | API | Medium | 6 |
| Apply path and name | API | Medium | 6 |
| Validate unique file name | API | Medium | 6 |
| Naming records | DB | Easy | 2 |
| Folder tree and file naming tests | Testing | Medium | 6 |
| Folder tree and file naming implementation documentation | Documentation | Easy | 2 |

**Feature total: 38 hours**
