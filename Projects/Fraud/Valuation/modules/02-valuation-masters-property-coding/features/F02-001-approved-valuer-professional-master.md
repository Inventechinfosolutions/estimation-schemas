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
1. Office user opens Valuer master and records name, Valuer Code, Category, Order Number, Rates of Valuation and Incidental Costs.
2. User links the master to the shared Person who will log in as that valuer.
3. Another Officer searches by Valuer Code and sees current rates.
4. Deactivating the master stops new assignments (F04-001) without creating a local password.

### Functional Capabilities
- Maintain Approved Valuer name, code, category, order number, rates and incidental costs
- Link each active master to one shared Person
- Search by Valuer Code
- Deactivate master to stop new assignments

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
|---|---|---|---:|
| Valuer professional master register | UI | Complex | 12 |
| Valuer master CRUD and Person link | API | Complex | 8 |
| Valuer master and rate history | Database | Medium | 4 |
| Shared Person link (no password store) | Integration | Easy | 8 |
| Valuer master tests | Testing | Complex | 8 |
| Valuer professional master guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Assignment UI is F04-001; billing application of rates is F08-002.
