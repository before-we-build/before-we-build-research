from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any

from wiki_quality_common import (
    REPO_ROOT,
    WikiPage,
    load_wiki_pages,
)

DEFAULT_OUTPUT_DIR = REPO_ROOT.parent / "before-we-build.github.io" / "wiki"

I18N = {
    "uk": {
        "site_title": "Before We Build · База знань",
        "home": "Головна",
        "tests": "Тести",
        "calculator": "Калькулятор",
        "wiki": "База знань",
        "search_placeholder": "Пошук по базі знань...",
        "toc": "Зміст статті",
        "metadata": "Метадані статті",
        "status": "Статус",
        "version": "Версія",
        "back_to_tests": "← До тестів Before We Build",
        "categories": {
            "overview": "Огляд та методологія",
            "concepts": "Теоретичні концепти",
            "entities": "Сутності (типи, аспекти, функції)",
            "relations": "Відношення та сумісність",
            "sources": "Джерела та література",
            "glossary": "Словники термінів",
        },
    },
    "en": {
        "site_title": "Before We Build · Knowledge Base",
        "home": "Home",
        "tests": "Tests",
        "calculator": "Calculator",
        "wiki": "Knowledge Base",
        "search_placeholder": "Search knowledge base...",
        "toc": "Table of contents",
        "metadata": "Article metadata",
        "status": "Status",
        "version": "Version",
        "back_to_tests": "← Back to Before We Build tests",
        "categories": {
            "overview": "Overview & Methodology",
            "concepts": "Theoretical Concepts",
            "entities": "Entities (types, aspects, functions)",
            "relations": "Relations & Compatibility",
            "sources": "Sources & Literature",
            "glossary": "Glossary of terms",
        },
    },
    "ru": {
        "site_title": "Before We Build · База знаний",
        "home": "Главная",
        "tests": "Тесты",
        "calculator": "Калькулятор",
        "wiki": "База знаний",
        "search_placeholder": "Поиск по базе знаний...",
        "toc": "Содержание статьи",
        "metadata": "Метаданные статьи",
        "status": "Статус",
        "version": "Версия",
        "back_to_tests": "← К тестам Before We Build",
        "categories": {
            "overview": "Обзор и методология",
            "concepts": "Теоретические концепты",
            "entities": "Сущности (типы, аспекты, функции)",
            "relations": "Отношения и совместимость",
            "sources": "Источники и литература",
            "glossary": "Словари терминов",
        },
    },
}


def slug_to_url(slug: str, lang: str | None = None) -> str:
    """Convert a page slug or path into an HTML link relative to /wiki/."""
    clean = slug.strip().replace(".md", "")
    if clean.startswith("wiki/"):
        clean = clean[5:]
    return f"{clean}.html"


