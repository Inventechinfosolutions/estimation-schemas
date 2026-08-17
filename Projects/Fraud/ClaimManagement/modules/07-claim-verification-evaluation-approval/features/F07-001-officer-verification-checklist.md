# F07-001 — Officer verification checklist

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Officer verification checklist |
| **Module** | 07 — Claim Verification, Evaluation & Approval |

### Description
An Officer opens a submitted claim and works through identity, investment details, scheme, customer ID, deposit records, uploads, bank details, previous returns, existing claims and eligibility, recording pass/fail or remarks on each item, then saves the checklist.

### Business Objective
Verify every submitted claim against the checklist items and store the result for the Competent Authority.

### Actors
Officer.

### User Journey
1. Officer opens a submitted claim (complete pack from Module 06).
2. Officer works through identity, investment details, scheme, customer ID, deposit records, uploads, bank details, previous returns, existing claims and eligibility.
3. Officer records pass/fail or remarks on each item and saves the checklist.

### Functional Capabilities
- Open submitted claim and work the full checklist.
- Record pass/fail or remarks per item.
- Save checklist without losing items.
- Use portfolio, KYC and imported scheme/FE as the comparison sources.

### Inputs
Submitted claim, KYC, portfolio, uploads, eligibility from the notification, existing claims.

### Outputs
Saved checklist with per-item results.

### Business Rules
- Every submitted claim can be verified against the checklist items and the result stored.
- Generative AI is prohibited. Agentic highlights are F07-003 and never auto-finalise.
- Need-to-know on the claim pack (F01-003/F01-009).

### Validations
- Checklist items are the SOW set (identity through eligibility).
- Save requires the Officer Person/Post attribution.

### Calculations
None beyond pass/fail tallies for the Officer’s view.

### Workflow
Open submitted claim → work items → save. Additional documents (F07-002) may pause and resume without losing ticks.

### Search Requirements
Submitted claims by FE, window, status, Officer.

### Documents
Pack documents already submitted; Officer views per F01-009.

### Reports
Checklist feeds the verification report (F07-004).

### Notifications
None required on save.

### Security
Only authorised Officer Posts. Checklist save is audited.

### Integrations
None (FIR/seized remain existing-app lookups in F05-007 if used as evidence).

### Dependencies
F06 submitted claims; F04; F05; F01.

### Assumptions
- Legal CMS petitions are out of this SOW.

### Risks
- Skipping checklist items would send an incomplete basis to the Competent Authority.

### Non Functional Requirements
Task-oriented checklist usable during claim-window volumes. No generative models.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Verification checklist workbench | UI | Very High | 16 |
| Checklist save operations | API | Complex | 8 |
| Checklist persistence | DB | Complex | 6 |
| Verification checklist tests | Testing | Very High | 12 |
| Verification checklist guide | Documentation | Complex | 4 |
| **Total** | | | **46** |

### Estimation Assumptions
- Uses Estimation Master values only.
- UI Very High is the dynamic checklist workbench (not UI Complex 8).
- Agentic highlight panel is F07-003.
