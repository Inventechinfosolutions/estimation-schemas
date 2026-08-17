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
1. User opens Keyword–Document Link Maintenance.
2. Links a keyword to a library or matter document, or opens a broken-link row after a catalogue change.
3. Repairs the target and saves.
4. Search and hyperlink navigation use the repaired address.

### Functional Capabilities
- Keyword–Document Link Register
- Broken-Link Repair screen
- Create link from keyword to library or matter document
- Repair after catalogue change (no silent break)
- Navigation uses the repaired link

### Inputs
Keyword; document address (library or matter); repair action; Person.

### Outputs
Link record; repaired target; broken-link queue clearance.

### Business Rules
- Changing a central keyword must not silently leave dead hyperlinks; repair is available.
- Originals in the library remain unchanged; only the link metadata is updated.
- Links are not auto-rewritten by generative AI.

### Validations
Keyword and document required; broken links flagged when the catalogue entry is renamed/deactivated; save required before navigation uses the new target.

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
Catalogue change events from F02-001/F02-002 feed the broken-link queue.

### Risks
Unrepaired links send users to missing documents during court preparation.

### Non Functional Requirements
Repair effective for subsequent search and hyperlink clicks.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Keyword–Document Link Register | UI | Medium | 6 |
| Broken-Link Repair screen | UI | Medium | 6 |
| Link create and repair operations | API | Medium | 6 |
| Link entities | Database | Easy | 2 |
| Library/matter document address resolve | Integration | Simple | 4 |
| Link maintenance tests | Testing | Easy | 4 |
| Keyword–document link guide | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Highlight/hyperlink rendering in search results is F03-007.
