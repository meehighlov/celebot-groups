from telegram import Update
from telegram.ext import CallbackContext

from app.auth import auth
from app.exceptions import handle_any_error
from database.models import User


@handle_any_error
@auth(set_user=True)
def handle(update: Update, context: CallbackContext, user: User):
    birth_day = user.birth_day
    message = "Your birthday is not set 🥴 use /setme to set it"
    if birth_day is not None:
        message = f"Your birthday is {birth_day}"

    context.bot.send_message(chat_id=update.message.chat_id, text=message)
