# ChatGPT Visualization Brief — F06-005: Examination Credential Generation and Secure Distribution Handoff

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `Feature_Specs/M06_examination-scheduling-and-allocation.md`  
**Module:** 06 Examination Scheduling & Allocation  
**Feature:** F06-005 — Examination Credential Generation and Secure Distribution Handoff  
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql`  
**Primary table:** `exam_credential`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the feature specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Credential generate → hash store → handoff → Module 07 dispatch → callback pipeline
2. Security swimlane: plaintext never in admin UI / DB / audit; transient handoff only
3. Credential + dispatch state machine (Eligible → Generated → Handoff Pending → Dispatched / Failed; Invalidated on regenerate)
4. Regenerate vs Resend decision flowchart
5. Sequence: Administrator ↔ Scheduling Service ↔ Notification Service (Mod 07) ↔ Candidate channels
6. ERD for `exam_credential` with hashed password and handoff correlation callouts
7. Dependency map: F06-005 ↔ F06-001/002, Modules 05/07/09

Do not invent features outside this specification. Do not include estimation hours or task tables.

---

### FEATURE OVERVIEW

**ID:** F06-005  
**Name:** Examination Credential Generation and Secure Distribution Handoff  
**Module:** 06 Examination Scheduling & Allocation  
**Primary data objects:** `exam_credential`, `candidate_allocation`, `exam_session`

### FEATURE SPECIFICATION

#### F06-005 — Examination Credential Generation and Secure Distribution Handoff

**One-liner / description:** Generates unique examination login identifiers and passwords for candidates after schedule finalisation and eligible allocation state. Stores credentials securely, exposes administrator batch generation and regenerati…

**Full description:** Generates unique examination login identifiers and passwords for candidates after schedule finalisation and eligible allocation state. Stores credentials securely, exposes administrator batch generation and regeneration controls, and hands off masked credential dispatch requests to the Notification Service via approved SMS and email channels without exposing plaintext passwords in administrative list views.

**Business objective:** Ensure each candidate receives unique, secure examination login credentials through approved communication channels only after scheduling and allocation are complete, enabling examination day login without administrator manual password handling.

**Actors:** Examination Administrator; Candidate

**User journey (11 steps):**
1. Examination Administrator opens Examination Credential Generation console for a selected examination.
2. System displays eligibility checklist: Published schedules, Finalised allocations, and schedule finalisation policy satisfied.
3. Administrator selects Generate Credentials for candidate scope.
4. System generates unique examination login ID and random password per eligible candidate, stores password using secure hashing, and queues credential records.
5. Administrator views credential generation status register showing generated, pending dispatch, dispatched, and failed rows with masked secret display only.
6. Administrator selects Initiate Distribution Handoff for batch; system publishes secure dispatch payload to Notification Service without logging plaintext password.
7. Module 07 dispatches SMS and/or email to candidate using configured templates; this feature records handoff correlation identifier and dispatch status callbacks.
8. For compromised or undelivered credentials, Administrator opens Regenerate Credentials dialog; system invalidates prior credential and creates new pair.
9. Administrator triggers Resend Distribution Handoff for individual candidate to Notification Service.
10. Candidate receives login ID and password via SMS/email from Notification Service (outside this feature UI).
11. Candidate uses credentials at examination login (Module 09 scope); this feature does not provide conduct interface.

**Functional capabilities:**
- Display credential generation console with schedule finalisation eligibility checklist
- Generate unique examination login ID and password batch for eligible candidates
- Store examination password using secure one-way hashing
- Display credential generation and dispatch status register with masked secrets
- Initiate secure distribution handoff batch to Notification Service
- Receive and persist dispatch status callback updates from Notification Service
- Regenerate credentials for individual candidate invalidating prior active credential
- Trigger resend distribution handoff for individual candidate
- Block credential generation until schedule finalisation and allocation prerequisites met
- Audit all generate, regenerate, and handoff actions without plaintext password retention in logs

**Inputs:**
- Examination identifier
- Published session schedule finalisation confirmation
- Candidate identifiers in eligible scope
- Regenerate credentials reason text
- Resend dispatch handoff confirmation
- Notification template routing identifiers from Module 07
- Dispatch status callback payload from Notification Service

**Outputs:**
- Examination login ID per candidate
- Securely hashed examination password record
- Credential generation batch status
- Distribution handoff request with correlation identifier
- Dispatch status per candidate (Pending, Dispatched, Failed)
- Regenerated credential pair with prior credential invalidated flag
- Administrator masked credential status view

**Business rules:**
- Credential generation permitted only after examination schedule finalisation policy is satisfied and allocations are Finalised
- Each candidate receives one active examination credential set per examination attempt
- Plaintext password shown only transiently during generation handoff to Notification Service, never in administrator registers
- Regeneration invalidates previous login password pair immediately
- Resend handoff uses current active credential without regenerating unless administrator explicitly regenerates
- Examination conduct login validation is out of scope; credentials prepared for Module 09 consumption

**Validations:**
- Eligibility checklist must pass before batch generation accepted
- Login ID must be unique within examination scope
- Generated password meets configured complexity and length rules
- Regenerate reason mandatory on administrator regenerate action
- Handoff blocked when candidate missing registered mobile or email required by channel policy
- Resend allowed only when active credential exists
- Dispatch callback correlation identifier must match existing handoff record

**Calculations:**
- Generate random password meeting complexity policy
- Derive credential eligibility from schedule finalisation and allocation composite state

**Workflow / states:** Not Eligible → Eligible (prerequisites met) → Generated (credential created) → Handoff Pending (dispatch request queued) → Dispatched (Notification Service success callback) | Handoff Pending → Handoff Failed (callback failure) → Handoff Pending (resend) | Generated → Invalidated (regenerate action) → Generated (new active credential).

**Search requirements:**
- Administrator search credential register by candidate name, registration number, login ID
- Filter by generation status, dispatch status, examination, session
- Sort by generation timestamp and dispatch status

**Reports:**
- Credential generation and dispatch status summary export for examination readiness review

**Notifications:**
- Examination credential dispatch handoff event to Module 07 for SMS delivery
- Examination credential dispatch handoff event to Module 07 for email delivery
- Credential regeneration notification handoff when policy requires informing candidate

**Security:**
- Passwords stored hashed; plaintext never persisted in database or audit tables
- Administrator views show login ID and masked password indicator only
- Handoff payload encrypted in transit to Notification Service
- Regenerate and handoff actions restricted to Examination Administrator credential permission
- Rate limit resend handoff to prevent abuse

**Integrations:**
- Module 07 Notification Service secure credential dispatch handoff API
- Module 07 dispatch status callback ingestion

**Dependencies:**
- F06-001 — Published and finalised examination session schedules
- F06-002 — Finalised candidate allocation
- Module 07 — Notification Template Catalog, channel configuration, and dispatch engine
- Module 05 — Candidate registered mobile and email contact points
- Module 01 — Examination Administrator credential management permissions
- Module 09 — Secure Examination Conduct consumes generated credentials at login time

**Assumptions:**
- Notification Service owns template wording and channel provider delivery
- Schedule finalisation for credentials aligns with Published schedule state plus optional administrator explicit finalisation flag
- Complexity drivers: secure secret handling, handoff idempotency, and dispatch status callback reconciliation

**Risks:** Credential delivery failure leaves candidates without login details near examination time; Regeneration after dispatch may confuse candidates receiving multiple messages; Misconfigured Notification templates may expose credentials improperly if template not masked

**Non-functional requirements:**
- Batch credential generation completes for examination-wide volumes
- Handoff processing idempotent to avoid duplicate SMS/email sends
- Credential hash algorithm meets organisational security standards

**Notes:** Credential plaintext distribution executed by Module 07 Notification Service; this feature generates credentials and hands off secure dispatch requests.

---

### MODULE PIPELINE CONTEXT (for dependency diagrams only)

```text
F06-001 Schedule → F06-002 Allocation → F06-003 Seat → F06-004 Hall Ticket
                              ↘ F06-005 Credentials → Module 07 Notify → Module 09 Conduct
```

Upstream modules commonly involved: 01 IAM · 03 Centre · 04 Config · 05 Registration.  
Highlight only dependencies listed for this feature.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: this feature’s services vs other Module 06 features vs external modules
- Call out audit, security, capacity, and lock/finalise gates explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **F06-005 Examination Credential Generation and Secure Distribution Handoff** (Module 06).
> Purpose: Generates unique examination login identifiers and passwords for candidates after schedule finalisation and eligible allocation state. Stores credentials securely, exposes administrator batch generation and regenerati…
> Primary table: `exam_credential`.
> Draw: generate→hash→handoff→Mod07 callback pipeline; security swimlane (no plaintext in admin/DB); regenerate vs resend flowchart; credential/dispatch state machine; ERD for `exam_credential`.
