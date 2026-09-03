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
1. Who creates: Officer
2. How they create: Officer opens the asset record.
3. How they edit: Officer confirms or selects the imported FE (mandatory).
4. How they send for approval: Where applicable, Officer searches a depositor profile and selects it. Select FE → optional depositor search → save association.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Later reports and claim checks show the asset against that FE and depositor.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Mandatory imported-FE association on the asset.
- Optional depositor profile search and link.
- Expose associations to reports and claim checks.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| FE and depositor association panel | Medium |
| Depositor search dialog for asset link | Easy |
| Depositor and fe asset association history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Association operations | Complex |
| Update depositor and fe asset association | Medium |
| Search depositor and fe asset association | Medium |
| Read depositor and fe asset association history | Easy |

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
| Depositor and fe asset association history | UI | Medium | 6 |
| Association operations | API | Complex | 8 |
| Update depositor and fe asset association | API | Medium | 6 |
| Search depositor and fe asset association | API | Medium | 6 |
| Read depositor and fe asset association history | API | Easy | 4 |
| Association persistence | DB | Easy | 2 |
| Depositor and FE asset association feature tests | Testing | Medium | 6 |
| Depositor and FE asset association implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **50** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