def render_markdown_to_html(md_text: str, current_lang: str, slug_map: dict[str, str]) -> tuple[str, list[dict[str, str]]]:
    """Lightweight, resilient Markdown to semantic HTML renderer with Wikilink & Callout support."""
    lines = md_text.splitlines()
    html_out: list[str] = []
    toc: list[dict[str, str]] = []
    
    in_code_block = False
    code_lang = ""
    code_lines: list[str] = []
    
    in_list = False
    in_table = False
    table_header_done = False

    def close_open_structures():
        nonlocal in_list, in_table, table_header_done
        if in_list:
            html_out.append("</ul>")
            in_list = False
        if in_table:
            html_out.append("</tbody></table></div>")
            in_table = False
            table_header_done = False

    def transform_inline(text: str) -> str:
        # Escape HTML entities except existing safe markup
        s = html.escape(text)
        
        # Wikilinks: [[target]] or [[target|label]]
        def replace_wikilink(match: re.Match) -> str:
            raw = match.group(1).strip()
            if "|" in raw:
                target, label = raw.split("|", 1)
            else:
                target, label = raw, raw
            target_clean = target.strip()
            dest_url = slug_map.get(target_clean, f"{target_clean}.html")
            return f'<a class="wiki-link" href="{html.escape(dest_url)}">{html.escape(label.strip())}</a>'

        s = re.sub(r"\[\[([^\]]+)\]\]", replace_wikilink, s)

        # Standard Markdown links: [label](url)
        def replace_md_link(match: re.Match) -> str:
            label, url = match.group(1), match.group(2)
            # Rewrite relative .md links
            if url.endswith(".md"):
                url = url[:-3] + ".html"
            return f'<a href="{html.escape(url)}">{label}</a>'

        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_md_link, s)

        # Bold and Italic
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        
        # Inline code
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # HTML Comments / section markers
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            i += 1
            continue

        # Code block
        if stripped.startswith("```"):
            close_open_structures()
            if not in_code_block:
                in_code_block = True
                code_lang = stripped[3:].strip()
                code_lines = []
            else:
                in_code_block = False
                escaped_code = html.escape("\n".join(code_lines))
                html_out.append(f'<pre><code class="language-{html.escape(code_lang)}">{escaped_code}</code></pre>')
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Blank line
        if not stripped:
            close_open_structures()
            i += 1
            continue

        # Headings
        if stripped.startswith("#"):
            close_open_structures()
            level = len(stripped.split()[0])
            heading_text = stripped.lstrip("#").strip()
            anchor_id = re.sub(r"[^\w\-_]+", "-", heading_text.lower()).strip("-")
            if level in (2, 3):
                toc.append({"level": str(level), "id": anchor_id, "title": heading_text})
            html_out.append(f'<h{level} id="{html.escape(anchor_id)}">{transform_inline(heading_text)} <a class="anchor-link" href="#{html.escape(anchor_id)}" aria-hidden="true">#</a></h{level}>')
            i += 1
            continue

        # Callouts / Blockquotes (> [!NOTE], etc.)
        if stripped.startswith(">"):
            close_open_structures()
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            
            callout_type = "note"
            if quote_lines and quote_lines[0].startswith("[!"):
                m = re.match(r"^\[!([A-Z]+)\]", quote_lines[0])
                if m:
                    callout_type = m.group(1).lower()
                    quote_lines[0] = quote_lines[0][len(m.group(0)):].strip()
            
            content_html = "<br/>".join(transform_inline(ql) for ql in quote_lines if ql)
            html_out.append(f'<div class="callout callout-{callout_type}"><div class="callout-title">{callout_type.upper()}</div><div class="callout-body">{content_html}</div></div>')
            continue

        # Table row
        if "|" in stripped and (stripped.startswith("|") or stripped.endswith("|")):
            if in_list:
                html_out.append("</ul>")
                in_list = False
            
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            # Check if separator row
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                table_header_done = True
                i += 1
                continue
            
            if not in_table:
                in_table = True
                table_header_done = False
                html_out.append('<div class="table-container"><table>')
                html_out.append("<thead><tr>")
                for c in cells:
                    html_out.append(f"<th>{transform_inline(c)}</th>")
                html_out.append("</tr></thead><tbody>")
            else:
                html_out.append("<tr>")
                for c in cells:
                    html_out.append(f"<td>{transform_inline(c)}</td>")
                html_out.append("</tr>")
            i += 1
            continue

        # Unordered list item
        if stripped.startswith("- ") or stripped.startswith("* "):
            if in_table:
                close_open_structures()
            if not in_list:
                in_list = True
                html_out.append("<ul>")
            item_text = stripped[2:].strip()
            html_out.append(f"<li>{transform_inline(item_text)}</li>")
            i += 1
            continue

        # Paragraph
        close_open_structures()
        html_out.append(f"<p>{transform_inline(stripped)}</p>")
        i += 1

    close_open_structures()
    return "\n".join(html_out), toc


