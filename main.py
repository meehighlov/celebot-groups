import random
import datetime
from database.create import rollout as init_db

import pytz
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from config import config
# from exceptions import handle_any_error

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.help import handle as help_command_handler
from handlers.start import handle as start_command_handler
from handlers.code import handle as code_command_handler


def main() -> None:
    init_db(config.APP_NAME)

    updater = Updater(config.BOTTOKEN_CELEBOT)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command_handler))
    dispatcher.add_handler(CommandHandler('help', help_command_handler))
    dispatcher.add_handler(code_command_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
