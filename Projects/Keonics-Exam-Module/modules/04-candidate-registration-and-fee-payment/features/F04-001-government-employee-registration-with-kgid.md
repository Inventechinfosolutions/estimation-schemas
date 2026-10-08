# F04-001 — Government Employee Registration with KGID

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Government Employee Registration with KGID |
| **Module** | 04 — Candidate Registration and Fee Payment |

### Description
Government-employee candidates complete Type 1 registration by entering a mandatory **KGID number**, retrieving available employee details from the KGID integration, confirming those details, and capturing additional fields required for examination registration. Registration cannot advance on this path without KGID capture and candidate confirmation of retrieved data (subject to integration availability).

### Business Objective
Ensure government candidates are identified against KGID where available, reduce manual demographic re-entry, and create a verified Type 1 registration draft that can continue into examination selection, preferences, fee and confirmation.

### Actors
Maker: Candidate (government employee) via candidate portal after OTP login (Module 02). Approver: none on this feature (administrator verification is F04-006). Auditor: Examination Administrator (read of KGID retrieval and confirmation events).

### User Journey
1. Who creates: The candidate who selects **Government employee** as registration type after OTP login.
2. How they create: Open registration → choose Government type → enter KGID → request retrieval → review returned employee fields → confirm accuracy → enter father’s name, mobile, email and other required additional fields → save Type 1 draft.
3. How they edit: Before fee/confirmation lock, the candidate may re-open the draft, re-fetch KGID (if allowed), correct additional fields, and re-confirm retrieved details; KGID-sourced fields that are locked after confirmation require explicit re-confirmation after a new retrieval.
4. How they send for approval: Does not apply on this feature — Type 1 identity capture is maker-side only; any admin verification of the completed registration is F04-006.
5. How the approver sees pending items: No approver inbox in this feature; administrators do not approve KGID confirmation here.
6. How the approver decides: No decision step in this feature.
7. How the applicant / maker sees history: Candidate sees retrieval status, last confirmation timestamp, and draft identity section within the registration journey and later on status (F04-005).
8. How the approver / auditor sees history: Examination Administrator can view KGID retrieval attempts, confirmation flag, source field snapshot and change events on the registration record (used later in F04-006 review).

### Functional Capabilities
- Government registration type selection distinct from other-organisation path (F04-002).
- Mandatory KGID capture with format validation before retrieval.
- Call KGID integration to retrieve available employee particulars.
- Present retrieved fields for candidate review with clear source labelling.
- Require explicit candidate confirmation of retrieved details before proceeding.
- Capture additional mandatory fields not returned by KGID (father’s name, mobile, email, configurable extras).
- Graceful handling when KGID API is unavailable or returns partial fields (manual completion of missing fields per Department rule).
- Block progression on this path if KGID is blank or confirmation is not completed (when integration is available).
- Persist Type 1 identity draft linked to the candidate OTP session identity.
- Prevent duplicate active Type 1 drafts for the same KGID against the same open examination (configurable).
- Mask or restrict display of sensitive KGID-linked fields per security policy.
- Audit every retrieval request, response outcome, confirmation and subsequent identity edits.
- Surface retrieval failure reasons to the candidate without exposing integration internals.

### UI Screens
| Screen | Purpose |
|---|---|
| Registration type selection screen | Candidate chooses Government vs Other Organisation path |
| KGID entry and retrieval screen | Enter KGID and trigger retrieval |
| Retrieved employee details confirmation screen | Review and confirm KGID-returned fields |
| Additional details capture form | Father’s name, mobile, email and other required fields |
| Type 1 identity draft summary screen | Read-only summary before continuing to F04-003 |
| KGID retrieval and confirmation history screen | Candidate/admin view of retrieval and confirmation events |

### Logical API operations
| Operation | Purpose |
|---|---|
| Select government registration type | Start Type 1 path and initialise draft |
| Submit KGID for employee retrieval | Validate KGID and invoke integration |
| Confirm retrieved employee details | Persist confirmation and lock confirmed fields |
| Save additional registration details | Persist non-KGID mandatory fields |
| Save Type 1 registration identity draft | Persist draft for later preference/fee steps |
| Get KGID retrieval and confirmation history | Return retrieval/confirmation audit for the draft |

