# F03-003 — Attachment order and valuation e-format

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Attachment order and valuation e-format |
| **Module** | 03 — Asset Attachment & Recovered Funds |

### Description
The Officer uploads the attachment order against the asset and enters valuation particulars in the prescribed e-format based on the valuation manual, then saves. The order file remains available on the asset record for later settlement and audit. When linked, the Officer may consume an accepted GIS valuation pack / auction-display photos from Valuation; this feature does not perform GIS field valuation.

### Business Objective
Keep the attachment order and a valuation e-format summary on the claim-side asset for settlement and audit.

### Actors
Officer; settlement Officer (later reader); Competent Authority (view).

### User Journey
1. Who creates: Officer
2. How they create: Officer opens the asset and uploads the attachment order.
3. How they edit: Officer enters valuation particulars in the prescribed e-format based on the valuation manual and saves.
4. How they send for approval: If a Valuation pack is linked (EVAL F07-007), Officer consumes the accepted summary / display photos rather than recapturing GIS field data. Upload order → enter/consume e-format → save. No GIS survey workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. The order file remains available on the asset for settlement and audit.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload and retain the attachment order on the asset.
- Capture valuation particulars in the prescribed e-format (summary, not field GIS).
- Consume linked accepted Valuation pack when present.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My attachment order and valuation e-format list / queue | Medium |
| Attachment order upload and e-format form | Complex |
| Attachment order and valuation e-format history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| E-format save operations | Complex |
| Update attachment order and valuation e-format | Medium |
| Search attachment order and valuation e-format | Medium |
| Read attachment order and valuation e-format history | Easy |

### Inputs
Attachment order file; e-format valuation fields; optional linked Valuation pack reference.

### Outputs
Order on the asset; saved e-format particulars; available to settlement/audit.

### Business Rules
- GIS field valuation, valuer Android and CA valuation Accept are not in this project.
- E-format is based on the valuation manual as a claim-side summary.
- Auction-display photo selection remains a Valuation output when linked.

### Validations
- Attachment order upload is required before treating the asset as ordered, per policy.
- E-format mandatory fields per the prescribed layout.

### Calculations
None beyond storing e-format figures as entered/consumed.

### Workflow
Upload order → enter/consume e-format → save. No GIS survey workflow.

### Search Requirements
Assets with/without attachment order; by FE.

### Documents
Attachment order; optional consumed Valuation pack artefacts.

### Reports
None standalone; figures feed F03-004 recovered funds and F09 court outputs.

### Notifications
None.

### Security
Need-to-know on orders. Document view/download follows F01-009 where the order is in a pack context.

### Integrations
Optional consume of accepted GIS valuation pack from Valuation (internal programme handoff, not GIS capture).

### Dependencies
F03-001; Valuation SOW when pack is linked.

### Assumptions
- Prescribed e-format layout is supplied by the Authority / valuation manual.

### Risks
- Re-implementing GIS capture here would duplicate Valuation and inflate hours incorrectly.

### Non Functional Requirements
Order file remains retrievable. E-format is structured, not a homepage PDF.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My attachment order and valuation e-format list / queue | UI | Medium | 6 |
| Attachment order upload and e-format form | UI | Complex | 12 |
| Attachment order and valuation e-format history | UI | Medium | 6 |
| E-format save operations | API | Complex | 8 |
| Update attachment order and valuation e-format | API | Medium | 6 |
| Search attachment order and valuation e-format | API | Medium | 6 |
| Read attachment order and valuation e-format history | API | Easy | 4 |
| Order and e-format persistence | DB | Medium | 4 |
| Accepted Valuation pack consume (when linked) | Integration | Easy | 8 |
| Attachment order and valuation e-format feature tests | Testing | Complex | 8 |
| Attachment order and valuation e-format implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
