from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from audit_claim_language import audit_claims  # noqa: E402
from add_wiki_section_ids import synchronize_section_ids  # noqa: E402
from check_wikilinks import check_links  # noqa: E402
from generate_wiki_index import check_index, render_index  # noqa: E402
from generate_wiki_inventory import AUDITED_BASELINE, build_inventory  # noqa: E402
from migrate_wiki_language_paths import (  # noqa: E402
    infer_role,
    normalize_frontmatter,
    rewrite_links,
)
from validate_wiki import validate_wiki  # noqa: E402
from wiki_quality_common import load_wiki_pages, parse_frontmatter  # noqa: E402


def page_text(
    group: str,
    lang: str,
    *,
    status: str = "active",
    version: int = 1,
    role: str = "explanation",
    caveats: str = "[context-required]",
    claim_id: str = "model-is-hypothesis",
    claim_status: str = "research-hypothesis",
    sources: str = "[raw/source.md]",
    sections: tuple[str, ...] = ("definition",),
    body: str = "Body.",
) -> str:
    markers = "\n".join(f"<!-- section:{item} -->\n## {item}" for item in sections)
    return f"""---
title: {group} ({lang})
lang: {lang}
translation_group: {group}
semantic_version: {version}
reviewed_semantic_version: {version}
document_status: {status}
page_role: {role}
claim_status: [{claim_status}]
claims:
  - id: {claim_id}
    status: {claim_status}
caveat_ids: {caveats}
sources: {sources}
---

# {group}

{markers}

{body}
"""


class RepositoryFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_directory.name)
        (self.root / "wiki").mkdir(parents=True)
        (self.root / "raw").mkdir(parents=True)
        (self.root / "raw" / "source.md").write_text("# Preserved source\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp_directory.cleanup()

    def write_page(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_triad(self, group: str, *, directory: str = "wiki", **kwargs: object) -> None:
        for lang in ("en", "ru", "uk"):
            self.write_page(
                f"{directory}/{group}-{lang}.md",
                page_text(group, lang, **kwargs),
            )


class FrontmatterTests(unittest.TestCase):
    def test_parses_claim_mapping_and_inline_lists(self) -> None:
        metadata, body, error = parse_frontmatter(page_text("sample", "en"))
        self.assertIsNone(error)
        self.assertEqual(metadata["caveat_ids"], ["context-required"])
        self.assertEqual(
            metadata["claims"],
            [{"id": "model-is-hypothesis", "status": "research-hypothesis"}],
        )
        self.assertIn("# sample", body)

    def test_language_migration_does_not_rewrite_raw_basename_collision(self) -> None:
        groups = {
            "guru": {
                "en": Path("/repo/wiki/entities/guru-en.md"),
                "ru": Path("/repo/wiki/entities/guru-ru.md"),
                "uk": Path("/repo/wiki/entities/guru-uk.md"),
            }
        }
        migrated = rewrite_links(
            "sources: [raw/temporistics/guru.md]\n[[guru]]\nwiki/entities/guru.md\n",
            "en",
            groups,
            {"wiki/entities/guru.md": "wiki/entities/guru-en.md"},
            {"guru.md"},
        )
        self.assertIn("raw/temporistics/guru.md", migrated)
        self.assertIn("[[guru-en]]", migrated)
        self.assertIn("wiki/entities/guru-en.md", migrated)

        russian = rewrite_links(
            "[[guru]]\nwiki/entities/guru.md\n",
            "ru",
            groups,
            {"wiki/entities/guru.md": "wiki/entities/guru-en.md"},
            {"guru.md"},
        )
        self.assertIn("[[guru-ru]]", russian)
        self.assertIn("wiki/entities/guru-ru.md", russian)

    def test_language_migration_preserves_explicit_language_switcher(self) -> None:
        groups = {
            "sample": {
                "en": Path("/repo/wiki/sample-en.md"),
                "ru": Path("/repo/wiki/sample-ru.md"),
                "uk": Path("/repo/wiki/sample-uk.md"),
            }
        }
        migrated = rewrite_links(
            "[[sample|English]] · [[sample-ru|Русский]] · [[sample-uk|Українська]]\n",
            "ru",
            groups,
            {"wiki/sample.md": "wiki/sample-en.md"},
        )
        self.assertIn("[[sample-en|English]]", migrated)
        self.assertIn("[[sample-ru|Русский]]", migrated)
        self.assertIn("[[sample-uk|Українська]]", migrated)

    def test_language_migration_infers_application_and_research_roles(self) -> None:
        self.assertEqual(
            infer_role(Path("wiki/concepts/christian-practice-en.md"), "concept"),
            "application",
        )
        self.assertEqual(
            infer_role(Path("wiki/concepts/socionics-test-specification-en.md"), "concept"),
            "research-appendix",
        )

    def test_language_migration_adds_complete_minimum_frontmatter(self) -> None:
        migrated = normalize_frontmatter(
            Path("wiki/concepts/sample-en.md"), "# Sample title\n\nBody.\n"
        )
        metadata, _, error = parse_frontmatter(migrated)
        self.assertIsNone(error)
        self.assertEqual(metadata["title"], "Sample title")
        self.assertEqual(metadata["sources"], [])
        self.assertEqual(metadata["translation_group"], "sample")


class WikiValidationTests(RepositoryFixture):
    def test_valid_triad_passes_strict_validation(self) -> None:
        self.write_triad("sample")
        self.assertEqual(validate_wiki(self.root, strict=True), [])

    def test_missing_locale_is_an_error_only_in_strict_mode(self) -> None:
        for lang in ("en", "ru"):
            self.write_page(f"wiki/sample-{lang}.md", page_text("sample", lang))
        migration = validate_wiki(self.root, strict=False)
        strict = validate_wiki(self.root, strict=True)
        self.assertIn("incomplete-active-triad", {item.code for item in migration})
        self.assertTrue(all(item.severity == "warning" for item in migration))
        self.assertTrue(any(item.code == "incomplete-active-triad" and item.severity == "error" for item in strict))

    def test_detects_version_claim_caveat_and_section_drift(self) -> None:
        self.write_page("wiki/sample-en.md", page_text("sample", "en"))
        self.write_page(
            "wiki/sample-ru.md",
            page_text(
                "sample",
                "ru",
                version=2,
                caveats="[different-caveat]",
                claim_id="different-claim",
                sections=("different-section",),
            ),
        )
        self.write_page("wiki/sample-uk.md", page_text("sample", "uk"))
        diagnostics = validate_wiki(self.root, strict=True)
        parity_messages = [item.message for item in diagnostics if item.code == "translation-parity"]
        self.assertTrue(any("semantic_version" in message for message in parity_messages))
        self.assertTrue(any("claims" in message for message in parity_messages))
        self.assertTrue(any("caveat_ids" in message for message in parity_messages))
        self.assertTrue(any("section_ids" in message for message in parity_messages))

    def test_detects_retired_simulation_term(self) -> None:
        self.write_triad("sample", body="The Digital Twin predicts the participant.")
        diagnostics = validate_wiki(self.root, strict=True)
        self.assertIn("retired-simulation-term", {item.code for item in diagnostics})

    def test_unsuffixed_filename_and_deprecated_hierarchy_fail(self) -> None:
        content = page_text("sample", "en").replace(
            "sources: [raw/source.md]", "canonical: sample.md\ntranslation_of: sample.md\nsources: [raw/source.md]"
        )
        self.write_page("wiki/sample.md", content)
        codes = {item.code for item in validate_wiki(self.root, strict=True)}
        self.assertIn("filename-language", codes)
        self.assertIn("deprecated-field", codes)

    def test_central_page_contract_requires_stable_sections(self) -> None:
        self.write_triad("main-idea", role="hub", sections=("definition-and-scope",))
        diagnostics = validate_wiki(self.root, strict=True)
        self.assertIn("central-page-contract", {item.code for item in diagnostics})

    def test_source_summary_contract_requires_assessment_sections(self) -> None:
        self.write_triad("source-note", role="source-summary")
        diagnostics = validate_wiki(self.root, strict=True)
        self.assertIn("source-summary-contract", {item.code for item in diagnostics})

    def test_source_references_accept_existing_raw_file_and_directory(self) -> None:
        (self.root / "raw" / "collection").mkdir()
        self.write_triad(
            "sample",
            sources="[raw/source.md, raw/collection]",
        )
        source_codes = {
            item.code
            for item in validate_wiki(self.root, strict=True)
            if "source" in item.code
        }
        self.assertEqual(source_codes, set())

    def test_source_references_report_missing_explicit_path(self) -> None:
        self.write_triad("sample", sources="[docs/missing.md]")
        diagnostics = validate_wiki(self.root, strict=True)
        self.assertIn("missing-source", {item.code for item in diagnostics})

    def test_source_references_report_ambiguous_bare_markdown_name(self) -> None:
        self.write_page("docs/shared.md", "# First\n")
        self.write_page("skills/shared.md", "# Second\n")
        self.write_triad("sample", sources="[shared.md]")
        diagnostics = validate_wiki(self.root, strict=True)
        self.assertIn("ambiguous-source", {item.code for item in diagnostics})

    def test_source_references_ignore_external_and_free_text_labels(self) -> None:
        sources = (
            '["https://example.org/paper.md#results", "web: https://example.org", '
            '"doi:10.1000/example", "arxiv: 2401.00001", '
            '"official project documentation", "unknown-slug", '
            '"before-we-build/Psyche-Yoga"]'
        )
        self.write_triad("sample", sources=sources)
        source_codes = {
            item.code
            for item in validate_wiki(self.root, strict=True)
            if "source" in item.code
        }
        self.assertEqual(source_codes, set())

    def test_source_references_resolve_bare_translation_group(self) -> None:
        self.write_triad("target")
        self.write_triad("sample", sources="[target]")
        source_codes = {
            item.code
            for item in validate_wiki(self.root, strict=True)
            if "source" in item.code
        }
        self.assertEqual(source_codes, set())

    def test_source_references_are_not_checked_on_draft_pages(self) -> None:
        self.write_triad("sample", status="draft", sources="[docs/missing.md]")
        source_codes = {
            item.code
            for item in validate_wiki(self.root, strict=True)
            if "source" in item.code
        }
        self.assertEqual(source_codes, set())

    def test_source_reference_cannot_escape_repository(self) -> None:
        self.write_triad("sample", sources="[../../outside.md]")
        diagnostics = validate_wiki(self.root, strict=True)
        self.assertIn("source-outside-root", {item.code for item in diagnostics})

    def test_source_references_use_manifest_and_localized_peer(self) -> None:
        self.write_triad("target")
        self.write_page(
            "wiki/slug-migrations.json",
            json.dumps({"migrations": {"wiki/old.md": "wiki/target-en.md"}}),
        )
        self.write_triad("old-reference", sources="[wiki/old.md]")
        self.write_page(
            "wiki/localized-reference-en.md",
            page_text("localized-reference", "en", sources="[wiki/target-ru.md]"),
        )
        self.write_page(
            "wiki/localized-reference-ru.md",
            page_text("localized-reference", "ru", sources="[wiki/target-ru.md]"),
        )
        self.write_page(
            "wiki/localized-reference-uk.md",
            page_text("localized-reference", "uk", sources="[wiki/target-uk.md]"),
        )
        diagnostics = validate_wiki(self.root, strict=True)
        codes = {item.code for item in diagnostics}
        self.assertIn("old-source-slug", codes)
        self.assertIn("cross-language-source", codes)

    def test_section_id_synchronizer_adds_equal_ids(self) -> None:
        for lang, title in (("en", "Shared idea"), ("ru", "Общая идея"), ("uk", "Спільна ідея")):
            content = page_text("sample", lang).replace(
                "<!-- section:definition -->\n## definition",
                f"## {title}",
            )
            self.write_page(f"wiki/sample-{lang}.md", content)
        issues, changed = synchronize_section_ids(self.root, write=True)
        self.assertEqual(issues, [])
        self.assertEqual(len(changed), 3)
        pages = load_wiki_pages(self.root)
        self.assertEqual({page.section_ids for page in pages}, {("shared-idea",)})


class LinkCheckerTests(RepositoryFixture):
    def test_broken_ambiguous_cross_language_anchor_and_old_slug(self) -> None:
        source_body = """[[missing-en]]
[[duplicate-en]]
[[target-ru]]
[[target-en#missing-anchor]]
[[old-page]]
"""
        self.write_page("wiki/source-en.md", page_text("source", "en", body=source_body))
        self.write_page("wiki/a/duplicate-en.md", page_text("duplicate", "en"))
        self.write_page("wiki/b/duplicate-en.md", page_text("duplicate", "en"))
        self.write_page("wiki/target-en.md", page_text("target", "en"))
        self.write_page("wiki/target-ru.md", page_text("target", "ru"))
        self.write_page(
            "wiki/slug-migrations.json",
            json.dumps({"wiki/old-page.md": "wiki/new-page-en.md"}),
        )
        diagnostics = check_links(self.root, strict=True, check_orphans=False)
        codes = {item.code for item in diagnostics}
        self.assertTrue(
            {"missing-link", "ambiguous-link", "cross-language-link", "missing-anchor", "old-slug"}
            <= codes
        )

    def test_language_switcher_is_an_explicit_cross_language_exception(self) -> None:
        body = "Languages: [[target-ru|Русский]]"
        self.write_page("wiki/source-en.md", page_text("source", "en", body=body))
        self.write_page("wiki/target-ru.md", page_text("target", "ru"))
        diagnostics = check_links(self.root, strict=True, check_orphans=False)
        self.assertNotIn("cross-language-link", {item.code for item in diagnostics})

    def test_detects_active_orphan_group(self) -> None:
        self.write_triad("orphan")
        diagnostics = check_links(self.root, strict=True, check_orphans=True)
        self.assertTrue(any(item.code == "orphan-group" for item in diagnostics))

    def test_report_mode_does_not_turn_findings_into_errors(self) -> None:
        self.write_page("wiki/source-en.md", page_text("source", "en", body="[[missing-en]]"))
        diagnostics = check_links(self.root, strict=False, check_orphans=False)
        self.assertTrue(diagnostics)
        self.assertTrue(all(item.severity == "warning" for item in diagnostics))


class ClaimAuditTests(RepositoryFixture):
    def test_flags_asserted_guarantee_but_not_negated_caveat(self) -> None:
        self.write_triad(
            "asserted",
            body="This type guarantees relationship success.",
        )
        self.write_triad(
            "negated",
            body="This type does not guarantee relationship success.",
        )
        diagnostics = audit_claims(self.root, strict=True)
        guarantee_paths = {item.path for item in diagnostics if item.code == "guaranteed-outcome"}
        self.assertTrue(any("asserted-" in path for path in guarantee_paths if path))
        self.assertFalse(any("negated-" in path for path in guarantee_paths if path))

    def test_attributed_claim_status_and_reasoned_marker_are_allowed(self) -> None:
        attributed = page_text(
            "attributed",
            "en",
            claim_id="quoted-source",
            claim_status="source-attribution",
            body="<!-- claim:quoted-source -->\nThe source says this is scientifically proven.",
        )
        marked = page_text(
            "marked",
            "en",
            body="<!-- claim-audit: allow reason=historical-quotation -->\nThe source guarantees success.",
        )
        self.write_page("wiki/attributed-en.md", attributed)
        self.write_page("wiki/marked-en.md", marked)
        diagnostics = audit_claims(self.root, strict=True)
        self.assertEqual(diagnostics, [])

    def test_flags_numeric_compatibility_score(self) -> None:
        self.write_page(
            "wiki/scoring-en.md",
            page_text("scoring", "en", body="The compatibility score is 82%."),
        )
        codes = {item.code for item in audit_claims(self.root, strict=True)}
        self.assertIn("compatibility-score", codes)

    def test_flags_bwb_as_personality_typology_but_allows_explicit_rejection(self) -> None:
        assertions = {
            "en": "Before We Build is a personality typology.",
            "ru": "Before We Build — типология личности.",
            "uk": "BWB — типологія особистості.",
        }
        rejections = {
            "en": "Before We Build is not a personality typology.",
            "ru": "Before We Build — не типология личности.",
            "uk": "BWB — не типологія особистості.",
        }
        for lang, body in assertions.items():
            self.write_page(
                f"wiki/asserted-personality-typology-{lang}.md",
                page_text("asserted-personality-typology", lang, body=body),
            )
        for lang, body in rejections.items():
            self.write_page(
                f"wiki/rejected-personality-typology-{lang}.md",
                page_text("rejected-personality-typology", lang, body=body),
            )
        diagnostics = audit_claims(self.root, strict=True)
        paths = {
            item.path for item in diagnostics if item.code == "bwb-personality-typology"
        }
        self.assertTrue(any("asserted-personality-typology-" in path for path in paths if path))
        self.assertFalse(any("rejected-personality-typology-" in path for path in paths if path))

    def test_flags_retired_simulation_entity_outside_wiki(self) -> None:
        self.write_page(
            "docs/active-design.md",
            "# Design\n\nThe Candidate Twin predicts a person's response.\n",
        )
        codes = {item.code for item in audit_claims(self.root, strict=True)}
        self.assertIn("retired-simulation-entity", codes)

    def test_prohibited_examples_are_not_reported_as_project_claims(self) -> None:
        self.write_page(
            "wiki/warnings-en.md",
            page_text(
                "warnings",
                "en",
                body="""## Non-claims

This page does not claim that:

- a type determines morality or destiny;
- compatibility guarantees marriage success;
- this typology is scientifically proven.
""",
            ),
        )
        self.assertEqual(audit_claims(self.root, strict=True), [])


class IndexAndInventoryTests(RepositoryFixture):
    def test_generated_index_and_stale_check(self) -> None:
        self.write_triad("start-here", role="hub")
        rendered = render_index(load_wiki_pages(self.root))
        self.assertIn("Complete EN/RU/UK triads: **1**", rendered)
        self.assertIn("[start-here (en)](wiki/start-here-en.md)", rendered)
        output = self.root / "index.md"
        output.write_text("stale\n", encoding="utf-8")
        matches, diff = check_index(output, rendered)
        self.assertFalse(matches)
        self.assertIn("generated", diff)
        output.write_text(rendered, encoding="utf-8")
        self.assertTrue(check_index(output, rendered)[0])

    def test_inventory_preserves_baseline_and_reports_current_graph(self) -> None:
        self.write_triad(
            "source",
            body="[[target-en]]\nStrategic level: values.\nThe compatibility score is 95%.",
        )
        self.write_triad("target")
        inventory = build_inventory(self.root)
        self.assertEqual(inventory["audited_baseline"], AUDITED_BASELINE)
        self.assertEqual(inventory["current_summary"]["pages"], 6)
        self.assertEqual(inventory["current_summary"]["translation_groups"], 2)
        self.assertEqual(inventory["current_summary"]["groups_with_duplicate_locales"], 0)
        self.assertEqual(
            inventory["current_summary"]["page_claim_statuses"],
            {"research-hypothesis": 6},
        )
        target_en = next(
            page for page in inventory["pages"] if page["path"] == "wiki/target-en.md"
        )
        self.assertTrue(target_en["inbound_links"])
        self.assertEqual(
            target_en["claims"], {"model-is-hypothesis": "research-hypothesis"}
        )
        self.assertEqual(target_en["caveat_ids"], ["context-required"])
        self.assertTrue(inventory["hits"]["numeric_scoring"])
        self.assertTrue(inventory["hits"]["old_model"])
        self.assertIn("validation_findings", inventory)


if __name__ == "__main__":
    unittest.main()
