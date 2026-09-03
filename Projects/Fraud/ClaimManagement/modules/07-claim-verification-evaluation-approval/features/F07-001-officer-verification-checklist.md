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
1. Who creates: Officer
2. How they create: Officer opens a submitted claim (complete pack from Module 06).
3. How they edit: Officer works through identity, investment details, scheme, customer ID, deposit records, uploads, bank details, previous returns, existing claims and eligibility.
4. How they send for approval: Officer records pass/fail or remarks on each item and saves the checklist. Open submitted claim → work items → save. Additional documents (F07-002) may pause and resume without losing ticks.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Open submitted claim and work the full checklist.
- Record pass/fail or remarks per item.
- Save checklist without losing items.
- Use portfolio, KYC and imported scheme/FE as the comparison sources.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My officer verification checklist list / queue | Medium |
| Verification checklist workbench | Very High |
| Officer verification checklist history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Checklist save operations | Complex |
| Update officer verification checklist | Medium |
| Search officer verification checklist | Medium |
| Read officer verification checklist history | Easy |

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
| My officer verification checklist list / queue | UI | Medium | 6 |
| Verification checklist workbench | UI | Very High | 16 |
| Officer verification checklist history | UI | Medium | 6 |
| Checklist save operations | API | Complex | 8 |
| Update officer verification checklist | API | Medium | 6 |
| Search officer verification checklist | API | Medium | 6 |
| Read officer verification checklist history | API | Easy | 4 |
| Checklist persistence | DB | Complex | 6 |
| Officer verification checklist feature tests | Testing | Very High | 12 |
| Officer verification checklist implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **74** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
