# F08-001 — Manuals, guidelines and SOP

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Manuals, guidelines and SOP |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
An authorised user uploads a manual, guideline or SOP, applies keywords, and saves. Another user searches by keyword or title and opens the document.

### Business Objective
Provide a searchable SOP/manuals/guidelines library with keywords for Legal Cell daily use.

### Actors
Authorised knowledge owner; Legal Cell; Advocate (read).

### User Journey
1. Who creates: Authorised knowledge owner
2. How they create: Authorised user uploads a manual, guideline or SOP, applies keywords, and saves.
3. How they edit: Another user searches by keyword or title and opens the document.
4. How they send for approval: Another user searches by keyword or title and opens the document. Upload → keyword → save → search/open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised knowledge owner works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised knowledge owner opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- SOP Library Register
- Upload and Keyword form
- Search by keyword or title
- Open document
- Not an LMS vendor product

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| SOP Library Register | Medium |
| Upload and Keyword form | Complex |
| Manuals, guidelines and sop history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| SOP CRUD | Medium |
| Update manuals, guidelines and sop | Medium |
| Search manuals, guidelines and sop | Medium |
| Read manuals, guidelines and sop history | Easy |

### Inputs
File; title; keywords; type (manual/guideline/SOP).

### Outputs
Knowledge document; search hits.

### Business Rules
- Keywords hyperlinked as for other knowledge items.
- Classroom/instructor-led training is out of scope unless separately ordered.
- No generative-AI SOP authoring.

### Validations
- Title and file required; keywords from catalogues when applied.

### Calculations
None.

### Workflow
Upload → keyword → save → search/open.

### Search Requirements
Keyword, title.

### Documents
Manuals, guidelines, SOP.

### Reports
SOP inventory.

### Notifications
Optional publish notice.

### Security
View per Post; some SOP may be Limited.

### Integrations
Keyword consume (Simple).

### Dependencies
F02-001; F01-003; F08-006 retention.

### Assumptions
- SPLOCA supplies SOP files.

### Risks
Out-of-date SOP without version note.

### Non Functional Requirements
Search by title or keyword as acceptance criterion.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| SOP Library Register | UI | Medium | 6 |
| Upload and Keyword form | UI | Complex | 12 |
| Manuals, guidelines and sop history | UI | Medium | 6 |
| SOP CRUD | API | Medium | 6 |
| Update manuals, guidelines and sop | API | Medium | 6 |
| Search manuals, guidelines and sop | API | Medium | 6 |
| Read manuals, guidelines and sop history | API | Easy | 4 |
| Manuals, guidelines and sop persistence | DB | Medium | 4 |
| Keyword consume | Integration | Simple | 4 |
| Manuals, guidelines and SOP feature tests | Testing | Easy | 4 |
| Manuals, guidelines and SOP implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
