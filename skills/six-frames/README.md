# Six Frames

An agent skill that makes your AI think about information the way Edward de Bono taught: one deliberate lens at a time, ending in a decision.

You hand it an article, report, email, pitch, claim or web page. It runs the source through six frames (Purpose, Accuracy, Point of view, Interest, Value, Outcome) and hands back a short breakdown that always ends with **a conclusion, a confidence level and one next action**.

It's not a summariser. Summaries tell you what something says. Six Frames tells you whether to trust it and what to do about it.

## Install

**Install just this skill:** `/plugin marketplace add davejrich/skills` then `/plugin install six-frames@davejrich`. Other methods are in the collection's [install section](../../README.md#install).

## Use it

```
/six-frames https://example.com/some-article

Purpose: I'm deciding whether to switch our team to this tool.
```

Or just paste something and say "run the six frames on this". If you don't give a purpose, it asks for one first. That's on purpose: without a purpose there's nothing to judge value against.

Say **"walk me through it"** for guided mode. It asks you each frame's question, waits for your answer, then adds its own view. That's the mode to use if you want the habit to stick in your own head, not just the agent's.

## The six frames

| | Frame | Asks |
|---|---|---|
| ▲ | **Triangle**: Purpose | Why am I looking at this? What do I need from it? |
| ● | **Circle**: Accuracy | How true is it? Every key claim gets rated: certain, likely, possible, unverified or doubtful. |
| ■ | **Square**: Point of view | Whose angle is this, what do they gain, and whose view is missing? |
| ♥ | **Heart**: Interest | What's surprising or worth following up, even if it's off-purpose? |
| ◆ | **Diamond**: Value | What's actually useful? What's noise? |
| ▬ | **Slab**: Outcome | So what? Conclusion, confidence, next action. |

The order is fixed. Purpose comes first because every later frame is judged against it. Outcome comes last because analysis that doesn't end in a decision is just reading.

Full question set and common mistakes: [`references/framework.md`](references/framework.md)

## What it looks like

[View the formatted example report online](https://davejrich.github.io/skills/examples/six-frames-vendor-review.html).

A made-up vendor email run through the skill (full run in [`examples/ai-vendor-claim.md`](examples/ai-vendor-claim.md)):

```
● Accuracy
"Cuts admin by 80%": doubtful. No baseline, no source.
"Never make mistakes": doubtful. No AI system can honestly claim this.

▬ Outcome
Conclusion: Don't book the demo off this email.
Confidence: high
Next action: Reply asking how client data is stored and which
accounting systems it integrates with. Book only if both answers
are specific.
```

## Good things to frame

- A vendor pitch before you take the call
- A viral post or "new study shows" headline before you repeat it
- A competitor's landing page
- **Your own** website, proposal or report, read as your customer would

That last one is the most useful and the most uncomfortable. The skill is told to be just as blunt about your work as anyone else's.

## Why a skill and not a prompt

A prompt gets you a one-off. A skill gets you the same discipline every time: the purpose is always locked first, claims are always rated rather than vibed, accuracy and bias are always kept separate, and it always ends with an action. You stop getting summaries dressed up as analysis.

## Credits

The Six Frames method is from Edward de Bono's book *Six Frames for Thinking About Information* (2008). This skill is an independent adaptation and isn't affiliated with or endorsed by the de Bono estate or de Bono Group. Read the book. It's short and better than any summary of it, including this one.

Built by [Dave J Rich](https://davejrich.com).

## License

[MIT](../../LICENSE)
