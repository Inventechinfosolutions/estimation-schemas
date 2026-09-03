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
1. Who creates: Officer
2. How they create: Officer or Administrator opens FE import and starts an import or initial load from the existing FE Management application.
3. How they edit: The system brings unique ID, name and aliases in as read-only references.
4. How they send for approval: Officer searches the imported FE register and confirms the FE is selectable. Authorised trigger → pull from existing FE application → store references → available for selection. No dossier workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer later selects that FE on depositor, investment, asset, notification, intake and settlement screens. Officer finds no Create FE dossier, FIR, court or seized-corpus screens in this application.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Trigger FE details import / initial load from the existing FE application.
- Store unique ID, name and aliases as read-only references.
- Provide FE lookup used by Modules 03–09.
- Omit any Create FE dossier action.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| FE import run screen | Complex |
| Imported FE reference register | Medium |
| Import fe details history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| FE import orchestration | Very High |
| Update import fe details | Medium |
| Search import fe details | Medium |
| Read import fe details history | Easy |

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
| Import fe details history | UI | Medium | 6 |
| FE import orchestration | API | Very High | 16 |
| Update import fe details | API | Medium | 6 |
| Search import fe details | API | Medium | 6 |
| Read import fe details history | API | Easy | 4 |
| FE reference persistence | DB | Medium | 4 |
| Existing FE application FE-details import | Integration | Complex | 24 |
| Import FE details feature tests | Testing | Very High | 12 |
| Import FE details implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **100** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
