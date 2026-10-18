# Seven Hats

Review a document through seven distinct perspectives, with evidence locators and a decision-focused conclusion. David Rich's adaptation adds Purple (connections and implications) to an approach inspired by Edward de Bono's Six Thinking Hats; it is not an official de Bono method.

## Use

```text
/seven-hats Review this PDF from a prospective client's perspective.
```

Supply a file, accessible link or pasted text. The skill produces a neutral summary, Blue, White, Red, Yellow, Black, Green and Purple perspectives, an alternative reading, a conclusion, confidence and one next action.

Read [SKILL.md](SKILL.md) for instructions and [the report schema](references/report-format.md) for renderer input. Python 3's standard library is sufficient to render an existing analysis; reading PDFs requires an available PDF reader separately.

## Worked example and observed test

On 19 October 2026 the skill was used in Codex to review Laura Zavelson's 29-page *Build Your AI Marketing Assistant* workshop PDF from a nontechnical client's perspective. Prompts inside the PDF were analysed as content rather than executed.

- [Readable review](examples/marketing-assistant-review.md)
- [Renderer input](examples/marketing-assistant-review.json)
- [Generated colour report](examples/marketing-assistant-review.html) — download and open in a browser; GitHub may show HTML source.

The source PDF is excluded. The example contains attributed analysis and limited paraphrases, not the source presentation. It is not an endorsement or independently validated marketing study.

### What was checked

| Check | Observed result |
| --- | --- |
| Source coverage | Text extracted and read from all 29 PDF pages. |
| Review structure | All seven hats, summary, alternative reading, conclusion, confidence, next action and limits present. |
| Evidence handling | Page locators supplied; interpretations and proposals labelled; external verification limited to OpenAI project documentation. |
| Renderer | Example JSON rendered successfully using Python's standard library. |
| Visual review | Incomplete: Chrome screenshot attempt failed with exit code 2147483651. No claim of visual approval. |
| Agent portability | Portable files packaged; no fresh-session Claude or other-agent behavior test performed. |

The example demonstrates an observed workflow, not comprehensive proof of analysis quality or repeatability. A human client usability test remains a proposed next step.

## Reproduce the report

From the repository root:

```sh
python skills/seven-hats/scripts/render_report.py skills/seven-hats/examples/marketing-assistant-review.json review.html
```

This reproduces the presentation of the saved analysis. To test reasoning independently, supply your own accessible copy of the PDF in a fresh agent session and use the example request above; do not treat the saved review as the expected wording.
