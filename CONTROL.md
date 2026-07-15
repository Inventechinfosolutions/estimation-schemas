# Estimation Pipeline — Main Control File

**This is the entry point for every estimation run.**  
When the user provides any SOW / FRS / BRD / RFP / functional document for module or feature extraction, follow this file end to end. Do not invent a parallel process.

| Schema / Artefact | Path | Used in |
|-------------------|------|---------|
| Production-grade SOW | `{OutputRoot}/SoW_{ProjectCode}_Detailed.md` **and** `.docx` | Step 1 |
| Module extraction | [`module_schema.md`](module_schema.md) | Step 2–3 |
| Feature specification & estimation | [`feature_schema.md`](feature_schema.md) | Step 5 |

---

## Inputs (ask if missing)

Before starting, confirm:

1. **Source document** — path to draft SOW / FRS / BRD / RFP / spec (`.md`, `.docx`, or other readable form)
2. **Project code** — short code for file naming (e.g. `CPMS`, `LMS`, `HMS`)
3. **Project name** — display name (e.g. `BDA Commercial Property Management System`)
4. **Output root** — folder where SOW, modules file, and `modules/` will be created  
   - Default: same directory as the source document  
   - Example: `BDA_CMPS/`
5. **SOW purpose** — RFP / internal estimation / both (default: RFP-ready business SOW)

Do not proceed without a source document and project code.

---

## Pipeline Overview

```text
Source Document (draft / outline)
      │
      ▼
┌──────────────────────────────┐
│ STEP 1 — Production-grade SOW │  ← ask clarifying Qs if needed
│ Write MD + DOCX (always both)
└──────────────┬───────────────┘
               │  user confirms SOW
               ▼
┌──────────────────────────────┐
│ STEP 2 — Extract modules      │  ← follow module_schema.md
│ Write {ProjectCode}_Modules.md
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ STEP 3 — Create folders       │  ← one folder per module
│ modules/{NN}-{slug}/
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ STEP 4 — User confirms        │  ← STOP and wait
│ modules list / folders
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ STEP 5 — Features / module    │  ← follow feature_schema.md
│ one feature file each
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ STEP 6 — Internal summary     │
│ roll-up + feature-wise MD
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ STEP 7 — Client export        │  ← Word client copy
│ no pipeline / AI tells
└──────────────────────────────┘
```

**Hard gates**

- Do **not** start module extraction until Step 1 SOW is confirmed (unless the user provides an already production-grade SOW and explicitly skips Step 1).
- Do **not** generate features until Step 4 confirmation (unless the user explicitly says to continue without review).
- Do **not** estimate hours during SOW drafting or module extraction.
- Do **not** design APIs, DB schemas, class diagrams, or UI wireframes in any step.
- Do **not** share internal markdown summaries with the client; use the Step 7 Word export only.

---

## STEP 1 — Production-Grade SOW

**When to run:** Always when the source is a draft outline, section list, short note, or incomplete SOW.  
**When to skip:** Only if the user points to an already detailed, RFP-ready SOW (e.g. prior `SoW_*_Detailed.md`) and says to skip SOW preparation.

### 1.1 Ask clarifying questions first (mandatory if material gaps exist)

Before writing the detailed SOW, ask concise questions where answers change scope. Typical areas:

1. Project code / display name / output filename  
2. Audience: RFP for BDA vs internal estimation only  
3. In-scope vs out-of-scope boundaries (related systems, portals, migration)  
4. Channels: officer portal, citizen portal, both  
5. Integrations (payment, SMS, email, GIS, other BDA apps)  
6. Whether Document Management / Workflow are separate modules or **embedded** in processes  
7. Phasing (single Phase 1 vs multi-phase)  
8. Legacy data migration yes/no  
9. Any stack/hosting constraints — usually **no deep technical design** in BDA RFP SOWs  

If the user answers “assume defaults”, proceed with defaults stated as Assumptions in the SOW.

### 1.2 Write the production-grade SOW (MD + DOCX — always)

**Always produce both formats** for every production-grade SOW (hard rule):

```text
{OutputRoot}/SoW_{ProjectCode}_Detailed.md
{OutputRoot}/SoW_{ProjectCode}_Detailed.docx
```

Examples:

- `BDA_CMPS/SoW_CPMS_Detailed.md` + `.docx`
- `BDA_LayoutMaster/SoW_LMS_Detailed.md` + `.docx`
- `BDA_Housing_Management/SoW_BHMS_Detailed.md` + `.docx`

