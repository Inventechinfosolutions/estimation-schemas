# F09-007 — Android documents

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-007 |
| **Feature Name** | Android documents |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user views or downloads a document, creates a folder, uploads a file, or opens a shared document, subject to the same rights as web.

### Business Objective
Give Android the Annexure-I document actions — view, download, create folder, upload, open shared — with the same rights as web.

### Actors
Advocate; Legal Cell.

### User Journey
1. Who creates: Advocate
2. How they create: User views or downloads a document, creates a folder, uploads a file, or opens a shared document.
3. How they edit: Same rights as web (F01-003, F04-004, F05-006).
4. How they send for approval: View-without-download still withheld when not granted. Browse → view/download/upload/create folder/open shared.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android Document list/folder
- View / Download / Upload
- Create folder
- Open shared documents
- Same rights as web

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Android Document list/folder | Complex |
| View / Download / Upload | Complex |
| Android documents history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Document operations | Complex |
| Update android documents | Medium |
| Search android documents | Medium |
| Read android documents history | Easy |

### Inputs
Matter/folder; file; action (view/download/upload).

### Outputs
Folder; uploaded version; viewer/download per rights.

### Business Rules
- Subject to the same rights as web.
- Access log still recorded (F01-003).
- No generative-AI on-device drafting.

### Validations
- Rights evaluated server-side; download withheld when not granted; folder name required.

### Calculations
None.

### Workflow
Browse → view/download/upload/create folder/open shared.

### Search Requirements
Folder/file name on device.

### Documents
Matter/library files as permitted.

### Reports
None.

### Notifications
Share notice as on web.

### Security
Downloaded files follow device policy; no bypass of classification.

### Integrations
Rights + web documents (Medium).

### Dependencies
F01-003; F04-004; F05-006; F01-004.

### Assumptions
- Preview formats as web allows; large PDFs stream.

### Risks
Downloaded copy on a shared phone.

### Non Functional Requirements
View/download over HTTPS; folder create synced.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Android Document list/folder | UI | Complex | 12 |
| View / Download / Upload | UI | Complex | 12 |
| Android documents history | UI | Medium | 6 |
| Document operations | API | Complex | 8 |
| Update android documents | API | Medium | 6 |
| Search android documents | API | Medium | 6 |
| Read android documents history | API | Easy | 4 |
| Android documents persistence | DB | Medium | 4 |
| Rights and web documents | Integration | Medium | 16 |
| Android documents feature tests | Testing | Complex | 8 |
| Android documents implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **85** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
