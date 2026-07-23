from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_FOLDER = BASE_DIR / "sample_files"
DESTINATION_FOLDER = BASE_DIR / "output"
LOG_FOLDER = BASE_DIR / "logs"

FILE_TYPES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".mp3": "Music",
    ".wav": "Music",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".zip": "Archives",
    ".rar": "Archives"
}