Keep the original draft source file unchanged (e.g. original draft `.docx` / short `SOW.md`).

The `.md` file is the working source of truth for the pipeline. The `.docx` is the BDA/RFP review copy and must stay content-equivalent to the markdown (plain professional formatting; no pipeline/AI language).

### 1.3 Required SOW structure (RFP / BDA style)

Model quality and structure on existing production SOWs in this repo (e.g. `SoW_CPMS_Detailed.md`, `SoW_LMS_Detailed.md`). Include at minimum:

1. Introduction  
2. Project Overview  
3. Project Objectives  
4. In Scope / Out of Scope  
5. Solution Expectations (business-level; avoid deep tech stack / API design)  
6. Consolidated Functional Modules (purpose, functional requirements, acceptance criteria)  
7. End-to-End Workflows  
8. Role-Based Access Control  
9. Channels (officer / citizen) where applicable  
10. Integrations  
11. Audit, Compliance & Security  
12. Non-Functional Requirements  
13. Data Migration (if in scope)  
14. Phased Delivery  
15. Deliverables  
16. Acceptance Criteria (program level)  
17. Expected Benefits  
18. Assumptions & Dependencies  
19. Vendor Response Expectations  
20. Appendices as needed (module consolidation map, entities, document types)

### 1.4 SOW writing rules

- Prefer **business / functional** language suitable for BDA RFP.  
- Consolidate related capabilities; avoid one “module” per screen.  
- Embed Document Management and Workflow **inside** business processes unless the user explicitly wants separate modules.  
- Do **not** invent commercial property / layout / housing scope that the source does not support.  
- Do **not** estimate hours in this step.  
- Do **not** design APIs, DB schemas, class diagrams, or wireframes.

### 1.5 Gate

Stop and ask the user to review/confirm the detailed SOW.  
**Only after confirmation** continue to Step 2 (module extraction), unless the user says to continue without review.

---

## STEP 2 — Extract Modules

**Instruction source:** Read and obey [`module_schema.md`](module_schema.md) fully.

**Source of truth for scope:** the Step 1 production-grade SOW (or the user-confirmed production SOW if Step 1 was skipped).

**Actions**

1. Read the production-grade SOW end to end.
2. Identify modules using the schema rules (merge related capabilities; prefer fewer stronger modules).
3. Perform the technical gap review from the schema.
4. Write:

```text
{OutputRoot}/{ProjectCode}_Modules.md
```

Example: `BDA_CMPS/CPMS_Modules.md`

**Output must include** (per `module_schema.md`)

- Summary table: `# | Module | Type | Summary | Source`
- Module Details for every module
- Excluded / Embedded Capabilities
- Assumptions
- Risks

**Do not in this step**

- Create feature files
- Estimate effort
- Create folders yet (that is Step 3)

**When done:** Briefly list the modules for the user and proceed to Step 3 (folders are part of module schema Section 3; create them next, then pause for confirmation).

---

## STEP 3 — Create Module Folders

**Instruction source:** `module_schema.md` → Section 3 (Folder Structure).

For each module in `{ProjectCode}_Modules.md`, create:

```text
{OutputRoot}/modules/{NN}-{module-slug}/
```

Rules:

- `{NN}` = two-digit sequence (`01`, `02`, …)
- `{module-slug}` = lowercase kebab-case
- One folder per module
- Do **not** create feature files in this step

Optional (recommended): place a short `README.md` inside each folder:

```markdown
# {NN}. {Module Name}

Type: {Business | Technical | Shared}
Summary: {one line}

Features: (pending Step 5)
```

Copy module metadata from `{ProjectCode}_Modules.md` — do not invent new scope here.

---

## STEP 4 — User Confirmation (mandatory gate)

Stop and ask the user to confirm:

- Module list (add / remove / rename / merge)
- Folder names
- Any modules to skip for feature generation

**Only after explicit confirmation** (or an explicit “skip review / generate all features”) continue to Step 5.

If the user requests changes, update `{ProjectCode}_Modules.md` and folders first, then re-confirm.

---

## STEP 5 — Generate Features Per Module

**Instruction source:** Read and obey [`feature_schema.md`](feature_schema.md) fully.

**Default order:** Process modules in sequence order (`01`, `02`, …), unless the user names specific modules.

For each module:

1. Read that module’s section in `{ProjectCode}_Modules.md` and the relevant parts of the production-grade SOW.
2. Identify every feature in the module.
3. For **each** feature, write one markdown file:

```text
{OutputRoot}/modules/{NN}-{module-slug}/features/{FeatureID}-{feature-slug}.md
```

