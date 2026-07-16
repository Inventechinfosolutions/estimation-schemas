# Module & Feature Numbering — Schema

**Used in:** CONTROL Step 1 (SOW), Steps 2–3 (modules), Step 5 (features), Step 6 (roll-up).  
**Purpose:** Auto-assign, format, and capture module numbers and feature IDs consistently across SOW, files, folders, and summaries.

All agents and engines must follow this schema. Do not invent alternate ID formats.

---

## 1. Module numbering

### 1.1 Format

| Token | Pattern | Example |
|-------|---------|---------|
| Module number `{NN}` | Two digits, zero-padded, `01`–`99` | `01`, `04`, `15` |
| Module slug | Lowercase kebab-case from module name | `user-role-management` |
| Module folder | `{NN}-{module-slug}` | `01-user-role-management` |
| Module heading | `{NN}. {Module Name}` | `01. User & Role Management` |

### 1.2 Auto-assignment rules

1. Assign `{NN}` in **implementation order** (foundational modules first: access, masters, then domain, then technical).  
2. Start at `01`; increment by 1; no gaps unless the user explicitly renumbers.  
3. One `{NN}` per module — never reuse a number for a different module.  
4. If a module is **removed** before features exist: leave the number unused or renumber the whole list (user choice).  
5. If a module is **inserted**: either use the next free `{NN}` or renumber all modules and folders (prefer next free number to avoid churn).  
6. `{module-slug}` must be unique, ASCII, lowercase, hyphens only — derive from module name (drop `&`, punctuation; collapse spaces to `-`).

### 1.3 Where module number must appear

| Location | Required format |
|----------|-----------------|
| `{ProjectCode}_Modules.md` summary table | `#` column = `{NN}` |
| `{ProjectCode}_Modules.md` detail heading | `### {NN}. {Module Name}` |
| Folder path | `modules/{NN}-{module-slug}/` |
| Module `README.md` title | `# {NN}. {Module Name}` |
| Feature spec `Module` field | `{NN} — {Module Name}` |
| SOW consolidated modules (Step 1) | `### {NN}. {Module Name}` + Key capabilities table `F{NN}-{SEQ}` (per `sow_schema.md` §4A) |
| SOW appendix | Module & feature index table |

---

## 2. Feature numbering

### 2.1 Format

| Token | Pattern | Example |
|-------|---------|---------|
| Feature ID `{FeatureID}` | `F{NN}-{SEQ}` | `F01-001`, `F04-012` |
| `{NN}` | Same two-digit module number as parent folder | `01`, `04` |
| `{SEQ}` | Three digits, zero-padded, per module `001`–`999` | `001`, `007` |
| Feature slug | Lowercase kebab-case from feature name | `person-master-person-post-mapping` |
| Feature filename | `F{NN}-{SEQ}-{feature-slug}.md` | `F01-001-person-master-person-post-mapping.md` |
| Feature heading (H1) | `# F{NN}-{SEQ} — {Feature Name}` | `# F01-001 — Person Master & Person–Post Mapping` |

### 2.2 Auto-assignment rules

1. `{NN}` **must match** the parent module folder’s `{NN}` — never mismatch (e.g. no `F02-001` inside `01-user-role-management`).  
2. Assign `{SEQ}` in **logical implementation order** within the module, starting at `001`.  
3. Increment `{SEQ}` by 1 per feature; no gaps unless user renumbers.  
4. One `{FeatureID}` per feature — never reuse within the same project.  
5. If a feature is **added** mid-module: use next `{SEQ}` (e.g. after `F04-005` → `F04-006`).  
6. If a feature is **removed**: leave gap or renumber all features in that module and rename files (prefer gap to avoid file churn).  
7. `{feature-slug}` must be unique within the module.

### 2.3 Where feature ID must appear

| Location | Required format |
|----------|-----------------|
| Feature file H1 | `# F{NN}-{SEQ} — {Feature Name}` |
| Feature spec table — Feature ID | `F{NN}-{SEQ}` |
| Feature spec table — Feature Name | Human name (no ID prefix) |
| Feature spec table — Module | `{NN} — {Module Name}` |
| `features/_index.md` | Columns: Feature ID, Feature Name, Total Hours, Notes |
| `_index.md` module header | `## {NN} — {Module Name}` |
| SOW Key capabilities table (Step 1) | `F{NN}-{SEQ}` per `sow_schema.md` §4A |
| SOW appendix | Module & feature index table |
| Estimation summaries | Same `F{NN}-{SEQ}` in feature-wise tables |

