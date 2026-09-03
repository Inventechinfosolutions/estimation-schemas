# F06-003 — Unify lists and update existing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-003 |
| **Feature Name** | Unify lists and update existing |
| **Module** | 06 — Unified Contact Database |

### Description
The user imports or merges another business contact list into the unified directory, or opens an existing contact and adds details, then saves without creating a duplicate where a match is confirmed.

### Business Objective
Convert multiple lists into one address book and update existing contacts without confirmed duplicates.

### Actors
Administrator; authorised Legal Cell.

### User Journey
1. Who creates: Administrator
2. How they create: User imports or merges another business contact list, or opens an existing contact and adds details.
3. How they edit: Reviews Duplicate Match Review where a match is proposed.
4. How they send for approval: Saves without creating a duplicate where a match is confirmed. Import → match review → merge or add → update existing.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Contact Import/Merge wizard
- Duplicate Match Review
- Update existing contact details
- No silent duplicate when match is confirmed
- Not a marketing CRM import

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Contact Import/Merge wizard | Very High |
| Duplicate Match Review | Complex |
| Unify lists and update existing history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Import and merge operations | Very High |
| Update unify lists and update existing | Medium |
| Search unify lists and update existing | Medium |
| Read unify lists and update existing history | Easy |

### Inputs
Source list file; match keys (name/phone/email); confirm/reject duplicate; additional details.

### Outputs
Unified contacts; merge log; rejected-duplicate decisions.

### Business Rules
- Unify/merge without confirmed duplicates.
- Unconfirmed matches must not auto-merge.
- Does not import Claim payee or valuation contacts as a hidden second purpose.

### Validations
- File type allowed; required columns; user confirmation before merge; existing contact id required for update path.

### Calculations
Match score/heuristic as configured — human confirms.

### Workflow
Import → match review → merge or add → update existing.

### Search Requirements
Merge log by date, source, operator.

### Documents
Imported source file retained for audit.

### Reports
Unify/merge log.

### Notifications
None required.

### Security
Import restricted; source file not published.

### Integrations
File import (Easy).

### Dependencies
F06-001; F06-002; F01-001.

### Assumptions
- SPLOCA supplies list formats; scanning of visiting cards is out of scope unless ordered.

### Risks
False-positive merge combines two different accused/advocates.

### Non Functional Requirements
Import of agreed batch sizes; auditable merge.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Contact Import/Merge wizard | UI | Very High | 16 |
| Duplicate Match Review | UI | Complex | 12 |
| Unify lists and update existing history | UI | Medium | 6 |
| Import and merge operations | API | Very High | 16 |
| Update unify lists and update existing | API | Medium | 6 |
| Search unify lists and update existing | API | Medium | 6 |
| Read unify lists and update existing history | API | Easy | 4 |
| Unify lists and update existing persistence | DB | Medium | 4 |
| File import | Integration | Easy | 8 |
| Unify lists and update existing feature tests | Testing | Complex | 8 |
| Unify lists and update existing implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **89** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
