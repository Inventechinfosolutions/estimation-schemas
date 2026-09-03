# F04-004 — Matter documents, versions and controlled share

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Matter documents, versions and controlled share |
| **Module** | 04 — Matter Management |

### Description
The user scans or uploads a document, or creates/edits text and saves a new version. The user shares the file only with Posts/Persons allowed. A person without access cannot open it. Previous versions remain available.

### Business Objective
Keep matter documents versioned and shared only with allowed Posts/Persons — not a standalone DMS product.

### Actors
Legal Cell; Advocate; named Limited members.

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens Matter Documents on the matter.
3. How they edit: Scans or uploads a file, or edits text and saves a new version.
4. How they send for approval: Shares only with Posts/Persons allowed (Limited named list or Community as F01-002). Upload/edit → new version → share to allowed list → open only if allowed.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. A person without access cannot open it; previous versions remain available.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Matter Document Register
- Upload/Scan and Version Viewer
- Controlled Share picker (Posts/Persons allowed)
- Previous versions retrievable
- Non-members cannot open
- Embedded document handling — not a separate DMS

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Matter Document Register | Complex |
| Upload/Scan and Version Viewer | Complex |
| Controlled Share picker | Medium |
| Matter documents, versions and controlled share history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Version and share operations | Complex |
| Update matter documents, versions and controlled share | Medium |
| Search matter documents, versions and controlled share | Medium |
| Read matter documents, versions and controlled share history | Easy |

### Inputs
File or text; version comment; share list; classification.

### Outputs
Versioned document; share ACL; denied-open for non-members.

### Business Rules
- Document versions are retrievable.
- Controlled share does not expose the file to non-members.
- F01-003 still governs download/edit.
- No generative-AI rewrite of uploaded pleadings.

### Validations
- Matter required; file or text required; share list must be active Persons/Posts; classification required before share of sensitive items.

### Calculations
None.

### Workflow
Upload/edit → new version → share to allowed list → open only if allowed.

### Search Requirements
Document name, type, version, uploader, date (within matter).

### Documents
Matter files (pleadings, orders copies, drafts).

### Reports
Matter document version register.

### Notifications
Share notice to named Persons.

### Security
Server-side ACL; access log on view/download.

### Integrations
Limited/Community rights (Easy).

### Dependencies
F01-002; F01-003; F04-002; F05-006 for purpose-based legal sharing.

### Assumptions
- Create/edit text is ordinary editor, not AI compose.

### Risks
Sharing to Community when Limited was intended over-exposes the file.

### Non Functional Requirements
Version retrieve; AES-256 at rest per programme NFR.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Matter Document Register | UI | Complex | 12 |
| Upload/Scan and Version Viewer | UI | Complex | 12 |
| Controlled Share picker | UI | Medium | 6 |
| Matter documents, versions and controlled share history | UI | Medium | 6 |
| Version and share operations | API | Complex | 8 |
| Update matter documents, versions and controlled share | API | Medium | 6 |
| Search matter documents, versions and controlled share | API | Medium | 6 |
| Read matter documents, versions and controlled share history | API | Easy | 4 |
| Matter documents, versions and controlled share persistence | DB | Medium | 4 |
| Limited/Community rights enforcement | Integration | Easy | 8 |
| Matter documents, versions and controlled share feature tests | Testing | Complex | 8 |
| Matter documents, versions and controlled share implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **83** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
