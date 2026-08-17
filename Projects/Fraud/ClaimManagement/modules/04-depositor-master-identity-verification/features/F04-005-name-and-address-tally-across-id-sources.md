# F04-005 — Name and address tally across ID sources

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Name and address tally across ID sources |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer (or the system on save) compares name and address on Aadhaar, PAN and EPIC with the bank passbook and the claim form. The Officer sees each source side by side and the tally result (match or differ) before proceeding.

### Business Objective
Show Officers a side-by-side name/address tally before identity is treated as consistent.

### Actors
Officer.

### User Journey
1. Officer opens tally for the depositor/claim.
2. The system compares name and address on Aadhaar, PAN and EPIC with the bank passbook and the claim form.
3. Officer sees each source side by side and the match-or-differ result.
4. Officer proceeds only after reviewing the tally; disagreements feed F04-006 mismatch queries.

### Functional Capabilities
- Side-by-side name and address from Aadhaar, PAN, EPIC, passbook and claim form.
- Tally result match or differ per field/source.
- Hand off disagreements to auto mismatch queries (F04-006).

### Inputs
Name/address as captured from each ID source, passbook and claim form.

### Outputs
Tally result set; inputs to mismatch queries.

### Business Rules
- Unverified Aadhaar name is not treated as proof (F04-009) even if displayed.
- Officer must see the tally before treating identity as clean.

### Validations
- Sources present are compared; missing source is shown as not available, not as a match.

### Calculations
Field-level match/differ.

### Workflow
Compare on save or on demand → display tally → optional mismatch query (F04-006).

### Search Requirements
Depositor/claim with differ flags.

### Documents
Underlying ID images remain originals; tally is structured.

### Reports
Tally exception list.

### Notifications
None beyond on-screen differ.

### Security
Side-by-side ID data is need-to-know.

### Integrations
None (compares captured values; Aadhaar verify is F04-009).

### Dependencies
F04-003, F04-009 for verified-Aadhaar status; claim form fields from Module 06 when present.

### Assumptions
- EPIC is captured when available; absence is recorded rather than invented.

### Risks
- Proceeding without viewing differ results would miss collusive or mistaken identity.

### Non Functional Requirements
Side-by-side layout is a staff task screen, not a public portal.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Side-by-side name/address tally screen | UI | Complex | 12 |
| Tally comparison operations | API | Complex | 8 |
| Tally result persistence | DB | Medium | 4 |
| ID-source tally tests | Testing | Complex | 8 |
| Tally guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Mismatch query workflow hours are in F04-006.
