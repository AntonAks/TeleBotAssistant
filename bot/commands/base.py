from abc import ABC,  abstractmethod
from telegram import Update
from telegram.ext import ContextTypes


class BaseCommand(ABC):

    @staticmethod
    @abstractmethod
    def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        pass
