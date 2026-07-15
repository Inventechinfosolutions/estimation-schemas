# Estimation Schemas

Reusable prompts and control pipeline for SOW / FRS / BRD / RFP estimation.

## Start here

**Main control file:** [`CONTROL.md`](CONTROL.md)

Attach `@CONTROL.md` plus your source document and run the pipeline. Every estimation run must follow that file.

## Files

| File | Role |
|------|------|
| [`CONTROL.md`](CONTROL.md) | **Entry point** — ordered steps, gates, folder layout |
| [`module_schema.md`](module_schema.md) | Step 1–2: identify modules + create module folders |
| [`feature_schema.md`](feature_schema.md) | Step 4: feature specs + Estimation Master hours |

## Pipeline (summary)

1. Extract modules → `{ProjectCode}_Modules.md` (`module_schema.md`)
2. Create `modules/{NN}-{slug}/` folders
3. **User confirms** module list
4. Generate features per module (`feature_schema.md`)
5. Write `{ProjectCode}_Estimation_Summary.md`

## Example invoke

```text
@CONTROL.md @BDA_CMPS/SoW_CPMS_Detailed.md
Run the estimation pipeline. Project code: CPMS. Output root: BDA_CMPS/
```

## Location

Keep schemas in this repo. Put project outputs next to the source document (e.g. `BDA_CMPS/`), not as copies of the schemas.

```text
estimation-schemas/          ← CONTROL + schemas (this folder)
  CONTROL.md
  module_schema.md
  feature_schema.md
  BDA_CMPS/                  ← project outputs for CPMS
    SoW_....md
    CPMS_Modules.md
    modules/
```
