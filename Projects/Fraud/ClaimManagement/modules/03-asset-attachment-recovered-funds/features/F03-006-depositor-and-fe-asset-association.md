# F03-006 — Depositor and FE asset association

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-006 |
| **Feature Name** | Depositor and FE asset association |
| **Module** | 03 — Asset Attachment & Recovered Funds |

### Description
On the asset record, the Officer links the imported FE (mandatory) and, where applicable, searches and selects a depositor profile. Later reports and claim checks can show that asset against that FE and depositor.

### Business Objective
Associate each attached asset to the imported FE and, where applicable, a depositor so reports and claim checks align.

### Actors
Officer.

### User Journey
1. Officer opens the asset record.
2. Officer confirms or selects the imported FE (mandatory).
3. Where applicable, Officer searches a depositor profile and selects it.
4. Later reports and claim checks show the asset against that FE and depositor.

### Functional Capabilities
- Mandatory imported-FE association on the asset.
- Optional depositor profile search and link.
- Expose associations to reports and claim checks.

### Inputs
Imported FE, optional depositor profile.

### Outputs
Asset–FE–depositor association used by Modules 07 and 09.

### Business Rules
- FE link is mandatory.
- Depositor link is used where applicable, not forced on every asset.

### Validations
- FE must be an imported reference (F02-001).
- Depositor must be an existing unique profile (F04-002) when linked.

### Calculations
None.

### Workflow
Select FE → optional depositor search → save association.

### Search Requirements
Depositor search by profile parameters; assets by FE and depositor.

### Documents
None additional.

### Reports
FE-wise / depositor-wise asset views in F09-006 consume this association.

### Notifications
None.

### Security
Depositor search respects need-to-know KYC visibility.

### Integrations
None.

### Dependencies
F03-001, F02-001; F04-002 when linking a depositor.

### Assumptions
- Not every attached asset has a single depositor; FE remains the mandatory anchor.

### Risks
- Wrong depositor link would mis-state claim-side asset checks.

### Non Functional Requirements
Depositor search uses unique-ID / name filters already required programme-wide.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| FE and depositor association panel | UI | Medium | 6 |
| Depositor search dialog for asset link | UI | Easy | 4 |
| Association operations | API | Complex | 8 |
| Association persistence | DB | Easy | 2 |
| Association tests | Testing | Medium | 6 |
| Association note | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Depositor master itself is Module 04; this feature only estimates the association.
