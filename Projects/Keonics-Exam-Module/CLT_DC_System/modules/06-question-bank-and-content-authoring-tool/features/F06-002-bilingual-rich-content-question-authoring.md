# F06-002 — Bilingual Rich-Content Question Authoring

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-002 |
| Feature Name | Bilingual Rich-Content Question Authoring |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Content Authoring Tool for SMEs: rich text editor with Kannada Unicode input, images, formulae (LaTeX / MathML), tables, practical / simulation item types (screen hotspot, drag-and-drop ordering, application screenshot tasks), English and Kannada versions linked as one item, four options with one correct answer, explanation, and metadata (topic, sub-topic, difficulty, type, skill, source, author, language).

### Business Objective
Allow SMEs to create high-quality bilingual items directly in the system.

### Actors
- SME Author

### User Journey
1. **Who creates:** The SME Author creates items against assigned targets.
2. **How they create:** The author selects type, writes stem and options in English and Kannada, adds media and metadata, previews as candidate, and saves.
3. **How they edit:** The author edits drafts and returned items; versions are kept.
4. **How they send for approval:** The author submits items to review.
5. **How the approver sees pending items:** Reviewers see submitted items (F06-003).
6. **How the approver decides:** Reviewers decide in F06-003.
7. **How the applicant / maker sees history:** The author sees status of own items and comments.
8. **How the approver / auditor sees history:** Auditors see item versions.

### Functional Capabilities
- Rich text with Kannada input
- Image upload and cropping
- Formula editor
- Simulation item types (hotspot, ordering, drag-and-drop)
- Bilingual linked versions
- Metadata tagging
- Candidate preview
- Autosave drafts
- Version history
- Duplicate / similarity check

### UI Screens
- Author workspace with targets
- Rich MCQ editor (bilingual)
- Simulation item editor
- Media library
- Candidate preview
- My items list

### Logical API Operations
- Save item draft with versioning
- Upload and process media
- Render formula
- Similarity check
- Submit for review
- Author item list

### Inputs
- Stem, options, media, metadata

### Outputs
- Submitted items

### Business Rules
- Both languages mandatory
- One correct option
- Metadata mandatory

### Validations
- Image size and type
- Formula syntax

### Calculations
- Similarity score

### Workflow
Draft → Submitted → Returned → Submitted

### Search Requirements
- Own items by topic, status

### Documents
- Item media

### Reports
- Author productivity

### Notifications
- Return notifications

### Security
- Items encrypted at rest; author sees own items only

### Integrations
- None

### Dependencies
- F06-001
- F16-001

### Assumptions
- SMEs work from KEONICS-approved locations

### Risks
- Simulation item complexity

### Non Functional Requirements
- Autosave every 30 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Author workspace with targets | Medium | 6 |
| UI | Rich MCQ editor (bilingual) | Very High | 16 |
| UI | Simulation item editor | Very High | 16 |
| UI | Media library | Medium | 6 |
| UI | Candidate preview | Complex | 12 |
| UI | My items list | Easy | 4 |
| API | Save item draft with versioning | Complex | 8 |
| API | Upload and process media | Medium | 6 |
| API | Render formula | Medium | 6 |
| API | Similarity check | Complex | 8 |
| API | Submit for review | Easy | 4 |
| API | Author item list | Easy | 4 |
| Database | Item, version and media store (encrypted) | Complex | 6 |
| Testing | Authoring tests across item types | Complex | 8 |
| Testing | Kannada rendering tests | Medium | 6 |
| Documentation | Content Authoring Tool manual | Medium | 3 |

**Feature Total: 119 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 60 | 36 | 6 | 0 | 14 | 3 | **119** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Rich and simulation editors rated Very High
- No external integration channel in this feature; Integration row omitted.
