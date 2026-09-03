# F02-006 — Keyword–document link maintenance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-006 |
| **Feature Name** | Keyword–document link maintenance |
| **Module** | 02 — Legal Masters, Keywords & Templates |

### Description
The user links a keyword to a library or matter document, or repairs a broken link after a catalogue change, then saves. Search and hyperlink navigation use the repaired link.

### Business Objective
Keep keyword-to-document hyperlinks valid after catalogue changes so search and library navigation do not silently break.

### Actors
Legal Cell; Administrator.

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens Keyword–Document Link Maintenance.
3. How they edit: Links a keyword to a library or matter document, or opens a broken-link row after a catalogue change.
4. How they send for approval: Repairs the target and saves. Detect/open broken link or new link → set target → save → search/hyperlink consume.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Search and hyperlink navigation use the repaired address.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Keyword–Document Link Register
- Broken-Link Repair screen
- Create link from keyword to library or matter document
- Repair after catalogue change (no silent break)
- Navigation uses the repaired link

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Keyword–Document Link Register | Medium |
| Broken-Link Repair screen | Medium |
| Keyword–document link maintenance history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Link create and repair operations | Medium |
| Update keyword–document link maintenance | Medium |
| Search keyword–document link maintenance | Medium |
| Read keyword–document link maintenance history | Easy |

### Inputs
Keyword; document address (library or matter); repair action; Person.

### Outputs
Link record; repaired target; broken-link queue clearance.

### Business Rules
- Changing a central keyword must not silently leave dead hyperlinks; repair is available.
- Originals in the library remain unchanged; only the link metadata is updated.
- Links are not auto-rewritten by generative AI.

### Validations
- Keyword and document required; broken links flagged when the catalogue entry is renamed/deactivated; save required before navigation uses the new target.

### Calculations
None.

### Workflow
Detect/open broken link or new link → set target → save → search/hyperlink consume.

### Search Requirements
Keyword, document title, link status (ok/broken), matter/library source.

### Documents
Library and matter documents already stored.

### Reports
Broken keyword-link register.

### Notifications
Optional alert to Legal Cell when catalogue change creates broken links.

### Security
Repair restricted to authorised Posts; access to the target document still follows F01-003.

### Integrations
Library/matter document address (Simple).

### Dependencies
F02-001; F02-002; Modules 03–04.

### Assumptions
- Catalogue change events from F02-001/F02-002 feed the broken-link queue.

### Risks
Unrepaired links send users to missing documents during court preparation.

### Non Functional Requirements
Repair effective for subsequent search and hyperlink clicks.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Keyword–Document Link Register | UI | Medium | 6 |
| Broken-Link Repair screen | UI | Medium | 6 |
| Keyword–document link maintenance history | UI | Medium | 6 |
| Link create and repair operations | API | Medium | 6 |
| Update keyword–document link maintenance | API | Medium | 6 |
| Search keyword–document link maintenance | API | Medium | 6 |
| Read keyword–document link maintenance history | API | Easy | 4 |
| Keyword–document link maintenance persistence | DB | Medium | 4 |
| Library/matter document address resolve | Integration | Simple | 4 |
| Keyword–document link maintenance feature tests | Testing | Easy | 4 |
| Keyword–document link maintenance implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **54** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