Examples:

```text
modules/04-revenue-billing-collections/features/F04-001-monthly-rent-demand.md
modules/04-revenue-billing-collections/features/F04-002-online-payment-collection.md
```

**Feature ID convention**

```text
F{NN}-{SEQ}
```

- `{NN}` = module number  
- `{SEQ}` = three-digit sequence within the module (`001`, `002`, …)

**Each feature file must contain** (per `feature_schema.md`)

1. **Feature Specification** — all required sections (Feature ID through Non Functional Requirements)
2. **Estimation Breakdown** — UI / API / Database / Integration / Testing / Documentation using the Estimation Master only (never invent hour values outside the master)

Also create or update:

```text
{OutputRoot}/modules/{NN}-{module-slug}/features/_index.md
```

With a table:

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|

**Do not in this step**

- Design APIs, DB tables, class diagrams, or wireframes
- Invent business scope not supported by the source document / module definition

**Batching:** If there are many modules, generate one module at a time and show a short progress summary after each, unless the user asks to run all in one pass.

---

## STEP 6 — Internal Project Summary

After features are generated for the requested modules, write or update **both** internal summaries:

```text
{OutputRoot}/{ProjectCode}_Estimation_Summary.md
{OutputRoot}/{ProjectCode}_Estimation_Summary_FeatureWise.md
```

### `{ProjectCode}_Estimation_Summary.md` (roll-up)

Include:

1. Module count and feature count  
2. Per-module total hours (sum of feature totals from each `_index.md`)  
3. Grand total hours  
4. Clear split of **recommended go-live** vs **optional / conditional** hours (when applicable)  
5. Open assumptions / risks carried forward  
6. Suggested next actions (review estimates, adjust scope, Step 7 client export)

### `{ProjectCode}_Estimation_Summary_FeatureWise.md` (detail)

Include:

1. Grand totals (all / go-live / optional)  
2. Module-wise summary table  
3. Feature-wise tables copied from each module `_index.md` (Feature ID, Name, Hours, Notes)  
4. Optional commercial line items (if any)  
5. Effort profile (e.g. top features, hours by module type) — optional but recommended  
6. Indicative phasing aligned to the source SOW  
7. Exclusions (services / infra not in feature hours)

**Audience:** internal estimation team only. These files may reference schemas, folder paths, Estimation Master language, and reconciliation notes.

**When done:** Proceed to Step 7 (client export), unless the user asks to stop after internal summaries.

---

## STEP 7 — Client Estimation Export

Produce a **client-facing Word document** after Step 6. The client must not be able to tell the estimate was produced by an internal pipeline or generative tooling.

```text
{OutputRoot}/{ProjectCode}_Estimation_Summary_FeatureWise_Client.docx
```

Examples:

- `BDA_CMPS/CPMS_Estimation_Summary_FeatureWise_Client.docx`
- `BDA_LayoutMaster/LMS_Estimation_Summary_FeatureWise_Client.docx`

### Content to include

1. Cover block: organisation, project name, “Module & Feature-wise Effort Estimate”, “Client Copy · Effort in person-hours”  
2. Short plain-language intro (what the hours cover / do not cover)  
3. Summary totals (recommended go-live / optional / all-in)  
4. Module-wise summary (module name, type, feature count, hours, % of go-live)  
5. Feature-wise tables per module (Feature ID, Feature Name, Hours, short business Notes)  
6. Optional commercial line items (if any)  
7. Effort profile (top features; hours by Business / Shared / Technical) — recommended  
8. Indicative delivery phasing from the SOW (business wording)  
9. Items not included in feature hours (training, hosting, AMC, scanning, etc.)  
10. Key planning assumptions (numbered, client-safe)  
11. Closing disclaimer: estimates are indicative for planning / commercial discussion  

### Forbidden in the client document (hard rules)

Do **not** include any of the following:

| Forbidden | Why |
|-----------|-----|
| Mentions of `CONTROL.md`, `module_schema.md`, `feature_schema.md`, Estimation Master, pipeline, Step N | Reveals internal method |
| Phrases like “generated”, “catalogued”, “reconciled hours”, “VH / Easy / Medium” complexity codes | Estimation-ops jargon |
| Repo paths, `modules/{NN}-…/features/`, markdown filenames, `_index.md` | Internal artefacts |
| “Document generated from N feature index rows” or similar footers | Obvious machine output |
| Duplicate or stacking notes such as `OPTIONAL · OPTIONAL`, `Mandatory VH`, `Uses Fxx-yyy` ownership accounting | Internal reconciliation |
| Status columns like “Complete / pending Step 4” | Pipeline residue |
| AI / Cursor / automation acknowledgements | Must read as consultant-authored |

