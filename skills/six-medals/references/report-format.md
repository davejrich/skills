# Branded report format

`scripts/render_report.py` turns a values map saved as JSON into a self-contained, print-ready HTML report (A4). Print it to PDF with a headless browser. Python standard library only.

```
python scripts/render_report.py map.json out.html [--brand brand.json]
```

Without `--brand` it uses a neutral default style. Use the optional `assets/aisharp-brand.json` preset or a trusted local brand file. Keep custom client brand files outside the public skill. The HTML embeds the logo and CSS; Google Fonts require network access, with system-font fallbacks offline.

## Map JSON

| Field | Required | Notes |
| --- | --- | --- |
| `audience` | no | `advisor` (default: "Confidential" badge, blunt labels) or `founder` (softer labels: "Biggest opportunity", "The big question", "Suggested next step"). |
| `business` | yes | Display name. |
| `founder` | no | Founder name, optionally with the legal entity. |
| `date`, `mode`, `purpose` | date and mode yes | `mode` is `desk` or `interview`. |
| `caveat` | no | Shown in a "Read this first" box above the summary. |
| `summary` | yes | `top_values` (list of 3), `gap`, `tension`, `confidence` (high/medium/low), `confidence_reason`, `next_action`. |
| `medals` | yes | All seven keys: `gold silver steel glass wood brass clay`. The script refuses a map with a medal missing. |
| `sources` | no | List of strings. |

Each medal: `key`, `rating` (`strong` / `present` / `weak` / `missing`, plus `thin` or `to discuss` for Clay), `evidence` (list), and optional `say_do`, `risk`, `opportunity`, `note`, `questions` (list).

For a founder version, write a separate JSON with `"audience": "founder"`: same ratings, reworded per the SKILL.md "Founder-friendly version" rules. Use `opportunity` instead of `risk`, and put Clay `questions` in place of guesses.

## Brand JSON

```json
{
  "name": "brand name (used if no logo)",
  "logo_svg_path": "path/to/logo.svg (relative to the brand file)",
  "accent_1": "#hex", "accent_1_ink": "#hex (darker, for text)", "accent_2": "#hex",
  "text": "#hex",
  "heading_font": "Google Font name", "body_font": "Google Font name",
  "google_fonts": "family query string for fonts.googleapis.com/css2",
  "footer": "contact line",
  "prepared_by": "name"
}
```

## Printing to PDF (Windows)

```
chrome.exe --headless=new --disable-gpu --no-pdf-header-footer --user-data-dir=<temp dir> --virtual-time-budget=6000 --print-to-pdf="out.pdf" "file:///C:/path/out.html"
```

Notes: Edge headless silently wrote nothing in testing (2026-10-20); Chrome with a separate `--user-data-dir` works and doesn't touch the user's open Chrome. `--virtual-time-budget` gives Google Fonts time to load. Chrome logs harmless extension/GCM errors to stderr.
