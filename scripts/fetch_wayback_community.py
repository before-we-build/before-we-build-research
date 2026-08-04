#!/usr/bin/env python3
"""
fetch_wayback_community.py - Wayback Machine CDX Extractor for Typology Archives

Extracts historical thread and article content from Wayback Machine archives for
defunct or blocked typology communities (Temporistics, Psychosophy, Socionics).
Saves raw JSON dumps and Markdown source summaries into `raw/<typology>/community-sources/`.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

class HTMLTextExtractor(HTMLParser):
    """Simple HTML to clean plain text extractor."""
    def __init__(self):
        super().__init__()
        self.result = []
        self.ignore_tags = {'script', 'style', 'head', 'title', 'meta', '[document]'}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag.lower()

    def handle_endtag(self, tag):
        if self.current_tag == tag.lower():
            self.current_tag = None

    def handle_data(self, data):
        if self.current_tag not in self.ignore_tags:
            text = data.strip()
            if text:
                self.result.append(text)

    def get_text(self):
        return "\n".join(self.result)

def fetch_cdx_urls(domain: str, limit: int = 50) -> list:
    """Fetch list of archived URLs for domain via Wayback CDX API."""
    cdx_url = (
        f"http://web.archive.org/cdx/search/cdx?url={domain}&matchType=domain"
        f"&output=json&fl=timestamp,original,mimetype,statuscode&filter=mimetype:text/html"
        f"&filter=statuscode:200&collapse=urlkey&limit={limit}"
    )
    req = urllib.request.Request(
        cdx_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if not data or len(data) <= 1:
                return []
            records = []
            for row in data[1:]:
                records.append({
                    "timestamp": row[0],
                    "original_url": row[1],
                    "mimetype": row[2],
                    "statuscode": row[3]
                })
            return records
    except Exception as e:
        print(f"[!] CDX API request failed for {domain}: {e}", file=sys.stderr)
        return []

def fetch_archive_snapshot(timestamp: str, original_url: str) -> str:
    """Fetch raw HTML snapshot from Wayback raw endpoint (id_)."""
    raw_archive_url = f"https://web.archive.org/web/{timestamp}id_/{original_url}"
    req = urllib.request.Request(
        raw_archive_url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw_bytes = resp.read()
            # Detect character encoding: try utf-8 first, fallback to windows-1251
            try:
                decoded = raw_bytes.decode("utf-8")
                if "" not in decoded:
                    return decoded
            except UnicodeDecodeError:
                pass
            
            # Legacy Russian forums (idealist.ru, socionik.com, etc.) used windows-1251
            try:
                return raw_bytes.decode("windows-1251")
            except UnicodeDecodeError:
                return raw_bytes.decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  [!] Failed fetching archive snapshot {raw_archive_url}: {e}", file=sys.stderr)
        return ""

def clean_html_to_markdown(html_content: str, title: str, original_url: str, timestamp: str) -> str:
    """Extract readable text from HTML snapshot and format as clean Markdown."""
    parser = HTMLTextExtractor()
    parser.feed(html_content)
    extracted_text = parser.get_text()

    md = f"""# {title}

> **Source URL:** `{original_url}`  
> **Archived Timestamp:** `{timestamp}`  
> **Extraction Date:** `{time.strftime('%Y-%m-%d')}`  

---

## Content

{extracted_text}
"""
    return md

def main():
    parser = argparse.ArgumentParser(description="Fetch community archives from Wayback Machine CDX API.")
    parser.add_argument("--target-domain", required=True, help="Target domain (e.g. temporistics.ru, socionik.com)")
    parser.add_argument("--typology", required=True, choices=["temporistics", "psychosophy", "socionics", "general"])
    parser.add_argument("--limit", type=int, default=20, help="Maximum snapshots to fetch")
    args = parser.parse_args()

    output_dir = Path(f"raw/{args.typology}/community-sources/{args.target_domain.replace('.', '_')}")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[*] Querying CDX for {args.target_domain} (limit: {args.limit})...")
    records = fetch_cdx_urls(args.target_domain, limit=args.limit)
    print(f"[✓] Found {len(records)} archived HTML URLs.")

    saved_count = 0
    for idx, rec in enumerate(records, 1):
        ts = rec["timestamp"]
        url = rec["original_url"]
        print(f"[{idx}/{len(records)}] Extracting: {url} ({ts})")

        html = fetch_archive_snapshot(ts, url)
        if not html:
            continue

        slug = re.sub(r'[^a-zA-Z0-9_-]', '_', url.replace('http://', '').replace('https://', ''))[:80]
        file_base = f"{ts}_{slug}"
        
        # Save raw JSON metadata + HTML
        dump_data = {
            "timestamp": ts,
            "original_url": url,
            "target_domain": args.target_domain,
            "typology": args.typology,
            "html_length": len(html),
            "html_content": html
        }
        json_path = output_dir / f"{file_base}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(dump_data, f, ensure_ascii=False, indent=2)

        # Save Markdown extracted summary
        md_text = clean_html_to_markdown(html, f"Archived Snapshot: {slug}", url, ts)
        md_path = output_dir / f"{file_base}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)

        saved_count += 1
        time.sleep(0.3)

    print(f"\n[✓] Ingestion complete. Saved {saved_count} raw dumps to {output_dir}")

if __name__ == "__main__":
    main()
