from bot.commands.base import BaseCommand
from telegram import Update, ForceReply
from telegram.ext import ContextTypes


class HelpCommand(BaseCommand):

    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Hey! I'm a simple example of an assistant bot.")
