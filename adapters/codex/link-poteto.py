#!/usr/bin/env python3
"""Link only Poteto Mode into Codex; leave every other skill entry alone."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
library = Path(__file__).resolve().parents[2]
source = library / "skills/also/poteto-mode"
destination = Path.home() / ".codex/skills/poteto-mode"
if not (source / "SKILL.md").is_file():
    parser.error("canonical Poteto Mode is missing")
if destination.is_symlink() and destination.resolve() == source.resolve():
    print(f"unchanged: {destination} -> {source}")
elif destination.exists() or destination.is_symlink():
    parser.error(f"refusing to replace existing entry: {destination}")
else:
    if not args.dry_run:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.symlink_to(source, target_is_directory=True)
    print(f"{'would create' if args.dry_run else 'created'}: {destination} -> {source}")
