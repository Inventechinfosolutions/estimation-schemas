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
1. Who creates: Officer
2. How they create: Officer opens tally for the depositor/claim.
3. How they edit: The system compares name and address on Aadhaar, PAN and EPIC with the bank passbook and the claim form.
4. How they send for approval: Officer sees each source side by side and the match-or-differ result. Compare on save or on demand → display tally → optional mismatch query (F04-006).
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Officer proceeds only after reviewing the tally; disagreements feed F04-006 mismatch queries.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Side-by-side name and address from Aadhaar, PAN, EPIC, passbook and claim form.
- Tally result match or differ per field/source.
- Hand off disagreements to auto mismatch queries (F04-006).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My name and address tally across id sources list / queue | Medium |
| Side-by-side name/address tally screen | Complex |
| Name and address tally across id sources history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Tally comparison operations | Complex |
| Update name and address tally across id sources | Medium |
| Search name and address tally across id sources | Medium |
| Read name and address tally across id sources history | Easy |

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
| My name and address tally across id sources list / queue | UI | Medium | 6 |
| Side-by-side name/address tally screen | UI | Complex | 12 |
| Name and address tally across id sources history | UI | Medium | 6 |
| Tally comparison operations | API | Complex | 8 |
| Update name and address tally across id sources | API | Medium | 6 |
| Search name and address tally across id sources | API | Medium | 6 |
| Read name and address tally across id sources history | API | Easy | 4 |
| Tally result persistence | DB | Medium | 4 |
| Name and address tally across ID sources feature tests | Testing | Complex | 8 |
| Name and address tally across ID sources implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
