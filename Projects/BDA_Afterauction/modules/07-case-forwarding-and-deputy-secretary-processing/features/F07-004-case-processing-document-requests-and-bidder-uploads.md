# F07-004 — Case Processing, Document Requests & Bidder Uploads

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-004 |
| Feature Name | Case Processing, Document Requests & Bidder Uploads |
| Module | 07 — Case Forwarding & Deputy Secretary Processing |
| Module Type | Business |
| Release | Go-live |

### Description
Processing actions in the DS office: case notes and remarks, internal note-sheet movement between case worker and DS, requests to the bidder for documents with due dates, bidder upload through the portal, verification of uploaded documents, and status updates visible to the bidder.

### Business Objective
Run DS processing digitally with clear communication to the bidder and a complete note-sheet record.

### Actors
- Case Worker
- Deputy Secretary
- Successful Bidder

### User Journey
1. **Who creates:** The case worker creates notes and document requests.
2. **How they create:** The case worker writes a note, attaches references, and raises a document request selecting document types and due date.
3. **How they edit:** Notes can be edited until forwarded; requests can be cancelled with reason.
4. **How they send for approval:** The case worker forwards the note-sheet to the DS for orders.
5. **How the approver sees pending items:** The DS sees cases awaiting orders.
6. **How the approver decides:** The DS writes orders (proceed to draft deed, seek more documents, return), optionally signing with DSC.
7. **How the applicant / maker sees history:** The bidder sees requests, uploads documents, and sees verification status.
8. **How the approver / auditor sees history:** Auditors see the note-sheet, requests and uploads.

### Functional Capabilities
- Note-sheet with chronological notes and orders
- Document request to bidder with checklist and due date
- Bidder upload with type, size and malware checks
- Document verification (accept / reject with reason)
- Timer pause while waiting for bidder
- Status update to bidder
- Proceed to draft deed stage

### UI Screens
- Note-sheet
- Document request form
- Bidder document upload (portal)
- Document verification
- DS orders screen

### Logical API Operations
- Add note / order
- Forward note-sheet
- Raise document request
- Bidder upload document
- Verify document
- Pause / resume timer
- Move case to next stage

### Inputs
- Notes
- Requests
- Uploads
- Orders

### Outputs
- Note-sheet
- Verified documents
- Stage change

### Business Rules
- Notes become read-only after forwarding
- Bidder uploads only against open requests
- Timer paused while waiting for bidder

### Validations
- File type PDF / JPG / PNG ≤ 10 MB

### Calculations
- None

### Workflow
Under Processing → Awaiting Bidder → Under Processing → Orders → Draft Deed Stage

### Search Requirements
- Requests by status

### Documents
- Bidder documents

### Reports
- Pending document requests

### Notifications
- Request and verification notices to bidder

### Security
- Malware scan

### Integrations
- None

### Dependencies
- F07-003
- F02-004
- F10-004

### Assumptions
- None

### Risks
- Bidder delays; tracked by timers

### Non Functional Requirements
- Upload within 10 seconds for 10 MB

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Note-sheet | Medium | 6 |
| UI | Document request form | Easy | 4 |
| UI | Bidder document upload (portal) | Medium | 6 |
| UI | Document verification | Easy | 4 |
| UI | DS orders screen | Medium | 6 |
| API | Add note / order | Medium | 6 |
| API | Forward note-sheet | Easy | 4 |
| API | Raise document request | Easy | 4 |
| API | Bidder upload document | Medium | 6 |
| API | Verify document | Easy | 4 |
| API | Pause / resume timer | Easy | 4 |
| API | Move case to next stage | Medium | 6 |
| Database | Note-sheet and document request store | Medium | 4 |
| Testing | Processing flow and upload tests | Medium | 6 |
| Testing | Timer pause tests | Easy | 4 |
| Documentation | Case processing guide | Easy | 2 |

**Feature Total: 76 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 34 | 4 | 0 | 10 | 2 | **76** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard workflow
- No external integration channel in this feature; Integration row omitted.
