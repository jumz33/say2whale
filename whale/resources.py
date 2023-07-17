"""
This file includes all message texts
which bot uses to interact with user.

All markup definitions must follow bot parse_mode requirements
"""

from enum import StrEnum


class Bot(StrEnum):
    DESCRIPTION = "<b>Say@Whale</b>\n" \
                  "Hello! Just send or forward message and I'll recognize it."
    STICKER_ID = "CAACAgEAAxkBAAEJfP5kmYVTv38j9YlIAwI2PT-gLNGtLAACGwMAArAHGESRLvZwzZJ9si8E"


class Author(StrEnum):
    GITHUB_TEXT = "Visit developer's Github"
    GITHUB_URL = "https://github.com/jumz33"


class ErrorText(StrEnum):
    RECOGNIZER_UNKNOWN_SPEECH = "<b>I cannot recognize words in this message</b>"
    RECOGNIZER_CONNECTION_LOST = "<b>Internal error was occurred</b>"
