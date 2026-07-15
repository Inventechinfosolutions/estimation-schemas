# Estimation Schemas

Reusable prompts and control pipeline for SOW / FRS / BRD / RFP estimation.

## Start here

**Main control file:** [`CONTROL.md`](CONTROL.md)

Attach `@CONTROL.md` plus your source document and run the pipeline. Every estimation run must follow that file.

## Files

| File | Role |
|------|------|
| [`CONTROL.md`](CONTROL.md) | **Entry point** — Steps 1–7, gates, folder layout, client export rules |
| [`module_schema.md`](module_schema.md) | Steps 2–3: identify modules + create module folders |
| [`feature_schema.md`](feature_schema.md) | Step 5: feature specs + Estimation Master hours |
| [`.cursor/rules/estimation-pipeline.mdc`](.cursor/rules/estimation-pipeline.mdc) | Always-on Cursor rule pointing agents at CONTROL |

## Pipeline (summary)

1. Production-grade SOW → `SoW_{ProjectCode}_Detailed.md` **and** `.docx`
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

## Location

Keep schemas in this repo root. Put project outputs under `Projects/`:

```text
estimation-schemas/                 ← CONTROL + schemas
  CONTROL.md
  module_schema.md
  feature_schema.md
  Projects/
    {ProjectFolder}/                ← project outputs
```

## Defaults (generic)

- Document Management and Workflow **embedded** unless the user or source says otherwise
- Access model taken from the **SOW / user answers** (not hardcoded)
- Client gets Word only — no pipeline/AI language in client exports
