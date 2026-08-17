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
1. Authorised Officer runs categorisation on portfolio data, using imported Director/Promoter names where relevant.
2. The system proposes depositor, colluder or accused under approved rules.
3. Officer accepts or overrides with remarks.
4. The category is stored on the profile for lists (F09-003) and verification (F07-001).

### Functional Capabilities
- Run rule-based categorisation using portfolio and imported Director/Promoter names.
- Propose depositor, colluder or accused.
- Require Officer accept or override with remarks.
- Store category for lists and verification.

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
| Categorisation workbench | UI | Complex | 12 |
| Categorisation rules and decision operations | API | Very High | 16 |
| Category persistence | DB | Medium | 4 |
| Categorisation tests | Testing | Complex | 8 |
| Categorisation guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Rule engine is API Very High; UI is the workbench, not a GIS dashboard.
