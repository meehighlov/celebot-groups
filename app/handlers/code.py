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
    tg_user = update.message.from_user.id

    user = get_user_by_id(tg_user)

    if not user:
        save_user(
            id=tg_user.id,
            name=tg_user.full_name,
            tgusername=tg_user.name,
            chatid=update.message.chat_id,
            isadmin=1,
        )
    else:
        user.isadmin = 1
        save_user(**user.as_dict())

    context.bot.send_message(chat_id=update.message.chat_id, text=message)

    return ConversationHandler.END


def club_code(update: Update, context: CallbackContext) -> int:
    message = 'You rock 🥳 Type /help to see all available commands'
    tg_user = update.message.from_user

    user = get_user_by_id(tg_user.id)

    if not user:
        save_user(
            id=tg_user.id,
            name=tg_user.full_name,
            tgusername=tg_user.name,
            chatid=update.message.chat_id,
        )
    else:
        user.isadmin = 0
        save_user(**user.as_dict())

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
