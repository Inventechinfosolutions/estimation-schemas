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
1. Who creates: Legal Cell
2. How they create: User selects Create Matter.
3. How they edit: Enters classification, description, imported FE, CA, court, opponents and date.
4. How they send for approval: Saves; the matter appears in Matter Search and on that user’s dashboard. Create Matter → enter fields → save → list/dashboard.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. FE is a programme reference, not a new FE dossier.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Create Matter form
- Matter Search/List
- Classification, description, imported FE, CA, court, opponents, date
- Matter visible on the creator’s dashboard after save
- No Claim settlement or eValueI case create

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Create Matter form | Complex |
| Matter Search/List | Medium |
| Create and classify matter history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create and classify operations | Complex |
| Update create and classify matter | Medium |
| Search create and classify matter | Medium |
| Read create and classify matter history | Easy |

### Inputs
Classification; description; FE reference; CA; court; opponents; date.

### Outputs
Matter record; search listing; dashboard card.

### Business Rules
- Matter is the hub for later tasks, documents, hearings, time and expenses.
- FE/CA are imported programme references, not a rebuilt FE application.
- Citizen matter portal is out of scope.

### Validations
- Classification, court and date required; FE/CA format as programme reference; opponents may be linked to contacts (Module 06) when known.

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
- Matter numbering scheme is agreed with SPLOCA.

### Risks
Creating a matter without FE/CA linkage fragments later reports.

### Non Functional Requirements
Save available for court-day use; auditable create.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Create Matter form | UI | Complex | 12 |
| Matter Search/List | UI | Medium | 6 |
| Create and classify matter history | UI | Medium | 6 |
| Create and classify operations | API | Complex | 8 |
| Update create and classify matter | API | Medium | 6 |
| Search create and classify matter | API | Medium | 6 |
| Read create and classify matter history | API | Easy | 4 |
| Create and classify matter persistence | DB | Medium | 4 |
| FE/CA programme reference import | Integration | Easy | 8 |
| Create and classify matter feature tests | Testing | Medium | 6 |
| Create and classify matter implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **68** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
