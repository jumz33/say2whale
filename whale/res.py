from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class String:
    BOT_DESCRIPTION = "<b>Say@Whale</b>\n" \
                      "Hello! Just send or forward message and I'll recognize it."
    AUTHOR_GITHUB_TEXT = "Visit developer's Github"
    AUTHOR_GITHUB_URL = "https://github.com/jumz33"
    RECOGNIZER_ERROR = "<b>I cannot recognize words in this message</b>"
