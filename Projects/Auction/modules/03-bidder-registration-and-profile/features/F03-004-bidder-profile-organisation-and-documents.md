# F03-004 — Bidder Profile, Organisation and Documents

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Bidder Profile, Organisation and Documents |
| **Module** | 03 — Bidder Registration and Profile |

### Description
An active bidder maintains the organisation name, contact details, and the master documents they keep on their account. These master documents travel with the bidder. They are not a substitute for the documents a particular auction asks for during participation, unless that auction’s instructions say a named profile document is enough.

### Business Objective
Evaluation staff can see who the bidder is and which standing documents the bidder has filed, separate from one auction’s participation pack.

### Actors
Maker: the active bidder. Approver: none. Reader: Evaluation Authority and the verifier, when they open a participant.

### User Journey
1. Who creates: the bidder creates profile updates and uploads master documents. The account already exists.
2. How they create: Profile → organisation and contact → Save. Documents → upload a named document → Save.
3. How they edit: they replace contact details or replace a document. The previous document remains in history and is not silently destroyed.
4. How they send for approval: they do not. Profile edits are not an auction submission. A verifier may still deactivate the account in F03-002 if the profile becomes unacceptable.
5. How the approver sees pending items: there is no approver inbox for profile edits.
6. How the approver decides: there is no approval decision on this feature.
7. How the maker sees history: the bidder sees previous organisation details and replaced documents.
8. How the auditor sees history: the Evaluation Authority sees the current profile and documents when evaluating a participation, and the change history. Other bidders see nothing.

### Functional Capabilities
- Update organisation and contact details
- Upload, replace, and list master documents
- Keep replaced documents in history
- Let evaluation staff read the profile of a bidder who has participated

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Organisation
- Contact name
- Email
- Mobile
- Document file and label

### Outputs
- Current bidder profile
- Master document set
- Change history

### Business Rules
- Only the bidder who owns the account, or the administrator, can change it.
- Email change cannot collide with another bidder.
- Master documents are labelled by the bidder. The auction’s required-document checklist is F07-004, not this list.
- Deactivated bidders can read their profile and cannot upload new documents or participate.

### Validations
- Organisation and contact remain mandatory.
- A document needs a label and a file.
- Empty file and unknown type are rejected.

### Calculations
None.

### Workflow
Save is immediate. No approval inbox.

### Search Requirements
The bidder does not search other profiles. Staff search bidders by organisation and email from the verification register when they need the profile.

### Documents
Bidder master documents stored on the account.

### Reports
None.

### Notifications
None for ordinary edits. Deactivation continues to use F03-002.

### Security
A bidder cannot open another bidder’s profile or documents. Evaluation staff can open them only in the context of a participation they are allowed to evaluate.

### Integrations
None.

### Dependencies
F03-002 active account.

### Assumptions
- The source asks the bidder to maintain profile, organisation, contact, and required bidder documents. It does not fix a statutory document list. Labels are bidder-supplied until an auction states its own checklist.

### Risks
Bidders may assume a profile document satisfies every auction. Participation still enforces F07-004.

### Non Functional Requirements
A document replaced during an open evaluation remains available to the evaluator from history so the pack they started from is not lost.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bidder profile form | UI | Complex | 12 |
| Organisation and contact form | UI | Medium | 6 |
| Bidder master document register | UI | Medium | 6 |
| Update bidder profile | API | Medium | 6 |
| Save bidder organisation | API | Medium | 6 |
| Upload bidder master document | API | Medium | 6 |
| Bidder profile and document records | DB | Medium | 4 |
| Bidder profile tests | Testing | Complex | 8 |
| Bidder profile notes | Documentation | Medium | 3 |

**Feature total: 57 hours**
