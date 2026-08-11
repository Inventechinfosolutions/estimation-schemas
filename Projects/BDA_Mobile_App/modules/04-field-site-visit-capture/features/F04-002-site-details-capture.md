# F04-002 — Site Details Capture

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F04-002 |
| Feature Name | Site Details Capture |
| Module | 04 — Field Site Visit Capture |
| Description | Capture site identification, shape, and regular or odd/irregular multi-side dimensions plus area/geo stamp. |
| Business Objective | Record correct site dimensions for CDR. |
| Actors | Engineer |

### User Journey

- Engineer enters identification → selects shape → enters L×B or multi-side lengths → area → geo stamp recorded.

### Functional Capabilities

- Site identification fields
- Regular L×B dimensions
- Odd/irregular variable sides
- Area
- Geo stamp

### Inputs

- Layout/survey/site refs
- Shape
- Side lengths
- Area

### Outputs

- Site details on application

### Business Rules

- Odd shape allows variable sides
- Not forced to L×B when odd

### Validations

- Mandatory ID/dimension fields as configured

### Calculations

- Area units sq.ft/sq.m

### Workflow

- Part of draft/submit

### Search Requirements

- None

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- Engineer within geo

### Integrations

- None

### Dependencies

- F04-001
- F02-002

### Assumptions

- Masters for shape/category available

### Risks

- Irregular sites hard to measure

### Non Functional Requirements

- Works on mobile online

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Site identification form | Medium | 6 |
| UI | Odd/irregular multi-side dimensions UI | Complex | 8 |
| API | Save site details & dimensions | Complex | 8 |
| Database | Persistence / constraints for this feature | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 37 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
