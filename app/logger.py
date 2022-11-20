import logging

from app.config import config


def init_logging():
    logging.basicConfig(
        filename=config.LOG_FILE,
        encoding='utf-8',
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
