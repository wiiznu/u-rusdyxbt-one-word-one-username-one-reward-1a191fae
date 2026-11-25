"""Write only this entry's username to the make.fun output file."""

from pathlib import Path
import shutil


OUTPUT_DIR = Path("/output")
ENTRY_FILE = OUTPUT_DIR / "entry.txt"
USERNAME = "wiiznu-bondet"


def clear_output_contents(directory: Path) -> None:
    """Remove output items while leaving the output directory in place."""
    for item in directory.iterdir():
        if item.is_dir() and not item.is_symlink():
            shutil.rmtree(item)
        else:
            item.unlink()


def main() -> None:
    # The runner may reuse an output directory, so start with it empty.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    clear_output_contents(OUTPUT_DIR)
    ENTRY_FILE.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
