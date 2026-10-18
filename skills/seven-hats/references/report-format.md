# Report data and rendering

Save UTF-8 JSON with these required fields:

```json
{
  "title": "Seven Hats — Document title",
  "purpose": "What this review helps the reader decide",
  "source": "Document title, author/date if supplied, scope and source URL if available",
  "summary": "Faithful neutral summary",
  "hats": {
    "blue": ["Purpose and decision raised [source locator]"],
    "white": ["Source claim: ... [source locator]. Not verified: ..."],
    "red": ["Interpretation: ... [source locator]"],
    "yellow": ["Potential benefit and conditions [source locator]"],
    "black": ["Material concern and its consequence [source locator]"],
    "green": ["Proposal: ..."],
    "purple": ["Interpretation: connection, relevance and uncertainty"]
  },
  "alternative": "Strongest reasonable alternative reading and evidence that would change the assessment",
  "conclusion": "Conclusion relative to purpose",
  "confidence": "Confidence, basis and important unknowns",
  "next_action": "One specific action",
  "references": [{"label": "Source title or source passage", "url": "https://example.org/source"}],
  "limitations": "Extraction scope and external verification status"
}
```

All content is plain text. Links belong in references; omit `url` for internal source locators. The renderer escapes text and accepts only HTTP(S) reference links. It does not fetch, verify, upload or publish anything.

Run:

```text
python scripts/render_report.py INPUT.json OUTPUT.html
```

HTML includes screen/print styles and all seven sections. Browser Print can produce PDF when requested, subject to visual inspection. For native Docs/Word, use the same palette: Blue #1E40AF, White #FFFFFF with #64748B border, Red #B91C1C, Yellow #FDE047 with dark text, Black #111827, Green #166534, Purple #7E22CE. Body text stays dark on white.

Portable package: copy the entire `seven-hats` directory into the receiving agent's skill directory. In this repository the Claude entry point points to the canonical Codex folder; for a standalone Claude installation copy the canonical folder itself, not the wrapper.
