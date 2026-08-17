# F09-008 — Android distribution and licensing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-008 |
| **Feature Name** | Android distribution and licensing |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The delivery includes a clear, non-speculative distribution method (including Play Store licensing where SPLOCA specifically approves). IP remains with SPLOCA.

### Business Objective
Document and implement a non-speculative Android distribution path — Play Store licensing only where SPLOCA specifically approves — with IP remaining with SPLOCA.

### Actors
Administrator; SPLOCA approver; delivery team.

### User Journey
1. SPLOCA records whether Play Store licensing is approved or an alternative official distribution (sideload/MDM/enterprise) is used.
2. Administrator uses Enrolment/Distribution admin and configuration screens.
3. Advocates/Legal Cell receive the app only via the approved path; licensing is recorded, not left speculative.
4. IP and source remain with SPLOCA.

### Functional Capabilities
- Enrolment / Distribution admin
- Play Store / alternative distribution configuration (only the approved path)
- Licensing record (non-speculative)
- No public consumer Play Store listing unless approved
- No iOS
- IP remains with SPLOCA

### Inputs
SPLOCA approval flag for Play Store; package identity; enrolment list of Legal Posts; licence/account artefacts as approved.

### Outputs
Distribution method on record; enrolled devices/Persons; licence documentation.

### Business Rules
- Play Store licensing only where specifically approved.
- Licensing shall be clear, not speculative.
- IP and source code solely with SPLOCA.
- Not a public Play Store consumer app unless that is the approved method.
- Second login directory is forbidden (F01-004).

### Validations
Approval flag required before Play Store path is enabled; enrolment only for Legal Posts; unsigned/unapproved tracks blocked.

### Calculations
None.

### Workflow
Record approval → configure distribution → enrol Persons/devices → ship via approved path.

### Search Requirements
Enrolment by Person, device, distribution method.

### Documents
Licensing/distribution note; IP statement.

### Reports
Enrolment and licensing register.

### Notifications
New version available via the approved store or MDM.

### Security
Signed builds; enrolment tied to shared Person; no open sideload without approval.

### Integrations
Play Store licensing / enterprise distribution as approved (Medium — auth, mapping, retry of store or MDM APIs). Not estimated unless the approved path is used.

### Dependencies
F01-004; all F09 functional screens.

### Assumptions
If Play Store is not approved, hours still cover enterprise/sideload enrolment and the licensing record. Store developer-account fees are commercial, not extra IAM.

### Risks
Leaving licensing ‘TBD’ — this feature exists to prevent that. Delay in SPLOCA approval blocks store publish.

### Non Functional Requirements
Clear distribution runbook; signed artefacts; IP with SPLOCA.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Enrolment / Distribution admin | UI | Medium | 6 |
| Play Store / approved-distribution configuration | UI | Easy | 4 |
| Distribution metadata operations | API | Medium | 6 |
| Licensing and enrolment records | Database | Easy | 2 |
| Play Store or approved enterprise distribution | Integration | Medium | 16 |
| Distribution and licensing tests | Testing | Medium | 6 |
| Android distribution and licensing guide (IP with SPLOCA) | Documentation | Complex | 4 |
| **Total** | | | **44** |

### Estimation Assumptions
- Play Store Integration Medium only for the approved licensing/distribution path — not a speculative multi-store consumer rollout.
- Does not transfer IP away from SPLOCA.
- iOS not estimated.
