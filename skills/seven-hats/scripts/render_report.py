"""Render plain-text Seven Hats JSON as escaped, standalone HTML (stdlib only)."""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlsplit

HATS = {
    'blue': ('Blue — Overview', '#1e40af', '#fff'),
    'white': ('White — Evidence', '#fff', '#111827'),
    'red': ('Red — Response', '#b91c1c', '#fff'),
    'yellow': ('Yellow — Benefits', '#fde047', '#111827'),
    'black': ('Black — Caution', '#111827', '#fff'),
    'green': ('Green — Possibilities', '#166534', '#fff'),
    'purple': ('Purple — Connections', '#7e22ce', '#fff'),
}


def esc(value):
    return html.escape(value, quote=True)


def render(data):
    fields = ('title', 'purpose', 'source', 'summary', 'alternative', 'conclusion',
              'confidence', 'next_action', 'limitations')
    for key in fields:
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key} must be non-empty text')
    hats = data.get('hats')
    if not isinstance(hats, dict) or set(hats) != set(HATS):
        raise ValueError('hats must contain exactly blue, white, red, yellow, black, green, purple')
    sections = []
    for key, (label, colour, ink) in HATS.items():
        points = hats[key]
        if not isinstance(points, list) or not points or any(
                not isinstance(p, str) or not p.strip() for p in points):
            raise ValueError(f'{key} requires a non-empty list of text observations')
        items = ''.join(f'<li>{esc(p)}</li>' for p in points)
        sections.append(f'<section><h2 style="background:{colour};color:{ink}">{label}</h2><ul>{items}</ul></section>')
    refs = data.get('references', [])
    if not isinstance(refs, list):
        raise ValueError('references must be a list')
    links = []
    for ref in refs:
        if not isinstance(ref, dict) or not isinstance(ref.get('label'), str):
            raise ValueError('each reference needs a text label')
        url = ref.get('url')
        label = esc(ref['label'])
        if url:
            if not isinstance(url, str) or urlsplit(url).scheme not in ('http', 'https') or not urlsplit(url).netloc:
                raise ValueError('reference URLs must be HTTP(S)')
            label = f'<a href="{esc(url)}">{label}</a>'
        links.append(f'<li>{label}</li>')
    end = ''.join(f'<h3>{label}</h3><p>{esc(data[key])}</p>' for key, label in (
        ('alternative', 'Alternative reading'), ('conclusion', 'Conclusion'),
        ('confidence', 'Confidence and unknowns'), ('next_action', 'Next action')))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(data['title'])}</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f1f5f9;color:#111827;font:17px/1.6 system-ui,sans-serif}}
main{{max-width:900px;margin:32px auto;padding:36px;background:white}}h1{{line-height:1.2;font-size:32px}}
h2{{font-size:21px;padding:10px 16px;border:1px solid #64748b;border-radius:5px;break-after:avoid}}
h3{{margin-bottom:4px}}p{{white-space:pre-line}}li{{margin:8px 0;overflow-wrap:anywhere}}a{{color:#1e40af}}
.meta,footer{{font-size:14px;color:#475569}}section{{margin-top:28px}}@media(max-width:600px){{main{{margin:0;padding:20px}}}}
@media print{{@page{{margin:18mm}}body{{background:white;font-size:11pt}}main{{max-width:none;margin:0;padding:0}}h2{{print-color-adjust:exact;-webkit-print-color-adjust:exact}}li{{break-inside:avoid}}}}
</style></head><body><main><h1>{esc(data['title'])}</h1>
<p class="meta">Dave J Rich's adaptation inspired by Edward de Bono's Six Thinking Hats. Purple is an added perspective.</p>
<p><strong>Purpose:</strong> {esc(data['purpose'])}</p><p class="meta">{esc(data['source'])}</p>
<h2>Document summary</h2><p>{esc(data['summary'])}</p>{''.join(sections)}
<section><h2>Synthesis</h2>{end}</section><h2>References</h2><ul>{''.join(links)}</ul>
<footer><strong>Scope and verification:</strong> {esc(data['limitations'])}</footer></main></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('input and output must be different files')
    output = render(json.loads(args.input.read_text(encoding='utf-8-sig')))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding='utf-8')
    print(args.output.resolve())


if __name__ == '__main__':
    main()
