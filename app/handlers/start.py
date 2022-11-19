from telegram import Update
from telegram.ext import CallbackContext

from app.enums import StaticMessages


def handle(update: Update, context: CallbackContext):
    message = StaticMessages.HELLO_MESSAGE
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
