# F05-003 — Hall Ticket Generation and Download

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Hall Ticket Generation and Download |
| **Module** | 05 — Scheduling, Allocation, Hall Tickets and Examination Credentials |

### Description
After schedule publication and centre allocation, generate and publish digital hall tickets for candidates. Candidates download/print hall tickets from the candidate login showing name, registration number, examination, date/time, reporting time, allotted centre and address, photograph/details if applicable, instructions, and credential information if applicable. Hall tickets are unavailable before scheduling and allocation.

### Business Objective
Provide each allocated candidate with an authoritative admit document for centre reporting and identity checks.

### Actors
Maker: Examination Administrator (generate/publish). Applicant: Candidate (download/print). Approver: none. Auditor: Examination Administrator (publish history).

### User Journey
1. Who creates: Examination Administrator triggers generation/publish for a schedule after allocation commit.
2. How they create: Hall ticket publish control → select schedule/examination → generate tickets for allocated candidates → publish → candidates become able to download.
3. How they edit: Republish after permitted allocation corrections; candidates cannot edit hall ticket content.
4. How they send for approval: Does not apply — publish is administrator action without checker inbox.
5. How the approver sees pending items: No approver inbox; not-ready candidates see a not-ready message instead of a ticket.
6. How the approver decides: No decision step.
7. How the applicant / maker sees history: Candidate sees current hall ticket and download access; admin sees publish history.
8. How the approver / auditor sees history: Hall ticket publish history screen records generation/publish events and actors.

### Functional Capabilities
- Block hall ticket access until schedule exists and allocation is committed.
- Generate hall ticket content from registration + schedule + allotted centre.
- Include name, registration number, examination, date/time, reporting time, centre and address.
- Include photograph/details if captured/applicable.
- Include instructions and credential information if applicable (credentials issued in F05-004 may be referenced).
- Publish hall tickets to candidate portal.
- Candidate download and print-friendly layout.
- Show clear not-ready message when prerequisites unmet.
- Support regeneration/republish after controlled allocation changes.
- Audit generation and publish events.
- Ensure allotted centre on ticket matches allocated session centre.

### UI Screens
| Screen | Purpose |
|---|---|
| Hall ticket publish control screen | Admin generate/publish for a schedule |
| Candidate hall ticket view screen | On-screen hall ticket in portal |
| Hall ticket download and print layout screen | Printable/downloadable presentation |
| Hall ticket not-ready message screen | Explain missing schedule/allocation |
| Hall ticket publish history screen | Admin audit of publish runs |

### Logical API operations
| Operation | Purpose |
|---|---|
| Generate hall tickets for schedule | Build ticket records for allocated cohort |
| Publish hall tickets to candidates | Make tickets visible/downloadable |
| Get hall ticket for candidate | Return ticket payload for logged-in candidate |
| Download hall ticket artefact | Return downloadable/print artefact |
| Get hall ticket publish history | Return publish audit trail |

### Inputs
Committed allocations; published schedule; registration pack; optional photograph; publish action; candidate session for download.

### Outputs
Hall ticket records; candidate-visible ticket; download artefact; publish history.

### Business Rules
- Unavailable before scheduling and allocation.
- Allocated centre on ticket must match committed allocation.
- Only the owning candidate (and authorised admin) may access the ticket.
- Republish supersedes prior ticket version with audit.

### Validations
- Prerequisites: published schedule + committed allocation.
- Candidate authentication for download.
- Ticket exists and is published before download.

### Calculations
None.

### Workflow
Allocation committed → admin generate → publish → candidate download/print. No approval inbox.

### Search Requirements
Admin may locate ticket status by registration number, centre, schedule.

### Documents
Hall ticket (generated digital artefact).

### Reports
Hall ticket issued counts feed Module 09.

### Notifications
Hall ticket available notification via Module 09 as configured.

### Security
Candidate-scoped download; admin publish restricted to Examination Administrator; audited publish.

### Integrations
None (notification dispatch consumed via Module 09).

### Dependencies
F05-001, F05-002, F04 confirmation; F05-004 may supply credential fields when applicable.

### Assumptions
- Exact layout/branding approved by Department.
- Photograph inclusion only if captured in registration or masters.

### Risks
Publishing before allocation freeze causes ticket churn; print layout issues on varied devices.

### Non Functional Requirements
Printable layout; fast download at peak; immutable published content per version.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Hall ticket publish control screen | UI | Medium | 6 |
| Candidate hall ticket view screen | UI | Complex | 12 |
| Hall ticket download and print layout screen | UI | Complex | 12 |
| Hall ticket not-ready message screen | UI | Simple | 2 |
| Hall ticket publish history screen | UI | Easy | 4 |
| Generate hall tickets for schedule | API | Complex | 8 |
| Publish hall tickets to candidates | API | Medium | 6 |
| Get hall ticket for candidate | API | Medium | 6 |
| Download hall ticket artefact | API | Easy | 4 |
| Get hall ticket publish history | API | Easy | 4 |
| Hall ticket record persistence | Database | Medium | 4 |
| Hall ticket generation and download tests | Testing | Complex | 8 |
| Hall ticket generation and download documentation | Documentation | Medium | 3 |

**Feature total: 79 hours**

### Estimation Assumptions
- Credential generation/communication hours remain on F05-004.
- SMS/email notification channel estimated on Module 09 / F05-004 as applicable, not duplicated here.
