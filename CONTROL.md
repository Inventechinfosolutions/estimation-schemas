# Estimation Pipeline — Main Control File

**This is the only entry point required.**  
Attach or pass **`CONTROL.md`** plus the source document to any agent (Cursor chat, API, or custom orchestrator). **No Cursor rules, MCP, or other config are required.**

When the user provides any SOW / FRS / BRD / RFP / functional document for module or feature extraction, follow this file end to end. Do not invent a parallel process.

| Schema / Artefact | Path | Used in |
|-------------------|------|---------|
| Production-grade SOW | [`sow_schema.md`](sow_schema.md) → `{OutputRoot}/SoW_{ProjectCode}_Detailed.md` **and** `.docx` | Step 1 |
| Module & feature numbering | [`numbering_schema.md`](numbering_schema.md) | Steps 1–6 |
| Module extraction | [`module_schema.md`](module_schema.md) | Step 2–3 |
| Feature specification & estimation | [`feature_schema.md`](feature_schema.md) | Step 5 |

### Schema loading (mandatory per step)

Before executing a step, **read the schema files listed below** from this repo (same directory as `CONTROL.md`). Do not rely on memory from earlier turns; re-read when resuming.

| Step | Read these files |
|------|------------------|
| 1 — SOW | `sow_schema.md`, `numbering_schema.md` |
| 2–3 — Modules + folders | `module_schema.md`, `numbering_schema.md` |
| 4 — Confirm | This file (gates only) |
| 5 — Features | `feature_schema.md`, `numbering_schema.md` |
| 6–7 — Summaries + client export | This file (Step 6–7 sections) |

Optional: `.cursor/rules/estimation-pipeline.mdc` is a **Cursor-only shortcut** that points at this file. It is not part of the pipeline definition.

---

## Inputs (ask if missing)

Before starting, confirm:

1. **Source document** — path to draft SOW / FRS / BRD / RFP / spec (`.md`, `.docx`, or other readable form)
2. **Project code** — short code for file naming (e.g. `ERP`, `CRM`, `HMS`)
3. **Project name** — display name (e.g. `Enterprise Housing Management System`)
4. **Output root** — folder where SOW, modules file, and `modules/` will be created  
   - **Default:** `Projects/{ProjectFolder}/`  
   - If the source already lives under a project folder, use that folder as OutputRoot  
   - Do not create project outputs at the repo root next to CONTROL/schemas
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

**Instruction source:** Read and obey [`sow_schema.md`](sow_schema.md) and [`numbering_schema.md`](numbering_schema.md) fully.

**When to run:** Always when the source is a draft outline, section list, short note, or incomplete SOW.  
**When to skip:** Only if the user points to an already detailed, RFP-ready SOW (e.g. prior `SoW_*_Detailed.md`) and says to skip SOW preparation.

**Actions (summary — details in `sow_schema.md`)**

1. Ask clarifying questions if material gaps affect scope.  
2. Write production-grade SOW as **both**:

```text
{OutputRoot}/SoW_{ProjectCode}_Detailed.md
{OutputRoot}/SoW_{ProjectCode}_Detailed.docx
```

3. Keep the original draft unchanged.  
4. No hours, APIs, DB design, wireframes, or pipeline/AI language.

**Gate:** Stop for user review/confirm.  
**Only after confirmation** continue to Step 2, unless the user says to continue without review.

---

## STEP 2 — Extract Modules

**Instruction source:** Read and obey [`module_schema.md`](module_schema.md) and [`numbering_schema.md`](numbering_schema.md) fully.

**Source of truth for scope:** the Step 1 production-grade SOW (module `{NN}` and feature `F{NN}-{SEQ}` from SOW must be preserved).

**Actions**

1. Read the production-grade SOW end to end.
2. Identify modules using the schema rules — **reuse `{NN}` and names from the SOW**; do not renumber unless the user requests changes.
3. Perform the technical gap review from the schema.
4. Write:

```text
{OutputRoot}/{ProjectCode}_Modules.md
```

Example: `Projects/{ProjectFolder}/{ProjectCode}_Modules.md`

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

After Step 3, create or update `{OutputRoot}/{ProjectCode}_Registry.json` with module numbers and slugs (per `numbering_schema.md` §4).

---

## STEP 3 — Create Module Folders

**Instruction source:** `module_schema.md` → Section 3; numbering per [`numbering_schema.md`](numbering_schema.md).

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

**Instruction source:** Read and obey [`feature_schema.md`](feature_schema.md) and [`numbering_schema.md`](numbering_schema.md) fully.

**Default order:** Process modules in sequence order (`01`, `02`, …), unless the user names specific modules.

For each module:

1. Read that module’s section in `{ProjectCode}_Modules.md` and the relevant parts of the production-grade SOW.
2. Identify every feature in the module — **reuse `F{NN}-{SEQ}` from the SOW Key capabilities table**; expand into full specs without changing IDs unless the user requests changes.
3. For **each** feature, auto-assign `F{NN}-{SEQ}` and write one markdown file (formats in [`numbering_schema.md`](numbering_schema.md)):

```text
{OutputRoot}/modules/{NN}-{module-slug}/features/F{NN}-{SEQ}-{feature-slug}.md
```

Examples:

```text
modules/04-revenue-billing/features/F04-001-monthly-demand.md
modules/04-revenue-billing/features/F04-002-online-payment-collection.md
```

