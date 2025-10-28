# Documentation Tools

Utilities to convert and tidy Markdown docs and to generate documentation from CAN KCD databases. These scripts are self‑contained and share the same Python environment.

## Quick start

- Python: 3.10+
- Optional but recommended: a virtual environment
- Install dependencies from `requirements.txt` (minimal, shared across all scripts)

```bash
# From this folder (Applications/documentation/tools)
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Scripts

### 1) kcd_to_md.py — Generate Markdown from a .kcd

Parses a CAN database (.kcd) and produces Markdown with:
- Message index table (with IDs, lengths, direction, cycle time)
- Per‑message sections with explicit anchors
- Per‑signal tables, units, scaling, enums
- Notes normalization (dedents while preserving code‑like blocks)
- MkDocs‑friendly pure Markdown tables by default

Usage:
```bash
python kcd_to_md.py \
  --kcd /path/to/database.kcd \
  --out /path/to/output.md \
  --reference-node Advantics_Charge_Controller \
  [--wrap-tables-in-divs]
```

Notes:
- Direction is inferred relative to `--reference-node` using KCD producers when available.
- Omit `--wrap-tables-in-divs` for MkDocs. Add it only if your renderer expects HTML wrappers.
- Anchors are emitted for messages and signals (e.g., `{ #Message_Name }`, `{ #Message_Name-Signal_Name }`).

### 2) convert_notes.py — Convert custom admonitions to MkDocs format

Converts blocks like:
```
> [!WARNING]
> Your message here
```
into MkDocs Admonitions:
```
!!! warning
    Your message here
```

Run from the docs root you want to process (defaults to current directory):
```bash
python convert_notes.py
```

### 3) id_regex_transformer.py — Normalize heading IDs

Transforms headings from Docsify style:
```
# Title :id=My-Anchor
```
into MkDocs style:
```
# Title { #My-Anchor }
```

Usage:
```bash
python id_regex_transformer.py [PATH]  # defaults to "."
```

### 4) cleanup_docsify_update.py — Remove Docsify update banner

Recursively strips the line `"[!UPDATE] {docsify-updated}"` if it appears as the first line in Markdown files.

Usage:
```bash
python cleanup_docsify_update.py  # starts from current directory
```

## Tips

- Always review changes with git after running bulk transforms.
- For large trees, consider running tools on a subfolder first.
- If you add a new tool that needs extra packages, add them to `requirements.txt` once for all scripts.

## Troubleshooting

- If you see a deprecation warning about `cantools.db`, it’s harmless. We can switch to `cantools.database` in a later update.
- If MkDocs doesn’t render tables, ensure you didn’t pass `--wrap-tables-in-divs` to `kcd_to_md.py`.
