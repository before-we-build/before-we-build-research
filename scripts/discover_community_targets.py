#!/usr/bin/env python3
"""
discover_community_targets.py - Typology Community Target Catalog & Wayback CDX Auditor

This script maintains a structured target inventory of Socionics, Psychosophy,
and Temporistics community websites, forums, and archives. It queries the Archive.org
CDX API to inspect available snapshots for defunct or geo-restricted sites.
"""

import json
import urllib.parse
import urllib.request
import sys
from pathlib import Path

TARGETS = [
    {
        "id": "temporistics-ru",
        "name": "Temporistics.ru (Primary Source Archive)",
        "typology": "temporistics",
        "domain": "temporistics.ru",
        "url": "http://temporistics.ru/",
        "level": "strategic",
        "frame_type": "temporal",
        "status": "archive-priority",
        "description": "Original articles and forum discussions on temporal aspects (P, N, F, E) by Latyshev / Sherman."
    },
    {
        "id": "sherman-lj",
        "name": "Nika Sherman LiveJournal",
        "typology": "temporistics",
        "domain": "sherman.livejournal.com",
        "url": "https://sherman.livejournal.com/",
        "level": "strategic",
        "frame_type": "temporal",
        "status": "archive-priority",
        "description": "Foundational discussions on temporistics and psychosophy phenomenology."
    },
    {
        "id": "socionik-com",
        "name": "Socionik.com Legacy Forum",
        "typology": "socionics",
        "domain": "socionik.com",
        "url": "http://socionik.com/",
        "level": "tactical",
        "frame_type": "information",
        "status": "archive-priority",
        "description": "One of the earliest socionics web portals with extensive user typing threads and articles."
    },
    {
        "id": "idealist-ru",
        "name": "Idealist.ru Socionics Portal",
        "typology": "socionics",
        "domain": "idealist.ru",
        "url": "http://idealist.ru/socionix/",
        "level": "tactical",
        "frame_type": "information",
        "status": "archive-priority",
        "description": "Historical socionics articles, intertype relation matrices, and function descriptions."
    },
    {
        "id": "socioforum-su",
        "name": "Socioforum.su (Socionics & Psychosophy Boards)",
        "typology": "general",
        "domain": "socioforum.su",
        "url": "https://socioforum.su/",
        "level": "tactical-and-operational",
        "frame_type": "information-and-action",
        "status": "active-or-blocked",
        "description": "Largest Russian-language typology forum spanning 20+ years of user discussions."
    },
    {
        "id": "24types-ru",
        "name": "24types.ru (Psychosophy Portal)",
        "typology": "psychosophy",
        "domain": "24types.ru",
        "url": "http://24types.ru/",
        "level": "operational",
        "frame_type": "action",
        "status": "archive-priority",
        "description": "Psychosophy function descriptions, accentuations, and compatibility discussions."
    },
    {
        "id": "systema-socionicas",
        "name": "School of System Socionics (SSS)",
        "typology": "socionics",
        "domain": "systema-socionicas.org",
        "url": "http://systema-socionicas.org/",
        "level": "tactical",
        "frame_type": "information",
        "status": "archive-priority",
        "description": "Dimensional functions (1D-4D), signs, and systemic information metabolism protocols by Eglit."
    }
]

def check_cdx_snapshot_count(domain: str) -> int:
    """Query Wayback Machine CDX API for total archived URLs under domain."""
    cdx_url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&fl=original&collapse=urlkey&limit=500"
    req = urllib.request.Request(
        cdx_url, 
        headers={"User-Agent": "BeforeWeBuild-ResearchBot/1.0 (+https://github.com/before-we-build)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            # Subtract 1 for the header line if present
            return max(0, len(data) - 1)
    except Exception as e:
        print(f"  [!] Failed CDX query for {domain}: {e}", file=sys.stderr)
        return -1

def main():
    print("==========================================================")
    print(" BEFORE WE BUILD - Typology Community Target Auditor")
    print("==========================================================\n")
    
    catalog_path = Path("raw/community_target_catalog.json")
    catalog_path.parent.mkdir(parents=True, exist_ok=True)

    audited_targets = []

    for t in TARGETS:
        print(f"[*] Auditing target: {t['name']} ({t['domain']})")
        snapshots_count = check_cdx_snapshot_count(t["domain"])
        t["cdx_unique_urls_count"] = snapshots_count
        audited_targets.append(t)
        print(f"    - Type: {t['typology'].upper()} | Level: {t['level']}")
        print(f"    - Wayback CDX unique URLs found: {snapshots_count}\n")

    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(audited_targets, f, ensure_ascii=False, indent=2)

    print(f"[✓] Saved community catalog to {catalog_path}")

if __name__ == "__main__":
    main()
