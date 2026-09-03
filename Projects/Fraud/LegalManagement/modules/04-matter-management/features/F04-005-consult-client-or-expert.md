# F04-005 — Consult client or expert

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Consult client or expert |
| **Module** | 04 — Matter Management |

### Description
The user raises a consultation to Client, External Expert, Research Expert or Other on the matter, attaches context, and records the response against the matter.

### Business Objective
Record consultations (Client, External Expert, Research Expert or Other) on the matter with context and response.

### Actors
Legal Cell; Advocate; authorised client-side user where permitted.

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens Consult on the matter and chooses Client, External Expert, Research Expert or Other.
3. How they edit: Attaches context and sends/raises the consultation.
4. How they send for approval: Records the response against the matter. Raise → attach context → record response → visible on matter.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Thread remains on the matter dashboard.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Raise Consultation form
- Consultation Thread / Response screen
- Types: Client / External Expert / Research Expert / Other
- Attach context; record response on the matter
- Not a public collaboration portal

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Raise Consultation form | Medium |
| Consultation Thread / Response screen | Medium |
| Consult client or expert history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Consultation operations | Medium |
| Update consult client or expert | Medium |
| Search consult client or expert | Medium |
| Read consult client or expert history | Easy |

### Inputs
Consultation type; addressee (contact); context attachments; response text/file.

### Outputs
Consultation record; response on the matter; activity on dashboard.

### Business Rules
- Consultations are matter-bound.
- External Expert is not a valuer billing flow (EVAL out of scope).
- Need-to-know applies to attachments.

### Validations
- Matter and type required; addressee identifiable; response stored against the same consultation.

### Calculations
None.

### Workflow
Raise → attach context → record response → visible on matter.

### Search Requirements
Consultation type, addressee, date, matter.

### Documents
Attached context and response files.

### Reports
Consultations on matter (list).

### Notifications
Notice to addressee/Legal Cell when a consultation is raised or answered.

### Security
Attachments follow F01-003; Limited space if used.

### Integrations
Contact lookup (Simple).

### Dependencies
F04-001; F06; F05-005 related queries/meetings.

### Assumptions
- ‘Client’ here is the authorised client-side Legal collaboration user, not a citizen portal.

### Risks
Advice captured off-matter in email only — this feature is the system of record when used.

### Non Functional Requirements
Thread retained with the matter.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Raise Consultation form | UI | Medium | 6 |
| Consultation Thread / Response screen | UI | Medium | 6 |
| Consult client or expert history | UI | Medium | 6 |
| Consultation operations | API | Medium | 6 |
| Update consult client or expert | API | Medium | 6 |
| Search consult client or expert | API | Medium | 6 |
| Read consult client or expert history | API | Easy | 4 |
| Consult client or expert persistence | DB | Medium | 4 |
| Contact lookup | Integration | Simple | 4 |
| Consult client or expert feature tests | Testing | Easy | 4 |
| Consult client or expert implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **54** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
