from bot.commands.base import BaseCommand
from telegram import Update, ForceReply
from telegram.ext import ContextTypes


class StartCommand(BaseCommand):
    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )
