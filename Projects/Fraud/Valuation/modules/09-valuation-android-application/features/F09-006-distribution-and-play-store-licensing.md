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
1. Vendor delivers a secure distribution path (enterprise/sideload or equivalent as SPLOCA directs).
2. Where SPLOCA specifically approves Play Store licensing, that licensing is stated in clear terms — not a speculative placeholder.
3. IP and source of the app lie with SPLOCA. iOS and public consumer app are out of scope.

### Functional Capabilities
- Secure Android distribution path
- Play Store licensing only where specifically approved, in clear terms
- Record licence/version for the official app
- IP with SPLOCA

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
|---|---|---|---:|
| Distribution and licence record | UI | Easy | 4 |
| Official version/licence check | API | Easy | 4 |
| Licence/version store | Database | Simple | 1 |
| Play Store / enterprise distribution | Integration | Complex | 24 |
| Distribution/licensing tests | Testing | Medium | 6 |
| Android licensing and distribution guide | Documentation | Complex | 4 |
| **Total** | | | **43** |

### Estimation Assumptions
- Integration Complex 24 for official distribution/licensing. Not GIS Very High 40.
