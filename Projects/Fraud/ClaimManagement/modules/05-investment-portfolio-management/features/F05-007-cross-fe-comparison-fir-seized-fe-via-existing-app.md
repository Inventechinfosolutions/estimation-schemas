# F05-007 — Cross-FE comparison (FIR / seized-FE via existing app)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-007 |
| **Feature Name** | Cross-FE comparison (FIR / seized-FE via existing app) |
| **Module** | 05 — Investment Portfolio Management |

### Description
The Officer selects one or more imported FEs and runs a duplication or collusion comparison across local investments, claims and attached assets. Where FIR or seized-FE data is needed, the Officer initiates a lookup to the existing FE application and reviews the returned indicators without storing a local FE dossier.

### Business Objective
Compare across FEs for duplication/collusion and look up FIR/seized indicators in the existing app without rebuilding an FE dossier.

### Actors
Officer.

### User Journey
1. Officer selects one or more imported FEs.
2. Officer runs duplication or collusion comparison across local investments, claims and attached assets.
3. Where FIR or seized-FE data is needed, Officer initiates a lookup to the existing FE application.
4. Officer reviews returned indicators without storing a local FE dossier.

### Functional Capabilities
- Cross-FE comparison of local investments, claims and attached assets.
- Lookup FIR / seized-FE indicators in the existing FE application.
- Display returned indicators without creating a local dossier (no FIR/court/seized corpus screens).

### Inputs
Imported FE selection, local portfolio/claim/asset data, lookup request.

### Outputs
Comparison results; viewed indicators from existing app (not a stored dossier).

### Business Rules
- FIR, court notifications, seized corpus and case status remain in the existing application.
- This application does not implement FE Management screens.
- Assists are rule-based; human reviews indicators.

### Validations
- Comparison requires at least one imported FE.

### Calculations
Duplication/collusion comparison rules on local data.

### Workflow
Select FEs → compare local data → optional existing-app lookup → review. No dossier workflow.

### Search Requirements
Comparison runs by FE, date, Officer.

### Documents
None stored as FE dossier papers.

### Reports
Comparison exception list.

### Notifications
None.

### Security
Lookup is authorised and audited. Indicators follow need-to-know.

### Integrations
Existing FE Management application — FIR / seized-FE lookup (not import of a dossier).

### Dependencies
F02-001, F05-001, Module 03 assets, Module 06 claims as available.

### Assumptions
- Existing FE application exposes lookup of FIR/seized indicators at business-interface level.

### Risks
- Storing returned FIR papers locally would recreate the excluded FE dossier.

### Non Functional Requirements
Interoperability with existing FE application; no second FE ledger.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Cross-FE comparison workbench | UI | Very High | 16 |
| Comparison and lookup operations | API | Very High | 16 |
| Comparison result persistence | DB | Medium | 4 |
| Existing FE application FIR/seized lookup | Integration | Complex | 24 |
| Cross-FE comparison tests | Testing | Very High | 12 |
| Cross-FE comparison guide | Documentation | Complex | 4 |
| **Total** | | | **76** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Complex is lookup/sync of indicators, not GIS and not rebuilding FE Management.
