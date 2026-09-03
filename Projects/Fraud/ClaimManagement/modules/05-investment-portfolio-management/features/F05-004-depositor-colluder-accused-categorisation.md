# F05-004 — Depositor / colluder / accused categorisation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-004 |
| **Feature Name** | Depositor / colluder / accused categorisation |
| **Module** | 05 — Investment Portfolio Management |

### Description
An authorised Officer runs the categorisation action on portfolio data (using imported Director/Promoter names where relevant). The system proposes depositor, colluder or accused under approved rules. The Officer accepts or overrides with remarks; the category is stored on the profile for lists and verification.

### Business Objective
Propose depositor/colluder/accused under approved rules, with mandatory human accept or override.

### Actors
Authorised Officer.

### User Journey
1. Who creates: Authorised Officer
2. How they create: Authorised Officer runs categorisation on portfolio data, using imported Director/Promoter names where relevant.
3. How they edit: The system proposes depositor, colluder or accused under approved rules.
4. How they send for approval: Officer accepts or overrides with remarks. Run → propose → Officer accept/override → store. Human confirmation mandatory.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised Officer opens history on the record. The category is stored on the profile for lists (F09-003) and verification (F07-001).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Run rule-based categorisation using portfolio and imported Director/Promoter names.
- Propose depositor, colluder or accused.
- Require Officer accept or override with remarks.
- Store category for lists and verification.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My depositor / colluder / accused categorisation list / queue | Medium |
| Categorisation workbench | Complex |
| Depositor / colluder / accused categorisation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Categorisation rules and decision operations | Very High |
| Update depositor / colluder / accused categorisation | Medium |
| Search depositor / colluder / accused categorisation | Medium |
| Read depositor / colluder / accused categorisation history | Easy |

### Inputs
Portfolio data, imported Director/Promoter names, Officer decision and remarks.

### Outputs
Stored category on the profile; audit of proposal and decision.

### Business Rules
- Assists are rule-based, not generative.
- No assist finalises category without human confirmation.
- Overrides require remarks.

### Validations
- Category is one of depositor / colluder / accused (or Authority-approved set).
- Override without remarks is refused.

### Calculations
Rule evaluation against approved categorisation rules.

### Workflow
Run → propose → Officer accept/override → store. Human confirmation mandatory.

### Search Requirements
Category, FE, depositor profile.

### Documents
None required beyond existing portfolio/people references.

### Reports
Accused and colluder lists consume stored category (F09-003).

### Notifications
None.

### Security
Categorisation is privileged and audited. Need-to-know on profiles.

### Integrations
None (Director/Promoter names already imported).

### Dependencies
F05-001, F02-002, F04-002.

### Assumptions
- Approved categorisation rules are supplied by the Authority.

### Risks
- Auto-finalising accused status would violate the no-unattended-assist rule.

### Non Functional Requirements
Human confirmation is required on every proposal. No generative models.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My depositor / colluder / accused categorisation list / queue | UI | Medium | 6 |
| Categorisation workbench | UI | Complex | 12 |
| Depositor / colluder / accused categorisation history | UI | Medium | 6 |
| Categorisation rules and decision operations | API | Very High | 16 |
| Update depositor / colluder / accused categorisation | API | Medium | 6 |
| Search depositor / colluder / accused categorisation | API | Medium | 6 |
| Read depositor / colluder / accused categorisation history | API | Easy | 4 |
| Category persistence | DB | Medium | 4 |
| Depositor / colluder / accused categorisation feature tests | Testing | Complex | 8 |
| Depositor / colluder / accused categorisation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