**Numbering:** `{NN}` = parent module number; `{SEQ}` = `001`, `002`, … per module. Update `{ProjectCode}_Registry.json` after each module (per `numbering_schema.md` §4).

**Each feature file must contain** (per `feature_schema.md`)

1. **Feature Specification** — all required sections in `feature_schema.md` (Feature ID through Non Functional Requirements), including the eight-point User Journey and named UI screens / logical API operations (not REST paths or wireframes)
2. **Estimation Breakdown** — one Estimation Master row per named UI screen and per logical API operation, plus Database, Integration (when there is a real channel), Testing and Documentation (never invent hour values outside the master)

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

**Feature quality (hard rules)**

- Each feature must be **specific** to the SOW capability (no generic template journeys such as “provide a controlled enterprise capability”).  
- User Journey must cover who creates, how they create, how they edit, how they send for approval, how the approver sees pending items, how the approver decides, and how applicant and approver/auditor see history (state explicitly when a step does not apply).  
- Estimation tables must name concrete UI/API artefacts (screens, registers, ledgers), not vague labels like “User experience and screens”. Bill **each** named screen and **each** logical API as its own row — do not collapse them into “main workspace” / “orchestration API”.  
- Prefer fewer estimable **features** over one feature per screen; that does **not** mean fewer billed screens inside a feature.  
- Vary hours using the Estimation Master — do not stamp every feature with the same total.  
- Model **access / authorisation features** according to the confirmed access model from Step 1 / the SOW — do not impose a project-specific hierarchy unless the source or user requires it.  
- After any feature hour or name change, regenerate Steps 6–7 (summaries + client docx).

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

Example: `Projects/{ProjectFolder}/{ProjectCode}_Estimation_Summary_FeatureWise_Client.docx`

### Content to include

1. Cover block: organisation (if known), project name, “Module & Feature-wise Effort Estimate”, “Client Copy · Effort in person-hours”  
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

- Write as a senior estimation / consulting deliverable suitable for RFP or commercial discussion.  
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
{RepoRoot}/                            # CONTROL + schemas only
├── CONTROL.md
├── sow_schema.md
├── numbering_schema.md
├── module_schema.md
├── feature_schema.md
├── README.md
└── Projects/
    └── {ProjectFolder}/               # OutputRoot for a project
        ├── {SourceDocument}           # user-provided draft
        ├── SoW_{ProjectCode}_Detailed.md
        ├── SoW_{ProjectCode}_Detailed.docx
        ├── {ProjectCode}_Modules.md
        ├── {ProjectCode}_Registry.json
        ├── {ProjectCode}_Estimation_Summary.md
        ├── {ProjectCode}_Estimation_Summary_FeatureWise.md
        ├── {ProjectCode}_Estimation_Summary_FeatureWise_Client.docx
        └── modules/
            ├── 01-{slug}/
            │   ├── README.md
            │   └── features/
            │       ├── _index.md
            │       └── F01-001-{slug}.md
            └── ...
```

---

## How to Invoke (for users)

**Minimum:** `CONTROL.md` + source document. Nothing else is required.

### Cursor / chat

1. Attach: `@CONTROL.md` and `@Projects/{ProjectFolder}/{SourceDocument}`  
2. Example prompts:
   - `Prepare a production-grade SOW first, then run estimation. Project code: HMS. Output root: Projects/{ProjectFolder}/`
   - `Run the estimation pipeline for this document. Project code: ERP`
   - `Continue pipeline — confirm modules and generate features for all`
   - `Generate features only for module 04`
   - `Create / refresh the client Word estimation summary`

### Custom engine / API

1. Load `CONTROL.md` into the system prompt (or first user message).  
2. At each step, inject the **Schema loading** files for that step (see table above).  
3. Write artefacts under `{OutputRoot}`; persist job state between steps.

The agent must follow **this file** and load the linked schemas for the active step. The Cursor rule file is optional convenience only.

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
4. Keep this repo’s schemas (`sow_schema.md`, `numbering_schema.md`, `module_schema.md`, `feature_schema.md`) as the single source of estimation rules.
5. When in doubt, stop and ask — especially at Step 1 (SOW questions) and Step 4 (module confirmation).
6. **Client vs internal:** Step 6 markdown = internal; Step 7 Word = client. Never paste pipeline metadata into the client export.
7. Estimation always uses the **production-grade SOW** from Step 1 (not the raw draft) unless the user explicitly designates another source.  
8. New project outputs go under **`Projects/{ProjectFolder}/`**, not the repo root.  
9. Access model, document/workflow embedding, and channel choices come from the **user and source document** — not from hardcoded project defaults.

---

## Change Log

| Version | Notes |
|---------|--------|
| 1.0 | Initial control pipeline: modules → folders → confirm → features → summary |
| 1.1 | Added feature-wise internal summary + client Word export (no pipeline/AI tells) |
| 1.2 | Added Step 1 production-grade SOW preparation; renumbered module→client steps to 2–7 |
| 1.3 | Step 1 always outputs SOW in both Markdown and Word (`.md` + `.docx`) |
| 1.4 | `Projects/` output root; feature quality rules; README/schema alignment |
| 1.5 | Prompts made org/project-agnostic — no hardcoded client, domain, or access-model defaults |
| 1.6 | Extracted Step 1 into dedicated `sow_schema.md` |
| 1.7 | Added `numbering_schema.md` — auto module/feature IDs + `{ProjectCode}_Registry.json` |
| 1.8 | `CONTROL.md` standalone — no Cursor rule required; mandatory schema-loading table per step |
