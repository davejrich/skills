# Changelog

Every change that reaches your agent gets a version here. The plugin version in `.claude-plugin/plugin.json` matches the latest entry, and each version is tagged as `vX.Y.Z` in git so you can see exactly what changed or grab an older copy.

When releasing: bump the version in `plugin.json`, add an entry here, then tag the merge commit (`git tag v1.4.0 && git push origin v1.4.0`). Claude Code uses the version to decide whether to update, so a change without a bump may not reach people at all.

If a skill starts behaving differently after an update, check here first. To roll back, download the tagged version from [Tags](https://github.com/davejrich/skills/tags) and copy the skill folder into `~/.claude/skills/` manually (remove the plugin first so you don't have it twice).

## 1.3.1 (2026-10-19)

### Changed
- **seven-hats** reports now credit Dave J Rich instead of David Rich, matching the rest of the repo.
- README adds a contributing section and links this changelog.

## 1.3.0 (2026-10-19)

### Added
- **meeting** skill in a new Admin category. Builds a time-boxed agenda from your calendar, email and previous minutes, then turns the transcript into minutes with decisions, owners and dates, and flags agenda items that never got covered.

### Changed
- README and website group skills into Thinking & decisions, Coaching administration and Admin.

## 1.2.0 (2026-10-19)

### Added
- **coaching-client-summary** skill. Turns coaching transcripts into client recaps with goals, agreed actions, owners and deadlines, plus a separate coach review section. Includes a wholly fictional worked example.

### Changed
- Website: formatted Six Frames worked example with its own heading and review button.

## 1.1.0 (2026-10-19)

### Added
- **seven-hats** skill. Reviews a document through seven perspectives with a colour report renderer and a documented client review example.
- Skills website on GitHub Pages with formatted example reports.

## 1.0.0 (2026-10-18)

### Added
- **six-frames** skill. Runs any article, pitch, claim or web page through Edward de Bono's Six Frames and ends with a conclusion, a confidence level and one next action.
- Claude Code plugin and marketplace manifests.
