from telegram import Update
from telegram.ext import CallbackContext

from database.ext.users import get_user_by_id, delete_user_by_id


def handle(update: Update, context: CallbackContext):
    message = "I'm sorry, there is something i still can't do. I'm gonna be better soon!😅"
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
