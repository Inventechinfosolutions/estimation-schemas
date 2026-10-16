# F05-001 — Online Test Booking & Slot Availability

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-001 |
| Feature Name | Online Test Booking & Slot Availability |
| Module | 05 — Online Test Booking, Fees & Hall Ticket |
| Module Type | Business |
| Release | Go-live |

### Description
Online Test Booking System showing a calendar of sessions by district and centre with colour-coded availability (available, filling fast, full), seat hold during booking and payment, category enforcement (employees on Saturdays, prospective on Sundays), support-adjusted seats, and confirmation.

### Business Objective
Let candidates choose date, time and place while preventing over-booking.

### Actors
- Candidate
- KEONICS Administrator (view)

### User Journey
1. **Who creates:** The candidate with an accepted registration starts booking.
2. **How they create:** The candidate selects district, centre, date and session from colour-coded slots; a seat is held for 15 minutes.
3. **How they edit:** The candidate can change selection before confirmation.
4. **How they send for approval:** Free bookings confirm immediately; paid bookings move to payment (F05-002).
5. **How the approver sees pending items:** The administrator sees booking counts per session.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees the booking, hall ticket and history.
8. **How the approver / auditor sees history:** Auditors see booking events and seat holds.

### Functional Capabilities
- Calendar and list views by district / centre
- Colour-coded availability
- Seat hold with expiry
- Category rules per day
- Accessible seat filtering
- Booking confirmation and number
- Concurrency control under peak load
- Booking window enforcement

### UI Screens
- Session calendar with colour-coded slots
- Centre and session selection
- Booking review and confirm
- My bookings

### Logical API Operations
- Availability by centre and date
- Hold seat with expiry
- Confirm booking
- Release expired holds
- Category and window validation
- My bookings

### Inputs
- Centre, date, session

### Outputs
- Confirmed booking

### Business Rules
- One active booking per candidate
- No mixing of categories in a session
- Booking closes at the configured cut-off
- No cancellation

### Validations
- Registration accepted
- Session open

### Calculations
- Available = capacity − confirmed − held

### Workflow
Held → Confirmed / Expired

### Search Requirements
- Sessions by district, date

### Documents
- None

### Reports
- Booking statistics

### Notifications
- Booking confirmation

### Security
- Own bookings only

### Integrations
- None

### Dependencies
- F02-003
- F04-005
- F05-002

### Assumptions
- Seat holds of 15 minutes

### Risks
- Peak load at booking open

### Non Functional Requirements
- Availability under 1 second; 1,000 concurrent booking requests

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Session calendar with colour-coded slots | Complex | 12 |
| UI | Centre and session selection | Medium | 6 |
| UI | Booking review and confirm | Medium | 6 |
| UI | My bookings | Easy | 4 |
| API | Availability by centre and date | Complex | 8 |
| API | Hold seat with expiry | Complex | 8 |
| API | Confirm booking | Medium | 6 |
| API | Release expired holds | Medium | 6 |
| API | Category and window validation | Medium | 6 |
| API | My bookings | Easy | 4 |
| Database | Booking and seat inventory | Complex | 6 |
| Testing | Booking concurrency and over-booking tests | Complex | 8 |
| Testing | Booking rule tests | Medium | 6 |
| Documentation | Booking guide (bilingual) | Easy | 2 |

**Feature Total: 88 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 38 | 6 | 0 | 14 | 2 | **88** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Seat inventory concurrency rated Complex
- No external integration channel in this feature; Integration row omitted.
