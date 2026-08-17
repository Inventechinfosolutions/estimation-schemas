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
1. Officer opens the asset and uploads the attachment order.
2. Officer enters valuation particulars in the prescribed e-format based on the valuation manual and saves.
3. If a Valuation pack is linked (EVAL F07-007), Officer consumes the accepted summary / display photos rather than recapturing GIS field data.
4. The order file remains available on the asset for settlement and audit.

### Functional Capabilities
- Upload and retain the attachment order on the asset.
- Capture valuation particulars in the prescribed e-format (summary, not field GIS).
- Consume linked accepted Valuation pack when present.

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
| Attachment order upload and e-format form | UI | Complex | 12 |
| E-format save operations | API | Complex | 8 |
| Order and e-format persistence | DB | Medium | 4 |
| Accepted Valuation pack consume (when linked) | Integration | Easy | 8 |
| Attachment order and e-format tests | Testing | Complex | 8 |
| E-format note | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Easy is REST/internal pack consume, not GIS Very High 40.
