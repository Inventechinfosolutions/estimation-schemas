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
1. User views or downloads a document, creates a folder, uploads a file, or opens a shared document.
2. Same rights as web (F01-003, F04-004, F05-006).
3. View-without-download still withheld when not granted.

### Functional Capabilities
- Android Document list/folder
- View / Download / Upload
- Create folder
- Open shared documents
- Same rights as web

### Inputs
Matter/folder; file; action (view/download/upload).

### Outputs
Folder; uploaded version; viewer/download per rights.

### Business Rules
- Subject to the same rights as web.
- Access log still recorded (F01-003).
- No generative-AI on-device drafting.

### Validations
Rights evaluated server-side; download withheld when not granted; folder name required.

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
Preview formats as web allows; large PDFs stream.

### Risks
Downloaded copy on a shared phone.

### Non Functional Requirements
View/download over HTTPS; folder create synced.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Document list/folder | UI | Complex | 12 |
| View / Download / Upload | UI | Complex | 12 |
| Document operations | API | Complex | 8 |
| Device folder cache | Database | Medium | 4 |
| Rights and web documents | Integration | Medium | 16 |
| Android document tests | Testing | Complex | 8 |
| Android documents guide | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Rights matrix remains F01-003.
