from pathlib import Path
import shutil

from app.config import SOURCE_FOLDER
from app.config import DESTINATION_FOLDER
from app.config import FILE_TYPES

from app.logger import logger
from app.utils import create_folder


class FileOrganizer:

    def organize(self):

        if not SOURCE_FOLDER.exists():
            raise FileNotFoundError(
                f"{SOURCE_FOLDER} not found"
            )

        files = list(SOURCE_FOLDER.iterdir())

        logger.info(f"Found {len(files)} files")

        for file in files:

            if not file.is_file():
                continue

            category = FILE_TYPES.get(
                file.suffix.lower(),
                "Others"
            )

            destination = DESTINATION_FOLDER / category

            create_folder(destination)

            shutil.move(
                str(file),
                destination / file.name
            )

            logger.info(
                f"Moved {file.name} -> {category}"
            )

            print(
                f"✔ {file.name} → {category}"
            )

        logger.info("Finished")