def build_site(output_dir: Path = DEFAULT_OUTPUT_DIR):
    print(f"Loading wiki pages from {REPO_ROOT}/wiki ...")
    pages = load_wiki_pages(REPO_ROOT)
    print(f"Loaded {len(pages)} pages.")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "concepts").mkdir(exist_ok=True)
    (output_dir / "entities").mkdir(exist_ok=True)
    (output_dir / "relations").mkdir(exist_ok=True)
    (output_dir / "sources").mkdir(exist_ok=True)

    # Build slug map and translation groups
    slug_map: dict[str, str] = {}
    groups: dict[str, dict[str, WikiPage]] = {}

    for page in pages:
        stem = page.path.stem
        rel_html = f"{page.path.parent.name}/{stem}.html" if page.path.parent.name in ("concepts", "entities", "relations", "sources") else f"{stem}.html"
        slug_map[stem] = rel_html
        
        group_id = page.translation_group
        if group_id not in groups:
            groups[group_id] = {}
        groups[group_id][page.language or "uk"] = page

    # Search index data
    search_index = []

    # Page template
    def render_full_page(page: WikiPage, content_html: str, toc: list[dict[str, str]]) -> str:
        lang = page.language or "uk"
        dict_i18n = I18N.get(lang, I18N["uk"])
        title = page.title
        group_peers = groups.get(page.translation_group, {})

        # Language switcher buttons
        lang_links = []
        for l in ("uk", "en", "ru"):
            if l in group_peers:
                peer_page = group_peers[l]
                peer_url = slug_to_url(peer_page.path.stem)
                if peer_page.path.parent.name in ("concepts", "entities", "relations", "sources"):
                    peer_url = f"{peer_page.path.parent.name}/{peer_page.path.stem}.html"
                active_cls = ' class="active"' if l == lang else ''
                lang_links.append(f'<a href="../{peer_url}"{active_cls}>{l.upper()}</a>')
            else:
                lang_links.append(f'<span class="disabled">{l.upper()}</span>')
        
        lang_switch_html = " ".join(lang_links)

        # TOC HTML
        toc_html = ""
        if toc:
            toc_items = "".join(f'<li class="toc-level-{t["level"]}"><a href="#{t["id"]}">{html.escape(t["title"])}</a></li>' for t in toc)
            toc_html = f'<nav class="page-toc"><h4>{dict_i18n["toc"]}</h4><ul>{toc_items}</ul></nav>'

        # Metadata badges
        meta_badges = []
        if page.metadata.get("page_role"):
            meta_badges.append(f'<span class="badge badge-role">{html.escape(str(page.metadata["page_role"]))}</span>')
        if page.metadata.get("semantic_version"):
            meta_badges.append(f'<span class="badge badge-version">v{html.escape(str(page.metadata["semantic_version"]))}</span>')
        if page.metadata.get("document_status"):
            meta_badges.append(f'<span class="badge badge-status">{html.escape(str(page.metadata["document_status"]))}</span>')

        meta_html = " ".join(meta_badges)

        depth = "../" if page.path.parent.name in ("concepts", "entities", "relations", "sources") else "./"

        return f"""<!doctype html>
<html lang="{lang}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title)} — {dict_i18n["site_title"]}</title>
    <meta name="theme-color" content="#74451f" />
    <link rel="manifest" href="{depth}../manifest.webmanifest" />
    <link rel="icon" href="{depth}../assets/icon.svg" type="image/svg+xml" />
    <link rel="apple-touch-icon" href="{depth}../assets/icon.svg" />
    <link rel="stylesheet" href="{depth}../assets/site.css" />
    <link rel="stylesheet" href="{depth}wiki.css" />
  </head>
  <body class="wiki-body">
    <header class="hero tests-hero">
      <nav class="nav" aria-label="Основна навігація">
        <a class="brand" href="{depth}../index.html"><span class="ichthys-mark" aria-label="ΙΧΘΥΣ">ΙΧΘΥΣ</span><b>Before We Build</b></a>
        <div class="nav-links">
          <a href="{depth}../index.html">{dict_i18n["tests"]}</a>
          <a href="{depth}../relations-calculator.html">{dict_i18n["calculator"]}</a>
          <a href="{depth}index.html" class="active">{dict_i18n["wiki"]}</a>
          <div class="lang-switch-peer">{lang_switch_html}</div>
        </div>
      </nav>
    </header>

    <div class="wiki-container">
      <aside class="wiki-sidebar">
        <div class="search-box">
          <input type="search" id="wikiSearchInput" placeholder="{dict_i18n["search_placeholder"]}" aria-label="Search" />
          <div id="searchResults" class="search-dropdown" hidden></div>
        </div>
        <div class="sidebar-nav">
          <a href="{depth}index.html" class="sidebar-hub-link">📚 {dict_i18n["home"]} Wiki</a>
          <div class="sidebar-section">
            <div class="sidebar-heading">{dict_i18n["categories"]["concepts"]}</div>
            <ul>
              <li><a href="{depth}concepts/latent-process-{lang}.html">Latent Process</a></li>
              <li><a href="{depth}concepts/four-levels-of-compatibility-{lang}.html">Four Levels</a></li>
              <li><a href="{depth}concepts/temporistics-temporal-orientations-{lang}.html">Temporistics</a></li>
              <li><a href="{depth}concepts/psychosophy-action-synthesis-{lang}.html">Psychosophy</a></li>
              <li><a href="{depth}concepts/socionics-reality-modeling-{lang}.html">Socionics</a></li>
            </ul>
          </div>
          <div class="sidebar-section">
            <div class="sidebar-heading">{dict_i18n["categories"]["glossary"]}</div>
            <ul>
              <li><a href="{depth}glossary-core-{lang}.html">Glossary Core</a></li>
              <li><a href="{depth}glossary-extended-{lang}.html">Glossary Extended</a></li>
            </ul>
          </div>
        </div>
      </aside>

      <main class="wiki-content">
        <article class="wiki-article">
          <header class="article-header">
            <div class="article-meta-top">{meta_html}</div>
            <h1>{html.escape(title)}</h1>
          </header>

          <div class="article-layout">
            <div class="article-body">
              {content_html}
            </div>
            {toc_html}
          </div>
        </article>
      </main>
    </div>

    <footer class="footer">
      <a href="{depth}../index.html">{dict_i18n["back_to_tests"]}</a> · Before We Build
    </footer>

    <script src="{depth}wiki-search.js"></script>
    <script>
      if ('serviceWorker' in navigator) {{
        window.addEventListener('load', () => {{
          navigator.serviceWorker.register('{depth}../sw.js');
        }});
      }}
    </script>
  </body>
</html>"""

    # Generate each page
    for page in pages:
        body_html, toc = render_markdown_to_html(page.body, page.language or "uk", slug_map)
        full_html = render_full_page(page, body_html, toc)
        
        target_path = output_dir / slug_map[page.path.stem]
        target_path.write_text(full_html, encoding="utf-8")

        # Add to search index
        search_index.append({
            "title": page.title,
            "url": slug_map[page.path.stem],
            "lang": page.language or "uk",
            "group": page.translation_group,
            "role": page.metadata.get("page_role", ""),
            "tags": page.metadata.get("tags", []),
        })

    # Write search index
    (output_dir / "search-index.json").write_text(json.dumps(search_index, ensure_ascii=False, indent=2), encoding="utf-8")

    # Generate Hub index.html for /wiki/
    index_uk_html = f"""<!doctype html>
<html lang="uk">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>База знань — Before We Build</title>
    <meta name="theme-color" content="#74451f" />
    <link rel="manifest" href="../manifest.webmanifest" />
    <link rel="icon" href="../assets/icon.svg" type="image/svg+xml" />
    <link rel="apple-touch-icon" href="../assets/icon.svg" />
    <link rel="stylesheet" href="../assets/site.css" />
    <link rel="stylesheet" href="wiki.css" />
  </head>
  <body class="wiki-body">
    <header class="hero tests-hero">
      <nav class="nav" aria-label="Основна навігація">
        <a class="brand" href="../index.html"><span class="ichthys-mark" aria-label="ΙΧΘΥΣ">ΙΧΘΥΣ</span><b>Before We Build</b></a>
        <div class="nav-links">
          <a href="../index.html">Тести</a>
          <a href="../relations-calculator.html">Калькулятор</a>
          <a href="index.html" class="active">База знань</a>
        </div>
      </nav>
    </header>

    <div class="wiki-hub-hero">
      <h1>База знань Before We Build</h1>
      <p class="lead">Дослідницький простір, онтологія 4 рівнів сумісності, розбір латентних процесів та практичні питання для діалогу пар.</p>
      <div class="search-box hub-search">
        <input type="search" id="wikiSearchInput" placeholder="Пошук по всій базі знань (поняття, типи, шкали)..." />
        <div id="searchResults" class="search-dropdown" hidden></div>
      </div>
    </div>

    <main class="wiki-hub-container">
      <div class="hub-grid">
        <div class="hub-card">
          <div class="hub-icon">🧭</div>
          <h2>4 Рівні сумісності</h2>
          <p>Ціннісно-моральний фундамент, Темпористика, Психософія та Соціоніка як моделі латентних процесів.</p>
          <a href="concepts/four-levels-of-compatibility-uk.html" class="hub-link">Читати розділ →</a>
        </div>

        <div class="hub-card">
          <div class="hub-icon">⏳</div>
          <h2>Темпористика</h2>
          <p>Сприйняття часу, синхронізація планів, бачення минулого, теперішнього, майбутнього та вічності.</p>
          <a href="concepts/temporistics-temporal-orientations-uk.html" class="hub-link">Читати розділ →</a>
        </div>

        <div class="hub-card">
          <div class="hub-icon">⚡</div>
          <h2>Психософія</h2>
          <p>Організація енергії та дій: Фізика, Логіка, Воля, Емоція. Ролі 1–4 позицій без ярликів.</p>
          <a href="concepts/psychosophy-action-synthesis-uk.html" class="hub-link">Читати розділ →</a>
        </div>

        <div class="hub-card">
          <div class="hub-icon">🧩</div>
          <h2>Соціоніка</h2>
          <p>Інформаційний фрейм та моделювання реальності. 8 операцій і позиційні ролі Моделі А.</p>
          <a href="concepts/socionics-reality-modeling-uk.html" class="hub-link">Читати розділ →</a>
        </div>

        <div class="hub-card">
          <div class="hub-icon">📖</div>
          <h2>Словник термінів</h2>
          <p>Точні визначення понять проекту для уникнення неоднозначностей і плутанини термінів.</p>
          <a href="glossary-core-uk.html" class="hub-link">Відкрити словник →</a>
        </div>

        <div class="hub-card">
          <div class="hub-icon">🤝</div>
          <h2>Відношення та пара</h2>
          <p>Аналіз ресурсів, зон тертя та питань для взаємної звірки в парі.</p>
          <a href="concepts/latent-process-uk.html" class="hub-link">Основи діалогу →</a>
        </div>
      </div>
    </main>

    <footer class="footer">
      <a href="../index.html">← До тестів Before We Build</a> · типові характери, не типи людини
    </footer>

    <script src="wiki-search.js"></script>
    <script>
      if ('serviceWorker' in navigator) {{
        window.addEventListener('load', () => {{
          navigator.serviceWorker.register('../sw.js');
        }});
      }}
    </script>
  </body>
</html>"""
    (output_dir / "index.html").write_text(index_uk_html, encoding="utf-8")
    (output_dir / "wiki.css").write_text(WIKI_CSS, encoding="utf-8")
    (output_dir / "wiki-search.js").write_text(WIKI_SEARCH_JS, encoding="utf-8")

    print(f"Successfully generated static wiki site in {output_dir}!")


