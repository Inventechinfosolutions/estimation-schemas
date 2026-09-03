# F04-003 — Outward Log and Physical Return

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Outward Log and Physical Return |
| **Module** | 04 — Quality Control and Physical Return |

### Description
After reconstitution (original tags/staples, serial page count), log return to the authorised Department officer with date-time and names/signatures fields matching the IFQ outward side of the register. Daily return.

### Business Objective
Every inward unique ID is either still in process or logged out intact.

### Actors
Maker: Operator/Supervisor. Department Officer: returned-to. Approver: none (countersignature is custody).

### User Journey
1. Who creates: Operator returning the physical file.
2. How they create: Outward register → unique ID → returned to (authorised officer), returned by, actual date/time, page count at return, damage flag if any → Department countersigns in tool or paper mirrored here.
3. How they edit: Correct only if both parties agree; history kept.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox. Files still in SP custody appear as not outward.
6. How the approver decides: No content decision.
7. How the maker sees history: Outward record on the file.
8. How the auditor sees history: Department Officer searches returns.

### Functional Capabilities
- Outward log fields
- Match to inward unique ID
- Damage flag
- List files not yet returned

### UI Screens
| Screen | Complexity |
|---|---|
| Outward log register | Medium |
| Outward log form | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Create outward log | Complex |
| Search outward logs | Medium |
| Match to inward | Medium |

### Inputs
Unique ID, returned to/by, datetime, page count, damage flag.

### Outputs
Custody closed for that day for that file.

### Business Rules
- Returned to / returned by authorised (F01-003).
- Page count at return recorded.
- Damage flagged for commercial penalty (penalty not calculated here).

### Validations
- Unique ID must be inward and not already outward unless re-issue (not typical).
- Authorised names.

### Calculations
None.

### Workflow
No approval inbox.

### Search Requirements
Date, officer, not-yet-returned.

### Documents
Physical file handed back.

### Reports
Returned vs in-process on MIS.

### Notifications
None.

### Security
Department Officer countersigns.

### Integrations
None.

### Dependencies
F02-002, F01-003.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Daily return is a process rule; the tool lists overdue expected-return dates.

### Risks
Files stay overnight without outward log.

### Non Functional Requirements
Handover desk speed.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Outward log register | UI | Medium | 6 |
| Outward log form | UI | Medium | 6 |
| Create outward log | API | Complex | 8 |
| Search outward logs | API | Medium | 6 |
| Match to inward | API | Medium | 6 |
| Outward log records | DB | Medium | 4 |
| Outward log and physical return tests | Testing | Medium | 6 |
| Outward log and physical return implementation documentation | Documentation | Easy | 2 |

**Feature total: 44 hours**
