# Dave J Rich: Skills

Agent skills I use to think clearly and get real work done with AI. Each one is a plain markdown file that teaches your agent a repeatable method, so you get the same discipline every time instead of whatever a one-off prompt happens to produce.

Built by [Dave J Rich](https://davejrich.com). Ex-clinical nurse, ex-Director of IT, now building AI workflows for real businesses.

## Install

**Claude Code plugin** (managed, updates automatically)

```
/plugin marketplace add davejrich/skills
/plugin install davejrich-skills@davejrich
```

**skills.sh** (editable copies, works with Claude Code, Codex and other agents)

```
npx skills@latest add davejrich/skills
```

**Manual**

Copy any folder from `skills/` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).

Pick one method. Using two installs every skill twice.

## Skills

| Skill | What it does |
|---|---|
| [**six-frames**](skills/six-frames/) | Runs any article, pitch, claim or web page through Edward de Bono's Six Frames (Purpose, Accuracy, Point of view, Interest, Value, Outcome). Ends with a conclusion, a confidence level and one next action. |

More coming. Watch the repo to hear when they land.

## Quick start

```
/six-frames https://example.com/some-article

Purpose: I'm deciding whether to switch our team to this tool.
```

See [six-frames](skills/six-frames/) for the full guide and a worked example.

## License

[MIT](LICENSE)