WIKI_CSS = """
.wiki-body {
  background: var(--bg);
  color: var(--ink);
}

.wiki-container {
  display: flex;
  max-width: 1280px;
  margin: 0 auto;
  padding: 24px 16px;
  gap: 32px;
}

.wiki-sidebar {
  flex: 0 0 280px;
  position: sticky;
  top: 24px;
  height: calc(100vh - 48px);
  overflow-y: auto;
  padding-right: 16px;
  border-right: 1px solid var(--line);
}

.sidebar-heading {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
  margin: 18px 0 8px 0;
}

.sidebar-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar-nav li {
  margin-bottom: 6px;
}

.sidebar-nav a {
  color: var(--ink);
  text-decoration: none;
  font-size: 0.95rem;
  display: block;
  padding: 4px 8px;
  border-radius: 8px;
  transition: background 0.15s;
}

.sidebar-nav a:hover,
.sidebar-nav a.active {
  background: var(--surface-soft);
  color: var(--primary-dark);
}

.sidebar-hub-link {
  font-weight: 700;
  color: var(--primary);
  display: inline-block;
  margin-bottom: 12px;
}

.wiki-content {
  flex: 1;
  min-width: 0;
}

.wiki-article {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 36px 40px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
}

.article-header {
  border-bottom: 1px solid var(--line);
  padding-bottom: 20px;
  margin-bottom: 28px;
}

.article-header h1 {
  margin: 10px 0 0 0;
  font-size: 2.2rem;
  line-height: 1.25;
  color: var(--ink);
}

.badge {
  display: inline-block;
  padding: 3px 10px;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 999px;
  margin-right: 6px;
}

.badge-role { background: var(--surface-strong); color: var(--primary-dark); }
.badge-version { background: var(--surface-soft); color: var(--muted); }
.badge-status { background: #e0f2fe; color: #0369a1; }

.article-layout {
  display: flex;
  gap: 32px;
}

.article-body {
  flex: 1;
  min-width: 0;
  font-size: 1.05rem;
  line-height: 1.7;
}

.article-body h2 {
  font-size: 1.5rem;
  margin-top: 36px;
  margin-bottom: 14px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--line);
  color: var(--ink);
}

.article-body h3 {
  font-size: 1.25rem;
  margin-top: 24px;
  margin-bottom: 10px;
}

.anchor-link {
  opacity: 0;
  color: var(--muted);
  text-decoration: none;
  font-weight: normal;
  margin-left: 6px;
  transition: opacity 0.15s;
}

h2:hover .anchor-link,
h3:hover .anchor-link {
  opacity: 1;
}

.page-toc {
  flex: 0 0 220px;
  position: sticky;
  top: 32px;
  align-self: flex-start;
  font-size: 0.85rem;
  background: var(--surface-soft);
  padding: 16px;
  border-radius: var(--radius-md);
}

.page-toc h4 {
  margin: 0 0 10px 0;
  font-size: 0.9rem;
  color: var(--primary-dark);
}

.page-toc ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.page-toc li {
  margin-bottom: 6px;
}

.page-toc a {
  color: var(--muted);
  text-decoration: none;
}

.page-toc a:hover {
  color: var(--primary);
}

.toc-level-3 {
  padding-left: 12px;
}

.wiki-link {
  color: var(--primary);
  font-weight: 500;
  text-decoration: underline;
  text-decoration-thickness: 1px;
}

.wiki-link:hover {
  color: var(--primary-dark);
  text-decoration-thickness: 2px;
}

.callout {
  border-left: 4px solid var(--primary);
  background: var(--surface-soft);
  padding: 16px 20px;
  border-radius: 0 12px 12px 0;
  margin: 24px 0;
}

.callout-title {
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  color: var(--primary-dark);
  margin-bottom: 6px;
}

.table-container {
  overflow-x: auto;
  margin: 24px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

th, td {
  padding: 10px 14px;
  border: 1px solid var(--line);
  text-align: left;
}

th {
  background: var(--surface-soft);
  font-weight: 600;
}

.search-box {
  position: relative;
  margin-bottom: 20px;
}

.search-box input {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid var(--line);
  border-radius: 12px;
  font-size: 0.95rem;
  background: var(--surface);
  color: var(--ink);
  outline: none;
}

.search-box input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(116, 69, 31, 0.15);
}

.search-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: var(--shadow);
  max-height: 360px;
  overflow-y: auto;
  z-index: 100;
  margin-top: 6px;
}

.search-item {
  display: block;
  padding: 10px 14px;
  text-decoration: none;
  color: var(--ink);
  border-bottom: 1px solid var(--line);
  font-size: 0.9rem;
}

.search-item:hover {
  background: var(--surface-soft);
}

.search-item-title {
  font-weight: 600;
  color: var(--primary);
}

.wiki-hub-hero {
  max-width: 960px;
  margin: 40px auto 20px auto;
  text-align: center;
  padding: 0 16px;
}

.wiki-hub-hero h1 {
  font-size: 2.6rem;
  color: var(--ink);
  margin-bottom: 12px;
}

.hub-search {
  max-width: 540px;
  margin: 28px auto 0 auto;
}

.wiki-hub-container {
  max-width: 1080px;
  margin: 32px auto 64px auto;
  padding: 0 16px;
}

.hub-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.hub-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 28px;
  transition: transform 0.15s, box-shadow 0.15s;
  display: flex;
  flex-direction: column;
}

.hub-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow);
}

.hub-icon {
  font-size: 2.2rem;
  margin-bottom: 14px;
}

.hub-card h2 {
  font-size: 1.35rem;
  margin: 0 0 10px 0;
  color: var(--ink);
}

.hub-card p {
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.55;
  flex: 1;
}

.hub-link {
  font-weight: 600;
  color: var(--primary);
  text-decoration: none;
  margin-top: 14px;
  display: inline-block;
}

.lang-switch-peer {
  display: flex;
  gap: 6px;
  margin-left: 12px;
}

.lang-switch-peer a,
.lang-switch-peer span {
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  text-decoration: none;
}

.lang-switch-peer a {
  background: var(--surface-soft);
  color: var(--primary);
}

.lang-switch-peer a.active {
  background: var(--primary);
  color: #fff;
}

.lang-switch-peer .disabled {
  opacity: 0.3;
  color: var(--muted);
}

@media (max-width: 900px) {
  .wiki-container {
    flex-direction: column;
  }
  .wiki-sidebar {
    position: static;
    height: auto;
    border-right: none;
    border-bottom: 1px solid var(--line);
    padding-bottom: 20px;
  }
  .article-layout {
    flex-direction: column;
  }
  .page-toc {
    order: -1;
    position: static;
    width: 100%;
  }
  .wiki-article {
    padding: 24px 18px;
  }
}
"""

