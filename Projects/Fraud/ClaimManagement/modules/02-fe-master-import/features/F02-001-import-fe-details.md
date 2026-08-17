# F02-001 — Import FE details

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Import FE details |
| **Module** | 02 — FE Master Import (from existing application) |

### Description
An authorised Officer or Administrator starts an FE import (or initial load) from the existing FE Management application. The system brings unique ID, name and aliases into this application as read-only references. The Officer then selects that FE on depositor, investment, asset, notification, intake and settlement screens. The Officer has no “Create FE dossier” action in this application.

### Business Objective
Supply claim modules with authoritative FE identity from the existing application without rebuilding an FE dossier.

### Actors
Officer; Administrator.

### User Journey
1. Officer or Administrator opens FE import and starts an import or initial load from the existing FE Management application.
2. The system brings unique ID, name and aliases in as read-only references.
3. Officer searches the imported FE register and confirms the FE is selectable.
4. Officer later selects that FE on depositor, investment, asset, notification, intake and settlement screens.
5. Officer finds no Create FE dossier, FIR, court or seized-corpus screens in this application.

### Functional Capabilities
- Trigger FE details import / initial load from the existing FE application.
- Store unique ID, name and aliases as read-only references.
- Provide FE lookup used by Modules 03–09.
- Omit any Create FE dossier action.

### Inputs
Import trigger, source FE unique ID/name/aliases as supplied by the existing application.

### Outputs
Read-only FE reference records; import run result (success, fail, counts).

### Business Rules
- Existing FE Management application is the system of record for the FE dossier.
- Imported FE records are selectable references only; they are not locally authored FIR/court/bank/seized corpora.
- Claim screens must not allow free-text creation of a new FE identity.

### Validations
- Import cannot complete without unique ID from the source.
- Duplicate unique IDs do not create a second FE identity (refresh is F02-004).

### Calculations
Import counts (read, inserted, skipped).

### Workflow
Authorised trigger → pull from existing FE application → store references → available for selection. No dossier workflow.

### Search Requirements
FE unique ID, name, aliases on the imported FE reference register.

### Documents
None of FIR, charge sheet, court order or seized papers; those remain in the existing application.

### Reports
FE import run log for Officer/Administrator.

### Notifications
On-screen import result; optional failure notice to the triggering user.

### Security
Only authorised Officer/Administrator Posts trigger import. Imported references follow need-to-know on later claim screens.

### Integrations
Existing FE Management application — FE details import (authoritative FE master).

### Dependencies
Module 01 access. Consumed by Modules 03–09.

### Assumptions
- The Authority provides working access to the existing FE application interface.
- Unique FE code generation remains in the existing application.

### Risks
- Poor source interface quality delays all claim modules that select an FE.
- Local editing of FE name would desynchronise from the dossier system of record.

### Non Functional Requirements
Import runs are auditable. Claim screens use searchable / type-ahead FE dropdowns. Interoperability with the existing FE application is mandatory.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| FE import run screen | UI | Complex | 12 |
| Imported FE reference register | UI | Medium | 6 |
| FE import orchestration | API | Very High | 16 |
| FE reference persistence | DB | Medium | 4 |
| Existing FE application FE-details import | Integration | Complex | 24 |
| FE import tests | Testing | Very High | 12 |
| FE import interface notes | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Import/export class API is Very High; multi-system FE master sync is Integration Complex (24), not a GIS Very High (40).
- Directors/promoters and schemes are estimated in F02-002 and F02-003.
