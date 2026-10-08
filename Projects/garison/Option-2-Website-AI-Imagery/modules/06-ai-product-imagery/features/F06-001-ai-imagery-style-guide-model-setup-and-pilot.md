# F06-001 — AI Imagery Style Guide, Model Setup & Pilot

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-001 |
| Feature Name | AI Imagery Style Guide, Model Setup & Pilot |
| Module | 06 — AI Product Imagery |
| Module Type | Technical |
| Release | Go-live |

### Description
Define the product image style (angle, lighting, background, wood or primed finish, shadow), choose a commercially licensed AI image service (preferably one offering output indemnity), set up the account, keys and spending limits, write prompt templates per category and finish, and run a pilot on 20 representative products for Garrison's approval before the full batch. Includes a legal checklist for Garrison's counsel.

### Business Objective
Agree a consistent, legally reviewed image style and prove accuracy on a sample before generating the full catalogue.

### Actors
- Delivery imagery specialist
- Delivery developer
- Garrison business owner

### User Journey
1. **Who creates:** The delivery imagery specialist prepares the style guide and pilot.
2. **How they create:** They define the style, set up the AI service, write prompt templates and generate the pilot set.
3. **How they edit:** Prompts and style are revised after Garrison's feedback on the pilot.
4. **How they send for approval:** The pilot set and style guide are sent to Garrison for approval.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's approval email releases the full batch (F06-003).
7. **How the maker sees history:** Garrison sees the pilot versions and style guide.
8. **How the approver / auditor sees history:** The delivery lead keeps the approved style guide, pilot set and legal checklist.

### Functional Capabilities
- Image style guide
- AI service selection with licence and indemnity check
- Account, keys and spending limits
- Prompt templates per category and finish
- 20-product pilot
- Legal checklist for Garrison's counsel

### UI Screens
- Style reference board (angle, lighting, background, finish)

### Logical API Operations
- Prompt template library per category and finish
- AI service account, keys and spending limits setup
- Pilot generation on 20 sample products

### Inputs
- Product dataset
- Profile silhouettes for pilot products (F06-002)
- Garrison style preferences

### Outputs
- Approved style guide
- Prompt templates
- Approved pilot set

### Business Rules
- Only services whose terms permit commercial use are used
- Source photographs are never sent to the AI service as input
- Full batch starts only after pilot approval

### Validations
- Pilot images match profile geometry within visual tolerance

### Calculations
- Pilot generation count and cost

### Workflow
Style → Setup → Pilot → Approved

### Search Requirements
- None

### Documents
- Style guide
- Legal checklist

### Reports
- None

### Notifications
- None

### Security
- API keys held in a secrets store; spending cap set on the account

### Integrations
- AI image generation service

### Dependencies
- F06-002

### Assumptions
- AI service fees are a pass-through cost, shown separately from effort

### Risks
- AI models can distort exact profile shapes; the pipeline controls geometry with a programmatic base render (F06-003)

### Non Functional Requirements
- Pilot delivered within one week of silhouette availability

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Style reference board (angle, lighting, background, finish) | Medium | 6 |
| API | Prompt template library per category and finish | Medium | 6 |
| API | AI service account, keys and spending limits setup | Easy | 4 |
| API | Pilot generation on 20 sample products | Medium | 6 |
| Integration | AI image generation service (API) | Medium | 16 |
| Testing | Pilot accuracy review against reference profiles | Medium | 6 |
| Documentation | AI imagery style guide and legal checklist | Medium | 3 |

**Feature Total: 47 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 16 | 0 | 16 | 6 | 3 | **47** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- One external AI service integration
