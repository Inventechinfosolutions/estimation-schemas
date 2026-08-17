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
1. User opens Matter Documents on the matter.
2. Scans or uploads a file, or edits text and saves a new version.
3. Shares only with Posts/Persons allowed (Limited named list or Community as F01-002).
4. A person without access cannot open it; previous versions remain available.

### Functional Capabilities
- Matter Document Register
- Upload/Scan and Version Viewer
- Controlled Share picker (Posts/Persons allowed)
- Previous versions retrievable
- Non-members cannot open
- Embedded document handling — not a separate DMS

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
Matter required; file or text required; share list must be active Persons/Posts; classification required before share of sensitive items.

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
Create/edit text is ordinary editor, not AI compose.

### Risks
Sharing to Community when Limited was intended over-exposes the file.

### Non Functional Requirements
Version retrieve; AES-256 at rest per programme NFR.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Matter Document Register | UI | Complex | 12 |
| Upload/Scan and Version Viewer | UI | Complex | 12 |
| Controlled Share picker | UI | Medium | 6 |
| Version and share operations | API | Complex | 8 |
| Document and version entities | Database | Complex | 6 |
| Limited/Community rights enforcement | Integration | Easy | 8 |
| Matter document tests | Testing | Complex | 8 |
| Matter documents and controlled share guide | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Purpose-based share (Information/Approval etc.) is F05-006.
