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
1. User sends a matter communication or internal message from the phone.
2. Recipients see it on web and Android.
3. It is stored on the matter.

### Functional Capabilities
- Android Matter Message screens
- Internal messaging
- Stored on the matter; visible both channels
- Not consumer WhatsApp replacement as a product — official matter messages

### Inputs
Matter; message; recipients as allowed.

### Outputs
Matter-stored message; dual-channel visibility.

### Business Rules
- Stored on the matter (F05-007).
- Limited/Community still apply.
- Email sync itself is web F05-008; device sends official messages.

### Validations
Matter required; session valid; recipients allowed.

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
Full email mailbox sync UI may remain web-primary (F05-008).

### Risks
Message sent to wrong matter from a small screen.

### Non Functional Requirements
Delivery once network available.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Matter Message screens | UI | Complex | 12 |
| Internal messaging | UI | Medium | 6 |
| Message send/sync operations | API | Complex | 8 |
| Device message cache | Database | Easy | 2 |
| Web communication backend | Integration | Medium | 16 |
| Android messaging tests | Testing | Complex | 8 |
| Android communication guide | Documentation | Medium | 3 |
| **Total** | | | **55** |

### Estimation Assumptions
- Email sync hours remain F05-008.
