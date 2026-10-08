# F03-002 — Booking Request with Conflict Prevention

| Field | Value |
|-------|-------|
| Feature ID | F03-002 |
| Feature Name | Booking Request with Conflict Prevention |
| Module | 03 — Booking & Room Allocation |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Employee creates a booking request for selected dates/room; system validates conflicts and prevents double booking.

### Business Objective
Capture booking intent while ensuring hard conflict prevention on the same room and overlapping dates.

### Actors
- Employee Guest

### User Journey
1. Employee creates booking from an available room result.
2. Employee confirms stay dates and guests/occupants within capacity, then saves booking in Pending Payment state.
3. Employee may cancel pending booking before payment; cannot edit dates after payment without admin override (Module 06).
4. Approval does not apply for standard booking — payment is the gate.
5. No approver inbox for standard path.
6. No approver decision for standard path.
7. Employee sees own booking list and status history.
8. Auditor/Admin sees booking creation history and conflict rejections.

### Functional Capabilities
- Create booking request
- Validate capacity and conflicts
- Hold room per policy until payment timeout
- Cancel pending booking
- List own bookings

### UI Screens
- Create booking form
- Conflict rejection dialog
- My bookings register
- Cancel pending booking confirmation

### Logical API Operations
- Create booking request
- Cancel pending booking
- List my bookings
- Get booking detail

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- No overlapping Confirmed/Held bookings for same room
- Occupants ≤ room capacity
- Identity Accepted required

### Validations
- Dates mandatory
- Room must be available for range
- User eligible

### Calculations
- Hold expiry time

### Workflow
Draft/PendingPayment → Cancelled | AwaitingPayment

### Search Requirements
Employee search own bookings by date/status

### Documents
None

### Reports
None

### Notifications
Optional hold expiry reminder

### Security
- User can access only own bookings
- Conflict checks server-side transactional

### Integrations
None

### Dependencies
- F03-001
- F01-002

### Assumptions
- Short payment hold to reduce ghost blocking

### Risks
- Race conditions under concurrent booking

### Non Functional Requirements
- Conflict check atomic

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Create booking form | Complex | 12 |
| UI | Conflict rejection dialog | Simple | 2 |
| UI | My bookings register | Medium | 6 |
| UI | Cancel pending booking confirmation | Simple | 2 |
| API | Create booking request | Very High | 16 |
| API | Cancel pending booking | Medium | 6 |
| API | List my bookings | Medium | 6 |
| API | Get booking detail | Easy | 4 |
| Database | Persistence for feature entities/constraints | Complex | 6 |
| Testing | Feature test coverage | Very High | 12 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 75 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Short payment hold to reduce ghost blocking / Race conditions under concurrent booking.
