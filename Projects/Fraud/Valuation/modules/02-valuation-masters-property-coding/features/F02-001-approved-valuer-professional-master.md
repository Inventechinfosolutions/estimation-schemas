# F02-001 — Approved valuer professional master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Approved valuer professional master |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
An Office user opens Valuer master and records Approved Valuer name, Valuer Code, Category, Order Number, Rates of Valuation and Incidental Costs. The user links that master to the shared Person who will log in. Another Officer can later search by Valuer Code and see current rates. Deactivating the master stops new assignments; it does not invent a second password store.

### Business Objective
Register approved valuers as professional master data (category, order, rates) distinct from login credentials.

### Actors
Office user; Administrator.

### User Journey
1. Who creates: Office user
2. How they create: Office user opens Valuer master and records name, Valuer Code, Category, Order Number, Rates of Valuation and Incidental Costs.
3. How they edit: User links the master to the shared Person who will log in as that valuer.
4. How they send for approval: Create/update master → link Person → active for assignment; deactivate → no new assignment.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Office user opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Maintain Approved Valuer name, code, category, order number, rates and incidental costs
- Link each active master to one shared Person
- Search by Valuer Code
- Deactivate master to stop new assignments

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Valuer professional master register | Complex |
| Approved valuer professional master create/edit form | Medium |
| Approved valuer professional master change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Valuer master CRUD and Person link | Complex |
| Update approved valuer professional master | Medium |
| Search approved valuer professional master register | Medium |
| Read approved valuer professional master change history | Easy |

### Inputs
Valuer name, Valuer Code, Category, Order Number, Rates of Valuation, Incidental Costs, linked shared Person, deactivate reason.

### Outputs
Professional valuer master row; current rates visible on search; assignment eligibility flag.

### Business Rules
- This is not the login record
- Each active valuer master is linked to the shared Person who logs in
- Deactivation stops new assignments; it does not store a second password
- Bill rates in Module 08 read from this master unless an authorised override is recorded

### Validations
- Valuer Code unique
- Linked Person exists on the shared component
- Rates and incidental costs present before the master is used on a bill

### Calculations
None on this feature (billing applies rates in F08-002).

### Workflow
Create/update master → link Person → active for assignment; deactivate → no new assignment.

### Search Requirements
Valuer Code, name, category, order number, active/inactive.

### Documents
Optional appointment/order scan stored on the master (embedded, not a DMS).

### Reports
Approved valuer register with current rates.

### Notifications
None.

### Security
Only authorised Office/Admin maintain rates. Login remains shared Person.

### Integrations
Lookup/link shared Person from Claim Module 01 (no credential write).

### Dependencies
F01-001; F01-002.

### Assumptions
- SPLOCA supplies the initial approved-valuer list and rate schedule.

### Risks
Unlinked master would allow assignment to a professional row with no login Person.

### Non Functional Requirements
Rate history retained when rates change; current rate used unless bill override (F08-002).

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Valuer professional master register | UI | Complex | 12 |
| Approved valuer professional master create/edit form | UI | Medium | 6 |
| Approved valuer professional master change history | UI | Medium | 6 |
| Valuer master CRUD and Person link | API | Complex | 8 |
| Update approved valuer professional master | API | Medium | 6 |
| Search approved valuer professional master register | API | Medium | 6 |
| Read approved valuer professional master change history | API | Easy | 4 |
| Approved valuer professional master identity persistence | DB | Medium | 4 |
| Shared Person link (no password store) | Integration | Easy | 8 |
| Approved valuer professional master feature tests | Testing | Complex | 8 |
| Approved valuer professional master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
