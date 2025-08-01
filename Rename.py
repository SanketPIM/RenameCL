
import os
import typer
import hashlib
import json
from typing import Optional

app = typer.Typer()

LOG_FILE = "rename_log.json"

@app.command()
def rename(
    folder: str = typer.Option(..., help="Folder path containing the files"),
    prefix: Optional[str] = typer.Option("", help="Prefix to add to file names"),
    suffix: Optional[str] = typer.Option("", help="Suffix to add to file names (ignored if auto-numbering)"),
    ext: Optional[str] = typer.Option(None, help="New extension to apply (e.g., jpg)"),
    dry_run: bool = typer.Option(False, help="Preview changes without renaming files"),
    auto_number: bool = typer.Option(True, help="Add an auto-incrementing number as suffix"),
    start: int = typer.Option(1, help="Starting number for auto-increment suffix")
):
    """Batch rename files in a folder with prefix/suffix/extension."""
    if not os.path.isdir(folder):
        typer.echo(f" Folder '{folder}' does not exist.")
        raise typer.Exit()

    files = sorted(os.listdir(folder))
    typer.echo(f" Found {len(files)} items in '{folder}'")

    renamed_count = 0
    changes = {}

    for index, file in enumerate(files, start=start):
        old_path = os.path.join(folder, file)

        if not os.path.isfile(old_path):
            continue  # Skip directories

        name, old_ext = os.path.splitext(file)
        new_ext = f".{ext}" if ext else old_ext
        current_suffix = f"_{index}" if auto_number else suffix
        new_name = f"{prefix}{name}{current_suffix}{new_ext}"
        new_path = os.path.join(folder, new_name)

        if dry_run:
            typer.echo(f" {file} → {new_name}")
        else:
            os.rename(old_path, new_path)
            changes[new_path] = old_path
            typer.echo(f" Renamed: {file} → {new_name}")
            renamed_count += 1

    if not dry_run:
        typer.echo(f"\n Done! Renamed {renamed_count} files.")
        with open(LOG_FILE, "w") as log:
            json.dump(changes, log, indent=2)

@app.command()
def undo(log_path: str = typer.Option(LOG_FILE, help="Path to the rename log file")):
    """Undo the last renaming operation using the rename log."""
    if not os.path.exists(log_path):
        typer.echo(" Rename log not found.")
        raise typer.Exit()

    with open(log_path, "r") as f:
        changes = json.load(f)

    for new_path, old_path in changes.items():
        if os.path.exists(new_path):
            os.rename(new_path, old_path)
            typer.echo(f" Restored: {new_path} → {old_path}")
        else:
            typer.echo(f" File missing: {new_path}")

    typer.echo("\n Undo complete.")

@app.command()
def find_duplicates(
    folder: str = typer.Option(..., help="Folder to search for duplicates"),
    dry_run: bool = typer.Option(True, help="Preview duplicates without deleting"),
    delete: bool = typer.Option(False, help="Delete duplicate files")
):
    """Find and optionally delete duplicate files by content."""
    if not os.path.isdir(folder):
        typer.echo(" Folder not found.")
        raise typer.Exit()

    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(path):
                with open(path, 'rb') as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()

                if file_hash in hashes:
                    duplicates.append(path)
                    if not dry_run and delete:
                        os.remove(path)
                        typer.echo(f" Deleted duplicate: {path}")
                else:
                    hashes[file_hash] = path

    if dry_run:
        typer.echo("\n Duplicate Files Found:")
        for dup in duplicates:
            typer.echo(f"Duplicate: {dup}")

    typer.echo(f"\n Duplicate check complete. Found {len(duplicates)} duplicates.")

if __name__ == "__main__":
    app()