### Style rules

- Write as a senior estimation / consulting deliverable for government RFP discussion.  
- Keep Notes short and business-facing (what the feature does), not how hours were calculated.  
- Prefer “Integrations” over raw technical module nicknames when speaking to the client, if clearer.  
- Use professional Word formatting (clear headings, grid tables, readable fonts such as Calibri).  
- Internal markdown files remain the source of truth for hour arithmetic; the Word file is a **presentation export**.

### Dual format rule (MD + DOCX)

For Step 7, also keep / refresh the internal FeatureWise **markdown** from Step 6. The client deliverable is the Word file; internal MD remains for the team.  
Whenever the user says “MD and docx” or “always both”, any SOW or client summary refresh must update **both** corresponding artefacts if both exist for that artefact type.

### When the user asks only for “client copy”

If Steps 1–6 already exist, run **Step 7 only**: rebuild the `.docx` from the current feature indexes / feature-wise summary, applying the forbidden-content rules above.

---

## Target Folder Layout

```text
{OutputRoot}/
├── {SourceDocument}                                      # user-provided draft
├── SoW_{ProjectCode}_Detailed.md                         # Step 1 (production SOW — MD)
├── SoW_{ProjectCode}_Detailed.docx                       # Step 1 (production SOW — DOCX)
├── {ProjectCode}_Modules.md                              # Step 2
├── {ProjectCode}_Estimation_Summary.md                   # Step 6 (internal)
├── {ProjectCode}_Estimation_Summary_FeatureWise.md       # Step 6 (internal)
├── {ProjectCode}_Estimation_Summary_FeatureWise_Client.docx  # Step 7 (client)
└── modules/
    ├── 01-{slug}/
    │   ├── README.md                                     # optional
    │   └── features/
    │       ├── _index.md
    │       ├── F01-001-{slug}.md
    │       └── ...
    ├── 02-{slug}/
    │   └── features/
    │       └── ...
    └── ...
```

---

## How to Invoke (for users)

In Cursor chat, attach or reference:

1. This control file: `@CONTROL.md`
2. The source document: e.g. `@BDA_Housing_Management/SoW_BDA Housing Management System.docx`
3. Say what to run, for example:
   - `Prepare a production-grade SOW first, then run estimation. Project code: HMS`
   - `Run the estimation pipeline for this document. Project code: CPMS`
   - `Continue pipeline — confirm modules and generate features for all`
   - `Generate features only for module 04`
   - `Create / refresh the client Word estimation summary`

The agent must follow **this file** and load the linked schemas for the active step.

---

## Resume / Partial Runs

| User intent | Start at |
|-------------|----------|
| Draft/outline SOW or new project | Step 1 |
| Production SOW already confirmed | Step 2 |
| Modules file exists; folders missing | Step 3 |
| Modules + folders done; need features | Step 4 → 5 (confirm first) |
| Features for one module only | Step 5 for that module |
| Features done; need totals | Step 6 |
| Internal summaries done; need client Word file | Step 7 |
| Re-estimate after scope change | Update SOW/modules if needed, regenerate affected features, then Steps 6–7 |

Always re-read `CONTROL.md` + the relevant schema before resuming.

---

## Consistency Rules

1. Schemas win on field-level format; this file wins on **order of steps and gates**.
2. Prefer consolidating related capabilities (aligned with `module_schema.md`).
3. Keep project work under `{OutputRoot}`; do not copy schemas into project folders.
4. Keep this repo’s schemas (`module_schema.md`, `feature_schema.md`) as the single source of estimation rules.
5. When in doubt, stop and ask — especially at Step 1 (SOW questions) and Step 4 (module confirmation).
6. **Client vs internal:** Step 6 markdown = internal; Step 7 Word = client. Never paste pipeline metadata into the client export.
7. Estimation always uses the **production-grade SOW** from Step 1 (not the raw draft) unless the user explicitly designates another source.

---

## Change Log

| Version | Notes |
|---------|--------|
| 1.0 | Initial control pipeline: modules → folders → confirm → features → summary |
| 1.1 | Added feature-wise internal summary + client Word export (no pipeline/AI tells) |
| 1.2 | Added Step 1 production-grade SOW preparation; renumbered module→client steps to 2–7 |
| 1.3 | Step 1 always outputs SOW in both Markdown and Word (`.md` + `.docx`) |
