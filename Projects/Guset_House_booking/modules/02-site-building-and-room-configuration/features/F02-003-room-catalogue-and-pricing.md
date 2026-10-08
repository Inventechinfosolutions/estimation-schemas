# F02-003 — Room Catalogue and Pricing

| Field | Value |
|-------|-------|
| Feature ID | F02-003 |
| Feature Name | Room Catalogue and Pricing |
| Module | 02 — Site, Building & Room Configuration |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Administrator defines rooms under floors with type, capacity, amenities, pricing, and availability status.

### Business Objective
Maintain bookable room inventory with commercial and amenity attributes.

### Actors
- Platform Administrator
- Site Administrator

### User Journey
1. Administrator creates room records under a floor.
2. Administrator enters type, capacity, amenities, base pricing, and availability status.
3. Administrator edits attributes; marks rooms under maintenance as unavailable.
4. Approval does not apply — direct save.
5. No approver inbox.
6. No approver decision.
7. Administrator sees room history of price/status changes.
8. Auditor reviews pricing/status change history.

### Functional Capabilities
- Create/edit room
- Set amenities and capacity
- Set pricing
- Set availability status
- Bulk status update (optional light)

### UI Screens
- Room register
- Room create/edit form
- Amenities selector dialog
- Room status change confirmation
- Room price/status history

### Logical API Operations
- List/search rooms
- Create room
- Update room
- Change room availability status
- Get room history

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Room uniquely identified within building
- Unavailable rooms excluded from booking search
- Price used in booking summary

### Validations
- Type, capacity, price mandatory
- Capacity > 0
- Price >= 0

### Calculations
- Derived display of occupancy capacity

### Workflow
Available ↔ Unavailable/Maintenance

### Search Requirements
Filter by site, building, floor, type, status

### Documents
None

### Reports
None

### Notifications
None

### Security
- Admin only
- Audit price changes

### Integrations
None

### Dependencies
- F02-002

### Assumptions
- Simple base price per night/day as configured; seasonal pricing out of scope unless added

### Risks
- Stale availability status causes overbooking pressure on conflict engine

### Non Functional Requirements
- Room register supports centre-scale inventories

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Room register | Medium | 6 |
| UI | Room create/edit form | Complex | 12 |
| UI | Amenities selector dialog | Easy | 4 |
| UI | Room status change confirmation | Simple | 2 |
| UI | Room price/status history | Easy | 4 |
| API | List/search rooms | Medium | 6 |
| API | Create room | Complex | 8 |
| API | Update room | Complex | 8 |
| API | Change room availability status | Medium | 6 |
| API | Get room history | Easy | 4 |
| Database | Persistence for feature entities/constraints | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 75 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Simple base price per night/day as configured; seasonal pricing out of scope unless added / Stale availability status causes overbooking pressure on conflict engine.
