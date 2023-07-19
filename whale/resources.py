"""
This file includes all message texts
which bot uses to interact with user.

All markup definitions must follow bot parse_mode requirements
"""

from enum import StrEnum


class Bot(StrEnum):
    DESCRIPTION = "<b>Say@Whale</b>\n" \
                  "Hello! Just send or forward message and I'll recognize it."


class Author(StrEnum):
    GITHUB_TEXT = "Visit developer's Github"
    GITHUB_URL = "https://github.com/jumz33"


class ErrorText(StrEnum):
    RECOGNIZER_UNKNOWN_SPEECH = "<b>I cannot recognize words in this message</b>"
