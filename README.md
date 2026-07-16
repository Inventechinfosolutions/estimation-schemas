# Estimation Schemas

Reusable prompts and control pipeline for SOW / FRS / BRD / RFP estimation.

## Start here

**Only file required:** [`CONTROL.md`](CONTROL.md)

Attach `@CONTROL.md` plus your source document. The control file tells the agent which step-schemas to read (`sow_schema.md`, `module_schema.md`, etc.). **No Cursor rule or extra config needed.**

## Files

| File | Role |
|------|------|
| [`CONTROL.md`](CONTROL.md) | **Entry point** — Steps 1–7, gates, schema-loading table, folder layout |
| [`sow_schema.md`](sow_schema.md) | Step 1: production-grade SOW (MD + DOCX) |
| [`numbering_schema.md`](numbering_schema.md) | Steps 1–6: module `{NN}`, feature `F{NN}-{SEQ}`, registry JSON |
| [`module_schema.md`](module_schema.md) | Steps 2–3: identify modules + create module folders |
| [`feature_schema.md`](feature_schema.md) | Step 5: feature specs + Estimation Master hours |
| [`.cursor/rules/estimation-pipeline.mdc`](.cursor/rules/estimation-pipeline.mdc) | *(Optional)* Cursor IDE shortcut only — not required |

## Pipeline (summary)

1. Production-grade SOW → `SoW_{ProjectCode}_Detailed.md` **and** `.docx` (`sow_schema.md`)
2. Extract modules → `{ProjectCode}_Modules.md` (`module_schema.md`)
3. Create `modules/{NN}-{slug}/` folders
4. **User confirms** module list
5. Generate features per module (`feature_schema.md`)
6. Internal summaries: `{ProjectCode}_Estimation_Summary.md` + `_FeatureWise.md`
7. Client Word: `{ProjectCode}_Estimation_Summary_FeatureWise_Client.docx`

## Example invoke

```text
@CONTROL.md @Projects/{ProjectFolder}/{SourceDocument}
Run the estimation pipeline. Project code: HMS. Output root: Projects/{ProjectFolder}/
```

Works in Cursor chat, Claude, ChatGPT (with file upload), or a custom API orchestrator that loads `CONTROL.md` + step schemas.

## Location

Keep schemas in this repo root. Put project outputs under `Projects/`:

```text
estimation-schemas/                 ← CONTROL + schemas
  CONTROL.md
  sow_schema.md
  numbering_schema.md
  module_schema.md
  feature_schema.md
  Projects/
    {ProjectFolder}/                ← project outputs
```

## Defaults (generic)

- Document Management and Workflow **embedded** unless the user or source says otherwise
- Access model taken from the **SOW / user answers** (not hardcoded)
- Client gets Word only — no pipeline/AI language in client exports
