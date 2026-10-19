# Meeting

Prep a meeting and write it up with one skill. Before the meeting it builds a time-boxed agenda from the calendar event, recent email and previous minutes, around the decisions you need. Afterwards it turns the transcript into minutes with decisions, action items and owners, and checks them against the agenda so anything that got skipped is flagged for next time.

## Use

```text
/meeting prep my call with Sam tomorrow
```

```text
/meeting Write up the minutes from this transcript.
```

PREP finds the meeting, gathers context, shows you a draft agenda and saves it once you approve it. MINUTES finds the matching agenda, writes the minutes, shows you the draft and saves it once you approve it. Either mode can then draft an email to attendees or add your action items to your task tool. Both ask first, and it never sends anything.

- [Skill instructions](SKILL.md)
- [Agenda and minutes formats](references/formats.md)
- [Fictional worked example, agenda to minutes](examples/project-check-in.md)

**Install just this skill:** `/plugin marketplace add davejrich/skills` then `/plugin install meeting@davejrich`. Other methods are in the collection's [install section](../../README.md#install).

## What it needs

Nothing is required. It works with whatever your agent has connected: a calendar, email, a document store and a task tool. Without them, tell it who the meeting is with and what it's about, or paste the transcript, and it still writes the agenda or minutes. It names any source it couldn't reach rather than pretending it checked.

Transcripts usually live in your meeting platform's recordings or AI summary area, not in your inbox, and some free plans don't produce one. Export the transcript and give it to the skill.

## Limits

Treat both outputs as drafts. The agenda's Background section is for you only and stays out of anything sent to attendees. Minutes only record owners and dates that were actually agreed; anything unclear is marked TBC. Some document tools can only share with a named email address, so you may need to switch on link sharing yourself for attendees on other platforms.

The example uses invented people and dialogue. It has been run end to end on a real meeting's prep, but not yet independently tested across platforms.
