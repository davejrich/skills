# Six Medals

An agent skill that works out what a founder really cares about and what their business actually values, using Edward de Bono's Six Value Medals plus one extra medal for the founder's own stakes.

You hand it a business: a name, a website, documents or your meeting notes. It maps the business across seven kinds of value and hands back a short report that always ends with **the founder's top 3 values, the biggest say/do gap, the biggest tension, a confidence level and one next action**.

It's built for anyone who advises, sells to or partners with business owners. Before the meeting, you know what drives them. After the meeting, you know whether you were right.

## Install

Comes with the [davejrich/skills](../../README.md#install) collection. Install that and `/six-medals` is ready to go.

## Use it

```
/six-medals https://example-plumbing.com.au

Purpose: I'm meeting the owner next week about an advisory role.
```

**Desk mode** (the default) reads the website, reviews, job ads and anything else you give it.

Say **"interview mode"** for questions to ask the founder, medal by medal. Paste your notes or transcript afterwards and it updates the map.

Want something to print or keep? Ask for a **branded report**. It renders the map as a print-ready HTML/PDF with your own logo, colours and fonts (`scripts/render_report.py`, Python standard library only).

Got a decision to make for that business? Ask **"does this fit their medals?"** and it tests each option against the saved map.

## The medals

| | Medal | Asks |
|---|---|---|
| 🥇 | **Gold**: people | How does the business treat staff, customers and the people around it? |
| 🥈 | **Silver**: organisation | What does the business itself need: profit, growth, cash, stability? |
| ⚙️ | **Steel**: quality | Does it do its job well? How seriously does it take its standards? |
| 🔷 | **Glass**: innovation | How much does it value new, simpler, better ways of working? |
| 🌳 | **Wood**: community and environment | What's its impact outside the business? |
| 🔔 | **Brass**: perception | How does it want to be seen, and how is it actually seen? |
| 🏺 | **Clay**: founder's stakes *(added)* | What does the founder personally want: lifestyle, control, legacy, exit? |

Each medal is rated **Strong / Present / Weak / Missing**, judged on what the business *does* (reviews, pricing, job ads, policies), not just what it *says*. The gaps between the two are flagged, because that's usually where the real conversation is.

**Why a seventh medal?** De Bono's six medals look at the value of an action or organisation. In a small business, the owner's personal stakes drive almost every decision, and they aren't covered by people (Gold) or organisation (Silver). Advice that grows the business but costs the founder their weekends gets politely ignored. Clay makes that visible. It's labelled as an addition wherever it appears.

Full definitions, where to find evidence, interview questions and common mistakes: [`references/framework.md`](references/framework.md)

## What it looks like

A made-up plumbing business (full run in [`examples/family-plumbing-business.md`](examples/family-plumbing-business.md)):

```
🔷 Glass (innovation): Weak
No online booking. Every quote emails the owner directly.
Value at risk: the owner is the bottleneck for every quote.

Biggest tension: Silver vs Clay. He wants growth, but every
quote runs through him personally.
Next action: Open with "What happens to the business when you
step back?"
```

## Privacy

Values maps hold a founder's personal stakes and blunt judgements. The skill saves them to a private folder excluded from version control, never a public or committed one. A founder-friendly version is available on request and is never sent without your OK.

## Credits

The Six Value Medals method is from Edward de Bono's book *The Six Value Medals* (2005). The Clay medal is this skill's addition. This skill is an independent adaptation and isn't affiliated with or endorsed by the de Bono estate or de Bono Group.

Built by [Dave J Rich](https://davejrich.com).

## License

[MIT](../../LICENSE)

## Render a branded report

From this skill folder:

```sh
python scripts/render_report.py examples/family-plumbing-business.json report.html --brand assets/aisharp-brand.json
```

Open `report.html` and print to PDF (A4, background graphics enabled), or use the headless-browser command in [report-format.md](references/report-format.md). Python 3 is required; the renderer has no third-party Python dependencies. PDF export requires a browser.

The optional AI Sharp preset includes its logo, colours and public contact footer. Copy the preset and replace those details for your own brand; omit `--brand` for an unbranded report. Brand files and SVG logos are trusted local configuration. Google Fonts load over the network; offline rendering uses system fallbacks. Client maps and reports stay private; the bundled example is wholly fictional.
