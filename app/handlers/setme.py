from telegram import Update
from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)
from app.config import config
from database.ext.users import get_user_by_id, save_user

from app.enums import CommandSetmeStates

from app.auth import auth


@auth(set_user=False)
def handle_entry_point(update: Update, context: CallbackContext) -> int:
    message = "Send me your birthday in format: dd.mm, for example 03.01"
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
    return CommandSetmeStates.SET


def handle_success(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    user = get_user_by_id(user_id)
    user.birthday = update.message.text
    save_user(**user.as_dict())
    message = "Cool, i've saved your birthday 😊"
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
    return ConversationHandler.END


def fallback(update: Update, context: CallbackContext) -> int:
    message = "Hmm, i guess there is a typo, try again please"
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
    return ConversationHandler.SET


handle = ConversationHandler(
    entry_points=[CommandHandler('setme', handle_entry_point)],
    states={
        CommandSetmeStates.SET: [MessageHandler(Filters.regex("^\d\d\.\d\d$"), handle_success)],
    },
    fallbacks=[MessageHandler(Filters.text, fallback)],
    allow_reentry=True,
    conversation_timeout=config.CONVERSATION_TIMEOUT,
)
