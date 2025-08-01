
#  File Renamer Tool (with Undo & Duplicate Finder)

A powerful and flexible CLI tool for renaming, undoing, and managing files using [Typer](https://typer.tiangolo.com/).

Features

-  Batch rename files with prefix/suffix/custom extension
-  Auto-increment file numbering (optional)
-  Dry-run mode to preview changes
-  Undo last renaming with a single command
-  Detect and optionally delete duplicate files by content (hash-based)

Installation

1. Make sure Python is installed:
bash
python --version

2. Install `typer`:
bash
pip install typer[all]

How to Use
1. Rename Files
bash
python Rename.py rename --folder "E:\your\folder" --prefix "img_" --ext jpg

Optional Flags:
| Flag | Description |
|------|-------------|
| `--prefix`      | Add text before the filename |
| `--suffix`      | Add text after the filename (ignored if `--auto-number` is on) |
| `--ext`         | Change file extension (e.g., jpg, txt) |
| `--auto-number` | Add `_1`, `_2`, ... after filenames |
| `--start`       | Starting number for `--auto-number` |
| `--dry-run`     | Preview changes without renaming |

Example:
bash
python Rename.py rename --folder "E:\photos" --prefix "holiday_" --ext jpg --dry-run

2. Undo Last Rename
bash
python Rename.py undo

> Uses the last `rename_log.json` to restore original file names.

3. Find Duplicate Files
bash
python Rename.py find-duplicates --folder "E:\folder"

Optional:
To delete them automatically:
bash
python Rename.py find-duplicates --folder "E:\folder" --delete --dry-run False

Output Logs
- Rename operations are stored in `rename_log.json`
- Undo command uses this to revert

Test It Safely

Always use `--dry-run` first to make sure everything looks correct!
