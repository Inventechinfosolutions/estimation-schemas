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
1. User imports or merges another business contact list, or opens an existing contact and adds details.
2. Reviews Duplicate Match Review where a match is proposed.
3. Saves without creating a duplicate where a match is confirmed.

### Functional Capabilities
- Contact Import/Merge wizard
- Duplicate Match Review
- Update existing contact details
- No silent duplicate when match is confirmed
- Not a marketing CRM import

### Inputs
Source list file; match keys (name/phone/email); confirm/reject duplicate; additional details.

### Outputs
Unified contacts; merge log; rejected-duplicate decisions.

### Business Rules
- Unify/merge without confirmed duplicates.
- Unconfirmed matches must not auto-merge.
- Does not import Claim payee or valuation contacts as a hidden second purpose.

### Validations
File type allowed; required columns; user confirmation before merge; existing contact id required for update path.

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
SPLOCA supplies list formats; scanning of visiting cards is out of scope unless ordered.

### Risks
False-positive merge combines two different accused/advocates.

### Non Functional Requirements
Import of agreed batch sizes; auditable merge.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Contact Import/Merge wizard | UI | Very High | 16 |
| Duplicate Match Review | UI | Complex | 12 |
| Import and merge operations | API | Very High | 16 |
| Match/merge entities | Database | Medium | 4 |
| File import | Integration | Easy | 8 |
| Unify/merge tests | Testing | Complex | 8 |
| Unify lists and update guide | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Free-text search is F06-004.
