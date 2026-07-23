import logging
from app.config import LOG_FOLDER

LOG_FOLDER.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FOLDER / "app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)