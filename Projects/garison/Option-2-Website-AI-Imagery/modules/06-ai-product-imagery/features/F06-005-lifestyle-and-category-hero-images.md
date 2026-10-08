# F06-005 — Lifestyle & Category Hero Images

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-005 |
| Feature Name | Lifestyle & Category Hero Images |
| Module | 06 — AI Product Imagery |
| Module Type | Technical |
| Release | Go-live |

### Description
AI-generated scene images for the home page hero, category banners and supporting page imagery (for example finished rooms showing crown, casing and baseboard), retouched and cropped to the approved layouts.

### Business Objective
Give the new website attractive imagery without a photo shoot.

### Actors
- Delivery imagery specialist
- Garrison business owner

### User Journey
1. **Who creates:** The delivery imagery specialist creates the scene images.
2. **How they create:** They write scene prompts per layout, generate candidates and retouch the chosen ones.
3. **How they edit:** Scenes are regenerated after Garrison's feedback.
4. **How they send for approval:** The scene set is shared with Garrison for approval.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's approval email releases the scenes for the website.
7. **How the maker sees history:** Garrison sees the scene image register.
8. **How the approver / auditor sees history:** The delivery lead keeps the approved register.

### Functional Capabilities
- Home hero scenes
- Category banners
- Supporting page imagery
- Retouch and crop to layouts

### UI Screens
- Home hero image set (3–5 scenes)
- Category banner images (up to 20)
- Supporting page imagery

### Logical API Operations
- Scene prompt series and generation runs
- Retouch and crop to layouts

### Inputs
- Approved designs
- Scene list

### Outputs
- About 25 approved scene images

### Business Rules
- Scenes are labelled illustrative and do not claim to show specific Garrison installations
- No recognisable people, brands or real properties

### Validations
- Each scene fits its layout crop at required resolution

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F01-003
- F06-001

### Assumptions
- About 25 scenes at about 10 candidates each

### Risks
- Scenes can look generic; Garrison photos preferred where available

### Non Functional Requirements
- Hero images under 250 KB after optimisation

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Home hero image set (3–5 scenes) | Medium | 6 |
| UI | Category banner images (up to 20) | Medium | 6 |
| UI | Supporting page imagery | Easy | 4 |
| API | Scene prompt series and generation runs | Medium | 6 |
| API | Retouch and crop to layouts | Easy | 4 |
| Testing | Brand and plausibility review of scenes | Easy | 4 |
| Documentation | Scene image register | Simple | 1 |

**Feature Total: 31 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 10 | 0 | 0 | 4 | 1 | **31** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Design-scale rows for scene sets
- No external integration channel in this feature; Integration row omitted.
