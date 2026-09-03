# F09-006 — Distribution and Play Store licensing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-006 |
| **Feature Name** | Distribution and Play Store licensing |
| **Module** | 09 — Valuation Android Application (Approved Valuers) |

### Description
The vendor delivers a secure distribution path. Where SPLOCA specifically approves Play Store licensing, that licensing is stated in clear terms (not a speculative placeholder). IP and source of the app lie with SPLOCA.

### Business Objective
Document and implement official Android distribution and licensing in non-speculative terms, with IP vested in SPLOCA.

### Actors
Administrator; vendor delivery; Approved Valuer (installs via approved path).

### User Journey
1. Who creates: Administrator
2. How they create: Vendor delivers a secure distribution path (enterprise/sideload or equivalent as SPLOCA directs).
3. How they edit: Where SPLOCA specifically approves Play Store licensing, that licensing is stated in clear terms — not a speculative placeholder.
4. How they send for approval: IP and source of the app lie with SPLOCA. iOS and public consumer app are out of scope. Agree path → deliver signed official build → optional Play Store listing if approved → version/licence record.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Administrator works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Administrator opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Secure Android distribution path
- Play Store licensing only where specifically approved, in clear terms
- Record licence/version for the official app
- IP with SPLOCA

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My distribution and play store licensing list / queue | Medium |
| Distribution and licence record | Easy |
| Distribution and play store licensing history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Official version/licence check | Easy |
| Update distribution and play store licensing | Medium |
| Search distribution and play store licensing | Medium |
| Read distribution and play store licensing history | Easy |

### Inputs
Approved distribution mode; licence terms if Play Store approved; app version.

### Outputs
Distribution runbook; licence record; version check against official build.

### Business Rules
- Licensing clear, not speculative
- Play Store only if SPLOCA approves
- iOS out of scope
- Public consumer app out of scope

### Validations
- Distribution mode is one SPLOCA named
- Version is the official build

### Calculations
None.

### Workflow
Agree path → deliver signed official build → optional Play Store listing if approved → version/licence record.

### Search Requirements
App version, distribution mode, licence id if any.

### Documents
Licensing statement; distribution runbook (operations).

### Reports
Installed official version extract if enrolment recorded.

### Notifications
None.

### Security
Only official signed builds; no public store listing unless approved.

### Integrations
Play Store / enterprise distribution as approved (mapping of package, signing, licence) — not a speculative store listing.

### Dependencies
F09-001; SPLOCA approval decision.

### Assumptions
- If Play Store is not approved, enterprise distribution alone is the path.

### Risks
Speculative Play Store line items; IP leakage.

### Non Functional Requirements
Clear licensing wording; IP/source with SPLOCA.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My distribution and play store licensing list / queue | UI | Medium | 6 |
| Distribution and licence record | UI | Easy | 4 |
| Distribution and play store licensing history | UI | Medium | 6 |
| Official version/licence check | API | Easy | 4 |
| Update distribution and play store licensing | API | Medium | 6 |
| Search distribution and play store licensing | API | Medium | 6 |
| Read distribution and play store licensing history | API | Easy | 4 |
| Distribution and play store licensing persistence | DB | Medium | 4 |
| Play Store / enterprise distribution | Integration | Complex | 24 |
| Distribution and Play Store licensing feature tests | Testing | Medium | 6 |
| Distribution and Play Store licensing implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **74** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
