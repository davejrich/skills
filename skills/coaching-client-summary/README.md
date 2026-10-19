# Coaching client summary

Turn a coaching transcript into a practical client recap: goals, insights, agreed actions, accountable owners, deadlines and follow-up. Keep suggestions and missing agreements visible rather than inventing commitments.

## Use

```text
/coaching-client-summary Summarise this coaching transcript for the client.
```

Supply a transcript, notes or accessible link. The skill returns a client draft followed by a separate coach evidence/review section. It includes coach-owned support and distinguishes desired outcomes from specific actions.

- [Skill instructions](SKILL.md)
- [Output format and evidence ledger](references/summary-format.md)
- [View the formatted fictional example](https://davejrich.github.io/skills/examples/coaching-client-summary.html)
- [Fictional input and worked output](examples/delegation-session.md)
- [Validation limits](references/pilot-status.md)

**Install just this skill:** `/plugin marketplace add davejrich/skills` then `/plugin install coaching-client-summary@davejrich`. Other methods are in the collection's [install section](../../README.md#install). The skill uses your agent's available document readers; no dedicated external account is required to work with pasted text.

## Review and refine

Treat the result as a draft until the coach checks it. The first version prioritises faithful commitments and clear unknowns. Refine tone, length and table detail with the coach over successive sessions. It does not send summaries or schedule reminders.

The public example uses entirely invented dialogue and generic roles. It does not use a real transcript, including as a renamed example. Independent behavioral testing and coach validation remain outstanding.
