import logging
from settings import settings
from llms.openai import generate_response

from bot.commands.start import StartCommand
from bot.commands.help import HelpCommand

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def is_admin(func):
    def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id != settings.ADMIN_KEY:
            context.bot.send_message(update.effective_chat.id, 'You are not an administrator.')
        return func(update, context)
    return wrapper


@is_admin
async def check_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = generate_response(update.message.text)
    answer = answer.choices[0].message.content
    await context.bot.send_message(update.effective_chat.id, answer)


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(settings.API_TELEGRAM_KEY).build()

    application.add_handler(CommandHandler("start", StartCommand.execute))
    application.add_handler(CommandHandler("help", HelpCommand.execute))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_text))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