WIKI_SEARCH_JS = """
let searchIndex = null;

async function loadSearchIndex() {
  if (!searchIndex) {
    try {
      const depth = window.location.pathname.includes('/concepts/') ||
                    window.location.pathname.includes('/entities/') ||
                    window.location.pathname.includes('/relations/') ||
                    window.location.pathname.includes('/sources/') ? '../' : './';
      const res = await fetch(depth + 'search-index.json');
      searchIndex = await res.json();
    } catch (e) {
      console.warn('Failed to load search index', e);
    }
  }
  return searchIndex || [];
}

const input = document.getElementById('wikiSearchInput');
const resultsBox = document.getElementById('searchResults');

if (input && resultsBox) {
  input.addEventListener('input', async (e) => {
    const q = e.target.value.trim().toLowerCase();
    if (q.length < 2) {
      resultsBox.hidden = true;
      resultsBox.innerHTML = '';
      return;
    }

    const index = await loadSearchIndex();
    const depth = window.location.pathname.includes('/concepts/') ||
                  window.location.pathname.includes('/entities/') ||
                  window.location.pathname.includes('/relations/') ||
                  window.location.pathname.includes('/sources/') ? '../' : './';

    const matches = index.filter(item => {
      return item.title.toLowerCase().includes(q) ||
             (item.tags && item.tags.some(t => t.toLowerCase().includes(q))) ||
             item.group.toLowerCase().includes(q);
    }).slice(0, 10);

    if (matches.length === 0) {
      resultsBox.innerHTML = '<div class="search-item" style="color:var(--muted)">Нічого не знайдено / No results</div>';
      resultsBox.hidden = false;
      return;
    }

    resultsBox.innerHTML = matches.map(item => `
      <a href="${depth}${item.url}" class="search-item">
        <div class="search-item-title">${item.title}</div>
        <div style="font-size:0.75rem; color:var(--muted)">[${item.lang.toUpperCase()}] ${item.group}</div>
      </a>
    `).join('');
    resultsBox.hidden = false;
  });

  document.addEventListener('click', (e) => {
    if (!input.contains(e.target) && !resultsBox.contains(e.target)) {
      resultsBox.hidden = true;
    }
  });
}
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build static HTML wiki site.")
    parser.add_argument("--output", "-o", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory for generated HTML site")
    args = parser.parse_args()
    build_site(output_dir=args.output)
