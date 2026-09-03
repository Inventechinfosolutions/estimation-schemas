# F03-001 — Attached asset register

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Attached asset register |
| **Module** | 03 — Asset Attachment & Recovered Funds |

### Description
An Officer selects an imported FE, opens Asset registration, and records the attached asset (identification, location). The Officer saves the record in the recovery lifecycle. Another Officer can later search the same asset by FE or identification and open its current status. This is the claim-side attached-asset register, not GIS field valuation.

### Business Objective
Hold a searchable register of attached assets per imported FE for recovery and settlement.

### Actors
Officer; Competent Authority (view as authorised).

### User Journey
1. Who creates: Officer
2. How they create: Officer selects an imported FE (F02-001) and opens Asset registration.
3. How they edit: Officer records identification and location of the attached asset and saves it in the recovery lifecycle.
4. How they send for approval: Another Officer searches by FE or identification and opens the same asset’s current status. Register → subsequent title/e-Khata (F03-002), e-format (F03-003), auction (F03-004). Direct save with audit.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer does not capture 3(2) GIS field measurements or valuer Android work here.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Register attached assets against an imported FE.
- Capture identification and location.
- Search the register by FE or identification and open current status.
- Keep the asset in a recovery lifecycle without executing GIS valuation.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Asset registration form | Complex |
| Attached asset search register | Medium |
| Attached asset register history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Asset register and lifecycle operations | Complex |
| Update attached asset register | Medium |
| Search attached asset register | Medium |
| Read attached asset register history | Easy |

### Inputs
Imported FE, asset identification, location, initial recovery status.

### Outputs
Attached asset record; searchable asset register.

### Business Rules
- GIS field valuation (eValueI/eValueM), 3(2) field capture, valuer Android and CA valuation Accept are out of this project (Valuation SOW).
- FE is selected from imported references; Officers do not create an FE dossier.

### Validations
- Imported FE is mandatory.
- Identification is mandatory and searchable.

### Calculations
None on this register beyond lifecycle status.

### Workflow
Register → subsequent title/e-Khata (F03-002), e-format (F03-003), auction (F03-004). Direct save with audit.

### Search Requirements
Imported FE, asset identification, location, current status.

### Documents
Supporting documents are F03-005; attachment order is F03-003.

### Reports
Asset register extract (structured operational report in F09-006).

### Notifications
None required.

### Security
Need-to-know on asset records (F01-003). Actions attributable to Person in Post.

### Integrations
None for GIS. FE is a local imported reference.

### Dependencies
F02-001 imported FE; Module 01.

### Assumptions
- Auction sale execution and recovered funds live in this module (F03-004), not in Valuation.

### Risks
- Confusing this register with GIS field valuation would duplicate the Valuation SOW.

### Non Functional Requirements
Staff asset screens use practical filters. Structured asset data supports later reports (not PDF-on-homepage).

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Asset registration form | UI | Complex | 12 |
| Attached asset search register | UI | Medium | 6 |
| Attached asset register history | UI | Medium | 6 |
| Asset register and lifecycle operations | API | Complex | 8 |
| Update attached asset register | API | Medium | 6 |
| Search attached asset register | API | Medium | 6 |
| Read attached asset register history | API | Easy | 4 |
| Asset register persistence | DB | Medium | 4 |
| Attached asset register feature tests | Testing | Complex | 8 |
| Attached asset register implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
