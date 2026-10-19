# Dave J Rich: Skills

Agent skills I use to think clearly and get real work done with AI. Each one is a plain markdown file that teaches your agent a repeatable method, so you get the same discipline every time instead of whatever a one-off prompt happens to produce.

Built by [Dave J Rich](https://davejrich.com). Ex-clinical nurse, ex-Director of IT, now building AI workflows for real businesses.

[Browse the skills website and formatted example reports](https://davejrich.github.io/skills/).

## Install

**Claude Code plugin** (managed, updates automatically)

Add the marketplace once:

```
/plugin marketplace add davejrich/skills
```

Then install only the skills you want:

```
/plugin install six-frames@davejrich
/plugin install seven-hats@davejrich
/plugin install coaching-client-summary@davejrich
/plugin install meeting@davejrich
```

Or grab everything, including skills added later:

```
/plugin install davejrich-skills@davejrich
```

Don't install the bundle and an individual skill together, or you'll get that skill twice.

**skills.sh** (editable copies, works with Claude Code, Codex and other agents)

```
npx skills@latest add davejrich/skills --skill six-frames
```

Leave off `--skill` to pick from a list or take them all.

**Manual**

Copy any single folder from `skills/` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).

Pick one method. Using two installs every skill twice.

**Updates.** The plugin tracks `main`, but every release gets a version number and a git tag. See the [changelog](CHANGELOG.md) for what changed and how to roll back.

## Skills

### Thinking & decisions

Question claims, explore perspectives and decide what to do next.

| Skill | What it does |
|---|---|
| [**six-frames**](skills/six-frames/) | Runs any article, pitch, claim or web page through Edward de Bono's Six Frames (Purpose, Accuracy, Point of view, Interest, Value, Outcome). Ends with a conclusion, a confidence level and one next action. |
| [**seven-hats**](skills/seven-hats/) | Reviews a document through seven perspectives, including evidence, benefits, caution and wider implications. Includes a colour report renderer and a documented client-view PDF review. |

### Coaching administration

Practical support for the Admin Free Coach community: useful session records and follow-up, with the coach retaining judgment.

| Skill | What it does |
|---|---|
| [**coaching-client-summary**](skills/coaching-client-summary/) | Turns coaching transcripts into client recaps with goals, agreed actions, owners and deadlines. Includes a wholly fictional worked example. |

### Admin

Less admin around the work itself: meetings, follow-up and records.

| Skill | What it does |
|---|---|
| [**meeting**](skills/meeting/) | Builds a time-boxed agenda from your calendar, email and previous minutes, then turns the transcript into minutes with decisions, owners and dates. Flags agenda items that never got covered. Includes a fictional worked example. |

More coming. Watch the repo to hear when they land.

## Quick start

```
/six-frames https://example.com/some-article

Purpose: I'm deciding whether to switch our team to this tool.
```

See [six-frames](skills/six-frames/) for its full guide and worked example, or [seven-hats](skills/seven-hats/) for a document review with a colour report.

## Contributing

Help is welcome. Here's what I'll actually take:

- **Skill misbehaving?** [Open an issue](https://github.com/davejrich/skills/issues/new) with the input you gave it, the output you got, and what you expected instead.
- **PRs to `SKILL.md` and `references/` are welcome.** Keep each one to a single skill and say what problem it fixes.
- **The `examples/` folders and the website are mine.** They're the worked examples I stand behind, so I don't take edits to them. Got a better example? Put it in an issue.

## License

[MIT](LICENSE)
