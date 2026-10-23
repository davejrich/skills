#!/usr/bin/env python3
"""Render a Six Medals values map (JSON) to a self-contained, print-ready HTML report.

Usage:
    python render_report.py map.json out.html [--brand brand.json]

Standard library only. Schema: ../references/report-format.md
"""
import argparse
import html
import json
import sys
from pathlib import Path

MEDALS = [
    ("gold", "Gold", "People", "#C9A227"),
    ("silver", "Silver", "Organisation", "#8E98A3"),
    ("steel", "Steel", "Quality", "#4A5A6A"),
    ("glass", "Glass", "Innovation", "#3FA9D6"),
    ("wood", "Wood", "Community & environment", "#7A5230"),
    ("brass", "Brass", "Perception", "#B5883A"),
    ("clay", "Clay", "Founder's stakes (added medal)", "#B5653F"),
]
RATINGS = {
    "strong": ("Strong", "#0e8f82", "#e3f8f5"),
    "present": ("Present", "#8a5a00", "#fdf1dc"),
    "weak": ("Weak", "#b3401f", "#fbe6df"),
    "missing": ("Missing", "#5b6170", "#eceef2"),
    "thin": ("Thin evidence", "#5b6170", "#eceef2"),
    "to discuss": ("To discuss", "#5b6170", "#eceef2"),
}
DEFAULT_BRAND = {
    "name": "",
    "logo_svg": "",
    "accent_1": "#2bd9c9",
    "accent_1_ink": "#0e8f82",
    "accent_2": "#f2a63d",
    "text": "#0a0d12",
    "heading_font": "Space Grotesk",
    "body_font": "Inter",
    "google_fonts": "Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600",
    "footer": "",
    "prepared_by": "",
}


def e(value):
    return html.escape(str(value or ""), quote=True)


def load_brand(path):
    brand = dict(DEFAULT_BRAND)
    if path:
        brand.update(json.loads(Path(path).read_text(encoding="utf-8")))
        logo = brand.get("logo_svg_path")
        if logo:
            logo_path = (Path(path).parent / logo).resolve()
            svg = logo_path.read_text(encoding="utf-8")
            if "<script" in svg.lower():
                sys.exit("Refusing logo SVG containing <script>.")
            brand["logo_svg"] = svg
    return brand


def validate(data):
    missing = [k for k in ("business", "date", "mode", "medals", "summary") if not data.get(k)]
    if missing:
        sys.exit(f"Missing required field(s): {', '.join(missing)}")
    keys = {m.get("key") for m in data["medals"]}
    absent = [m[1] for m in MEDALS if m[0] not in keys]
    if absent:
        sys.exit(f"Missing medal(s): {', '.join(absent)}. Use rating 'missing' rather than dropping a medal.")
    for m in data["medals"]:
        if m.get("rating", "").lower() not in RATINGS:
            sys.exit(f"Unknown rating '{m.get('rating')}' on {m.get('key')}. Use: {', '.join(RATINGS)}")


def badge(rating):
    label, ink, bg = RATINGS[rating.lower()]
    return f'<span class="badge" style="color:{ink};background:{bg};border-color:{ink}">{e(label)}</span>'


def items(values):
    return "".join(f"<li>{e(v)}</li>" for v in values or [])


