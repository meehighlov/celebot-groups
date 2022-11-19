from telegram import Update, ForceReply
from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)
from app.config import config
from database.ext.users import save_user

from app.enums import CommandCodeStates


def handle_entry_point(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text='Enter access code',
    )

    return CommandCodeStates.CHECK


def fallback(update: Update, context: CallbackContext) -> int:
    message = 'Incorrect code 🙂'
    context.bot.send_message(chat_id=update.message.chat_id, text=message)
    
    return ConversationHandler.END


def admin_code(update: Update, context: CallbackContext) -> int:
    message = 'Hello, mister admin 😎 Type /help to see all available commands'
    user = update.message.from_user

    save_user(
        id_=user.id,
        name=user.full_name,
        tgusername=user.name,
        chatid=update.message.chat_id,
        isadmin=1,
    )

    context.bot.send_message(chat_id=update.message.chat_id, text=message)

    return ConversationHandler.END


def club_code(update: Update, context: CallbackContext) -> int:
    message = 'You rock 🥳 Type /help to see all available commands'
    user = update.message.from_user

    save_user(
        id_=user.id,
        name=user.full_name,
        tgusername=user.name,
        chatid=update.message.chat_id,
    )

    context.bot.send_message(chat_id=update.message.chat_id, text=message)

    return ConversationHandler.END


handle = ConversationHandler(
    entry_points=[CommandHandler('code', handle_entry_point)],
    states={
        CommandCodeStates.CHECK: [
            MessageHandler(Filters.regex(config.ADMINCODE), admin_code),
            MessageHandler(Filters.regex(config.CLUBCODE), club_code),
        ],
    },
    fallbacks=[MessageHandler(Filters.text, fallback)],
    allow_reentry=True,
)
