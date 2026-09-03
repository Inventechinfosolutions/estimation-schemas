# F01-003 — Legal document rights

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Legal document rights |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An Advocate or Legal Cell user opens a petition, order or opinion and can view, download, share or edit only as their Post and the document classification allow. A user without download right can view but not download. The system records who viewed or downloaded which legal document and when.

### Business Objective
Apply classification-aware view/download/share/edit on legal documents so sensitive files are not freely redistributable.

### Actors
Advocate; Legal Cell; Competent Authority; Auditor (access log).

### User Journey
1. Who creates: Advocate
2. How they create: User opens a petition, order or opinion from the library or matter.
3. How they edit: System evaluates Post rights and document classification.
4. How they send for approval: User views; download, share or edit appear only if allowed. Open document → evaluate matrix + space → allow or withhold controls → record view/download.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record. A user without download right sees the viewer but the download control is withheld. Each view and download is written to the legal document access log.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Legal Document Rights Matrix screen (Post × classification → view/download/share/edit)
- Document viewer with rights overlay (download withheld when not granted)
- Access log: who viewed or downloaded which legal document and when
- Refuse share/edit when classification or Post does not allow
- Sensitive legal documents are not freely redistributable

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Legal Document Rights Matrix screen | Complex |
| Document viewer with rights overlay | Medium |
| Legal document rights history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Rights evaluation and access-log operations | Complex |
| Update legal document rights | Medium |
| Search legal document rights | Medium |
| Read legal document rights history | Easy |

### Inputs
Document identity and classification; acting Person/Post; requested action (view/download/share/edit).

### Outputs
Allowed-action set; viewer/download decision; legal document access log.

### Business Rules
- View, download, share and edit follow classification and Post rights.
- View-without-download is a valid combination.
- Limited/Community membership (F01-002) is an additional gate, not a substitute for document rights.
- Access log is attributable to the shared Person.
- No generative-AI redaction or auto-classification.

### Validations
- Document must exist; classification required before first share; Post must be active; download/share/edit rejected when not in the matrix.

### Calculations
None.

### Workflow
Open document → evaluate matrix + space → allow or withhold controls → record view/download.

### Search Requirements
Access log by Person, document, action (view/download), date.

### Documents
Petitions, orders, opinions and other legal files already stored in library/matter.

### Reports
Legal document access log (Excel).

### Notifications
None required on every view; optional notice on denied download of a sensitive classification.

### Security
Rights evaluated server-side; viewer watermark/session bound to shared Person; audit of matrix changes.

### Integrations
Library and matter document identity (Simple); shared Post for the actor (F01-001).

### Dependencies
F01-001; F01-002; library/matter document stores (Modules 03–04).

### Assumptions
- Classifications used by Legal (e.g. sensitive vs ordinary) are maintained as central masters (F02-005) or document metadata.

### Risks
Over-permissive matrix allows download of sensitive petitions; missing log undermines forensic review.

### Non Functional Requirements
Access log retained with the programme audit policy; HTTPS delivery of viewed files.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Legal Document Rights Matrix screen | UI | Complex | 12 |
| Document viewer with rights overlay | UI | Medium | 6 |
| Legal document rights history | UI | Medium | 6 |
| Rights evaluation and access-log operations | API | Complex | 8 |
| Update legal document rights | API | Medium | 6 |
| Search legal document rights | API | Medium | 6 |
| Read legal document rights history | API | Easy | 4 |
| Legal document rights persistence | DB | Medium | 4 |
| Library/matter document identity handoff | Integration | Simple | 4 |
| Legal document rights feature tests | Testing | Medium | 6 |
| Legal document rights implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
