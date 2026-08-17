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
1. User opens a petition, order or opinion from the library or matter.
2. System evaluates Post rights and document classification.
3. User views; download, share or edit appear only if allowed.
4. A user without download right sees the viewer but the download control is withheld.
5. Each view and download is written to the legal document access log.

### Functional Capabilities
- Legal Document Rights Matrix screen (Post × classification → view/download/share/edit)
- Document viewer with rights overlay (download withheld when not granted)
- Access log: who viewed or downloaded which legal document and when
- Refuse share/edit when classification or Post does not allow
- Sensitive legal documents are not freely redistributable

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
Document must exist; classification required before first share; Post must be active; download/share/edit rejected when not in the matrix.

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
Classifications used by Legal (e.g. sensitive vs ordinary) are maintained as central masters (F02-005) or document metadata.

### Risks
Over-permissive matrix allows download of sensitive petitions; missing log undermines forensic review.

### Non Functional Requirements
Access log retained with the programme audit policy; HTTPS delivery of viewed files.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Legal Document Rights Matrix screen | UI | Complex | 12 |
| Document viewer with rights overlay | UI | Medium | 6 |
| Rights evaluation and access-log operations | API | Complex | 8 |
| Rights matrix and access-log entities | Database | Medium | 4 |
| Library/matter document identity handoff | Integration | Simple | 4 |
| Document rights tests | Testing | Medium | 6 |
| Legal document rights guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Does not rebuild DMS; applies rights on library/matter documents.
- Login audit remains Claim F01-010; this log is legal-document view/download only.
