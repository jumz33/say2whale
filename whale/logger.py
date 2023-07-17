from telebot.async_telebot import AsyncTeleBot
from datetime import datetime
from enum import StrEnum

_TIME_STAMP_FORMAT = "%d/%m/%Y %H:%M:%S"
_INFO_FORMAT = "[%l] [%t] %n: '%a'"


class _LoggerLevel(StrEnum):
    CRITICAL = "CRITICAL"


class Logger:
    """
    This class is implementation of default logger,
    but all errors are logging to Telegram's chat.

    :param bot: :class:`telebot.async_telebot.AsyncTeleBot` instance to send logs
    :param log_chat_id: chat id to send logs
    """

    def __init__(self, bot: AsyncTeleBot, log_chat_id: int):
        self._bot = bot
        self._log_chat_id = log_chat_id

    async def critical(self, *, from_exception: Exception):
        text = self._get_exception_info(from_exception, _LoggerLevel.CRITICAL)
        await self._bot.send_message(self._log_chat_id, text)

    @classmethod
    def _get_exception_info(cls, exception: Exception, level: _LoggerLevel) -> str:
        return _INFO_FORMAT \
            .replace("%l", level) \
            .replace("%t", cls._get_time_stamp()) \
            .replace("%n", type(exception).__name__) \
            .replace("%a", str(exception))

    @staticmethod
    def _get_time_stamp() -> str:
        return datetime.today().strftime(_TIME_STAMP_FORMAT)