### Inputs
KGID number; candidate confirmation action; father’s name; mobile; email; other configurable Type 1 fields; candidate portal session identity.

### Outputs
Type 1 registration identity draft; KGID retrieval snapshot; confirmation timestamp; audit events; readiness flag for examination selection (F04-003).

### Business Rules
- Government path requires KGID; blank KGID cannot proceed.
- Candidate must confirm retrieved details when the integration returns data.
- When integration is unavailable, Department-approved fallback (retry / deferred / limited manual) applies without inventing KGID authority.
- Confirmed KGID-sourced fields are not silently overwritten without a new retrieval and re-confirmation.
- Type 1 draft does not complete registration by itself; fee and confirmation gates remain in F04-004 / F04-005.
- One candidate portal identity owns the draft; KGID uniqueness rules against open examinations follow Module 03 / Department policy.

### Validations
- KGID format and mandatory presence.
- Mobile and email format for additional fields.
- Confirmation checkbox/action required when retrieved payload is present.
- Duplicate KGID against same examination when configured.
- Session must be authenticated candidate OTP session.

### Calculations
None beyond field completeness indicators for draft readiness.

### Workflow
Draft started → KGID submitted → retrieval attempted → details confirmed (or partial/fallback path) → additional fields saved → Type 1 identity draft ready for F04-003. No maker–checker approval inside this feature.

### Search Requirements
Administrator may locate drafts by KGID, mobile, name (from retrieval), and draft status for support and later verification (F04-006).

### Documents
None in this feature (competent-authority document is F04-002 only).

### Reports
Operational counts of Type 1 drafts and KGID retrieval success/failure feed Module 09; no dedicated report artefact billed here.

### Notifications
Optional retrieval-failure guidance in-portal; lifecycle SMS/email for registration completion is owned by F04-005 / Module 09.

### Security
Candidate may create/edit only own draft; KGID payloads logged with controlled access; staff view of KGID data requires Examination Administrator privilege; all retrieval and confirmation events audited.

### Integrations
**KGID system / API** — retrieve government employee details (subject to API and data availability). Estimated as Integration **Very High**.

### Dependencies
Module 02 (candidate OTP login); Module 03 (examination/fee masters for later steps); F04-003 onwards consume the Type 1 draft.

### Assumptions
- KGID connector is estimated on this feature (not a separate integration module).
- Exact KGID field catalogue is as facilitated by the Department/API; missing fields are completed manually.
- Rebuild of the KGID system itself is out of scope.
- Hours use Estimation Master; each named screen and logical API is a separate Section 2 row.

### Risks
KGID API field gaps or downtime force fallback paths and may increase manual correction and admin verification load (F04-006).

### Non Functional Requirements
Retrieval timeout and retry messaging; auditable integration calls; PII protection for employee details; production-grade validation and error handling.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Registration type selection screen | UI | Medium | 6 |
| KGID entry and retrieval screen | UI | Medium | 6 |
| Retrieved employee details confirmation screen | UI | Complex | 12 |
| Additional details capture form | UI | Complex | 12 |
| Type 1 identity draft summary screen | UI | Easy | 4 |
| KGID retrieval and confirmation history screen | UI | Easy | 4 |
| Select government registration type | API | Easy | 4 |
| Submit KGID for employee retrieval | API | Complex | 8 |
| Confirm retrieved employee details | API | Medium | 6 |
| Save additional registration details | API | Medium | 6 |
| Save Type 1 registration identity draft | API | Medium | 6 |
| Get KGID retrieval and confirmation history | API | Easy | 4 |
| Type 1 identity and KGID snapshot persistence | Database | Complex | 6 |
| KGID system / API employee retrieval | Integration | Very High | 40 |
| Government KGID registration tests | Testing | Very High | 12 |
| Government KGID registration implementation documentation | Documentation | Complex | 4 |

**Feature total: 140 hours**

### Estimation Assumptions
- KGID Integration billed at Estimation Master **Very High (40)** on this feature.
- Payment, centre preferences, confirmation number and admin verification are separate features.
- Enterprise-grade logging, retry and partial-response handling are included in Integration and API rows.
