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
1. Who creates: Officer
2. How they create: Authorised Officer or Competent Authority opens a claim pack they are allowed to see (F01-003).
3. How they edit: They view identity proof, investment proof, bank documents, affidavit or heir papers as permitted.
4. How they send for approval: If their Post has no download right, view is allowed and download is refused. Open pack → view or download → audit event. No approval step for an authorised view.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Each view or download is recorded (Person, Post, document, action, timestamp). An auditor can retrieve who viewed or downloaded which document and when (F01-010).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Open claim-pack documents under Post-based view rights.
- Allow view without download where download is not granted.
- Record view and download events per document.
- Cover identity, investment, bank, affidavit and heir papers in the pack.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My claim-pack document rights list / queue | Medium |
| Claim pack viewer with view/download controls | Complex |
| Claim-pack document rights history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Document rights enforcement operations | Complex |
| Update claim-pack document rights | Medium |
| Search claim-pack document rights | Medium |
| Read claim-pack document rights history | Easy |

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
| My claim-pack document rights list / queue | UI | Medium | 6 |
| Claim pack viewer with view/download controls | UI | Complex | 12 |
| Claim-pack document rights history | UI | Medium | 6 |
| Document rights enforcement operations | API | Complex | 8 |
| Update claim-pack document rights | API | Medium | 6 |
| Search claim-pack document rights | API | Medium | 6 |
| Read claim-pack document rights history | API | Easy | 4 |
| View/download audit persistence | DB | Medium | 4 |
| Claim-pack document rights feature tests | Testing | Medium | 6 |
| Claim-pack document rights implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
