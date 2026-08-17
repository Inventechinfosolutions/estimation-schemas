# F04-001 — Create and classify matter

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Create and classify matter |
| **Module** | 04 — Matter Management |

### Description
A Legal Cell user or Advocate selects Create Matter, enters classification, description, imported FE, CA, court, opponents and date, and saves. The matter appears in search and on that user’s dashboard.

### Business Objective
Open a court matter as the hub record with classification, FE/CA references, court, opponents and date.

### Actors
Legal Cell; Advocate.

### User Journey
1. User selects Create Matter.
2. Enters classification, description, imported FE, CA, court, opponents and date.
3. Saves; the matter appears in Matter Search and on that user’s dashboard.
4. FE is a programme reference, not a new FE dossier.

### Functional Capabilities
- Create Matter form
- Matter Search/List
- Classification, description, imported FE, CA, court, opponents, date
- Matter visible on the creator’s dashboard after save
- No Claim settlement or eValueI case create

### Inputs
Classification; description; FE reference; CA; court; opponents; date.

### Outputs
Matter record; search listing; dashboard card.

### Business Rules
- Matter is the hub for later tasks, documents, hearings, time and expenses.
- FE/CA are imported programme references, not a rebuilt FE application.
- Citizen matter portal is out of scope.

### Validations
Classification, court and date required; FE/CA format as programme reference; opponents may be linked to contacts (Module 06) when known.

### Calculations
None.

### Workflow
Create Matter → enter fields → save → list/dashboard.

### Search Requirements
Matter number/title, FE, CA, court, classification, date, opponent.

### Documents
None at create except later filings.

### Reports
New matters register.

### Notifications
Optional notice to assigned team when a matter is created.

### Security
Create restricted to Legal Posts; visibility follows spaces and Post.

### Integrations
FE/CA reference import from programme/common data (Easy) — not Claim settlement APIs.

### Dependencies
F01-001; F02-001; F02-005; F04-002 dashboard.

### Assumptions
Matter numbering scheme is agreed with SPLOCA.

### Risks
Creating a matter without FE/CA linkage fragments later reports.

### Non Functional Requirements
Save available for court-day use; auditable create.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Create Matter form | UI | Complex | 12 |
| Matter Search/List | UI | Medium | 6 |
| Create and classify operations | API | Complex | 8 |
| Matter entities | Database | Medium | 4 |
| FE/CA programme reference import | Integration | Easy | 8 |
| Create matter tests | Testing | Medium | 6 |
| Create and classify matter guide | Documentation | Easy | 2 |
| **Total** | | | **46** |

### Estimation Assumptions
- Dashboard widgets are F04-002.
- Variables edit is F04-003.
