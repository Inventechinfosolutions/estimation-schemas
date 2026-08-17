# F01-009 — Claim-pack document rights

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-009 |
| **Feature Name** | Claim-pack document rights |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
An authorised Officer or Competent Authority opens a claim pack and views or downloads identity proof, investment proof, bank documents, affidavit or heir papers according to their Post rights. A user without download right can view but not download. The system records who viewed or downloaded which document and when.

### Business Objective
Apply need-to-know view/download rights on claim-pack documents and keep a retrieval trail.

### Actors
Officer; Competent Authority; user without download right; auditor.

### User Journey
1. Authorised Officer or Competent Authority opens a claim pack they are allowed to see (F01-003).
2. They view identity proof, investment proof, bank documents, affidavit or heir papers as permitted.
3. If their Post has no download right, view is allowed and download is refused.
4. Each view or download is recorded (Person, Post, document, action, timestamp).
5. An auditor can retrieve who viewed or downloaded which document and when (F01-010).

### Functional Capabilities
- Open claim-pack documents under Post-based view rights.
- Allow view without download where download is not granted.
- Record view and download events per document.
- Cover identity, investment, bank, affidavit and heir papers in the pack.

### Inputs
Claim pack, document type, requested action (view / download), acting Person and Post.

### Outputs
Rendered or downloaded working copy; append-only view/download trail.

### Business Rules
- Document rights follow Post/Role permissions.
- Need-to-know still applies: another officer’s restricted pack is refused (F01-003).
- Original files remain unaltered; downloads are of stored originals or authorised copies.

### Validations
- View and download are separately authorised.
- Missing document types simply do not appear; they are not invented.

### Calculations
None.

### Workflow
Open pack → view or download → audit event. No approval step for an authorised view.

### Search Requirements
Within an authorised pack, documents by type; no global document search for unauthorised Posts.

### Documents
Identity proof; investment proof; bank documents; affidavit; nominee/heir papers as present on the pack.

### Reports
Document access trail extract (forensic detail in F01-010).

### Notifications
None.

### Security
Least privilege on KYC and bank papers. View/download events are privileged-action audit.

### Integrations
None (embedded document handling; Idea/Adobe working copies are F09-005).

### Dependencies
F01-003; claim packs from Module 06; depositor documents from Module 04.

### Assumptions
- Document management remains embedded; this is not a standalone DMS module.

### Risks
- Granting download to overly broad Posts would leak identity and bank documents.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. Source files remain immutable; working copies are identifiable if conversion is used elsewhere.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Claim pack viewer with view/download controls | UI | Complex | 12 |
| Document rights enforcement operations | API | Complex | 8 |
| View/download audit persistence | DB | Medium | 4 |
| Document rights tests | Testing | Medium | 6 |
| Claim-pack document rights note | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Forensic register filters are estimated in F01-010.
- No OCR effort here (F04-001).
