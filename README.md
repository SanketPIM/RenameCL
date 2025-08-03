# RenameCL

A command-line tool to batch rename files, undo renames, and find/delete duplicate files. Built with Python and [Typer](https://typer.tiangolo.com).

##  Features

-  Batch rename files with prefix/suffix/custom extension
-  Auto-increment file numbering
-  Dry-run mode for previewing changes
- ↩ Undo last renaming using a log file
-  Detect and optionally delete duplicate files (based on SHA-256 hash)
-  Target specific files with `--filter` option

---

##  Installation

1. Make sure Python is installed:
```bash
python --version
```

2. Install Typer (and dependencies):
```bash
pip install typer[all]
```

---

## 🛠 Usage

###  Rename Files

```bash
python Rename.py rename --folder "D:\your\folder" --prefix "img_" --ext jpg
```

####  Optional Flags

| Flag         | Description |
|--------------|-------------|
| `--prefix`   | Add text before the filename |
| `--suffix`   | Add text after the filename *(ignored if `--auto-number` is on)* |
| `--ext`      | Change file extension (e.g., jpg, png) |
| `--auto-number` | Add `_1`, `_2`, etc. to filenames |
| `--start`    | Starting number for auto-numbering |
| `--dry-run`  | Preview changes without renaming |
| `--filter`   | Only rename selected files (comma-separated) |

####  Example

```bash
python Rename.py rename --folder "D:\photos" --prefix "holiday_" --ext jpg --auto-number True --start 10
```

####  Rename only specific files

```bash
python Rename.py rename --folder "D:\myfiles" --prefix "new_" --ext jpg --filter "img1.jpg,img3.jpg,img7.jpg"
```

---

### 🔙 Undo Last Rename

```bash
python Rename.py undo
```

Uses `rename_log.json` to restore original file names.

---

###  Find Duplicate Files

```bash
python Rename.py find-duplicates --folder "D:\folder"
```

To delete them automatically:

```bash
python Rename.py find-duplicates --folder "D:\folder" --delete --dry-run False
```

---

##  Output Logs

- All rename operations are logged in `rename_log.json`
- The `undo` command uses this file to revert changes

---

##  Tips

- Always use `--dry-run` first to preview changes safely.
- Works across drives (C:, D:, etc.) — just make sure the file paths are correct.
- `--filter` is helpful when only a few files need changes in a large folder.

---

##  License

MIT

##  Powered By

[Typer](https://github.com/tiangolo/typer) - Build great CLIs. Easy to code. Based on Python type hints.
