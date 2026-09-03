# F09-005 — Legacy web app and document-software hooks

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-005 |
| **Feature Name** | Legacy web app and document-software hooks |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
An authorised Officer or Administrator sends or retrieves agreed claim outcomes to the legacy / existing web application, and opens working copies in in-use document software (for example Idea or Adobe Suite) where that interface exists, without creating a second unofficial claim ledger.

### Business Objective
Interface with legacy/web app and in-use document software at business level without a duplicate claim ledger.

### Actors
Officer; Administrator.

### User Journey
1. Who creates: Officer
2. How they create: Authorised Officer or Administrator sends or retrieves agreed claim outcomes to the legacy / existing web application.
3. How they edit: Where the interface exists, user opens working copies in in-use document software (for example Idea or Adobe Suite).
4. How they send for approval: No second unofficial claim ledger is created. Select outcome → send/retrieve → optional open in document software.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Send/retrieve agreed claim outcomes to legacy / existing web application.
- Open working copies in in-use document software as interfaces allow.
- Avoid duplicate claim data island.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Outcome send/retrieve screen | Medium |
| Working-copy open action | Easy |
| Legacy web app and document-software hooks history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Handoff operations | Complex |
| Update legacy web app and document-software hooks | Medium |
| Search legacy web app and document-software hooks | Medium |
| Read legacy web app and document-software hooks history | Easy |

### Inputs
Agreed outcome payload, document working-copy reference.

### Outputs
Handoff confirmation; opened working copy; this application remains the claim ledger.

### Business Rules
- Legacy/web-application integration is a business interface, not a second claim ledger.
- Document software is for working copies and published packs as interfaces allow.
- FE dossier remains in the existing FE application (Module 02), not rebuilt here.

### Validations
- Only agreed outcome types are sent/retrieved.

### Calculations
None.

### Workflow
Select outcome → send/retrieve → optional open in document software.

### Search Requirements
Handoff runs by date, outcome type, status.

### Documents
Working copies in Idea/Adobe as allowed; originals remain in this application.

### Reports
Handoff log.

### Notifications
On-screen result.

### Security
Authorised Posts only. Handoffs audited. Need-to-know on outcomes.

### Integrations
Legacy system and existing web application; in-use document software (Idea, Adobe Suite and similar).

### Dependencies
Claim outcomes from Modules 06–08; Module 01.

### Assumptions
- Access to legacy and document-software interface points is provided.
- Interfaces allow the hooks; this is not a full DMS rebuild.

### Risks
- A parallel unofficial ledger would split settlement truth from court outputs.

### Non Functional Requirements
Interoperability with legacy web application and document-software hooks.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Outcome send/retrieve screen | UI | Medium | 6 |
| Working-copy open action | UI | Easy | 4 |
| Legacy web app and document-software hooks history | UI | Medium | 6 |
| Handoff operations | API | Complex | 8 |
| Update legacy web app and document-software hooks | API | Medium | 6 |
| Search legacy web app and document-software hooks | API | Medium | 6 |
| Read legacy web app and document-software hooks history | API | Easy | 4 |
| Handoff persistence | DB | Easy | 2 |
| Legacy / existing web application | Integration | Complex | 24 |
| Document software (Idea/Adobe) hook | Integration | Easy | 8 |
| Legacy web app and document-software hooks feature tests | Testing | Complex | 8 |
| Legacy web app and document-software hooks implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **86** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
