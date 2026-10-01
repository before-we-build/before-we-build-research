# Migraine / forecasting ingest review

Date: 2026-10-01. Scope: selected literature digest and a proposed research route; no participant study, diagnosis, recruitment, publication or agent-policy changes.

## Ownership and review

- Clinical-neurologist-expert performed bounded primary-source research and then reviewed the new source register and research proposal. No clinical claim blockers found. Access descriptions for Sedley and Gago-Veiga were corrected after the reviewer clarified that full-text opens failed; abstract/indexed-excerpt access is recorded honestly.
- Temporistics-researcher audited preserved sources and existing wiki, identifying Captain/1F as an aspect-position hypothesis with route/goal language, not a measured forecasting ability. No migraine claim or canonical «прогнозатор» alias found in these materials.
- Wiki-contributor wrote the EN/RU/UK source-summary triad and localized inbound references from Captain pages. Root reviewed semantic correspondence of all three peers and activated the editorial group at version 1/1. Active status means reviewed content, not empirical support for the user-origin association.
- These are bounded AI reviews. No independent human clinical, psychometric, statistical or ethics review is claimed. Proposed participant research requires those decisions before recruitment.

## Decisions

Preserve the user's unquantified observation and distinguish H1 (migraine/forecast accuracy), H2 (migraine/independently coded 1F) and H3 (accuracy/independently coded 1F). Six external sources cover classification, a theoretical mechanism, mixed interoception findings and symptom-based attack anticipation. Search is exploratory; no direct study was located, which does not prove universal absence. No pooled effect or individual disease prediction was produced.

The new group has same-language inbound references and links to the research route. Original archives were preserved; a new dated provenance register was added. No source article was copied in full. No personal health records are retained.

## Validation

Strict wiki validation, synchronized section IDs, strict wikilinks, strict claim-language audit, generated index check and static agent lint passed. Python 3.12 is invoked as `python -X utf8` because this Windows environment has no `python3` command and its default cp1251 decoding causes unrelated failures. The generated catalog and migration inventory were refreshed.

Full unittest baseline and final run with UTF-8: 110 tests ran, 105 passed, five errored in existing migration-path tests. The same failures appeared before the digest was finalized: `re.error` on backslashes in replacement strings in `scripts/migrate_wiki_language_paths.py:478`, including a subprocess failure from that migration. An intermediate generated-site check exposed links to research documents that are not included in the wiki-only export; all three peers were corrected to show the repository path, and the final generated-site check passed. This ingestion does not modify scripts or tests; no green full-suite result is claimed.

Reproduction: `python -X utf8 -m unittest discover -s tests -v` (with `PYTHONUTF8=1` for spawned Python), and the eight checks specified in AGENTS.md, substituting `python -X utf8` for `python3`. New content checks pass; full-suite migration failures remain a repository/platform limitation.
