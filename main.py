import logging
from app.exceptions import error_handler
from app.logger import init_logging
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
from app.handlers.delete import handle as delete_command_handler


logger = logging.getLogger(__name__)


def main() -> None:
    init_logging()
    init_db()

    logger.info('database is ready')

    updater = Updater(config.BOTTOKEN_CELEBOT)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command_handler))
    dispatcher.add_handler(CommandHandler('help', help_command_handler))
    dispatcher.add_handler(CommandHandler('me', me_command_handler))
    dispatcher.add_handler(CommandHandler('chat', chat_command_handler))
    dispatcher.add_handler(CommandHandler('del', delete_command_handler))
    dispatcher.add_handler(setme_command_handler)
    dispatcher.add_handler(code_command_handler)

    dispatcher.add_error_handler(error_handler)

    updater.start_polling()

    msg = f'polling launched, {config.APP_NAME} is up and ready'
    logger.info(msg)
    updater.idle()


if __name__ == '__main__':
    main()
