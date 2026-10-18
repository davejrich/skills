---
name: six-frames
description: Think critically about a piece of information using Edward de Bono's Six Frames (Triangle/Purpose, Circle/Accuracy, Square/Point of view, Heart/Interest, Diamond/Value, Slab/Outcome). Use on "/six-frames", "run the six frames on this", "frame this", "is this worth acting on", "can I trust this", or when an article, report, email, pitch, claim or web page is shared with a request to evaluate it rather than summarise it. Always ends with a conclusion, a confidence level and one next action.
---

# Six Frames

Runs a piece of information through de Bono's six frames, one at a time, in a fixed order. The output is a short frame-by-frame breakdown that ends on a Slab: what to conclude and what to do next.

Read `references/framework.md` before the first run in a session. It has the full question set for each frame and the common mistakes to avoid.

## What this skill is NOT

- **Not a summary.** A summary describes the information. This judges it against a purpose.
- **Not idea generation.** Use a brainstorm or Six Thinking Hats for that. Six Frames is for taking information in.
- **Not a fact-checker.** It flags what needs checking and does cheap checks, but the rating is a judgement, not a verdict.

## Modes

**Quick (default).** Run all six frames on the source and present the result. The user reviews and pushes back.

**Guided.** Triggered by "walk me through it", "guided" or "teach me". Ask the user each frame's question one at a time, wait for their answer, add your own view, then move on. Use when the user wants to build the habit or is learning the method.

## Inputs

- **The source.** Pasted text, a file path, a URL (fetch it), or any document the agent can read.
- **The purpose.** If the user hasn't said why they're looking at it, ask before doing anything else. One line is enough: "What's this for? A decision, a piece of content, a client, or just curious?" If they say "just curious", the Triangle is exploration and the Diamond judges by general usefulness.
- **Optional context.** Any project or priorities files the agent has access to, so the Diamond can rank value against what actually matters to this user.

## Execution

### Step 1: Lock the Triangle

Confirm the purpose before reading deeply. State it back in one sentence. Everything else is judged against it.

### Step 2: Read the source

Read it fully. If it's long, note the main claims as you go. Those feed the Circle.

### Step 3: Run the frames in order

Keep each frame tight: 2 to 5 short points, no padding.

1. **▲ Triangle: Purpose.** The one-line purpose, plus what "enough" looks like.
2. **● Circle: Accuracy.** List the key claims and rate each one: certain / likely / possible / unverified / doubtful, with a few words on why. Flag anything that should be checked before relying on it. If a claim is cheap to verify with a quick search, do it and say what you found.
3. **■ Square: Point of view.** Who is speaking, what they gain, what bias is baked in, and one or two viewpoints that are missing.
4. **♥ Heart: Interest.** What is surprising, contrarian, or sparks a connection, even if it's off-purpose.
5. **◆ Diamond: Value.** What directly serves the Triangle, what is valuable to someone else, and what is noise to drop.
6. **▬ Slab: Outcome.** The conclusion in 1 or 2 sentences, a confidence level (taken from the Circle), and one specific next action. "Ignore it" is a valid outcome.

### Step 4: Present

Use this layout:

```
## Six Frames: <source title>

▲ Purpose: <one line>

● Accuracy
<claim>: <rating>, <why>

■ Point of view
...

♥ Interest
...

◆ Value
...

▬ Outcome
Conclusion: ...
Confidence: high / medium / low
Next action: ...
```

Keep it scannable on a phone. If a frame genuinely has nothing to say, write "Nothing notable" rather than inventing points.

### Step 5: Offer one follow-on

Pick the single most relevant one. Don't list them all.

- Low Circle on an important claim: offer to dig into the sources.
- Strong Diamond: offer to save the key points somewhere the user keeps notes.
- Strong Heart: offer to turn the interesting angle into content or a next question.
- Feeds a decision: offer to write the decision down with the reasoning.

## Guided mode questions

Ask one frame at a time. Wait for the answer, then add your take before moving on.

- ▲ "Why are you looking at this, and what would make it worth your time?"
- ● "Which claims here would you bet money on? Which wouldn't you?"
- ■ "Who made this and what do they want? Who would disagree?"
- ♥ "What jumped out at you, even if it's off-topic?"
- ◆ "Of everything here, what would you actually use? What can you drop?"
- ▬ "So what are you going to do with it?"

## Edge cases

- **Several sources on one topic.** Run the Triangle once, then the Circle and Square per source so conflicts show up, then one combined Heart, Diamond and Slab.
- **Very short input (one claim or a headline).** Collapse to one line per frame.
- **Source can't be fetched (paywall, login).** Say so and ask the user to paste it. Never frame a source you haven't read.
- **The user made the source (their own website, report or pitch).** Be just as straight in the Circle and Square. That's the point of the frames.
