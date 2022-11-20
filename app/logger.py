import logging

from app.config import config


logging.basicConfig(filename=config.LOG_FILE, encoding='utf-8', level=logging.DEBUG)


def log(message: str, level=logging.ERROR):
    logging.log(message, level=level)
