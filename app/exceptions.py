import logging
import traceback
import json
from functools import wraps

from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from app.config import config

# TODO add more type hints

logger = logging.getLogger(__name__)


class CelebotError(Exception):
    pass


class UserNotFoundError(CelebotError):
    pass


def error_handler(update: Update, context: CallbackContext):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = json.dumps(update_str, indent=2, ensure_ascii=False) + ' with treaceback: ' + tb_string

    logger.error(message)

    try:
        context.bot.send_message(chat_id=config.MY_CHAT_ID, text=message)
    except Exception as e:
        logger.error('failed to send error info due to: ' + str(e))
