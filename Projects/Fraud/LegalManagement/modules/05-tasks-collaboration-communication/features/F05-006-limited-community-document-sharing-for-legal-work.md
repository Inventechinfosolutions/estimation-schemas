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
1. Who creates: Legal Cell
2. How they create: User chooses a document and a purpose: Information, Response, Correction, Opinion, Drafting or Approval.
3. How they edit: Chooses Limited (named Persons) or Community.
4. How they send for approval: Only those members can open it. Select document → purpose → Limited/Community → enforce on open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Share Purpose picker (Information / Response / Correction / Opinion / Drafting / Approval)
- Limited vs Community Share dialog
- Open only for members
- Purpose stored on the share

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Share Purpose picker (Information, Response, Correction, Opinion, Drafting, Approval) | Medium |
| Limited vs Community Share dialog | Complex |
| Limited/community document sharing for legal work history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Purpose-based share operations | Complex |
| Update limited/community document sharing for legal work | Medium |
| Search limited/community document sharing for legal work | Medium |
| Read limited/community document sharing for legal work history | Easy |

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
- Purpose required; Limited requires at least one named Person; document must exist.

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
- F04-004 versions the file; this feature adds purpose-based legal sharing.

### Risks
Wrong purpose (Approval vs Information) misleads the recipient.

### Non Functional Requirements
Immediate membership enforcement.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Share Purpose picker (Information, Response, Correction, Opinion, Drafting, Approval) | UI | Medium | 6 |
| Limited vs Community Share dialog | UI | Complex | 12 |
| Limited/community document sharing for legal work history | UI | Medium | 6 |
| Purpose-based share operations | API | Complex | 8 |
| Update limited/community document sharing for legal work | API | Medium | 6 |
| Search limited/community document sharing for legal work | API | Medium | 6 |
| Read limited/community document sharing for legal work history | API | Easy | 4 |
| Limited/community document sharing for legal work persistence | DB | Medium | 4 |
| Limited/Community space enforcement | Integration | Simple | 4 |
| Limited/Community document sharing for legal work feature tests | Testing | Medium | 6 |
| Limited/Community document sharing for legal work implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
