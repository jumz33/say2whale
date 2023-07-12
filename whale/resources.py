from enum import StrEnum


class Bot(StrEnum):
    DESCRIPTION = "<b>Say@Whale</b>\nПривет! Просто отправь мне голосовое сообщение и я переведу его в текст"
    STICKER_ID = "CAACAgEAAxkBAAEJfP5kmYVTv38j9YlIAwI2PT-gLNGtLAACGwMAArAHGESRLvZwzZJ9si8E"


class Author(StrEnum):
    GITHUB_TEXT = "Посетить Github разработчика"
    GITHUB_URL = "https://github.com/jumz33"


class ErrorText(StrEnum):
    UNABLE_TO_RECOGNIZE = "Не могу распознать слова в сообщении."
