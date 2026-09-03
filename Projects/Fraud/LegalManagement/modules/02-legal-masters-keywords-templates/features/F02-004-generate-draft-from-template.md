# F02-004 — Generate draft from template

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-004 |
| **Feature Name** | Generate draft from template |
| **Module** | 02 — Legal Masters, Keywords & Templates |

### Description
A Legal Cell user or Advocate opens a matter, selects a template type, fills the matter/FE/CA/addressee fields, generates the draft, reviews it on screen, and only then marks it ready to issue. There is no generative-AI compose action.

### Business Objective
Produce statutory and court drafts from stored templates with mandatory human verification before issue.

### Actors
Legal Cell; Advocate; Competent Authority (review where required).

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens a matter and selects Generate Draft From Template.
3. How they edit: Chooses type (e.g. 5(2), notice, 7(1), 8(1), Caveat) from available templates (F02-003).
4. How they send for approval: Fills matter, FE, CA and addressee fields (Tahsildar, Banks, Claimants, Competent Authority or Government as applicable). Select matter → select template → fill fields → generate → on-screen review → human verify → ready to issue.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Generates the draft and reviews it on the Draft Preview screen. Marks ready to issue only after human verification; no generative-AI compose control exists.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Generate Draft From Template wizard
- Draft Field Fill and Preview screen
- Merge stored template with matter/FE/CA/addressee fields
- Human-verification status required before issue
- Explicit absence of generative-AI compose

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Generate Draft From Template wizard | Very High |
| Draft Field Fill and Preview screen | Complex |
| Generate draft from template history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Template merge and human-verify workflow | Very High |
| Update generate draft from template | Medium |
| Search generate draft from template | Medium |
| Read generate draft from template history | Easy |

### Inputs
Matter; template type/version; FE/CA; addressee; filled fields; verifier Person.

### Outputs
Draft document; verification status; ready-to-issue flag; version retained on the matter.

### Business Rules
- Drafts come only from stored templates (F02-003).
- Generative AI shall not compose the text.
- Human verification is mandatory before issue.
- Addressees are Tahsildar, Banks, Claimants, Competent Authority or Government as the template type allows — not Claim settlement workflow.
- Investigation/market-intelligence process remains out of scope except issuing these template notices.

### Validations
- Matter required; template must be available; required merge fields complete; ready-to-issue blocked until verified; font/spacing preserved from template.

### Calculations
None beyond field merge into the stored layout.

### Workflow
Select matter → select template → fill fields → generate → on-screen review → human verify → ready to issue.

### Search Requirements
Drafts by matter, template type, verifier, status (draft/verified/ready to issue).

### Documents
Generated draft on the matter; previous versions retained.

### Reports
Template issue register (type, matter, verifier, date).

### Notifications
Optional notice to CA when a draft is marked ready to issue.

### Security
Issue action attributable to shared Person; download of issued draft follows F01-003.

### Integrations
Matter/FE/CA field mapping (Easy).

### Dependencies
F02-003; F04-001; F01-003; keywords F02-001.

### Assumptions
- Merge is rule-based fill of stored templates, not model-generated prose.

### Risks
User treats preview as optional and issues unverified text — status must block that path.

### Non Functional Requirements
Preview faithful to court font/spacing; auditable verify step.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Generate Draft From Template wizard | UI | Very High | 16 |
| Draft Field Fill and Preview screen | UI | Complex | 12 |
| Generate draft from template history | UI | Medium | 6 |
| Template merge and human-verify workflow | API | Very High | 16 |
| Update generate draft from template | API | Medium | 6 |
| Search generate draft from template | API | Medium | 6 |
| Read generate draft from template history | API | Easy | 4 |
| Generate draft from template persistence | DB | Medium | 4 |
| Matter/FE/CA/addressee field mapping | Integration | Easy | 8 |
| Generate draft from template feature tests | Testing | Very High | 12 |
| Generate draft from template implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **94** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
