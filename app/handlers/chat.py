from telegram import Update
from telegram.ext import CallbackContext

from database.ext.users import get_all_users
from app.auth import auth


@auth(set_user=False)
def handle(update: Update, context: CallbackContext):
    message = []
    for user in get_all_users():
        message.append(
            f'{user.name} {user.tgusername} {user.birthday}'
        )

    message = '\n'.join(message)
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
