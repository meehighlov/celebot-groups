from database.create import rollout as init_db

from telegram.ext import Updater, CommandHandler

from app.config import config

from telegram.ext import CommandHandler

from app.handlers.help import handle as help_command_handler
from app.handlers.start import handle as start_command_handler
from app.handlers.code import handle as code_command_handler
from app.handlers.me import handle as me_command_handler
from app.handlers.setme import handle as setme_command_handler
from app.handlers.chat import handle as chat_command_handler


def main() -> None:
    init_db()

    updater = Updater(config.BOTTOKEN_CELEBOT)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command_handler))
    dispatcher.add_handler(CommandHandler('help', help_command_handler))
    dispatcher.add_handler(CommandHandler('me', me_command_handler))
    dispatcher.add_handler(CommandHandler('chat', chat_command_handler))
    dispatcher.add_handler(setme_command_handler)
    dispatcher.add_handler(code_command_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