def render(data, brand):
    validate(data)
    by_key = {m["key"]: m for m in data["medals"]}
    s = data["summary"]
    founder_view = data.get("audience") == "founder"

    strip = "".join(
        f'<div class="chip" style="--medal:{colour}"><span class="dot"></span>'
        f'<b>{e(name)}</b><small>{e(kind.split(" (")[0])}</small>{badge(by_key[key]["rating"])}</div>'
        for key, name, kind, colour in MEDALS
    )

    cards = []
    for key, name, kind, colour in MEDALS:
        m = by_key[key]
        rows = [f"<ul>{items(m.get('evidence'))}</ul>" if m.get("evidence") else ""]
        for field, label in (("say_do", "Say / do"), ("risk", "Value at risk"),
                             ("opportunity", "Opportunity"), ("note", "Note")):
            if m.get(field):
                rows.append(f'<p class="tag"><b>{label}:</b> {e(m[field])}</p>')
        if m.get("questions"):
            rows.append(f'<p class="tag"><b>To talk about:</b></p><ul class="q">{items(m["questions"])}</ul>')
        cards.append(
            f'<section class="medal" style="--medal:{colour}">'
            f'<header><span class="disc">{e(name[0])}</span><div><h3>{e(name)}</h3>'
            f'<small>{e(kind)}</small></div>{badge(m["rating"])}</header>{"".join(rows)}</section>'
        )

    top = "".join(f"<li>{e(v)}</li>" for v in s.get("top_values", []))
    summary_rows = []
    for field, label in (("gap", "Biggest say/do gap" if not founder_view else "Biggest opportunity"),
                         ("tension", "Biggest tension" if not founder_view else "The big question")):
        if s.get(field):
            summary_rows.append(f'<div class="kv"><h4>{label}</h4><p>{e(s[field])}</p></div>')
    if s.get("confidence"):
        summary_rows.append(
            f'<div class="kv"><h4>Confidence</h4><p><b>{e(s["confidence"]).capitalize()}</b>'
            f'{" — " + e(s.get("confidence_reason")) if s.get("confidence_reason") else ""}</p></div>'
        )

    caveat = f'<div class="caveat"><b>Read this first:</b> {e(data["caveat"])}</div>' if data.get("caveat") else ""
    sources = f'<h4>Sources</h4><ul>{items(data.get("sources"))}</ul>' if data.get("sources") else ""
    conf = ('<span class="conf">Confidential: advisor working notes</span>' if not founder_view
            else '<span class="conf soft">Prepared for ' + e(data.get("founder") or data["business"]) + '</span>')
    meta = " · ".join(e(x) for x in (data.get("date"), f'{data["mode"].capitalize()} mode', data.get("purpose")) if x)
    prepared = f' · Prepared by {e(brand["prepared_by"])}' if brand.get("prepared_by") else ""
    fonts = (f'<link rel="preconnect" href="https://fonts.googleapis.com">'
             f'<link href="https://fonts.googleapis.com/css2?family={brand["google_fonts"]}&display=swap" rel="stylesheet">'
             if brand.get("google_fonts") else "")

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Values Map: {e(data["business"])}</title>{fonts}
<style>
:root{{--a1:{brand["accent_1"]};--a1i:{brand["accent_1_ink"]};--a2:{brand["accent_2"]};--text:{brand["text"]};
--t2:#3b404c;--t3:#626879;--bg2:#f5f7fa;--line:rgba(10,13,18,.10);--grad:linear-gradient(100deg,var(--a1),var(--a2))}}
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:var(--text);font:15px/1.55 '{brand["body_font"]}',system-ui,-apple-system,'Segoe UI',sans-serif;-webkit-font-smoothing:antialiased}}
h1,h2,h3,h4{{font-family:'{brand["heading_font"]}',system-ui,sans-serif;margin:0;letter-spacing:-.01em;line-height:1.2}}
.page{{max-width:880px;margin:0 auto;padding:32px 24px 48px}}
.top{{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}}
.logo svg{{height:34px;width:auto;display:block}}
.conf{{font-size:.72rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#b3401f;border:1px solid #b3401f;border-radius:999px;padding:4px 10px}}
.conf.soft{{color:var(--a1i);border-color:var(--a1i)}}
.hero{{margin:28px 0 8px}}
.eyebrow{{font-size:.78rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--a1i)}}
h1{{font-size:2.2rem;font-weight:700;margin:6px 0 4px}}
.who{{font-size:1.05rem;color:var(--t2)}}
.meta{{color:var(--t3);font-size:.88rem;margin-top:6px}}
.bar{{height:5px;border-radius:5px;background:var(--grad);margin:20px 0 24px}}
.caveat{{background:#fff8ec;border-left:4px solid var(--a2);padding:12px 16px;border-radius:8px;margin-bottom:22px;color:var(--t2)}}
.summary{{border:1px solid var(--line);border-radius:16px;padding:22px;background:var(--bg2);margin-bottom:26px;break-inside:avoid}}
.summary h2{{font-size:1.25rem;margin-bottom:12px}}
.summary ol{{margin:0 0 14px;padding-left:22px;font-weight:600}}
.summary ol li{{margin:3px 0}}
.kv{{margin:10px 0}}
.kv h4{{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--t3);margin-bottom:2px}}
.kv p{{margin:0}}
.next{{margin-top:14px;background:#fff;border-radius:12px;padding:14px 16px;border:2px solid transparent;
background-image:linear-gradient(#fff,#fff),var(--grad);background-origin:border-box;background-clip:padding-box,border-box}}
.next h4{{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--a1i);margin-bottom:4px}}
.next p{{margin:0;font-weight:600}}
h2.sec{{font-size:1.25rem;margin:8px 0 12px;break-after:avoid}}
.medal:first-of-type{{break-before:auto}}
.strip{{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:8px;margin-bottom:26px}}
.chip{{border:1px solid var(--line);border-top:4px solid var(--medal);border-radius:10px;padding:10px;display:flex;flex-direction:column;gap:3px;break-inside:avoid}}
.chip small{{color:var(--t3);font-size:.75rem;line-height:1.3}}
.chip .dot{{display:none}}
.chip .badge{{align-self:flex-start;margin-top:4px}}
.badge{{display:inline-block;font-size:.72rem;font-weight:600;border:1px solid;border-radius:999px;padding:2px 9px;white-space:nowrap}}
.medal{{border:1px solid var(--line);border-left:6px solid var(--medal);border-radius:12px;padding:16px 18px;margin-bottom:12px;break-inside:avoid}}
.medal header{{display:flex;align-items:center;gap:12px;margin-bottom:8px}}
.medal header>div{{flex:1}}
.medal h3{{font-size:1.1rem}}
.medal small{{color:var(--t3)}}
.disc{{width:34px;height:34px;border-radius:50%;background:var(--medal);color:#fff;display:grid;place-items:center;font-weight:700;font-family:'{brand["heading_font"]}',sans-serif;flex:none}}
.medal ul{{margin:4px 0 8px;padding-left:20px;color:var(--t2)}}
.medal li{{margin:3px 0}}
.tag{{margin:6px 0 0;color:var(--t2)}}
.tag b{{color:var(--text)}}
.foot{{margin-top:28px;border-top:1px solid var(--line);padding-top:16px;color:var(--t3);font-size:.82rem}}
.foot h4{{font-size:.85rem;color:var(--t2);margin:10px 0 4px}}
.foot ul{{margin:0;padding-left:18px}}
.brandline{{margin-top:16px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font-weight:500;color:var(--t2)}}
@media (min-width:700px){{.strip{{grid-template-columns:repeat(7,1fr);gap:6px}}.chip{{padding:8px}}}}
@media (max-width:560px){{h1{{font-size:1.7rem}}.page{{padding:20px 16px 36px}}}}
@page{{size:A4;margin:14mm}}
@media print{{.strip{{grid-template-columns:repeat(7,1fr);gap:6px}}.chip{{padding:8px}}.page{{padding:0;max-width:none}}body{{font-size:12.5px}}a{{color:inherit}}}}
</style></head>
<body><div class="page">
<div class="top"><div class="logo">{brand.get("logo_svg") or e(brand.get("name"))}</div>{conf}</div>
<div class="hero"><div class="eyebrow">Six Medals · Values Map</div>
<h1>{e(data["business"])}</h1>
<div class="who">{e(data.get("founder"))}</div>
<div class="meta">{meta}</div></div>
<div class="bar"></div>
{caveat}
<section class="summary"><h2>{"What drives this business" if not founder_view else "What we heard matters to you"}</h2>
<ol>{top}</ol>{"".join(summary_rows)}
<div class="next"><h4>{"Next action" if not founder_view else "Suggested next step"}</h4><p>{e(s.get("next_action"))}</p></div></section>
<h2 class="sec">The seven medals at a glance</h2>
<div class="strip">{strip}</div>
<h2 class="sec">Medal by medal</h2>
{"".join(cards)}
<div class="foot">{sources}
<h4>Method</h4><p>Based on Edward de Bono's <i>The Six Value Medals</i> (2005). Clay (the founder's own stakes) is an added medal, not part of de Bono's method. Ratings weigh what the business does over what it says. Independent adaptation, not affiliated with the de Bono estate.</p>
<div class="brandline"><span>{e(brand.get("footer"))}</span><span>{e(data.get("date"))}{prepared}</span></div></div>
</div></body></html>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("map_json")
    ap.add_argument("out_html")
    ap.add_argument("--brand", help="brand JSON (colours, fonts, logo_svg_path, footer)")
    args = ap.parse_args()
    data = json.loads(Path(args.map_json).read_text(encoding="utf-8"))
    out = render(data, load_brand(args.brand))
    Path(args.out_html).write_text(out, encoding="utf-8")
    print(f"Wrote {args.out_html}")


if __name__ == "__main__":
    main()
