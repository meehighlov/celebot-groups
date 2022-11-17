from functools import wraps

from telegram import Update
from telegram.ext import  CallbackContext

from config import config
from database.ext.users import get_user_by_id


def is_auth_user(user_id: int) -> bool:
    user = get_user_by_id(user_id)
    return user is not None


def auth(set_user=False):

    def auth_handling(handler):

        @wraps(handler)
        def check_username(update: Update, context: CallbackContext, *args, **kwargs):

            user_id = update.message.from_user.id
            user = get_user_by_id(user_id)

            if not user:
                return

            if set_user:
                return handler(update, context, user=user)

            return handler(update, context)

        return check_username

    return auth_handling
