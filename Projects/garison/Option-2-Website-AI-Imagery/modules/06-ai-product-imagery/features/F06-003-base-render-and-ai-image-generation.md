# F06-003 — Base Render & AI Image Generation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-003 |
| Feature Name | Base Render & AI Image Generation |
| Module | 06 — AI Product Imagery |
| Module Type | Technical |
| Release | Go-live |

### Description
Batch process that extrudes each silhouette into a 3D moulding segment and renders a neutral base image at the agreed angle (geometry is exact). The base render, which is our own content, is then passed to the AI service with the category and finish prompt to add realistic wood or primed texture, lighting and shadow. Several candidates are produced per product and stored with prompt, model, cost and date metadata. Approved images get web derivatives.

### Business Objective
Produce realistic, original product images whose shape matches the real profile, at predictable cost.

### Actors
- Delivery developer
- Delivery imagery specialist

### User Journey
1. **Who creates:** The delivery developer runs the generation batches.
2. **How they create:** The pipeline renders base images, calls the AI service in batches and stores candidates with metadata.
3. **How they edit:** Rejected products are re-queued with revised prompts (F06-004).
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees batch logs with counts, failures and cost to date.
8. **How the approver / auditor sees history:** The delivery lead reviews cost against the AI budget each batch.

### Functional Capabilities
- Programmatic 3D extrusion and base render
- Batch AI generation (image-to-image from own base render)
- Multiple candidates per product
- Prompt/model/cost metadata
- Rate-limit, retry and batch scheduling
- Cost tracking against budget cap
- Web derivatives for approved images

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Programmatic 3D extrusion base render from silhouette
- Batch AI image generation from base render and prompt
- Store candidates with prompt and model metadata
- Track generation cost against budget
- Retry, rate-limit and batch scheduling
- Generate web derivatives for approved images

### Inputs
- SVG silhouettes
- Prompt templates
- Product finish/species

### Outputs
- Candidate images
- Approved image set with derivatives
- Generation and cost log

### Business Rules
- Only our own base renders and text prompts are sent to the AI service
- Batch stops when the cost cap is reached
- About 4 candidates per product on average, including regenerations

### Validations
- Output resolution at least 1536 px on the long side
- Every approved image traced to its prompt and model

### Calculations
- Cost = generations × per-image price; tracked per batch

### Workflow
Silhouette → Base render → AI pass → Candidates → Review (F06-004)

### Search Requirements
- None

### Documents
- None

### Reports
- Batch and cost log

### Notifications
- None

### Security
- API keys in secrets store

### Integrations
- AI image generation service
- 3D rendering tool

### Dependencies
- F06-001
- F06-002

### Assumptions
- Batch processing pricing used where available

### Risks
- AI pass occasionally alters edges; geometry checked in review and fallback is the plain base render with studio lighting

### Non Functional Requirements
- Full catalogue batch completes within two working days

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Programmatic 3D extrusion base render from silhouette | Complex | 8 |
| API | Batch AI image generation from base render and prompt | Complex | 8 |
| API | Store candidates with prompt and model metadata | Easy | 4 |
| API | Track generation cost against budget | Easy | 4 |
| API | Retry, rate-limit and batch scheduling | Medium | 6 |
| API | Generate web derivatives for approved images | Easy | 4 |
| Database | Generation log (prompts, candidates, costs) | Easy | 2 |
| Integration | 3D rendering tool automation (for example Blender scripting) | Medium | 16 |
| Testing | Full batch run with failure handling | Medium | 6 |
| Documentation | Generation run guide | Easy | 2 |

**Feature Total: 60 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34 | 2 | 16 | 6 | 2 | **60** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Hybrid render plus AI pipeline; AI fees shown separately
