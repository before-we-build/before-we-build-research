#!/usr/bin/env python3
"""
Wiki link checker - validates wikilinks in markdown files.

Usage: python scripts/check_wikilinks.py
"""

import re
import os
from pathlib import Path
from typing import Set, List, Tuple


WIKI_DIR = Path(__file__).parent.parent / "wiki"
MARKDOWN_EXTENSIONS = {".md", ".markdown"}


def find_wiki_files(directory: Path) -> List[Path]:
    """Find all markdown files in wiki directory."""
    files = []
    for ext in MARKDOWN_EXTENSIONS:
        files.extend(directory.rglob(f"*{ext}"))
    return sorted(files)


def extract_wikilinks(content: str) -> Set[str]:
    """Extract all [[wikilinks]] from content."""
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    return set(matches)


def wikilink_to_filename(wikilink: str) -> str:
    """Convert wikilink to expected filename."""
    # Handle aliases like [[page|label]]
    if "|" in wikilink:
        wikilink = wikilink.split("|", 1)[0]

    # Handle anchors like [[page#section]]
    if "#" in wikilink:
        wikilink = wikilink.split("#", 1)[0]
    
    # Convert to kebab-case (lowercase with hyphens)
    # Example: "Socionics Model A" -> "socionics-model-a.md"
    filename = wikilink.lower().replace(" ", "-") + ".md"
    return filename


def check_wikilinks(verbose: bool = False) -> Tuple[List[str], List[str]]:
    """
    Check all wikilinks in wiki directory.
    
    Returns:
        Tuple of (errors, warnings)
    """
    errors = []
    warnings = []
    
    files = find_wiki_files(WIKI_DIR)
    existing_files = {f.name.lower() for f in files}
    
    all_links: Set[str] = set()
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        links = extract_wikilinks(content)
        all_links.update(links)
        
        for link in links:
            expected_filename = wikilink_to_filename(link)
            
            # Check exact match
            if expected_filename.lower() in existing_files:
                continue
            
            # Check if any file contains the link (case-insensitive)
            found = False
            for existing in existing_files:
                if existing.lower() == expected_filename.lower():
                    found = True
                    if verbose:
                        warnings.append(f"{filepath.relative_to(WIKI_DIR)}: '{link}' -> '{expected_filename}' (case differs)")
                    break
            
            if not found:
                errors.append(f"{filepath.relative_to(WIKI_DIR)}: Missing '[[{link}]]' -> {expected_filename}")
    
    return errors, warnings


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Check wikilinks in wiki")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show warnings")
    args = parser.parse_args()
    
    print("Checking wikilinks in wiki/ ...")
    print()
    
    errors, warnings = check_wikilinks(verbose=args.verbose)
    
    if errors:
        print(f"❌ {len(errors)} ERROR(S):")
        for error in errors:
            print(f"  {error}")
        print()
    
    if warnings:
        print(f"⚠️  {len(warnings)} WARNING(S):")
        for warning in warnings:
            print(f"  {warning}")
        print()
    
    if not errors and not warnings:
        print("✅ All wikilinks are valid!")
    elif not errors:
        print("✅ No errors, but some warnings above.")
    else:
        print("❌ Check failed. Fix errors above.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
