# F09-003 — Android communication and messaging

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-003 |
| **Feature Name** | Android communication and messaging |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user sends a matter communication or internal message from the phone. Recipients see it on web and Android; it is stored on the matter.

### Business Objective
Send matter communication and internal messages from Android, stored on the matter and visible on web.

### Actors
Advocate; Legal Cell.

### User Journey
1. Who creates: Advocate
2. How they create: User sends a matter communication or internal message from the phone.
3. How they edit: Recipients see it on web and Android.
4. How they send for approval: It is stored on the matter. Compose on Android → save on matter → web and Android recipients.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Android Matter Message screens
- Internal messaging
- Stored on the matter; visible both channels
- Not consumer WhatsApp replacement as a product — official matter messages

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Android Matter Message screens | Complex |
| Internal messaging | Medium |
| Android communication and messaging history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Message send/sync operations | Complex |
| Update android communication and messaging | Medium |
| Search android communication and messaging | Medium |
| Read android communication and messaging history | Easy |

### Inputs
Matter; message; recipients as allowed.

### Outputs
Matter-stored message; dual-channel visibility.

### Business Rules
- Stored on the matter (F05-007).
- Limited/Community still apply.
- Email sync itself is web F05-008; device sends official messages.

### Validations
- Matter required; session valid; recipients allowed.

### Calculations
None.

### Workflow
Compose on Android → save on matter → web and Android recipients.

### Search Requirements
On device by matter thread; full Person/Date/Case/Keyword search remains web F05-007 if not fully replicated.

### Documents
Optional attachment.

### Reports
None.

### Notifications
Recipient in-app.

### Security
No leak of Limited threads.

### Integrations
Web comms backend (Medium).

### Dependencies
F05-007; F01-004; F01-002.

### Assumptions
- Full email mailbox sync UI may remain web-primary (F05-008).

### Risks
Message sent to wrong matter from a small screen.

### Non Functional Requirements
Delivery once network available.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Android Matter Message screens | UI | Complex | 12 |
| Internal messaging | UI | Medium | 6 |
| Android communication and messaging history | UI | Medium | 6 |
| Message send/sync operations | API | Complex | 8 |
| Update android communication and messaging | API | Medium | 6 |
| Search android communication and messaging | API | Medium | 6 |
| Read android communication and messaging history | API | Easy | 4 |
| Android communication and messaging persistence | DB | Medium | 4 |
| Web communication backend | Integration | Medium | 16 |
| Android communication and messaging feature tests | Testing | Complex | 8 |
| Android communication and messaging implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
