from telebot.async_telebot import AsyncTeleBot
from datetime import datetime
from whale import settings
from enum import StrEnum

_TIME_STAMP_FORMAT = "%d/%m/%Y %H:%M:%S"
_INFO_FORMAT = "[%l] [%t] %n: '%a'"


class _BotLoggerLevel(StrEnum):
    CRITICAL = "CRITICAL"


class BotLogger:
    """
    This class is implementation of default logger,
    but all errors are logging to Telegram's chat, defined in *settings.LOG_CHAT_ID*.

    Logger uses *telebot.async_telebot.AsyncTeleBot* instance to send messages.

    **Version added: 1.3**
    """

    def __init__(self, bot: AsyncTeleBot):
        self._bot = bot

    async def critical(self, *, from_exception: Exception):
        text = self._get_exception_info(from_exception, _BotLoggerLevel.CRITICAL)
        await self._bot.send_message(settings.LOG_CHAT_ID, text)

    @classmethod
    def _get_exception_info(cls, exception: Exception, level: _BotLoggerLevel) -> str:
        return _INFO_FORMAT \
            .replace("%l", level) \
            .replace("%t", cls._get_time_stamp()) \
            .replace("%n", type(exception).__name__) \
            .replace("%a", str(exception))

    @staticmethod
    def _get_time_stamp() -> str:
        return datetime.today().strftime(_TIME_STAMP_FORMAT)
