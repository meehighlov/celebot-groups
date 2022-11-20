from functools import wraps

from telegram import Update
from telegram.ext import CallbackContext

from app.logger import log

# TODO add more type hints


def handle_any_error(handler):
    @wraps
    def error_handler(update: Update, context: CallbackContext, *args, **kwargs):
        try:
            return handler(update, context, *args, **kwargs)
        except Exception as e:
            exc_text = str(e)
            try:
                context.bot.send_message(
                    chat_id=update.message.chat_id,
                    text="Ooops, there is a problem occured, i'm working on it 😅"
                )
            except Exception as sending_exc:
                exc_text += '\nwarning message was not sent due to: {sending_exc}'

            log(exc_text)

    return error_handler
