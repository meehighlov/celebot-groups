from telegram import Update
from telegram.ext import CallbackContext
from app.exceptions import handle_any_error

from database.ext.users import get_user_by_id


def command_list_for_auth_user() -> list[str]:
    return [
        '/me - show your birthday',
        '/setme - set your birthday',
        '/code - pass access code',
    ]


def command_list_for_not_auth_user() -> list[str]:
    return [
        '/code - pass access code',
    ]


def command_list_for_admin() -> list[str]:
    return [
        '/me - show your birthday',
        '/setme - set your birthday',
        '/code - pass access code',
        '/chat - show all birthdays in chat',
    ]


@handle_any_error
def handle(update: Update, context: CallbackContext):
    user_id: int = update.message.from_user.id
    user = get_user_by_id(user_id)
    message = '\n'.join(command_list_for_not_auth_user())
    if user:
        message = '\n'.join(command_list_for_auth_user())
        if user.is_admin:
            message = '\n'.join(command_list_for_admin())

    context.bot.send_message(chat_id=update.message.chat_id, text=message)
