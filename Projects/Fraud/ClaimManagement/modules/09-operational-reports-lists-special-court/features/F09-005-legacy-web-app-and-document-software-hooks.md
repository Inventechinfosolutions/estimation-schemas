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
1. Authorised Officer or Administrator sends or retrieves agreed claim outcomes to the legacy / existing web application.
2. Where the interface exists, user opens working copies in in-use document software (for example Idea or Adobe Suite).
3. No second unofficial claim ledger is created.

### Functional Capabilities
- Send/retrieve agreed claim outcomes to legacy / existing web application.
- Open working copies in in-use document software as interfaces allow.
- Avoid duplicate claim data island.

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
| Handoff operations | API | Complex | 8 |
| Handoff persistence | DB | Easy | 2 |
| Legacy / existing web application | Integration | Complex | 24 |
| Document software (Idea/Adobe) hook | Integration | Easy | 8 |
| Legacy and document-software tests | Testing | Complex | 8 |
| Interface notes | Documentation | Complex | 4 |
| **Total** | | | **64** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Legacy integration is Complex (24). Document-software hook is Easy (8). Not GIS Very High 40.