---

## 3. Index file (`_index.md`)

Each module folder must contain:

```text
{OutputRoot}/modules/{NN}-{module-slug}/features/_index.md
```

**Template:**

```markdown
# Feature Index

## {NN} — {Module Name}

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|------------:|-------|
| F{NN}-001 | {Name} | {hours} | {short note} |
| F{NN}-002 | {Name} | {hours} | {short note} |

**Module Total:** **{sum} hours**
```

**Rules**

- Rows sorted by `{SEQ}` ascending.  
- `Feature ID` column = exact `F{NN}-{SEQ}` (zero-padded).  
- `Total Hours` = sum of Estimation Master breakdown for that feature.  
- Update `_index.md` every time a feature file is created or hours change.

---

## 4. Machine-readable registry (capture)

After modules are confirmed (Step 4) and as features are generated (Step 5), maintain:

```text
{OutputRoot}/{ProjectCode}_Registry.json
```

**Purpose:** Single source for orchestrators, validators, and roll-up scripts.

**Schema:**

```json
{
  "project_code": "{ProjectCode}",
  "project_name": "{Project Name}",
  "output_root": "{OutputRoot}",
  "updated_at": "ISO-8601",
  "modules": [
    {
      "nn": "01",
      "name": "User & Role Management",
      "slug": "user-role-management",
      "type": "Shared",
      "folder": "modules/01-user-role-management",
      "feature_count": 7,
      "total_hours": 395,
      "features": [
        {
          "id": "F01-001",
          "seq": "001",
          "name": "Person Master & Person–Post Mapping",
          "slug": "person-master-person-post-mapping",
          "file": "modules/01-user-role-management/features/F01-001-person-master-person-post-mapping.md",
          "hours": 65
        }
      ]
    }
  ]
}
```

**Update rules**

| When | Action |
|------|--------|
| Step 3 — folders created | Write `modules[]` with `nn`, `name`, `slug`, `folder`; `features` = `[]` |
| Step 5 — each feature written | Append/update feature entry; set `hours` from feature file total |
| Step 5 — module complete | Set `feature_count`, `total_hours` |
| Module add/remove/rename | Regenerate affected `modules[]`; renumber if user requested |

Validators must reject:

- `F{NN}-{SEQ}` where `{NN}` ≠ parent module `nn`  
- Duplicate `id` or `seq` within a module  
- Filename not matching `F{NN}-{SEQ}-{slug}.md`  
- `_index.md` rows not matching registry

---

## 5. Slug derivation (auto)

Apply to both module and feature slugs:

1. Lowercase  
2. Replace `&` with `and`  
3. Remove characters other than letters, digits, spaces, hyphens  
4. Replace spaces and `_` with `-`  
5. Collapse repeated hyphens  
6. Trim leading/trailing hyphens  
7. Truncate to 80 characters if needed (keep whole words)

**Examples**

| Name | Slug |
|------|------|
| User & Role Management | `user-and-role-management` or `user-role-management` (prefer shorter if clear) |
| Online Payment Management | `online-payment-management` |
| F04-001 — Monthly Rent Demand | `monthly-rent-demand` |

---

## 6. Renumbering checklist

When the user changes module or feature order:

- [ ] Update `{ProjectCode}_Modules.md`  
- [ ] Rename module folders `{NN}-{slug}` if `{NN}` changed  
- [ ] Rename feature files `F{NN}-{SEQ}-{slug}.md`  
- [ ] Update H1 and Feature ID inside each feature file  
- [ ] Regenerate all `_index.md` files  
- [ ] Regenerate `{ProjectCode}_Registry.json`  
- [ ] Regenerate Steps 6–7 summaries  

---

## 7. Quick reference

```text
Module folder:     modules/{NN}-{module-slug}/
Feature file:      modules/{NN}-{module-slug}/features/F{NN}-{SEQ}-{feature-slug}.md
Feature ID:        F{NN}-{SEQ}
Module in spec:    {NN} — {Module Name}
Registry:          {ProjectCode}_Registry.json
```
