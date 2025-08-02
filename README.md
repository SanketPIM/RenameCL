
<p align="center">
  <img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg#only-light" alt="Typer" width="180">
</p>

<p align="center">
  <strong>RenameCL</strong> – A powerful CLI tool to batch rename files, undo changes, and find/delete duplicates.<br>
  Built with Python and Typer.
</p>

<p align="center">
  <a href="https://github.com/SanketPIM/RenameCL">
    <img src="https://img.shields.io/github/license/SanketPIM/RenameCL" alt="License">
  </a>
  <a href="https://pypi.org/project/typer/">
    <img src="https://img.shields.io/pypi/v/typer?label=Typer&color=34D058" alt="Typer Version">
  </a>
</p>

---

##  Features

-  Batch rename files with prefix, suffix, and custom extension
-  Auto-increment file numbering (`_1`, `_2`, ...)
-  Dry-run mode to preview changes without renaming
-  Undo renames using a log file
-  Detect and optionally delete duplicate files (by content hash)

---

##  Installation

### 1. Make sure Python is installed

```bash
python --version
```

### 2. Install dependencies

```bash
pip install typer[all]
```

---

##  Usage

> Use the `python Rename.py` command with one of the following subcommands:

---

### 🔁 `rename` – Rename Files

```bash
python Rename.py rename --folder "E:\photos" --prefix "img_" --ext jpg
```

#### Options:

| Flag            | Description                                             |
|-----------------|---------------------------------------------------------|
| `--prefix`      | Text to add **before** the filename                     |
| `--suffix`      | Text to add **after** the filename (ignored if `--auto-number` is used) |
| `--ext`         | Change file extension (e.g. `jpg`, `txt`)               |
| `--auto-number` | Auto-add numbers like `_1`, `_2`, etc. (default: true)  |
| `--start`       | Starting number for auto-number (default: 1)           |
| `--dry-run`     | Show what will happen without actually renaming files  |

#### Example:

```bash
python Rename.py rename --folder "E:\docs" --prefix "file_" --ext txt --auto-number False --suffix "_final"
```

---

### ↩️ `undo` – Undo Last Rename

```bash
python Rename.py undo
```

- Restores original filenames based on the saved `rename_log.json`.

---

###  `find-duplicates` – Find Duplicate Files

```bash
python Rename.py find-duplicates --folder "E:\myfiles"
```

#### Additional Options:

| Flag         | Description                          |
|--------------|--------------------------------------|
| `--dry-run`  | Only preview duplicates (default: True) |
| `--delete`   | Actually delete duplicates           |

#### Example:

```bash
python Rename.py find-duplicates --folder "E:\myfiles" --delete --dry-run False
```

---

##  Logging

- All rename operations are logged in `rename_log.json`.
- The `undo` command uses this log to restore files to their original names.

---

##  How Duplicate Detection Works

This tool uses `hashlib` with the **SHA-256** algorithm to generate a unique fingerprint of each file’s content. If two files have the same hash, they are duplicates — even if their names differ.

---

##  Best Practices

-  Use `--dry-run` before making permanent changes
-  Backup important files before running delete operations
-  Test in a safe folder first to understand behavior

---

##  License

This project is licensed under the MIT License.

---

##  Author

**SanketPIM**  
GitHub: [https://github.com/SanketPIM](https://github.com/SanketPIM)

---

##  Contributing

Pull requests and suggestions are welcome! If you find bugs or want new features, open an issue or PR.
