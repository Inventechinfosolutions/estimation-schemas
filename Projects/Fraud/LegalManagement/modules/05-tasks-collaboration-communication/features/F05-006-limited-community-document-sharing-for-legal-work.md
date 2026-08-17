# F05-006 — Limited/Community document sharing for legal work

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-006 |
| **Feature Name** | Limited/Community document sharing for legal work |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
The user shares a document for Information, Response, Correction, Opinion, Drafting or Approval, choosing Limited (named Persons) or Community. Only those members can open it.

### Business Objective
Share legal-work documents with a stated purpose and Limited or Community audience, honouring named-member closure.

### Actors
Legal Cell; Advocate; named Limited members.

### User Journey
1. User chooses a document and a purpose: Information, Response, Correction, Opinion, Drafting or Approval.
2. Chooses Limited (named Persons) or Community.
3. Only those members can open it.

### Functional Capabilities
- Share Purpose picker (Information / Response / Correction / Opinion / Drafting / Approval)
- Limited vs Community Share dialog
- Open only for members
- Purpose stored on the share

### Inputs
Document; purpose; space type; named Persons for Limited.

### Outputs
Share record; member-only open.

### Business Rules
- Limited-space shares are not visible to non-members.
- Community still subject to hierarchy/need-to-know (F01-002).
- Purpose does not override F01-003 download/edit rights.
- Not a market-intelligence investigation room.

### Validations
Purpose required; Limited requires at least one named Person; document must exist.

### Calculations
None.

### Workflow
Select document → purpose → Limited/Community → enforce on open.

### Search Requirements
Shares by purpose, space type, document, matter.

### Documents
The shared legal document.

### Reports
Legal share register (purpose and audience).

### Notifications
Share notice to named/Community-eligible members.

### Security
Non-members get no listing; access log on open.

### Integrations
F01-002 space enforcement (Simple).

### Dependencies
F01-002; F01-003; F04-004.

### Assumptions
F04-004 versions the file; this feature adds purpose-based legal sharing.

### Risks
Wrong purpose (Approval vs Information) misleads the recipient.

### Non Functional Requirements
Immediate membership enforcement.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Share Purpose picker (Information, Response, Correction, Opinion, Drafting, Approval) | UI | Medium | 6 |
| Limited vs Community Share dialog | UI | Complex | 12 |
| Purpose-based share operations | API | Complex | 8 |
| Share records | Database | Medium | 4 |
| Limited/Community space enforcement | Integration | Simple | 4 |
| Legal share tests | Testing | Medium | 6 |
| Limited/Community legal sharing guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Space create/membership UI is F01-002.
