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
1. User opens Consult on the matter and chooses Client, External Expert, Research Expert or Other.
2. Attaches context and sends/raises the consultation.
3. Records the response against the matter.
4. Thread remains on the matter dashboard.

### Functional Capabilities
- Raise Consultation form
- Consultation Thread / Response screen
- Types: Client / External Expert / Research Expert / Other
- Attach context; record response on the matter
- Not a public collaboration portal

### Inputs
Consultation type; addressee (contact); context attachments; response text/file.

### Outputs
Consultation record; response on the matter; activity on dashboard.

### Business Rules
- Consultations are matter-bound.
- External Expert is not a valuer billing flow (EVAL out of scope).
- Need-to-know applies to attachments.

### Validations
Matter and type required; addressee identifiable; response stored against the same consultation.

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
‘Client’ here is the authorised client-side Legal collaboration user, not a citizen portal.

### Risks
Advice captured off-matter in email only — this feature is the system of record when used.

### Non Functional Requirements
Thread retained with the matter.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Raise Consultation form | UI | Medium | 6 |
| Consultation Thread / Response screen | UI | Medium | 6 |
| Consultation operations | API | Medium | 6 |
| Consultation entities | Database | Easy | 2 |
| Contact lookup | Integration | Simple | 4 |
| Consultation tests | Testing | Easy | 4 |
| Consult client or expert guide | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Queries/meetings lifecycle is F05-005.
